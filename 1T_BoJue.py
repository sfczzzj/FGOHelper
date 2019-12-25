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
	FGOFunc.FGO_Action_UseSkill(1, 2, None)	#伯爵黄金率
	FGOFunc.FGO_WaitFor_Attack()
	FGOFunc.FGO_Action_UseSkill(2, 1, 1) #CBA绿魔放
	FGOFunc.FGO_WaitFor_Attack()
	FGOFunc.FGO_Action_UseSkill(3, 1, 1) #CBA绿魔放
	FGOFunc.FGO_WaitFor_Attack()
	FGOFunc.FGO_Action_UseSkill(2, 3, 1) #CBA给伯爵充能
	FGOFunc.FGO_WaitFor_Attack()
	FGOFunc.FGO_Action_UseSkill(2, 2, None) #CBA降防
	FGOFunc.FGO_WaitFor_Attack()
	FGOFunc.FGO_Action_UseSkill(3, 2, None) #CBA降防
	FGOFunc.FGO_WaitFor_Attack()
	FGOFunc.FGO_Action_UseSkill(3, 3, 1) #CBA给伯爵充能
	FGOFunc.FGO_WaitFor_Attack()
	FGOFunc.FGO_Action_UseSkill(1, 1, None) #伯爵加攻
	FGOFunc.FGO_WaitFor_Attack()
	FGOFunc.FGO_Action_UseMasterSkill(2, 1) #御主技能加攻
	FGOFunc.FGO_WaitFor_Attack()
	FGOFunc.FGO_Action_UseMasterSkill(3, 1) #御主技能加攻
	FGOFunc.FGO_WaitFor_Attack()
	FGOFunc.FGO_Action_Attck()
	FGOFunc.FGO_Action_SelectNoble(1) #伯爵宝具
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
	res = FGOFunc.FGO_WaitFor_FinishBattleNextButton(5)
	if res == True:
		FGOFunc.FGO_Action_FinishBattle()
