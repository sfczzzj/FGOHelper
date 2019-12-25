import basefunc
import time
import AntiCheck
import datetime
import random

#默认副本按键
DefaultStage_X = 1040
DefaultStage_Y = 290
DefaultStage_R = 60

#金苹果
EatGoldApple_X = 420
EatGoldApple_Y = 405
EatGoldApple_R = 60

#吃苹果确认
EatAppleConfirm_X = 950
EatAppleConfirm_Y = 670
EatAppleConfirm_R = 30

#助战刷新
RefreshAssisant_X = 940;
RefreshAssisant_Y = 180;
RefreshAssisant_R = 30;

#助战刷新确认
RefreshAssisantConfirm_X = 940;
RefreshAssisantConfirm_Y = 670;
RefreshAssisantConfirm_R = 30;

#助战滑动
SwipeAssisant_X1 = 740
SwipeAssisant_Y1 = 705
SwipeAssisant_X2 = 740
SwipeAssisant_Y2 = 455
SwipeAssisant_R = 0

#开始任务
StartMission_X = 1340
StartMission_Y = 795
StartMission_R = 20

#攻击按键检索范围
AttackButton_X1 = 1140
AttackButton_Y1 = 570
AttackButton_X2 = 1430
AttackButton_Y2 = 860

#攻击按键
AttackButton_X = 1275
AttackButton_Y = 715
AttackButton_R = 50

#技能键
Skill_X = [[78, 160, 290], [435, 540, 645], [795, 900, 1005]]
Skill_Y = 685
Skill_R = 20

#从者位置
Servant_X = [380, 720, 1070]
Servant_Y = 535
Servant_R = 100

#御主技能按键
UseMasterSkill_X = 1345
UseMasterSkill_Y = 400
UseMasterSkill_R = 40

#御主技能
MasterSkill_X = [1018, 1120, 1210]
MasterSkill_Y = 386
MasterSkill_R = 25

#宝具卡位置
Noble_X = [465, 720, 1000]
Noble_Y = 280
Noble_R = 60

#指令卡位置
Card_X = [155, 445, 725, 1015, 1315]
Card_Y = 610
Card_R = 60

#战斗结束下一步
Next_X = 1250
Next_Y = 800
Next_R = 30

#换人从者位置
OrderChange_X = [160, 380, 605, 825, 1050, 1280]
OrderChange_Y = 420
OrderChange_R = 80

#换人按键
OrderChangeButton_X = 720
OrderChangeButton_Y = 740
OrderChangeButton_R = 40

#回合数
Round_X1 = 970
Round_Y1 = 50
Round_X2 = 995
Round_Y2 = 80

#友情召唤按键搜索坐标范围
FriendSummon_X1 = 770
FriendSummon_Y1 = 600
FriendSummon_X2 = 1100
FriendSummon_Y2 = 720

#友情召唤决定按键搜索坐标范围
FriendSummonConfirm_X1 = 800
FriendSummonConfirm_Y1 = 630
FriendSummonConfirm_X2 = 1100
FriendSummoConfirmn_Y2 = 720

#友情池抽卡点击
FriendSummonIdle_X = 1320
FriendSummonIdle_Y = 700

#友情结果召唤按键搜索坐标范围
FriendSummon2_X1 = 750
FriendSummon2_Y1 = 740
FriendSummon2_X2 = 950
FriendSummon2_Y2 = 830

def FGO_WaitFor_StageSelect():
	res = None
	#basefunc.Log("等待选择副本界面")
	while (res == None):
		AntiCheck.RandomSleep()
		res = basefunc.FindImageInRect(1140, 670, 1440, 870, "MenuButton.png", 0.8)
	basefunc.Log("已进入选择副本界面")

def FGO_WaitFor_AssistantSelect():
	res = None
	#basefunc.Log("等待选择助战界面")
	while (res == None):
		AntiCheck.RandomSleep()
		res = basefunc.FindImageInRect(1140, 10, 1440, 160, "SelectAssistant.png", 0.8)
	basefunc.Log("已进入选择助战界面")

def FGO_WaitFor_TeamConfrim():
	res = None
	#basefunc.Log("等待队伍确认界面")
	while (res == None):
		AntiCheck.RandomSleep()
		res = basefunc.FindImageInScreen("TeamConfrim.png")
	basefunc.Log("已进入队伍确认界面")

def FGO_WaitFor_Attack(waitSeconds = None):
	res = None
	#basefunc.Log("等待战斗界面")
	#AntiCheck.RandomClick()
	starttime = datetime.datetime.now()
	while (res == None):
		AntiCheck.RandomSleep()
		res = basefunc.FindImageInRect(AttackButton_X1, AttackButton_Y1, AttackButton_X2, AttackButton_Y2, "AttackButton.png", 0.8)
		endtime = datetime.datetime.now()
		duringtime = endtime - starttime
		if waitSeconds != None:
			if duringtime.seconds > waitSeconds:
				return False
	AntiCheck.RandomSleep()
	return True
	#basefunc.Log("已进入战斗界面")

