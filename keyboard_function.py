#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 依赖包下载
# pyperclip==1.8.0
# pynput==1.7.1
import os
import time
import pyperclip
import threading
from pynput import keyboard

# 复制快捷键
copy_list = ["Key.cmd", "c"]
# 粘贴快捷键
paste_list = ["Key.cmd", "v"]
# 全局键盘多个按键
global_keyboard_list = []
# 存储复制内容
global_save_list = []


def copy_exec():
    """执行复制操作"""
    time.sleep(0.1)
    curr_copy = pyperclip.paste()
    global_save_list.append(curr_copy)
    print(f"内容:{curr_copy},加入成功：{global_save_list}")


def paste_exec():
    """执行粘贴操作"""
    if not global_save_list:
        print("没有复制内容")
        return None
    curr_copy = global_save_list[0]
    del global_save_list[0]
    pyperclip.copy(curr_copy)
    print(f"取出内容:{curr_copy}")


def on_press(key):
    """监听键盘按下"""

    global_keyboard_list.append(str(key).replace("'", ""))
    if global_keyboard_list == copy_list:
        copy_exec()
    elif global_keyboard_list == paste_list:
        paste_exec()
    print(global_keyboard_list)


def on_release(key):
    """监听键盘松开"""
    # 停止运行
    if key == keyboard.Key.esc:
        os._exit(0)
    global_keyboard_list.clear()


def monitor_keyboard():
    """监听键盘操作"""
    while True:
        with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()


def main():
    """
    1.线程监听键盘输入情况
    2.判断输入复制或粘贴快捷键
    3.执行复制或粘贴快捷键方法
    """
    thread_monitor = threading.Thread(target=monitor_keyboard)
    thread_monitor.start()


if __name__ == '__main__':
    main()
