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


from Customize.mathf import tuple_add



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
    def FindTargetWithoutTimeOut(self, img, threshold =0.8, left_top = (0, 0), right_bottom = (0, 0)):
        '''
        寻找图片所在位置
        :param img: 图片名称
        :param max_time: 寻找图片最大时间
        :param interval: 寻找时间间隔
        :param threshold: 图片匹配阈值
        '''
        if right_bottom[0] > len(self.gameImage[0]) or right_bottom[1] > len(self.gameImage) or right_bottom == (0, 0):
            right_bottom = (len(self.gameImage[0]), len(self.gameImage))
        
        self.gameImage = self.gameImage[left_top[1] : right_bottom[1], left_top[0] : right_bottom[0]]
        # 寻找图片的范围
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
        else:
            print('no find image')



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
        # 寻找图片的范围
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
        else:
            print('no find image')

        


        
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
            LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\djgb.png"), max_time=1), 1.2)

    @staticmethod
    def move(location):
        triangle_offset = (54, 51)
        for i in range(len(location)):
            location[i] = tuple_add(location[i], triangle_offset)
        if location[0][1] < 337:
            print('top')
            LeftSingleClick((636,306))
            time.sleep(1)
        elif location[0][1] > 451:
            print('down')
            LeftSingleClick((636,492))
            time.sleep(1)
        
        time.sleep(1)
        LeftDoubleClick([(1023,717)], interval_=0.5)

        if location[0][0] < 714:
            print("left")
            LeftSingleClick((511,394))
            time.sleep(1)
        elif location[0][0] > 714:
            print("right")
            LeftSingleClick((764,394))
            time.sleep(1)


    def fu_ben(self):
        fb = ".\\image\\fuben\\"


        while True:
            cj_image = self.FindTargetWithoutTimeOut(GetImage(".\\image\\yanxi\\cj.png"))


            if cj_image:
                LeftDoubleClick(cj_image)
                time.sleep(30)
                LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\djjx.png"), 120, 5, threshold=0.6, left_top=(85,625), right_bottom=(280,700)))
                LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\djjx1.png")))
                LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\qd.png"), threshold=0.6, left_top=(1087,665), right_bottom=(1267,730)))
            else:
                time.sleep(1)
                LeftDoubleClick([(1023,717)], interval_=0.5)
                one_location = self.FindTargetWithoutTimeOut(GetImage(fb + "1.png"), threshold=0.7)
                two_location = self.FindTargetWithoutTimeOut(GetImage(fb + "2.png"), threshold=0.7)
                there_location = self.FindTargetWithoutTimeOut(GetImage(fb + "3.png"), threshold=0.7)
                print(one_location)
                print(two_location)
                print(there_location)
                if one_location:
                    self.move(one_location)
                elif two_location:
                    self.move(two_location)
                elif there_location:
                    self.move(there_location)
    

    def fu_ben_hard(self):
        fb = ".\\image\\fuben\\"
        triangle_offset = (54, 51)
        timer_= -1

        while True:
            cj_image = self.FindTargetWithoutTimeOut(GetImage(".\\image\\yanxi\\cj.png"))
            gb_image = self.FindTargetWithoutTimeOut(GetImage(".\\image\\fuben\\gb.png"))

            # 有伏击，则点击规避
            if gb_image:
                LeftDoubleClick(gb_image)

            if cj_image:
                LeftDoubleClick(cj_image)
                time.sleep(30)
                LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\djjx.png"), 120, 5, threshold=0.6, left_top=(85,625), right_bottom=(280,700)))
                LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\djjx1.png")))
                LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\qd.png"), threshold=0.6, left_top=(1087,665), right_bottom=(1267,730)))
            else:
                


                time.sleep(1)
                # LeftDoubleClick([(1023,717)], interval_=0.5)
                # one_location = self.FindTargetWithoutTimeOut(GetImage(fb + "1.png"), threshold=0.7)
                two_location = self.FindTargetWithoutTimeOut(GetImage(fb + "2.png"), threshold=0.7)
                there_location = self.FindTargetWithoutTimeOut(GetImage(fb + "3.png"), threshold=0.7)
                # print(one_location)
                print(two_location)
                print(there_location)
                # if one_location:
                #     for i in range(len(one_location)):
                #         one_location[i] = tuple_add(one_location[i], triangle_offset)
                #     LeftSingleClick(one_location)
                if two_location:
                    for i in range(len(two_location)):
                        two_location[i] = tuple_add(two_location[i], triangle_offset)
                    LeftSingleClick(two_location)
                elif there_location:
                    for i in range(len(there_location)):
                        there_location[i] = tuple_add(there_location[i], triangle_offset)
                    LeftSingleClick(there_location)
                else:
                    # drag_screen
                    distance = [(400,0), (-400,0), (0,400), (0,-400)]
                    timer_ += 1 if timer_ < 3 else -3
                    Drag(distance[timer_][0], distance[timer_][1])




            

            





        # LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\cj.png")))
        # time.sleep(30)
        # LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\djjx.png"), 120, 5, threshold=0.6, left_top=(85,625), right_bottom=(280,700)))
        # LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\qd.png"), threshold=0.6, left_top=(1087,665), right_bottom=(1267,730)))
        # LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\qd.png"), threshold=0.6, left_top=(1087,665), right_bottom=(1267,730)))







    def ji_chu_xun_huan(self, timer):
        LeftSingleClick(self.FindTarget(GetImage(".\\image\\zuozhandangan\\" + "lkqw.png")))
        timer -= 1
        LeftSingleClick(self.FindTarget(GetImage(".\\image\\zuozhandangan\\" + "qd.png")))
        
        t = threading.Thread(target=self.zheng_li)
        t.start()

        print("{} runs left".format(timer))
        time.sleep(300)


        while timer > 0:
            timer -= 1
            # LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\djjx.png"), 120, 5, threshold=0.6, left_top=(85,625), right_bottom=(280,700)))
            # LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\djjx1.png")))
            # LeftSingleClick(self.FindTarget(GetImage(".\\image\\yanxi\\qd.png"), threshold=0.6, left_top=(1087,665), right_bottom=(1267,730)))
            LeftSingleClick(self.FindTarget(GetImage(".\\image\\zuozhandangan\\" + "zcqw.png"), 180, 5))
            LeftSingleClick(self.FindTarget(GetImage(".\\image\\zuozhandangan\\" + "qd.png")))
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), "wait for fight:")
            print("----------------------------还剩：", timer, "次")
            time.sleep(360)
        print("zuo_zhan_dang_an is over")
        self.flag = False
        print("close the zheng_li, self.flag=", self.flag)






    def zuo_zhan_dang_an(self, number, timer):
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


