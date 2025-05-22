# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
from module.logger import logger
from time import sleep

from module.exception import TaskEnd
from tasks.GameUi.game_ui import GameUi
from tasks.Wish.assets import WishAssets
from tasks.GameUi.page import page_main, page_guild


class ScriptTask(GameUi, WishAssets):

    wishNum: int = 0

    def run(self):
        self.ui_get_current_page()
        self.ui_goto(page_guild)

        # 进入祈愿
        self.ui_click(self.I_ENTER_WISH, self.I_ENTER_WISH_CHECK, interval=2)

        self.wishNum = 0
        self.doWish()

        # 进入好友界面
        self.ui_click(self.I_SWITCH_FRIEND_1, self.I_SWITCH_FRIEND_2)
        self.ui_click(self.I_SWITCH_FRIEND_2, self.I_SWITCH_FRIEND_CHECK)
        sleep(1)

        self.doWish()

        self.ui_get_current_page()
        self.ui_goto(page_main)
        self.set_next_run(task='Wish', success=self.wishNum > 0, finish=True)
        raise TaskEnd

    def doWish(self):
        """
        查找好友并赠与
        """
        back = self.I_BESTOW.roi_back
        isSwipeEnd, area = self.getNameArea()
        if not area == (0, 0, 0, 0):
            self.doBestow(back, area)
        elif isSwipeEnd:
            logger.warn("name not found")

        self.I_BESTOW.roi_back = back

    def doBestow(self, back, area):
        """
        计算赠与按钮位置并赠与
        """
        # 计算赠与按钮位置
        self.I_BESTOW.roi_back = [area[0] + 560, area[1] - 10, back[2] + 20, back[3] + 20]
        logger.info(f"bestow button roi_back is:{self.I_BESTOW.roi_back}")
        self.screenshot()
        # 确认赠与
        if self.wait_until_appear_then_click(self.I_BESTOW):
            # 点击确认会出现新的赠与按钮 。所以点击确认后不允许点赠与
            if self.wait_until_appear_then_click(self.I_BESTOW_CONFIRM):
                logger.info("bestow success")
                self.wishNum += 1
        else:
            logger.warn("bestow button not found")

    def getNameArea(self):
        """
        通过角色名查找好友位置
        """
        self.O_NAME.keyword = self.config.wish.wish_config.name
        checkNum = 0
        endNum = 0
        # 下滑寻找角色
        area = (0, 0, 0, 0)
        while 1:
            self.screenshot()
            if checkNum >= 3:
                break
            if endNum >= 3:
                break
            if self.appear(self.I_SWITCH_END_CHECK_2):
                break
            if self.appear(self.I_SWITCH_END_CHECK_3):
                break

            area = self.O_NAME.ocr(self.device.image)
            if not area == (0, 0, 0, 0):
                # 等待页面稳定,别捐错了！！！
                checkNum += 1
                continue

            if self.appear(self.I_SWITCH_END_CHECK):
                endNum += 1
                continue

            self.swipe(self.S_LIST_DOWN, interval=2)
            sleep(2)
            self.device.click_record_clear()

        return checkNum >= 3, area


if __name__ == "__main__":
    from module.device.device import Device
    from module.config.config import Config

    config = Config('oas1')
    device = Device(config)
    t = ScriptTask(config, device)
    t.run()

    # t.screenshot()
    # WishAssets.O_NAME.keyword = ''
    # area = WishAssets.O_NAME.ocr(t.device.image)
    # back = WishAssets.I_BESTOW.roi_back
    # WishAssets.I_BESTOW.roi_back = [area[0] + 560, area[1] - 10, back[2] + 20, back[3] + 20]
    # print(area)
    # print(WishAssets.I_BESTOW.roi_back)
    # print(t.appear(WishAssets.I_BESTOW))
