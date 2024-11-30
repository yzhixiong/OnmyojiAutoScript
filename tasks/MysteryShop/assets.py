from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class MysteryShopAssets: 


	# Image Rule Assets
	# 进入 
	I_ME_ENTER = RuleImage(roi_front=(52,494,59,44), roi_back=(52,494,59,44), threshold=0.8, method="Template matching", file="./tasks/MysteryShop/ms/ms_me_enter.png")
	# 点击分享 
	I_MS_SHARE = RuleImage(roi_front=(24,571,100,100), roi_back=(24,571,100,100), threshold=0.8, method="Template matching", file="./tasks/MysteryShop/ms/ms_ms_share.png")
	# 上一个 
	I_MS_BEFORE = RuleImage(roi_front=(25,317,39,52), roi_back=(25,317,39,52), threshold=0.8, method="Template matching", file="./tasks/MysteryShop/ms/ms_ms_before.png")
	# 下一个 
	I_MS_NEXT = RuleImage(roi_front=(1226,315,36,53), roi_back=(1226,315,36,53), threshold=0.8, method="Template matching", file="./tasks/MysteryShop/ms/ms_ms_next.png")
	# 分享 
	I_INVITE_ENSURE = RuleImage(roi_front=(711,545,127,60), roi_back=(711,545,127,60), threshold=0.8, method="Template matching", file="./tasks/MysteryShop/ms/ms_invite_ensure.png")


	# Ocr Rule Assets
	# 好友名字 
	O_MS_FRIEND = RuleOcr(roi=(1017,660,58,38), area=(1017,660,58,38), mode="Single", method="Default", keyword="", name="ms_friend")
	# 记录购买多少个的 
	O_MS_RECORDS = RuleOcr(roi=(338,638,30,36), area=(338,638,30,36), mode="Digit", method="Default", keyword="", name="ms_records")


	# Image Rule Assets
	# 蓝票 
	I_MS_BLUE = RuleImage(roi_front=(850,379,117,98), roi_back=(179,81,829,471), threshold=0.7, method="Template matching", file="./tasks/MysteryShop/ms/ms_ms_blue.png")
	# 黑蛋 
	I_MS_BLACK = RuleImage(roi_front=(851,353,114,102), roi_back=(170,64,850,448), threshold=0.6, method="Template matching", file="./tasks/MysteryShop/ms/ms_ms_black.png")
	# description 
	I_MS_TAIKO_3 = RuleImage(roi_front=(176,353,140,104), roi_back=(144,50,866,494), threshold=0.8, method="Template matching", file="./tasks/MysteryShop/ms/ms_ms_taiko_3.png")
	# description 
	I_MS_TAIKO_4 = RuleImage(roi_front=(204,372,90,88), roi_back=(156,81,874,473), threshold=0.8, method="Template matching", file="./tasks/MysteryShop/ms/ms_ms_taiko_4.png")
	# description 
	I_MS_TAIKO_6 = RuleImage(roi_front=(0,0,100,100), roi_back=(0,0,100,100), threshold=0.8, method="Template matching", file="./tasks/MysteryShop/ms/ms_ms_taiko_6.png")
	# description 
	I_MS_EXP = RuleImage(roi_front=(0,0,100,100), roi_back=(0,0,100,100), threshold=0.8, method="Template matching", file="./tasks/MysteryShop/ms/ms_ms_exp.png")
	# description 
	I_MS_CHECK_BLUE = RuleImage(roi_front=(592,241,88,94), roi_back=(455,235,261,146), threshold=0.8, method="Template matching", file="./tasks/MysteryShop/ms/ms_ms_check_blue.png")
	# description 
	I_MS_CHECK_BLACK = RuleImage(roi_front=(598,258,86,92), roi_back=(455,238,273,123), threshold=0.8, method="Template matching", file="./tasks/MysteryShop/ms/ms_ms_check_black.png")
	# description 
	I_MS_CHECK_TAIKO_3 = RuleImage(roi_front=(567,259,70,81), roi_back=(465,245,252,124), threshold=0.8, method="Template matching", file="./tasks/MysteryShop/ms/ms_ms_check_taiko_3.png")
	# description 
	I_MS_CHECK_TAIKO_4 = RuleImage(roi_front=(591,277,66,73), roi_back=(453,235,280,146), threshold=0.8, method="Template matching", file="./tasks/MysteryShop/ms/ms_ms_check_taiko_4.png")
	# description 
	I_MS_CHECK_TAIKO_6 = RuleImage(roi_front=(580,253,100,100), roi_back=(430,220,334,171), threshold=0.8, method="Template matching", file="./tasks/MysteryShop/ms/ms_ms_check_taiko_6.png")
	# description 
	I_MS_CHECK_EXP = RuleImage(roi_front=(589,255,100,100), roi_back=(472,225,243,149), threshold=0.8, method="Template matching", file="./tasks/MysteryShop/ms/ms_ms_check_exp.png")
	# description 
	I_MS_REWARD_3 = RuleImage(roi_front=(511,630,48,47), roi_back=(511,630,48,47), threshold=0.7, method="Template matching", file="./tasks/MysteryShop/ms/ms_ms_reward_3.png")
	# description 
	I_MS_REWARD_5 = RuleImage(roi_front=(682,632,48,42), roi_back=(682,632,48,42), threshold=0.7, method="Template matching", file="./tasks/MysteryShop/ms/ms_ms_reward_5.png")
	# description 
	I_MS_REWARD_10 = RuleImage(roi_front=(851,637,47,32), roi_back=(851,637,47,32), threshold=0.7, method="Template matching", file="./tasks/MysteryShop/ms/ms_ms_reward_10.png")


