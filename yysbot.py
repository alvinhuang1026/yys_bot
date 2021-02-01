import pyautogui, sys, time, random
print('Auto player started')
Scenes = ['lobby', 'discover', 'makeTeam',]
gameWindow = None
team = None
yuhun = None
def init():
    yysWindow = pyautogui.locateOnScreen('yysWindow.png')
    if window is None:
        sys.exit('Could not find game on screen. Is the game visible?')
    gameWindow = window

def identifyScene():
    while True:
        currScene = pyautogui.locateOnScreen('team.png')
        if currScene is not None:
            team = currScene
            break
        currScene = pyautogui.locateOnScreen('yuhun.png')
        if currScene is not None:
            team = currScene
            break

        
if __name__ == "__main__":
    init()
