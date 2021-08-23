import os
import keyboard
import time
from random import randint
version = "0.0.2"
status = False
settingsmenu = False
times = 0
delay = 0.1
fpscontrol = 0.001
startspam = keyboard.KEY_UP
stopspam = keyboard.KEY_DOWN

messages = [
    "Привет","Как дела","Я твою мать ебал","Лол","Иди нахуй)","Ладно","Прохладно","Я гуль","1000-7","zxc","Всем привет дорогие друзья",
    "Ребят киньте дискорд","Пожалуйста","Нет","Да","А может ты?","Ваня блять","Как же ахуенно","Согласен","Ахахаха","ретард","я??"]
def FileHandler():
    try:
        file = open(input(),"r", encoding='utf-8')
        messages.clear()
        for msg in file:
            msg = msg.replace("\n","")
            messages.append(msg)
        return True
    except Exception:
        return False
def onLaunch():
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
def createmessage():
    return messages[(randint(0,len(messages)-1))]
def settings():
    print("           Settings")
    print('Для изменения задержки нажмите "D"')
    print('Для выхода из настроек нажмите "S"')
    print('Для выбора кастомных сообщений нажмите "F"')
    print('Кадровая задержка: ' + str(fpscontrol) +"\n")
onLaunch()
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
            print("Введите путь к файлу: ",end ="")
            if FileHandler():
                os.system('cls')
                print("Успех!")
                time.sleep(1)
                os.system('cls')
                settings()
            else:
                os.system('cls')
                print("        Что-то пошло не так!")
                print('*Возможно вы не правильно указали путь*')
                time.sleep(1)
                os.system('cls')
                settings()
        if keyboard.is_pressed("S"): #Выход из меню настроек
            settingsmenu = False
            os.system('cls')
            onLaunch()

                #C:\Users\AsRock\Desktop\full\csgospam\spamer.txt