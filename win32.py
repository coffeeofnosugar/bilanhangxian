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
import random
import json


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
        def wrapper(self, img, max_time = 10, interval = 0.5, *args, **kwargs):
            start_time = time.time()
            # timer = 0
            while True:
                time.sleep(interval)
                elapsed_time = time.time() - start_time
                # timer += 1
                if elapsed_time > max_time:
                    break
                result = func(self, img, max_time, interval, *args, **kwargs)
                if result:
                    return result
        return wrapper
    

    def GetScreenShot(func):
        """获取屏幕截图"""
        # def wrapper(self, img, max_time = 10, interval = 0.5, threshold =0.8, left_top = (0, 0), right_bottom = (0, 0)):
        def wrapper(self, *args, **kwargs):
            print("get screenshot")
            screenshot = np.array(pyautogui.screenshot())
            roi = screenshot[ : self.height,  : self.width]
            # 转换为灰度图
            self.gameImage = cv2.cvtColor(np.array(roi), cv2.COLOR_BGR2GRAY)
            # cv2.imshow("Output", self.gameImage)
            # cv2.waitKey(0)
            return func(self, *args, **kwargs)
        return wrapper

    @GetScreenShot
    def FindTargetWithoutTimeOut(self, img, max_time = 10, interval = 0.5, threshold =0.8, left_top = (0, 0), right_bottom = (0, 0)):
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


        num = len(locations)
        if num != 0:
            print("find {} matching image".format(num))
            for i in range(num):
                top_left = locations[i]
                bottom_right = (top_left[0] + img.shape[1], top_left[1] + img.shape[0])
                locations[i] = (int(top_left[0] + img.shape[1]/2) + left_top[0], int(top_left[1] + img.shape[0]/2) + left_top[1])
                cv2.rectangle(self.gameImage, top_left, bottom_right, (0, 255, 0), 2)               # 画方框，标记出来
                # print("------------------------------find image: ", locations[i])
                # cv2.imshow("Output", self.gameImage)
                # cv2.waitKey(0)

            # 去重
            result = []
            img_hw = img.shape[1]/2
            img_hh = img.shape[0]/2
            for x, y in locations:
                flag = False
                for rx, ry in result:
                    if rx - img_hw < x < rx + img_hw and ry - img_hh < y < ry + img_hh:
                        flag = True
                        break
                if not flag:
                    result.append((x, y))
            print("duplicate removal result: ", result)
            return result



    @TimeOut
    @GetScreenShot
    def FindTarget(self, img, max_time = 10, interval = 0.5, threshold =0.9, left_top = (0, 0), right_bottom = (0, 0)):
        '''
        寻找图片所在位置
        :param img: 图片
        :param max_time: 寻找图片最大时间
        :param interval: 寻找时间间隔
        :param threshold: 图片匹配阈值
        '''
        if right_bottom[0] > len(self.gameImage[0]) or right_bottom[1] > len(self.gameImage) or right_bottom == (0, 0):
            right_bottom = (len(self.gameImage[0]), len(self.gameImage))
        
        self.gameImage = self.gameImage[left_top[1] : right_bottom[1], left_top[0] : right_bottom[0]]
        # cv2.imshow("Output", self.gameImage)
        # cv2.waitKey(0)
        result = cv2.matchTemplate(self.gameImage, img, cv2.TM_CCOEFF_NORMED)

        print("finding image:")
        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))

        num = len(locations)
        if num != 0:
            print("find {} matching image".format(num))
            for i in range(num):
                top_left = locations[i]
                bottom_right = (top_left[0] + img.shape[1], top_left[1] + img.shape[0])
                locations[i] = (int(top_left[0] + img.shape[1]/2) + left_top[0], int(top_left[1] + img.shape[0]/2) + left_top[1])
                cv2.rectangle(self.gameImage, top_left, bottom_right, (0, 255, 0), 2)               # 画方框，标记出来
                # print("------------------------------find image: ", locations[i])
                # cv2.imshow("Output", self.gameImage)
                # cv2.waitKey(0)

            # 去重
            result = []
            img_hw = img.shape[1]/2
            img_hh = img.shape[0]/2
            for x, y in locations:
                flag = False
                for rx, ry in result:
                    if rx - img_hw < x < rx + img_hw and ry - img_hh < y < ry + img_hh:
                        flag = True
                        break
                if not flag:
                    result.append((x, y))
            print("duplicate removal result: ", result)
            return result

        


        
    def GetImageOnGame(self, left_top, right_bottom):
        '''
        从游戏中获取图片
        '''
        print("get image on game")
        screenshot = np.array(pyautogui.screenshot())
        # # 画线，测试用
        # cv2.rectangle(screenshot, left_top, right_bottom, (0, 255, 0), 1)
        # cv2.imshow("Output", screenshot)
        # cv2.waitKey(0)
        print(left_top[0] , left_top[1], right_bottom[0] , right_bottom[1])
        # 截取图片参数为[y1 : y2, x1 : x2]
        roi = screenshot[left_top[1] : right_bottom[1], left_top[0] : right_bottom[0]]
        img = cv2.cvtColor(np.array(roi), cv2.COLOR_BGR2GRAY)
        # cv2.imshow("Output", roi)
        # cv2.waitKey(0)
        return img
    

    def wheel(self, position=(640,404), lenth=0.1):
        pass

















        
    def zheng_li(self):
        self.flag = True
        zl = ".\\image\\zhengli\\"
        zl_img = GetImage(zl + "zl.png")
        while self.flag:
            time.sleep(10)
            result = LeftSingleClick(self.FindTargetWithoutTimeOut(zl_img))
            if result:
                LeftSingleClick(self.FindTarget(GetImage(zl + "yjty.png")))
                time.sleep(1)
                LeftSingleClick(self.FindTarget(GetImage(zl + "qd.png"), left_top=(920,640), right_bottom=(1110,720)))
                LeftSingleClick(self.FindTarget(GetImage(zl + "djjx.png")))
                LeftSingleClick(self.FindTarget(GetImage(zl + "qd.png")))
                LeftSingleClick(self.FindTarget(GetImage(zl + "qd.png")))
                LeftSingleClick(self.FindTarget(GetImage(zl + "djjx.png")))
                time.sleep(1)
                LeftSingleClick((55, 88))
                LeftSingleClick(self.FindTarget(GetImage(zl + "zlxd.png")))

    def yan_xi(self, timer):
        imgName = ".\\image\\cj.png"
        result = LeftSingleClick(self.FindTarget(GetImage(imgName)))
        result = LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\yx.png")))


        while timer > 0:
            timer -= 1
            LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\zhsl.png")))
            LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\ksyx.png")))
            LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\cj.png")))
            time.sleep(30)
            LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\djjx.png"), 120, 5, threshold=0.6, left_top=(85,625), right_bottom=(280,700)))
            LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\djjx1.png")))
            LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\qd.png"), threshold=0.6, left_top=(1087,665), right_bottom=(1267,730)))
            LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\djgb.png"), max_time=3), 1.2)



    def zuo_zhan_dang_an(self, timer):
        zzda = ".\\image\\zuozhandangan\\"
        LeftSingleClick(self.FindTarget(GetImage(".\\image\\cj.png")))
        LeftSingleClick(self.FindTarget(GetImage(zzda + "zzda.png")))
        LeftSingleClick(self.FindTarget(GetImage(zzda + "no2.png")))
        LeftSingleClick(self.FindTarget(GetImage(zzda + "D3.png")))
        timer -= 1
        LeftSingleClick(self.FindTarget(GetImage(zzda + "lkqw.png")))
        LeftSingleClick(self.FindTarget(GetImage(zzda + "lkqw1.png")))
        LeftSingleClick(self.FindTarget(GetImage(zzda + "qd.png")))
        
        t = threading.Thread(target=self.zheng_li)
        t.start()

        print("{} runs left".format(timer))
        time.sleep(360)
        print("timer:", timer)
        while timer > 0:
            timer -= 1
            LeftSingleClick(self.FindTarget(GetImage(zzda + "zcqw.png"), 180, 5))
            LeftSingleClick(self.FindTarget(GetImage(zzda + "qd.png")))
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), "wait for fight:")
            print("----------------------------还剩：", timer, "次")
            time.sleep(360)
        print("zuo_zhan_dang_an is over")
        self.flag = False
        print("close the zheng_li, self.flag=", self.flag)

    

    def ji_dian_mei_shi(self):
        one = [(182, 265), (305, 352)]
        two = [(310, 265), (433, 352)]
        there = [(438, 265), (561, 352)]


        jdms = ".\\image\\jidianmeishi\\"
        LeftSingleClick(self.FindTarget(GetImage(jdms + "ksyx.png")))
        timer = 9
        while timer > 0:
            timer -= 1
            print(f"还剩{timer}次")
            time.sleep(1)
            one_img = self.GetImageOnGame(one[0], one[1])
            two_img = self.GetImageOnGame(two[0], two[1])
            there_img = self.GetImageOnGame(there[0], there[1])

            time.sleep(5.5)

            isDone_one = LeftSingleClick(self.FindTarget(one_img, max_time=1, interval=0.1, threshold=0.6, left_top=(600, 250), right_bottom=(1110,660)), wait=0.2)
            time.sleep(random.random())
            isDone_two = LeftSingleClick(self.FindTarget(two_img, max_time=1, interval=0.1, threshold=0.6, left_top=(600, 250), right_bottom=(1110,660)), wait=0.2)
            time.sleep(random.random())
            isDone_there = LeftSingleClick(self.FindTarget(there_img, max_time=1, interval=0.1, threshold=0.6, left_top=(600, 250), right_bottom=(1110,660)), wait=0.2)
            time.sleep(random.random())
            if isDone_one == False or isDone_two == False or isDone_there == False:
                print("至少有一个匹配失败")
                LeftSingleClick([(670, 330)], 0.2)
                LeftSingleClick([(850,330)], 0.2)
                LeftSingleClick([(1030,330)], 0.2)
                LeftSingleClick([(670, 470)], 0.2)
                LeftSingleClick([(850,470)], 0.2)
                LeftSingleClick([(1030,470)], 0.2)
            if timer > 0:
                LeftSingleClick(self.FindTarget(GetImage(jdms + "jxyx.png")))
        
    def huo_dong(self, timer):
        hd = ".\\image\\huodong\\"
        LeftSingleClick(self.FindTarget(GetImage(hd + "HT6.png")))
        LeftSingleClick(self.FindTarget(GetImage(hd + "lkqw.png")))
        time.sleep(0.5)
        timer -= 1
        LeftSingleClick(self.FindTarget(GetImage(hd + "lkqw.png")))
        time.sleep(400)


        while timer > 0:
            timer -= 1
            LeftSingleClick(self.FindTarget(GetImage(hd + "zcqw.png"), max_time=180, interval=5))
            time.sleep(400)







