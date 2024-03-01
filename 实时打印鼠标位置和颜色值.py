import pyautogui
import time

while True:
    x, y = pyautogui.position()
    color = pyautogui.pixel(x, y)
    print(f"鼠标位置： ({x}, {y})，颜色值： {color}")
    time.sleep(1)  # 每隔1秒打印一次鼠标位置
