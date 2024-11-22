from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class SecretAssets: 


	# Click Rule Assets
	# description 
	C_SE_CLICK_LAYER = RuleClick(roi_front=(434,155,100,100), roi_back=(434,155,100,100), name="se_click_layer")
	# 跳过对话 
	C_SE_CLICK_DIALOGUE = RuleClick(roi_front=(589,160,495,300), roi_back=(589,160,495,300), name="se_click_dialogue")


	# Image Rule Assets
	# 进入 
	I_SE_ENTER = RuleImage(roi_front=(1145,593,100,100), roi_back=(1145,593,100,100), threshold=0.8, method="Template matching", file="./tasks/Secret/se/se_se_enter.png")
	# 秘闻挑战 
	I_SE_FIRE = RuleImage(roi_front=(1108,551,100,100), roi_back=(1100,541,120,120), threshold=0.7, method="Template matching", file="./tasks/Secret/se/se_se_fire.png")
	# 排行 
	I_SE_PLACEMENT = RuleImage(roi_front=(1013,570,50,48), roi_back=(996,555,79,81), threshold=0.8, method="Template matching", file="./tasks/Secret/se/se_se_placement.png")
	# 勾玉 
	I_SE_JADE = RuleImage(roi_front=(305,208,28,33), roi_back=(305,208,28,33), threshold=0.8, method="Template matching", file="./tasks/Secret/se/se_se_jade.png")
	# 最后一个的勾玉 
	I_SE_JADE_LAST = RuleImage(roi_front=(302,565,37,40), roi_back=(302,565,37,40), threshold=0.8, method="Template matching", file="./tasks/Secret/se/se_se_jade_last.png")
	# 战斗赢 
	I_SE_BATTLE_WIN = RuleImage(roi_front=(436,62,100,100), roi_back=(436,62,100,100), threshold=0.8, method="Template matching", file="./tasks/Secret/se/se_se_battle_win.png")
	# 已经完成可以退出 
	I_SE_FINISHED_1 = RuleImage(roi_front=(441,546,40,43), roi_back=(441,546,40,43), threshold=0.8, method="Template matching", file="./tasks/Secret/se/se_se_finished_1.png")
	# 录像按钮 
	I_N_VIDEO = RuleImage(roi_front=(1081.5,551,25,17), roi_back=(1166,206,25,26), threshold=0.8, method="Template matching", file="./tasks/Secret/se/se_n_video.png")
	# 挑战 
	I_N_FIRE = RuleImage(roi_front=(355,386.5,42,22), roi_back=(1067,551,71,22), threshold=0.8, method="Template matching", file="./tasks/Secret/se/se_n_fire.png")
	# 首次金币 
	I_N_FIRST_GOLD = RuleImage(roi_front=(341,316,42,41), roi_back=(322,126,96,542), threshold=0.8, method="Template matching", file="./tasks/Secret/se/se_n_first_gold.png")
	# 退出 
	I_N_BOOS_QUIT = RuleImage(roi_front=(355,490,34,16), roi_back=(1156,96,47,45), threshold=0.8, method="Template matching", file="./tasks/Secret/se/se_n_boos_quit.png")
	# 未选中首次战斗 
	I_N_FIRST_BATTLE = RuleImage(roi_front=(244,335,127,21), roi_back=(235,144,151,511), threshold=0.8, method="Template matching", file="./tasks/Secret/se/se_n_first_battle.png")
	# 选中首次战斗 
	I_N_FIRST_BATTLE_SELECTED = RuleImage(roi_front=(313,335,66,21), roi_back=(235,144,151,511), threshold=0.8, method="Template matching", file="./tasks/Secret/se/se_n_first_battle_selected.png")
	# 跳过战斗结束对话 
	I_N_QUIT_SKIT_DIALOGUE = RuleImage(roi_front=(338,230,39,21), roi_back=(848,490,39,21), threshold=0.8, method="Template matching", file="./tasks/Secret/se/se_n_quit_skit_dialogue.png")
	# 壹层 
	I_N_LAYER_ONE = RuleImage(roi_front=(848,490,34,16), roi_back=(307,198,409,412), threshold=0.8, method="Template matching", file="./tasks/Secret/se/se_n_layer_one.png")
	# 壹层选中状态 
	I_N_LAYER_ONE_2 = RuleImage(roi_front=(672,499,36,30), roi_back=(672,499,36,30), threshold=0.8, method="Template matching", file="./tasks/Secret/se/se_n_layer_one_2.png")
	# boos界面排行榜 
	I_SE_PLACEMENT_OUTSIDE = RuleImage(roi_front=(305,208,23,25), roi_back=(1179,492,30,31), threshold=0.8, method="Template matching", file="./tasks/Secret/se/se_se_placement_outside.png")


	# Ocr Rule Assets
	# 未通关 
	O_SE_NO_PASS = RuleOcr(roi=(428,151,262,248), area=(428,151,262,248), mode="Full", method="Default", keyword="未通关", name="se_no_pass")
	# 第一个位置的层数 
	O_SE_LAYER_1 = RuleOcr(roi=(210,150,44,39), area=(210,150,44,39), mode="Single", method="Default", keyword="", name="se_layer_1")
	# Ocr-description 
	O_SE_LAYER_10 = RuleOcr(roi=(210,507,34,34), area=(210,507,34,34), mode="Single", method="Default", keyword="拾", name="se_layer_10")
	# Ocr-description 
	O_SE_LAYER_9 = RuleOcr(roi=(211,373,35,33), area=(211,373,35,33), mode="Single", method="Default", keyword="玖", name="se_layer_9")
	# Ocr-description 
	O_SE_LAYER_8 = RuleOcr(roi=(212,237,34,34), area=(212,237,34,34), mode="Single", method="Default", keyword="捌", name="se_layer_8")
	# 后面的时候识别为通关的 
	O_SE_NO_PASS_LAST = RuleOcr(roi=(429,381,180,234), area=(429,381,180,234), mode="Full", method="Default", keyword="未通关", name="se_no_pass_last")
	# 勾玉 
	O_SE_JADE = RuleOcr(roi=(327,230,23,24), area=(327,230,23,24), mode="Digit", method="Default", keyword="", name="se_jade")
	# 金币 
	O_SE_GOLD = RuleOcr(roi=(363,226,48,21), area=(363,226,48,21), mode="Digit", method="Default", keyword="", name="se_gold")


	# Swipe Rule Assets
	# 向下滑动 
	S_SE_DOWN_SEIPE = RuleSwipe(roi_front=(229,520,124,27), roi_back=(217,390,145,35), mode="default", name="se_down_seipe")


