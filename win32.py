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
import ctypes
import sys


# def get_window_titles():
#     titles = []

#     def callback(hwnd, lParam):
#         if win32gui.IsWindowVisible(hwnd):
#             titles.append(win32gui.GetWindowText(hwnd))
#             # if "MuMu" in win32gui.GetWindowText(hwnd):
#             #     win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0, 0, 0, 0, win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)
#             #     print("yes")
#         return True
#     win32gui.EnumWindows(callback, None)
#     return titles


# titles = get_window_titles()
# print(titles)

class BiLanHangXian():
    def __init__(self):
        self.width, self.height = 1720, 1050
        self.gameImage = ""
    # 子类被定义时执行，也就是class MySubclass(MyClass):
    def __init_subclass__(cls):
        pass

    @staticmethod  # 声明该方法为静态方法
    def MoveWindown():
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
        hwnd_cmd = win32gui.FindWindow(None, r"D:\anaconda\python.exe")
        if hwnd_cmd != 0:
            win32api.SendMessage(hwnd_cmd, win32con.WM_CLOSE, 0, 0)

    def GetScreenShot(self):
        """获取屏幕截图
        """
        screenshot = np.array(pyautogui.screenshot())

        # 截取指定区域，切片方法
        roi = screenshot[ : self.height,  : self.width]
        # 将图片转换成黑白
        self.gameImage = cv2.cvtColor(np.array(roi), cv2.COLOR_BGR2GRAY)

        # # 显示截图
        # cv2.imshow("ROI", gray_image)
        # cv2.waitKey(0)


class YanXi(BiLanHangXian):
    def __init__(self):
        super().__init__()
        # 移动游戏窗口到屏幕的左上角
        super().MoveWindown()
        pass

    def SingleClick(self, imgName):
        # 第二个参数设置为0，是将图片读取为黑白图片
        img = cv2.imread(imgName, 0)
        # 匹配方法：
        # result = cv2.matchTemplate(map_thresh, target_img, cv2.TM_CCOEFF_NORMED)
        # print(img)
        # print(self.gameImage)
        result = cv2.matchTemplate(self.gameImage, img, cv2.TM_CCOEFF_NORMED)
        print(type(result))


if __name__ == '__main__':
    yanxi = YanXi()

    yanxi.GetScreenShot()
    yanxi.SingleClick("bilanhangxian.png")
