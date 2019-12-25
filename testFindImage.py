import basefunc
import cv2
import FGOFunc

#basefunc.GetBaseRect("命运-冠位指定 - MuMu模拟器")
#pos = basefunc.FindImageInRect(980, 60, 1005, 90, "Stage1.png", 0.7)
#print("Round1:")
#print(pos)
#pos = basefunc.FindImageInRect(980, 60, 1005, 90, "Stage2.png", 0.7)
#print("Round2:")
#print(pos)
#pos = basefunc.FindImageInRect(980, 60, 1005, 90, "Stage3.png", 0.7)
#print("Round3:")
#print(pos)
#print(FGOFunc.FGO_Action_CheckStage())
FGOFunc.FGO_Action_RandomPickCard(3)