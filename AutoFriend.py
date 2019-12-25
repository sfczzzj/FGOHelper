import basefunc
import FGOFunc
import AntiCheck
import time
import os

while(True):
	FGOFunc.FGO_WaitAndClick_FriendSummon()
	FGOFunc.FGO_WaitAndClick_FriendSummonConfirm()
	FGOFunc.FGO_WaitAndClick_FinishFriendSummon()
