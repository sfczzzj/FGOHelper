import basefunc
import FGOFunc
import AntiCheck
import time
import os

basefunc.GetBaseRect("命运-冠位指定 - MuMu模拟器")
#basefunc.GetBaseRect("MuMu模拟器")

while(True):
	FGOFunc.FGO_WaitFor_StageSelect()
	FGOFunc.FGO_Action_SelectDefaultStage()
	FGOFunc.FGO_WaitFor_AssistantSelect()
	FGOFunc.FGO_Action_SelectAssisant("PreferAssistant_BoJue.png")
	FGOFunc.FGO_WaitFor_TeamConfrim()
	FGOFunc.FGO_Action_ConfirmTeam()
	FGOFunc.FGO_WaitFor_Attack()
	#第一面
	#FGOFunc.FGO_Action_UseSkill(2, 1, None)	#尼托一技能
	#FGOFunc.FGO_WaitFor_Attack()
	FGOFunc.FGO_Action_UseSkill(2, 2, None) #尼托充能
	FGOFunc.FGO_WaitFor_Attack()
	FGOFunc.FGO_Action_Attck()
	FGOFunc.FGO_Action_SelectNoble(2) #尼托宝具
	FGOFunc.FGO_Action_RandomPickCard(2)
	FGOFunc.FGO_WaitFor_Attack()
	Stage = FGOFunc.FGO_Action_CheckStage()
	while (Stage == 1):	#未切换到下一面自由攻击补刀
		FGOFunc.FGO_Action_FreeAttack()
		FGOFunc.FGO_WaitFor_Attack()
		Stage = FGOFunc.FGO_Action_CheckStage()
	#第二面
	FGOFunc.FGO_Action_OrderChange(4, 2) #尼托换CBA
	FGOFunc.FGO_WaitFor_Attack()
	FGOFunc.FGO_Action_UseSkill(2, 1, 1) #CBA绿魔放
	FGOFunc.FGO_WaitFor_Attack()
	FGOFunc.FGO_Action_UseSkill(3, 1, 1) #CBA绿魔放
	FGOFunc.FGO_WaitFor_Attack()
	#FGOFunc.FGO_Action_UseSkill(1, 2, None) #伯爵黄金率
	#FGOFunc.FGO_WaitFor_Attack()
	FGOFunc.FGO_Action_Attck()
	FGOFunc.FGO_Action_SelectNoble(1) #伯爵宝具
	FGOFunc.FGO_Action_RandomPickCard(2)
	FGOFunc.FGO_WaitFor_Attack()
	Stage = FGOFunc.FGO_Action_CheckStage()
	while (Stage == 2):	#未切换到下一面自由攻击补刀
		FGOFunc.FGO_Action_FreeAttack()
		FGOFunc.FGO_WaitFor_Attack()
		Stage = FGOFunc.FGO_Action_CheckStage()
	#第三面
	FGOFunc.FGO_Action_UseSkill(2, 2, None) #CBA降防
	FGOFunc.FGO_WaitFor_Attack()
	FGOFunc.FGO_Action_UseSkill(3, 2, None) #CBA降防
	FGOFunc.FGO_WaitFor_Attack()
	FGOFunc.FGO_Action_UseSkill(2, 3, 1) #CBA给伯爵充能
	FGOFunc.FGO_WaitFor_Attack()
	FGOFunc.FGO_Action_UseSkill(3, 3, 1) #CBA给伯爵充能
	FGOFunc.FGO_WaitFor_Attack()
	#FGOFunc.FGO_Action_UseSkill(1, 1, None) #伯爵加攻
	#FGOFunc.FGO_WaitFor_Attack()
	#FGOFunc.FGO_Action_UseMasterSkill(1, None) #御主技能加攻
	#FGOFunc.FGO_WaitFor_Attack()
	FGOFunc.FGO_Action_Attck()
	FGOFunc.FGO_Action_SelectNoble(1)
	FGOFunc.FGO_Action_RandomPickCard(2)
	#回合结束
	isEnd = FGOFunc.FGO_WaitFor_BattleEnd(10)
	while (isEnd == False): #未结束战斗自由攻击补刀
		isInStage = FGOFunc.FGO_WaitFor_Attack(5)
		if isInStage == True:
			FGOFunc.FGO_Action_FreeAttack()
		isEnd = FGOFunc.FGO_WaitFor_BattleEnd(10)
	FGOFunc.FGO_WaitFor_FinishBattleNextButton()
	FGOFunc.FGO_Action_FinishBattle()
