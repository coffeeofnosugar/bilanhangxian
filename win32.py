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
import threading


class BiLanHangXian():
    def __init__(self):
        self.width, self.height = 1280, 809
        self.gameImage = ""
        # 移动游戏窗口到屏幕的左上角
        self.MoveWindow()
        self.flag = True
    # 子类被定义时执行，也就是class MySubclass(MyClass):
    def __init_subclass__(cls):
        pass

    @staticmethod  # 声明该方法为静态方法
    def MoveWindow():
        """将游戏窗口移动到屏幕左上角
        
        声明成为了静态方法

        在创建子类时在__init__()函数中调用此方法
        """
        # 定义回调函数，用于查找窗口
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

    def TimeOut(func):
        '''控制函数的执行时间和间隔
            默认每0.5s执行一次,共执行10s
        '''
        def wrapper(self, img, max_time = 10, interval = 0.5, threshold =0.8):
            start_time = time.time()
            # timer = 0
            while True:
                time.sleep(interval)
                elapsed_time = time.time() - start_time
                # timer += 1
                if elapsed_time > max_time:
                    break
                if func(self, img, max_time, interval, threshold):
                    return func(self, img, max_time, interval, threshold)
        return wrapper
    

    def GetScreenShot(func):
        """获取屏幕截图"""
        def wrapper(self, img, max_time = 10, interval = 0.5, threshold =0.8):
            print("get screenshot")
            screenshot = np.array(pyautogui.screenshot())
            roi = screenshot[ : self.height,  : self.width]
            self.gameImage = cv2.cvtColor(np.array(roi), cv2.COLOR_BGR2GRAY)
            # cv2.imshow("Output", self.gameImage)
            # cv2.waitKey(0)
            return func(self, img, max_time, interval, threshold)
        return wrapper


    @TimeOut
    @GetScreenShot
    def FindTarget(self, img, max_time = 10, interval = 0.5, threshold =0.8):
        '''
        寻找图片所在位置
        :param img: 图片名称
        :param max_time: 寻找图片最大时间
        :param interval: 寻找时间间隔
        :param threshold: 图片匹配阈值
        '''
        result = cv2.matchTemplate(self.gameImage, img, cv2.TM_CCOEFF_NORMED)
        print("finding image:")
        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))
        if len(locations) != 0:
            top_left = locations[0]
            bottom_right = (top_left[0] + img.shape[1], top_left[1] + img.shape[0])
            locations[0] = (int(top_left[0] + img.shape[1]/2), int(top_left[1] + img.shape[0]/2))
            cv2.rectangle(self.gameImage, top_left, bottom_right, (0, 255, 0), 2)
            # cv2.imshow("Output", self.gameImage)
            # cv2.waitKey(0)
            print("start find--------------------", locations[0])
            return locations[0]
        
    def zheng_li(self):
        self.flag = True
        zl = ".\\image\\zhengli\\"
        while self.flag:
            print(self.flag)
            result = LeftSingleClick(self.FindTarget(GetImage(zl + "zl.png"), 10, interval=10))
            if result:
                LeftSingleClick(self.FindTarget(GetImage(zl + "yjty.png")))
                LeftSingleClick(self.FindTarget(GetImage(zl + "qd.png")))
                LeftSingleClick(self.FindTarget(GetImage(zl + "djjx.png")))
                LeftSingleClick(self.FindTarget(GetImage(zl + "qd.png")))
                LeftSingleClick(self.FindTarget(GetImage(zl + "qd.png")))
                LeftSingleClick(self.FindTarget(GetImage(zl + "djjx.png")))
                time.sleep(1)
                LeftSingleClick((55, 88))
                LeftSingleClick(self.FindTarget(GetImage(zl + "zlxd.png")))

    def yan_xi(self):
        imgName = ".\\image\\cj.png"
        result = LeftSingleClick(self.FindTarget(GetImage(imgName)))
        result = LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\yx.png")))



        result = LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\zhsl.png")))
        result = LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\ksyx.png")))
        result = LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\cj.png")))
        result = LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\djjx.png"), 120, 5))
        result = LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\djjx1.png")))
        result = LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\qd.png"), threshold=0.5))
        result = LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\djgb.png")))


    def zuo_zhan_dang_an(self, timer):
        LeftSingleClick(self.FindTarget(GetImage(".\\image\\cj.png")))
        zzda = ".\\image\\zuozhandangan\\"
        LeftSingleClick(self.FindTarget(GetImage(zzda + "zzda.png")))
        LeftSingleClick(self.FindTarget(GetImage(zzda + "no2.png")))
        LeftSingleClick(self.FindTarget(GetImage(zzda + "D3.png")))
        LeftSingleClick(self.FindTarget(GetImage(zzda + "lkqw.png")))
        LeftSingleClick(self.FindTarget(GetImage(zzda + "lkqw1.png")))
        LeftSingleClick(self.FindTarget(GetImage(zzda + "qd.png")))
        
        t = threading.Thread(target=self.zheng_li)
        t.start()
        print("start find zheng_li", self.flag)

        timer -= 1
        print("{} runs left".format(timer))
        time.sleep(360)

        while timer > 0:
            timer -= 1
            print("{} runs left".format(timer - 1))
            LeftSingleClick(self.FindTarget(GetImage(zzda + "zcqw.png"), 180, 5))
            LeftSingleClick(self.FindTarget(GetImage(zzda + "qd.png")))
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), "wait for fight:")
            time.sleep(360)
        print("zuo_zhan_dang_an over".format())
        self.flag = False
        print(self.flag)







    

def GetImage(imgName):
    print("turn :", imgName)
    return cv2.imread(imgName, 0)



def LeftSingleClick(pos):
    '''左键单击'''
    time.sleep(0.5)
    if pos:
        # pyautogui.click(pos[0])
        print(pos)
        pydirectinput.leftClick(int(pos[0]), int(pos[1]))
        print("click success")
        return True
    else:
        print("no find image")
        return False


if __name__ == '__main__':
    b = BiLanHangXian()
    time.sleep(1)
    # while True:
    #     a = input()
    #     if a == "yanxi":
    #         b.yan_xi()
    #     elif a == "zzda" or a == "zuozhandangan":
            # b.zuo_zhan_dang_an()
    b.zuo_zhan_dang_an(2)