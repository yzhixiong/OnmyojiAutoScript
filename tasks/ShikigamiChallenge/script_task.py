# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
import time

from cached_property import cached_property

from module.logger import logger
from tasks.Exploration.base import BaseExploration, Scene
from tasks.Exploration.config import ExplorationLevel
from tasks.GameUi.game_ui import GameUi
from tasks.GameUi.page import page_main, page_exploration
from tasks.ShikigamiChallenge.assets import ShikigamiChallengeAssets


class ScriptTask(BaseExploration, GameUi, ShikigamiChallengeAssets):
    _cnt_challenge: int = 0

    @cached_property
    def _config(self):
        return self.config.model.shikigami_challenge

    def run(self):
        logger.hr('exploration')
        self.ui_get_current_page()
        # 探索页面
        self.ui_goto(page_exploration)

        # 进行式神挑战
        # self.run_challenge()
        # 式神碎片副本
        self.run_shikigami_debris()

        self.ui_get_current_page()
        self.ui_goto(page_main)

        self.set_next_run(task='ShikigamiChallenge', success=True, finish=False)

    def run_challenge(self):
        if not self._config.shikigami_challenge_config.enable:
            return
        self.config.exploration.exploration_config.exploration_level = self._config.shikigami_challenge_config.exploration_level
        shikigami_leve = None
        while 1:
            self.screenshot()
            scene = self.get_current_scene()

            if scene == Scene.WORLD:
                if self.check_exit():
                    break
                self.open_expect_level()
                continue
            elif (self.appear(self.I_UI_BACK_RED)
                  and (self.appear(self.I_E_EXPLORATION_CLICK)
                       or self.appear(self.I_FIRE_CHALLENGE)
                       or self.appear(self.I_CHALLENGE_PAGE_CHECK))):
                if self.check_exit():
                    break
                self.ui_click_until_disappear(self.I_SWITCH_CHALLENGE)

                if self.O_CHALLENGE_TICKET.ocr(self.device.image) == 0:
                    logger.info("challenge ticket loss")
                    break
                if not self.appear(self.I_FIRE_CHALLENGE):
                    logger.info("no fire challenge button")
                    break
                if self.appear(self.I_NOT_SHIKIGAMI):
                    logger.info("no shikigami")
                    break

                if shikigami_leve is not None:
                    shikigami_sort = shikigami_leve - 1
                else:
                    shikigami_sort = 0

                while 1:
                    if shikigami_leve == 2:
                        self.click(self.C_SHIKIGAMI_2, interval=1)
                    elif shikigami_leve == 3:
                        self.click(self.C_SHIKIGAMI_3, interval=1)

                    shikigami_sort += 1
                    self.screenshot()
                    ocr = self.O_SHIKIGAMI_NAME.ocr(self.device.image)
                    if ocr == self._config.shikigami_challenge_config.shikigami_name:
                        self.ui_click_until_disappear(self.I_FIRE_CHALLENGE)
                        self.run_general_battle(self._config.general_battle_config)
                        self._cnt_challenge += 1
                        shikigami_leve = shikigami_sort
                        break
                    if shikigami_sort == 1 and self.appear_then_click(self.I_SHIKIGAMI_1, self.C_SHIKIGAMI_2,
                                                                      interval=1):
                        continue
                    if shikigami_sort == 2 and self.appear_then_click(self.I_SHIKIGAMI_2, self.C_SHIKIGAMI_3,
                                                                      interval=1):
                        continue
                    if shikigami_sort == 3:
                        break
                continue

        self.wait_until_stable(self.I_UI_BACK_RED)
        if self.appear(self.I_UI_BACK_RED):
            self.ui_click_until_disappear(self.I_UI_BACK_RED)

    def check_exit(self) -> bool:
        if self._cnt_challenge >= self._config.shikigami_challenge_config.cnt_challenge:
            logger.info(f'Reach challenge count:{self._cnt_challenge}')
            return True
        return False

    def run_shikigami_debris(self):
        """式神碎片"""
        if not self._config.shikigami_debris_config.enable:
            return
        shikigami_debris_entry_list = [self.I_SHIKIGAMI_DEBRIS_ENTRY_X2, self.I_SHIKIGAMI_DEBRIS_ENTRY_X3,
                                       self.I_SHIKIGAMI_DEBRIS_ENTRY_X4, self.I_SHIKIGAMI_DEBRIS_ENTRY_X1,
                                       self.I_SHIKIGAMI_DEBRIS_ENTRY_X5]
        if not any(self.appear(item) for item in shikigami_debris_entry_list):
            # 点第九章后副本会出现在右上角
            self.config.exploration.exploration_config.exploration_level = ExplorationLevel.EXPLORATION_9
            self.open_expect_level()

            self.wait_until_stable(self.I_UI_BACK_RED)
            if self.appear(self.I_UI_BACK_RED):
                self.ui_click_until_disappear(self.I_UI_BACK_RED)

        self.O_SHIKIGAMI_DEBRIS_NAME.keyword = self._config.shikigami_debris_config.shikigami_name
        x, y, w, h = self.I_SHIKIGAMI_DEBRIS_SELECT.roi_back

        self._cnt_challenge = 0

        def find_and_fight_debris():
            """查找并挑战目标碎片"""
            for ocr_count in range(4):  # 最多尝试4行
                self.screenshot()
                self.I_SHIKIGAMI_DEBRIS_SELECT.roi_back = (x, y + (100 * ocr_count), w, h)

                if self.appear(self.I_SHIKIGAMI_DEBRIS_SELECT):
                    roi_y = self.I_SHIKIGAMI_DEBRIS_SELECT.roi_front[1] - 45
                    self.O_SHIKIGAMI_DEBRIS_NAME.roi[1] = roi_y

                    if self.ocr_appear(self.O_SHIKIGAMI_DEBRIS_NAME):
                        while self.appear_then_click(self.I_SHIKIGAMI_DEBRIS_SELECT, interval=1):
                            self.appear_then_click(self.I_SHIKIGAMI_DEBRIS_FIRE, interval=1)
                        self.run_general_battle(self._config.general_battle_config)
                        self._cnt_challenge += 1
                        return True
            return False

        while True:
            self.screenshot()
            if self._cnt_challenge >= self._config.shikigami_debris_config.cnt_challenge:
                logger.info(f'Reach challenge count:{self._cnt_challenge}')
                return True
            # 如果在式神碎片界面
            if self.appear(self.I_SHIKIGAMI_DEBRIS_CHECK):
                select_count = 0
                for select_count in range(3):
                    if find_and_fight_debris():
                        break

                    # 战斗结束后检查是否还在碎片界面
                    if not self.appear(self.I_SHIKIGAMI_DEBRIS_CHECK):
                        break

                    # 下滑查找更多碎片
                    self.swipe(self.S_SHIKIGAMI_DEBRIS_SELECT)
                    time.sleep(1)

                # 最多下滑3次
                if select_count > 1:
                    logger.info(f'too many swipe:{select_count + 1}')
                    break

            # 点击世界的契约碎片入口
            if any(self.appear_then_click(item) for item in shikigami_debris_entry_list):
                time.sleep(3)
            # 点击式神碎片入口
            elif self.appear(self.I_SHIKIGAMI_DEBRIS_NO):
                logger.info('no shikigami debris')
                break
            # 点击式神碎片入口
            elif self.appear_then_click(self.I_SHIKIGAMI_DEBRIS_ENTRY_2, self.C_SHIKIGAMI_DEBRIS_ENTRY):
                continue

        self.ui_click_until_disappear(self.I_UI_BACK_RED)


if __name__ == "__main__":
    from module.config.config import Config
    from module.device.device import Device

    config = Config('oas2')
    device = Device(config)
    t = ScriptTask(config, device)
    # t.run()
    t.screenshot()

    shikigami_debris_entry_list = [t.I_SHIKIGAMI_DEBRIS_ENTRY_X2, t.I_SHIKIGAMI_DEBRIS_ENTRY_X3,
                                   t.I_SHIKIGAMI_DEBRIS_ENTRY_X4, t.I_SHIKIGAMI_DEBRIS_ENTRY_X1,
                                   t.I_SHIKIGAMI_DEBRIS_ENTRY_X5]
    if not any(t.appear(item) for item in shikigami_debris_entry_list):
        print("x1")
    if any(t.appear_then_click(item) for item in shikigami_debris_entry_list):
        print("x21")
