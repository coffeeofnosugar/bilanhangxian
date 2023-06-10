# -*- coding: utf-8 -*-
from typing import Any
import numpy as np
import ctypes
import sys
import os
import win32gui
import win32api
import win32con
import cv2
import pyautogui
import pydirectinput
import ctypes
import sys
import time

# 找图的最大时间
max_time = 2

def TimeOut(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        # timer = 0
        while True:
            elapsed_time = time.time() - start_time
            # timer += 1
            if elapsed_time > max_time:
            # if timer > 50:
                break
            if func(*args, **kwargs):
                return func(*args, **kwargs)
    return wrapper




class BiLanHangXian():
    def __init__(self):
        self.width, self.height = 1280, 809
        self.gameImage = ""
        # 设置阈值
        self.threshold = 0.8
        # 移动游戏窗口到屏幕的左上角
        self.MoveWindow()
    # 子类被定义时执行，也就是class MySubclass(MyClass):
    def __init_subclass__(cls):
        pass

    @staticmethod  # 声明该方法为静态方法
    def MoveWindow():
        """将游戏窗口移动到屏幕左上角
        
        声明成为了静态方法

        在创建子类时在__init__()函数中调用此方法
        """
        # 定义回调函数，用于查找窗叄1�71ￄ1�77
        def callback(hwnd, extra):
            # 如果窗口标题匹配，则设置窗口位置
            if extra in win32gui.GetWindowText(hwnd):
                win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0, 0, 0, 0, win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)

        # 绕开管理系统
        def is_admin():
            try:
                return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                return False

        if is_admin():
            # Code of your program here
            # 遍历所有窗口，查找指定窗口并设置位置
            win32gui.EnumWindows(callback, "MuMu")
            print('done')
        else:
            # Re-run the program with admin rightsd
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        # 寻找命令行窗口，并关闭
        hwnd_cmd = win32gui.FindWindow(None, r"C:\Users\zhengchang\AppData\Local\Programs\Python\Python311\python.exe")
        if hwnd_cmd != 0:
            win32api.SendMessage(hwnd_cmd, win32con.WM_CLOSE, 0, 0)
        # hwnd_cmd = win32gui.FindWindow(None, r"win32.bat - 快捷方式")
        # if hwnd_cmd != 0:
        #     win32api.SendMessage(hwnd_cmd, win32con.WM_CLOSE, 0, 0)

    def GetScreenShot(func):
        """获取屏幕截图"""
        def wrapper(self, img):
            print("get screenshot")
            screenshot = np.array(pyautogui.screenshot())
            roi = screenshot[ : self.height,  : self.width]
            self.gameImage = cv2.cvtColor(np.array(roi), cv2.COLOR_BGR2GRAY)
            # cv2.imshow("Output", self.gameImage)
            # cv2.waitKey(0)
            return func(self, img)
        return wrapper


    @TimeOut
    @GetScreenShot
    def FindTarget(self, img):
        result = cv2.matchTemplate(self.gameImage, img, cv2.TM_CCOEFF_NORMED)
        print("finding image")
        locations = np.where(result >= self.threshold)
        locations = list(zip(*locations[::-1]))
        if len(locations) != 0:
            top_left = locations[0]
            bottom_right = (top_left[0] + img.shape[1], top_left[1] + img.shape[0])
            locations[0] = (int(top_left[0] + img.shape[1]/2), int(top_left[1] + img.shape[0]/2))
            cv2.rectangle(self.gameImage, top_left, bottom_right, (0, 255, 0), 2)
            # cv2.imshow("Output", self.gameImage)
            # cv2.waitKey(0)
            print("start find--------------------", locations)
            return locations[0]
    
    @GetScreenShot
    def FindTargetByTime(self, img, time):
        while True:
            result = cv2.matchTemplate(self.gameImage, img, cv2.TM_CCOEFF_NORMED)
            print("finding image")
            locations = np.where(result >= self.threshold)
            locations = list(zip(*locations[::-1]))
            top_left = locations[0]
            bottom_right = (top_left[0] + img.shape[1], top_left[1] + img.shape[0])
            locations[0] = (int(top_left[0] + img.shape[1]/2), int(top_left[1] + img.shape[0]/2))
            cv2.rectangle(self.gameImage, top_left, bottom_right, (0, 255, 0), 2)
            # cv2.imshow("Output", self.gameImage)
            # cv2.waitKey(0)
            print("start find--------------------", locations[0])
            if len(locations) != 0:
                return locations[0]

    

    def yan_xi(self):
        imgName = ".\\image\\cj.png"
        result = LeftSingleClick(self.FindTarget(GetImage(imgName)))
        if result:
            result = LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\yx.png")))


            if result:
                LeftSingleClick((220, 220))
                result = LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\ksyx.png")))
                if result:
                    LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\cj.png")))
        time.sleep(60)
        LeftSingleClick((220, 220))
        LeftSingleClick((220, 220))
        result = LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\qd.png")))
        if result:
            result = LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\djgb.png")))
                        

    

def GetImage(imgName):
    print("turn :", imgName)
    return cv2.imread(imgName, 0)


# def LeftSingleClick(pos):
#     time.sleep(0.5)
#     if pos:
#         win32api.SetCursorPos(pos[0])
#         win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, pos[0][0], pos[0][1], 0, 0)
#         win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, pos[0][0], pos[0][1], 0, 0)
#         # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, pos[0][0], pos[0][1], 0, 0)
#         # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, pos[0][0], pos[0][1], 0, 0)
#         return True
#     else:
#         return False


def LeftSingleClick(pos):
    '''左键单击'''
    time.sleep(0.5)
    if pos:
        # pyautogui.click(pos[0])
        print(pos)
        pydirectinput.leftClick(int(pos[0]), int(pos[1]))
        print("click success")
        time.sleep(4)
        return True
    else:
        print("no find image")
        return False


if __name__ == '__main__':
    b = BiLanHangXian()
    time.sleep(1)
    # imgName = input()
    # imgName = "xs"
    # imgName = imgName + ".png"
    # timeout =  LeftSingleClick(b.FindTarget(GetImage(imgName)))
    b.yan_xi()