def ReturnPath(relative_path:str) -> str:
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)



def GetImage(imgName):
    print("turn :", imgName)

    return cv2.imread(ReturnPath(imgName), 0)


def LeftSingleClick(locations, wait = 0.5):
    '''
    单击左键
     :param locations: 坐标组，[(x1,y1), (x2, y2)...]
     :param wait_: 等待时间, 默认0.5秒
    '''
    print("wait_    ", wait)
    time.sleep(wait)
    if locations:
        # pyautogui.click(pos[0])
        print(locations)
        pydirectinput.leftClick(int(locations[0][0]), int(locations[0][1]))
        print("click success")
        return True
    else:
        print("no find image")
        return False

def test(item):
    print("++++++++++++++++++++++++++++++++++++")


if __name__ == '__main__':
    print(__name__)
    pass
    b = BiLanHangXian()
    # time.sleep(1)
    b.ji_dian_mei_shi()



    # while True:
    #     a = input()
    #     if a == "yanxi":
    # b.yan_xi(1)
    #     elif a == "zzda" or a == "zuozhandangan":
            # b.zuo_zhan_dang_an()
    # b.zuo_zhan_dang_an(3)
    # b.ji_dian_mei_shi()
    # b.huo_dong(3)


    # b.zheng_li()
    # zl = ".\\image\\zhengli\\"
    # b.FindTarget(GetImage(zl + "qd.png"), left_top=(920,640), right_bottom=(1110,720))
    # b.FindTarget(GetImage(".\\image\\jidianmeishi\\ksyx.png"), left_top=(600, 250), right_bottom=(1110,660))
    
    
    # LeftSingleClick(b.FindTarget(GetImage("a.png")))




    # b.FindTarget(GetImage(".\\image\\yanxi\\zhsl.png"), left_top=(100, 260))
    # test(b.FindTarget(GetImage(".\\image\\test.png")))


    # test(b.FindTarget(GetImage(".\\image\\test_1.png")))
    