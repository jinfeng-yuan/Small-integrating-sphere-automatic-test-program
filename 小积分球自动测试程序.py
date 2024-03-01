from re import I
import pyautogui

strat = 50 #输入开始电流
finish = 150 #输入结束电流
interval = 5 #输入间隔电流
i = 0

while i < finish:
    if i == 0:
        print("开始测试...")
        pyautogui.moveTo(864,214,1,pyautogui.easeInOutQuad)
        pyautogui.click()
        pyautogui.hotkey('ctrl','a')
        pyautogui.hotkey('del')
        pyautogui.write(str(strat))
        pyautogui.hotkey('enter')
        pyautogui.moveTo(864,214,5,pyautogui.easeInOutQuad) #第一次测试时间
        pyautogui.click()
        pyautogui.hotkey('ctrl','a')
        pyautogui.hotkey('del')
        i = strat
        print("电流I=" + str(i) + "ma")
    elif i == finish - interval:
        i = i + interval        
        pyautogui.moveTo(864,214,0.2,pyautogui.easeInOutQuad)
        pyautogui.click()
        pyautogui.write(str(i))
        pyautogui.moveTo(864,214,0.5,pyautogui.easeInOutQuad)
        pyautogui.hotkey('enter')
        print("电流I=" + str(i) + "ma")
        print("测试结束")
        
    else:
        i = i + interval        
        pyautogui.moveTo(864,214,0.2,pyautogui.easeInOutQuad)
        pyautogui.click()
        pyautogui.write(str(i))
        pyautogui.moveTo(864,214,0.5,pyautogui.easeInOutQuad)
        pyautogui.hotkey('enter')
        pyautogui.moveTo(864,214,5,pyautogui.easeInOutQuad) #测试时间
        pyautogui.click()
        pyautogui.hotkey('ctrl','a')
        pyautogui.hotkey('del')
        print("电流I=" + str(i) + "ma")

#pyautogui.moveTo(x,y,z,pyautogui.easeInOutQuad)其中x,y为屏幕坐标，z为鼠标移动时间
#author：袁工
        
