# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
from pydantic import BaseModel, Field

from tasks.Component.config_base import ConfigBase
from tasks.Component.config_scheduler import Scheduler
from tasks.Component.GeneralBattle.config_general_battle import GeneralBattleConfig
from tasks.Exploration.config import ExplorationLevel


class ShikigamiChallengeConfig(BaseModel):
    enable: bool = Field(title='启用', default=True, description='shikigami_challenge_enable_help')
    cnt_challenge: int = Field(title='战斗次数', default=15, ge=0, description='shikigami_challenge_cnt_challenge_help')
    shikigami_name: str = Field(title='挑战妖式神名称', default='', description='shikigami_challenge_name_help')
    exploration_level: ExplorationLevel = Field(title='探索等级', default=ExplorationLevel.EXPLORATION_28,
                                                description='shikigami_challenge_exploration_level_help')

class ShikigamidebrisConfig(BaseModel):
    enable: bool = Field(title='启用', default=True, description='shikigami_debris__enable_help')
    cnt_challenge: int = Field(title='战斗次数', default=50, ge=0, description='shikigami_debris__cnt_challenge_help')
    shikigami_name: str = Field(title='挑战妖式神名称', default='', description='shikigami_debris_shikigami_name_help')


class ShikigamiChallenge(ConfigBase):
    scheduler: Scheduler = Field(default_factory=Scheduler)
    general_battle_config: GeneralBattleConfig = Field(default_factory=GeneralBattleConfig)
    shikigami_challenge_config: ShikigamiChallengeConfig = Field(default_factory=ShikigamiChallengeConfig)
    shikigami_debris_config: ShikigamidebrisConfig = Field(default_factory=ShikigamidebrisConfig)