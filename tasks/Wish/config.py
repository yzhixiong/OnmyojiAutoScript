# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
from pydantic import BaseModel, Field

from tasks.Component.config_scheduler import Scheduler
from tasks.Component.config_base import ConfigBase

class WishConfig(BaseModel):
    name: str = Field(default="", description='name_help')
    pass

class Wish(ConfigBase):
    scheduler: Scheduler = Field(default_factory=Scheduler)
    wish_config: WishConfig = Field(default_factory=WishConfig)