def FGO_WaitFor_BattleEnd(waitSeconds = 60):
	res = None
	basefunc.Log("等待战斗结束界面")
	#AntiCheck.RandomClick()
	starttime = datetime.datetime.now()
	while (res == None):
		AntiCheck.RandomSleep()
		res = basefunc.FindImageInScreen("BattleEnd.png")
		endtime = datetime.datetime.now()
		duringtime = endtime - starttime
		if duringtime.seconds > waitSeconds:
			return False
	basefunc.Log("已进入战斗结束界面")
	return True
	
def FGO_WaitFor_FinishBattleNextButton(waitSeconds = None):
	res = None
	starttime = datetime.datetime.now()
	while (res == None):
		AntiCheck.RandomSleep()
		AntiCheck.RangeClick(Next_X, Next_Y - 5 * Next_R, Next_R)
		res = basefunc.FindImageInScreen("FinishBattleNextButton.png")
		endtime = datetime.datetime.now()
		duringtime = endtime - starttime
		if waitSeconds != None:
			if duringtime.seconds > waitSeconds:
				return False
	return True

##########################################################################################

def FGO_WaitAndClick_FriendSummon():
	res = None
	while (res == None):
		AntiCheck.RandomSleep(1)
		res = basefunc.FindImageInRect(FriendSummon_X1, FriendSummon_Y1, FriendSummon_X2, FriendSummon_Y2, "FriendSummon.png", 0.8)
	AntiCheck.RangeClick(res[0], res[1], 20)

def FGO_WaitAndClick_FriendSummonConfirm():
	res = None
	while (res == None):
		AntiCheck.RandomSleep(1)
		res = basefunc.FindImageInRect(FriendSummon_X1, FriendSummon_Y1, FriendSummon_X2, FriendSummon_Y2, "FriendSummonConfirm.png", 0.8)
	AntiCheck.RangeClick(res[0], res[1], 20)
	
def FGO_WaitAndClick_FinishFriendSummon():
	res = None
	while (res == None):
		AntiCheck.RandomSleep(1)
		AntiCheck.RangeClick(FriendSummonIdle_X, FriendSummonIdle_Y, 50)
		res = basefunc.FindImageInScreen("FriendSummon2.png")
	AntiCheck.RangeClick(res[0], res[1], 20)
	
#########################################################################################

def FGO_Action_SelectDefaultStage():
	AntiCheck.RandomSleep()
	AntiCheck.RangeClick(DefaultStage_X, DefaultStage_Y, DefaultStage_R)
	basefunc.Log("已选择默认副本")
	
	#处理吃苹果
	time.sleep(1)
	AntiCheck.RandomSleep()
	res = basefunc.FindImageInScreen("NeedEatApple.png")
	if res != None:
		basefunc.Log("体力不足，吃金苹果")
		AntiCheck.RandomSleep()
		AntiCheck.RangeClick(EatGoldApple_X, EatGoldApple_Y, EatGoldApple_R)
		AntiCheck.RandomSleep()
		AntiCheck.RangeClick(EatAppleConfirm_X, EatAppleConfirm_Y, EatAppleConfirm_R)

def FGO_Action_SelectAssisant(PreferAssistantPic):
	res = None
	i = 0
	while (True):
		AntiCheck.RandomSleep()
		
		if i > 12:			
			basefunc.Log("未找到任何可用助战")
			AntiCheck.RangeClick(RefreshAssisant_X, RefreshAssisant_Y, RefreshAssisant_R)
			time.sleep(0.5)
			res = basefunc.FindImageInScreen("RefreshAssisantCloseButton.png")
			if res != None:
				basefunc.Log("暂时无法刷新助战")
				time.sleep(10)
				continue
			AntiCheck.RangeClick(RefreshAssisantConfirm_X, RefreshAssisantConfirm_Y, RefreshAssisantConfirm_R)
			i = 0
		res = basefunc.FindImageInScreen(PreferAssistantPic)
		if res != None:
			AntiCheck.RangeClick(res[0] - basefunc.baseLeft, res[1] - basefunc.baseTop, 20)
			basefunc.Log("已选择目标助战 坐标 " + str(res[0]) + "," + str(res[1]))
			return
		
		AntiCheck.RangeSwipe(SwipeAssisant_X1, SwipeAssisant_Y1, SwipeAssisant_R, SwipeAssisant_X2, SwipeAssisant_Y2, SwipeAssisant_R)
		time.sleep(1)
		i = i + 1

