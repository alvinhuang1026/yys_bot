import pyautogui, sys, time, random
print('Program started.')

# Note where the bot's window is..
input('打开游戏，组队界面，锁定阵容自动邀请，自动接受邀请, 回车开始')
yysWindow = pyautogui.locateOnScreen('yysWindow.png')
if yysWindow is None:
    sys.exit('Could not find game on screen. Is the game visible?')
print('Game Starts, auto-playing')
# mouse click at (x,y) by random variance of z.
def randomClick(x, y, z):
    clickNum = random.randint(3,5)
    speed = random.randint(10,40)
    for i in range(clickNum):
        pyautogui.moveTo(x + random.randint(0,z),y+ random.randint(0,z), speed/100)
        pyautogui.click()
    

def randomMove(moveTime):
    x = moveTime + time.perf_counter()
    while time.perf_counter() < x:
        speed = random.randint(10,100)
        pyautogui.moveTo(random.randint(yysWindow[0],yysWindow[0]+1136),random.randint(yysWindow[1],yysWindow[1]+640),speed/30)
        time.sleep(speed/50)

def HostMode():
    print('Host Mode')
    while True:
        startIcon =  pyautogui.locateOnScreen('start.png')
        if startIcon is not None:
            randomClick(startIcon[0], startIcon[1], 50)
            randomMove(20)
            print('waiting for game to finish')
            while True:
                successIcon = pyautogui.locateOnScreen('success.png')
                if successIcon is not None:
                    print('Succeed')
                    randomClick(yysWindow[0]+100, yysWindow[1]+400, 100)
                    time.sleep(1.5)
                    randomClick(yysWindow[0]+800, yysWindow[1]+400, 200)
                    break

def PassengerMode():
    print('passenger Mode')
    while True:
        successIcon = pyautogui.locateOnScreen('success.png')
        if successIcon is not None:
            print('Succeed')
            randomClick(yysWindow[0]+100, yysWindow[1]+400, 100)
            time.sleep(1.5)
            randomClick(yysWindow[0]+100, yysWindow[1]+300, 200)
            print('waiting for game to finish')
            randomMove(20)
            
if __name__ == "__main__":
    mode = input ("房主输入1，乘客输入2 ")
    print(mode)
    if mode == '1':
        print("Auto play will be enabled at Ready page \n Do not click during the time")
        HostMode()
    if mode == '2':
        print("Auto play enabled \n Do not click during the time")
        PassengerMode()
      