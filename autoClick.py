# This is a sample Python script.
#coding=utf-8
from selenium import webdriver

import time
import re
import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # option = webdriver.ChromeOptions()
    # option.add_argument(r"--user-data-dir=C:\Users\yang\AppData\Local\Google\Chrome\User Data")
    driver = webdriver.Chrome(executable_path=r"D:\install_dir\code\webTest\chromedriver.exe")


    # 打开首页并且登陆
    driver.get("https://sports.sjtu.edu.cn/login")



    driver.maximize_window()
    driver.find_element_by_class_name('isoffCampus').click()
    driver.find_element_by_name("username").send_keys(pswd[0])
    driver.find_element_by_name("password").send_keys(pswd[1])
    tmp = input("validateCode：")
    driver.find_element_by_name("validateCode").send_keys(tmp)

    #点击登陆
    driver.find_element_by_class_name("btn-block").click()
    time.sleep(3)

    #进入核销页面
    driver.find_element_by_xpath("//*[@id='side-menu']/li[4]/a").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='side-menu']/li[4]/ul/li/a").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='side-menu']/li[4]/ul/li/ul/li/a").click()
    time.sleep(1)
    driver.switch_to.frame("iframe2")
    hexiao = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[1]/div/div/a[2]")
    hexiao.click()
    driver.switch_to.frame("layui-layer-iframe1")
    writecode = driver.find_element_by_xpath("//*[@id='writeCode']")

    code = input("input the code:\n")
    writecode.send_keys(code)

    driver.switch_to.parent_frame()

    confirm = driver.find_element_by_xpath("//*[@id='layui-layer1']/div[3]/a[1]")
    time.sleep(2)

    confirm.click()
    time.sleep(2)
    i = 1
    tmpStr = "layui-layer-iframe"
    while(1):
        i += 2

        #点击核销界面
        hexiao.click()
        # button_confirm = driver.find_element_by_xpath("//*[@id='layui-layer1']/div[3]/a[1]")

        # 输入核销码
        tmpStr = "layui-layer-iframe"

        driver.switch_to.frame(tmpStr+str(i))
        writecode = driver.find_element_by_xpath("//*[@id='writeCode']")

        code = input("input the code:\n")
        writecode.send_keys(code)
        time.sleep(1)
        driver.switch_to.parent_frame()
        tmpStr = "layui-layer"
        tmpStr1 = tmpStr+str(i)
        confirm = driver.find_element_by_xpath("//*[@id='%s']/div[3]/a[1]"%tmpStr1)
        #点击确定键

            # driver.switch_to_default_content()
            # driver.switch_to.frame("iframe2")
        time.sleep(2)

        confirm.click()
        # driver.switch_to.frame("iframe2")


        #错误处理，码过期了
        # driver.switch_to.frame("layui-layer-iframe1")
        #
        # result = driver.find_element_by_xpath("//*[@id='layui-layer1']/div[2]").text
        # print(result)
        # if u"已过期" in result:
        #     time.sleep(1)
        #
        #     messagebox.showerror("title", "已过期")
        #     continue
        # else:
        #     time.sleep(1)
        #
        #     break
        # driver.find_element_by_xpath("//*[@id='layui-layer5']/span[1]/a").click()
        print("success!times:%d"%(i/2))
        # driver.switch_to_default_content()

        # driver.switch_to.frame("iframe2")
        # driver.find_element_by_name("writeCode").send_keys(code)

        time.sleep(2)
        #确定按钮



    # driver.find_element_by_id('su').click()
    # # 等待3秒
    # time.sleep(3)
    # # 退出浏览器
    #

    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