def FGO_Action_ConfirmTeam():
	basefunc.Log("队伍确认")
	AntiCheck.RandomSleep()
	AntiCheck.RangeClick(StartMission_X, StartMission_Y, StartMission_R)

def FGO_Action_UseSkill(Servant, SkillNo, To):
	AntiCheck.RandomSleep()
	basefunc.Log("使用从者" + str(Servant) + " 技能" + str(SkillNo) + " 目标从者" + str(To))
	AntiCheck.RangeClick(Skill_X[Servant - 1][SkillNo - 1], Skill_Y, Skill_R)
	if To != None:
		AntiCheck.RandomSleep(2)
		AntiCheck.RangeClick(Servant_X[To - 1], Servant_Y, Servant_R)

def FGO_Action_UseMasterSkill(SkillNo, To):
	AntiCheck.RandomSleep()
	AntiCheck.RangeClick(UseMasterSkill_X, UseMasterSkill_Y, UseMasterSkill_R)
	AntiCheck.RandomSleep()
	basefunc.Log("使用御主技能" + str(SkillNo) + " 目标从者" + str(To))
	AntiCheck.RangeClick(MasterSkill_X[SkillNo - 1], MasterSkill_Y, MasterSkill_R)
	if To != None:
		time.sleep(0.5)
		AntiCheck.RandomSleep()
		AntiCheck.RangeClick(Servant_X[To - 1], Servant_Y, Servant_R)

def FGO_Action_Attck():
	AntiCheck.RandomSleep(1)
	basefunc.Log("开始选择攻击卡牌")
	AntiCheck.RangeClick(AttackButton_X, AttackButton_Y, AttackButton_R)
	AntiCheck.RandomSleep()
	time.sleep(1)
	
def FGO_Action_SelectNoble(Servant):
	AntiCheck.RandomSleep()
	basefunc.Log("选择从者" + str(Servant) + "宝具")
	AntiCheck.RangeClick(Noble_X[Servant - 1], Noble_Y, Noble_R)
	
def FGO_Action_SelectCard(CardIndex):
	AntiCheck.RandomSleep(1)
	basefunc.Log("选择指令卡" + str(CardIndex))
	AntiCheck.RangeClick(Card_X[CardIndex - 1], Card_Y, Card_R)

def FGO_Action_FinishBattle():
	AntiCheck.RandomSleep()
	basefunc.Log("战斗结束")
	AntiCheck.RangeClick(Next_X, Next_Y, Next_R)
	time.sleep(3)
	res = basefunc.FindImageInScreen("DoNotAddFriend.png")
	if res != None:
		AntiCheck.RangeClick(res[0] - basefunc.baseLeft, res[1] - basefunc.baseTop, 40)

def FGO_Action_OrderChange(SubIndex, MainIndex):
	AntiCheck.RandomSleep()
	basefunc.Log("礼装换人 后排" + str(SubIndex) + " 换到前排" + str(MainIndex))
	AntiCheck.RangeClick(UseMasterSkill_X, UseMasterSkill_Y, UseMasterSkill_R)
	AntiCheck.RandomSleep(4)
	AntiCheck.RangeClick(MasterSkill_X[2], MasterSkill_Y, MasterSkill_R)
	time.sleep(0.8)
	AntiCheck.RandomSleep()
	AntiCheck.RangeClick(OrderChange_X[SubIndex - 1], OrderChange_Y, OrderChange_R)
	AntiCheck.RandomSleep(1)
	AntiCheck.RangeClick(OrderChange_X[MainIndex - 1], OrderChange_Y, OrderChange_R)
	AntiCheck.RandomSleep(1)
	AntiCheck.RangeClick(OrderChangeButton_X, OrderChangeButton_Y, OrderChangeButton_R)

def FGO_Action_RandomPickCard(CardNum):
	Cards = []
	while (CardNum != 0):
		Card = random.randint(1, 5)
		if (Card in Cards):
			continue
		Cards.append(Card)
		CardNum = CardNum - 1
	
	for i in Cards:
		FGO_Action_SelectCard(i)

def FGO_Action_FreeAttack():
	basefunc.Log("开始自由攻击")	
	FGO_Action_Attck()
	FGO_Action_RandomPickCard(3)

def FGO_Action_CheckStage():
	pos = basefunc.FindImageInRect(Round_X1, Round_Y1, Round_X2, Round_Y2, "Stage1.png", 0.7)
	if pos != None:
		return 1
	pos = basefunc.FindImageInRect(Round_X1, Round_Y1, Round_X2, Round_Y2, "Stage2.png", 0.7)
	if pos != None:
		return 2
	pos = basefunc.FindImageInRect(Round_X1, Round_Y1, Round_X2, Round_Y2, "Stage3.png", 0.7)
	if pos != None:
		return 3
		
	return None
	