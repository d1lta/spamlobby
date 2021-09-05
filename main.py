import os
import keyboard
import time
from random import randint
from threading import Thread
version = "0.0.2"
status = False
settingsmenu = False
times = 0
delay = 0.1
fpscontrol = 0.001
startspam = keyboard.KEY_UP
stopspam = keyboard.KEY_DOWN
path = ""

messages = [
    "Привет","Как дела","Я твою мать ебал","Лол","Иди нахуй)","Ладно","Прохладно","Я гуль","1000-7","zxc","Всем привет дорогие друзья",
    "Ребят киньте дискорд","Пожалуйста","Нет","Да","А может ты?","Ваня блять","Как же ахуенно","Согласен","Ахахаха","ретард","я??"]

messagesasdefault = [
    "Привет","Как дела","Я твою мать ебал","Лол","Иди нахуй)","Ладно","Прохладно","Я гуль","1000-7","zxc","Всем привет дорогие друзья",
    "Ребят киньте дискорд","Пожалуйста","Нет","Да","А может ты?","Ваня блять","Как же ахуенно","Согласен","Ахахаха","ретард","я??"]

def FileUpdater():
    filec = ""
    try:
        f = open("cgs.save", "r")
        file = open(f.read(), "r", encoding='utf-8')
        filec = file.read()
    except:
        pass
    while True:
        time.sleep(1)
        try:
            f = open("cgs.save", "r")
            file = open(f.read(), "r", encoding='utf-8')
            filec1 = file.read()
            if filec1 != filec:
                filec = filec1
                FileHandler("nosavepath")
        except:
            pass

def save(path):
    f = open("cgs.save","w")
    f.write(path)
    f.close()
def FileHandler(way):
    if way == "savepath":
        try:
            global path
            lpath = input()
            file = open(lpath,"r", encoding='utf-8')
            messages.clear()
            for msg in file:
                msg = msg.replace("\n","")
                messages.append(msg)
            path = ""
            path = lpath
            save(path)
            return True
        except Exception:
            return False
    if way == "nosavepath":
        f = open(path,"r", encoding='utf-8')
        messages.clear()
        for msg in f:
            msg = msg.replace("\n", "")
            messages.append(msg)
        return True

def printonLaunch():
    print("                Welcome")
    print(" Чтобы начать спамить нажми стрелку вверх.")
    print("Чтобы перестать спамить зажми стрелку вниз.")
    print("Важно: нужно находиться в лобби и нажать на")
    print("    поле в которое нужно вводить текст")
    print("   Также не забудь выключить скрипт после")
    print("         того как найдёшь игру!")
    print("           K - меню настроек")
    print("         Текущая задержка: " + str(delay))
    print("              by d1lta_")
def funconLaunch():
    global path
    try:
        f = open("cgs.save","r")
        path = str(f.read())
    except Exception:
        save("null")
    try:
        file = open(path, "r", encoding='utf-8')
        messages.clear()
        for msg in file:
            msg = msg.replace("\n", "")
            messages.append(msg)
    except FileNotFoundError:
        path = "null"
        messages.clear()
        for msg in messagesasdefault:
            messages.append(msg)

def createmessage():
    return messages[(randint(0,len(messages)-1))]
def settings():
    print("           Settings")
    print('Для изменения задержки нажмите "D"')
    print('Для выбора кастомных сообщений нажмите "F"')
    print('Для выхода из настроек нажмите "S"')
    print('Кадровая задержка: ' + str(fpscontrol))
    if path == "null":
        print('Выбрана стандартная библиотека\n')
    else:
        print('Путь к библиотеке: ' + path + "\n")
funconLaunch()
th = Thread(target=FileUpdater)
th.start()
printonLaunch()
while True:
    time.sleep(fpscontrol)
    while status and settingsmenu == False:
        keyboard.write(createmessage())
        keyboard.press("enter")
        time.sleep(delay)
        times += 1
        break

    if keyboard.is_pressed(startspam) and settingsmenu == False:
        status = True

    if keyboard.is_pressed(stopspam) and settingsmenu == False:
        if status:
            keyboard.write("Отправлено " + str(times) + " сообщений")
        status = False

    if status == False and keyboard.is_pressed("K") and settingsmenu == False:
        os.system('cls')
        settingsmenu = True
        settings()
    if status == False and settingsmenu == True:
        if keyboard.is_pressed("D"): #Изменение задержки
            while True:
                try:
                    os.system('cls')
                    print("При задержке 0.005 и меньше может залагать игра")
                    print("Введите задержку: ", end="")
                    remainingdelay = input()
                    if remainingdelay == "0":
                        print("Не рекомендую.")
                        time.sleep(1)
                        remainingdelay = "0.01"
                    delay = float(remainingdelay)
                    os.system('cls')
                    print("Теперь задержка между сообщениями: " + str(delay) + "\n")
                    time.sleep(1)
                    os.system('cls')
                    settings()
                    break
                except ValueError:
                    os.system('cls')
                    print("Введите число.")
        if keyboard.is_pressed("F"): #Кастом сообщения
            os.system('cls')
            print("Вам нужно выбрать файл с расширением .txt")
            print("В котором будут написаны слова для спама в каждой строке.")
            print("Пример:")
            print("line1: Предложение №1")
            print("line2: Предложение №2")
            print("line3: Предложение №3")
            print("Введите путь к файлу: ",end ="")
            if FileHandler("savepath") == True:
                os.system('cls')
                print("Успех!")
                time.sleep(1)
                os.system('cls')
                settings()
            else:
                os.system('cls')
                print("Что-то пошло не так!")
                time.sleep(1)
                os.system('cls')
                settings()
        if keyboard.is_pressed("S"): #Выход из меню настроек
            settingsmenu = False
            os.system('cls')
            printonLaunch()

                #C:\Users\AsRock\Desktop\full\csgospam\spamer.txt