def LeftSingleClick(locations, wait = 0.5, offset=(0,0)):
    '''
    单击左键
     :param locations: 坐标组，[(x1,y1), (x2, y2)...]
     :param wait_: 等待时间, 默认0.5秒
    '''
    time.sleep(wait)
    if type(locations) == tuple:
        locations = [locations]
    if locations:
        # pyautogui.click(pos[0])
        print("click", locations)
        pydirectinput.leftClick(int(locations[0][0] + offset[0]), int(locations[0][1] + offset[1]))
        print("click success")
        return True
    else:
        print("no find image")
        return False
    

def LeftDoubleClick(locations, wait=0.5, offset=(0,0), interval_=0):
    '''
    左键双击
     :param locations: 坐标组
     :param wait: 等待时间
     :param offset: 偏移量
     :param interval: 双击的间隔时间
    '''
    time.sleep(wait)
    if locations:
        # pyautogui.click(pos[0])
        print(locations)
        pydirectinput.doubleClick(int(locations[0][0] + offset[0]), int(locations[0][1] + offset[1]), interval=interval_)
        print("doubleClick success")
        return True
    else:
        print("doubleClick no find image")
        return False
    

def Drag(xOffset=400, yOffset=400):
    pyautogui.mouseDown(638,398)
    pyautogui.moveRel(xOffset, yOffset, 1)
    pyautogui.mouseUp()
    
    

def wheel(length=1, pos=(640,404)):
    pydirectinput.moveTo(pos[0], pos[1])


    # win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -win32con.WHEEL_DELTA, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, length * 200, 0)





def test(item):
    print("++++++++++++++++++++++++++++++++++++")


if __name__ == '__main__':
    print("win32.py     ", __name__)
    print("start win32.py")
    # pass
    b = BiLanHangXian()
    # # time.sleep(1)
    # b.ji_dian_mei_shi()
    # b.ji_chu_xun_huan(2)
    # wheel()
    b.fu_ben_hard()




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
    