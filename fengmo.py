import pyautogui, sys, time, random
import datetime as dt
print('Program started.')
# screen size: 1136*640
# Note where the bot's window is.
input('自动逢魔')
botWindow = pyautogui.position()

# mouse click at (x,y) by random variance z.
def randomClick(x , y, z):
    clickNum = 2
    for i in range(clickNum):
        pyautogui.moveTo(x + random.randint(0,z),y+ random.randint(0,z))
        pyautogui.click()

def waitFM():
    print('Searching for fengmo')
    while True:
        fengmo1 =  pyautogui.locateOnScreen('fengmo.png')
        fengmo2 =  pyautogui.locateOnScreen('fengmo2.png')
        if fengmo1 is not None or fengmo2 is not None:
            if fengmo1 is not None:
                randomClick(fengmo1[0], fengmo1[1], 0)
            else:
                randomClick(fengmo2[0], fengmo2[1], 0)
            break
        time.sleep(30)
        

def startFM():
    print('Start fengmo')
    while True:
        fengmo1 =  pyautogui.locateOnScreen('participate.png')
        fengmo2 =  pyautogui.locateOnScreen('goto.png')
        if fengmo1 is not None or fengmo2 is not None:
            if fengmo1 is not None:
                randomClick(fengmo1[0], fengmo1[1], 0)
            else:
                randomClick(fengmo2[0], fengmo2[1], 0)
                break

def clickFM():
    print('click 4 times search')
    while True:
        fengmo1 = pyautogui.locateOnScreen('xian.png')
        if fengmo1 is not None:
            for x in range(4):
                randomClick(fengmo1[0]+40, fengmo1[1]-30, 0)
                time.sleep(5)
            randomClick(fengmo1[0]+120, fengmo1[1]-400, 0)
            break

def FMBoss():
    print('Find Boss')
    while True:
        boss =  pyautogui.locateOnScreen('findboss.png') 
        if boss is not None:
            randomClick(boss[0], boss[1], 0)
            randomClick(boss[0]-350,boss[1]-300,0)
        fightboss = pyautogui.locateOnScreen('fightboss.png') 
        if fightboss is not None:
            randomClick(fightboss[0], fightboss[1], 0)
        yes = pyautogui.locateOnScreen('yes.png') 
        if yes is not None:
            randomClick(yes[0], yes[1], 0)
            break


if __name__ == "__main__":
    sleepTime = int(input("输入几小时后开始封魔:  ")) 
    print("将游戏界面拉到最左，等待封魔开始 \n")
    time.sleep(sleepTime*3600)
    waitFM()
    startFM()
    clickFM()
    FMBoss()