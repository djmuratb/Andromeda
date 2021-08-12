#План действий:
    #Установка пароля на базу данных словаря
        #запрашивать пароль пользователя. По шифру (любому) делать преобразования строк, где n-итераций, пароль
    #Округление кнопки
#Готово:
    #Добавить кнопку отсчистить
    #добавить русский язык
    #Добавить кнопку копирования
    #Добавить столбцы словаря до 5 минимум, 10 максимум
    #Просмотр Хэш-суммы словаря
    #Кнопка смены ключей !!!
    #Изменить буквы в алфавите на рандомный алфавит
    #Удалить шифр Цезаря
    #Импортирование шифра !!!
    #Добавить цифры
    #Добавить кнопку копирования
from tkinter import *  
from tkinter import ttk
from tkinter import scrolledtext
import tkinter.messagebox as mb
import sqlite3
import random
import hashlib
import pyperclip




def enter_pass():
    #____
    def random_dic():
        letters = 'ÆÊÓÕÖÁ¿µÌáãúóñðîì×ôøĎěĘĶĳĦķœŒŞŶűŖƇƍƓƙƶƵƪƫƼǄǇțȎȽȻȹȴȱɁɊɍɎɂɄɔɠɚɕɷʊʘʚʓɻʠ'
    #a_n
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_1[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_2[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_3[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_4[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_5[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_6[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_7[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_8[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_9[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_10[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_11[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_12[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_13[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_14[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_15[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_16[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_17[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_18[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_19[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_20[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_21[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_22[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_23[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_24[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_25[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_26[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_27[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_28[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_29[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_30[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_31[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_32[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_33[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_34[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_35[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_36[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_37[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_38[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_39[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_40[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_41[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_42[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_43[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_44[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_45[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_46[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_47[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_48[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_49[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_50[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_51[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            a_52[i] = string_generate
    #b_n
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            b_1[i] = string_generate#space
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            b_2[i] = string_generate#dot
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            b_3[i] = string_generate#comma
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            b_4[i] = string_generate#que
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            b_5[i] = string_generate#1
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            b_6[i] = string_generate#2
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            b_7[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            b_8[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            b_9[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            b_10[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            b_11[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            b_12[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            b_13[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            b_14[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            b_15[i] = string_generate
    #c_n
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_1[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_2[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_3[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_4[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_5[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_6[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_7[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_8[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_9[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_10[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_11[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_12[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_13[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_14[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_15[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_16[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_17[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_18[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_19[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_20[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_21[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_22[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_23[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_24[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_25[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_26[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_27[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_28[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_29[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_30[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_31[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_32[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_33[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_34[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_35[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_36[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_37[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_38[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_39[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_40[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_41[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_42[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_43[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_44[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_45[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_46[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_47[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_48[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_49[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_50[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_51[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_52[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_53[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_54[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_55[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_56[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_57[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_58[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_59[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_60[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_61[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_62[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_63[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_64[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_65[i] = string_generate
        for i in range (10):
            c_ord = 0
            string_generate = ''
            while c_ord <  4000:
                random_ord = random.choices(letters)
                string_generate = string_generate + random_ord[0]
                c_ord = c_ord + ord(random_ord[0])
            c_66[i] = string_generate
        cur.execute("DELETE from users;")
        db.commit()
    #a_n
        key = str(a_1)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_2)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_3)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_4)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_5)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_6)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_7)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_8)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_9)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_10)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_11)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_12)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_13)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_14)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_15)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_16)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_17)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_18)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_19)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_20)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_21)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_22)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_23)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_24)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_25)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_26)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_27)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_28)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_29)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_30)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_31)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_32)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_33)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_34)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_35)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_36)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_37)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_38)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_39)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_40)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_41)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_42)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_43)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_44)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_45)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_46)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_47)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_48)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_49)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_50)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_51)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(a_52)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
    #b_n
        key = str(b_1)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(b_2)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(b_3)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(b_4)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(b_5)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(b_6)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(b_7)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(b_8)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(b_9)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(b_10)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(b_11)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(b_12)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(b_13)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(b_14)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(b_15)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
    #c_n
        key = str(c_1)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_2)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_3)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_4)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_5)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_6)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_7)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_8)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_9)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_10)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_11)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_12)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_13)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_14)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_15)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_16)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_17)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_18)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_19)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_20)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_21)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_22)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_23)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_24)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_25)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_26)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_27)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_28)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_29)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_30)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_31)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_32)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_33)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_34)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_35)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_36)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_37)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_38)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_39)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_40)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_41)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_42)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_43)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_44)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_45)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_46)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_47)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_48)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_49)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_50)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_51)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_52)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_53)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_54)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_55)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_56)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_57)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_58)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_59)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_60)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_61)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_62)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_63)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_64)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_65)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))
        key = str(c_66)
        cur.execute("INSERT INTO users VALUES(?, ?)", (key,empty))

        db.commit()

    #c_n
    def code(coding_string): #Функция зашифровки
        str = coding_string
        for kol in range(len(str)):         #Перебираем каждый элемент строки
            rand1= random.randint (0,9)    
            rand2= random.randint (0,9)
            rand3= random.randint (0,9)
            rand4= random.randint (0,9)
            rand5= random.randint (0,9)
            rand6= random.randint (0,9)
            rand7= random.randint (0,9)
            rand8= random.randint (0,9)
            rand9= random.randint (0,9)    
            rand10= random.randint (0,9)
            rand11= random.randint (0,9)
            rand12= random.randint (0,9)
            rand13= random.randint (0,9)
            rand14= random.randint (0,9)
            rand15= random.randint (0,9)
            rand16= random.randint (0,9)
            rand17= random.randint (0,9)    
            rand18= random.randint (0,9)
            rand19= random.randint (0,9)
            rand20= random.randint (0,9)
            rand21= random.randint (0,9)
            rand22= random.randint (0,9)
            rand23= random.randint (0,9)
            rand24= random.randint (0,9)
            rand25= random.randint (0,9)    
            rand26= random.randint (0,9)
            rand27= random.randint (0,9)
            rand28= random.randint (0,9)
            rand29= random.randint (0,9)
            rand30= random.randint (0,9)
            rand31= random.randint (0,9)
            rand32= random.randint (0,9)
            rand33= random.randint (0,9)
            rand34= random.randint (0,9)
            rand35= random.randint (0,9)
            rand36= random.randint (0,9)
            rand37= random.randint (0,9)
            rand38= random.randint (0,9)
            rand39= random.randint (0,9)
            rand40= random.randint (0,9)
            rand41= random.randint (0,9)    
            rand42= random.randint (0,9)
            rand43= random.randint (0,9)
            rand44= random.randint (0,9)
            rand45= random.randint (0,9)
            rand46= random.randint (0,9)
            rand47= random.randint (0,9)
            rand48= random.randint (0,9)
            rand49= random.randint (0,9)    
            rand50= random.randint (0,9)
            rand51= random.randint (0,9)
            rand52= random.randint (0,9)
            rand53= random.randint (0,9)
            rand54= random.randint (0,9)
            rand55= random.randint (0,9)
            rand56= random.randint (0,9)
            rand57= random.randint (0,9)
            rand58= random.randint (0,9)
            rand59= random.randint (0,9)
            rand60= random.randint (0,9)
            rand61= random.randint (0,9)
            rand62= random.randint (0,9)
            rand63= random.randint (0,9)
            rand64= random.randint (0,9)
            rand65= random.randint (0,9)
            rand66= random.randint (0,9)
            rand67= random.randint (0,9)
            rand68= random.randint (0,9)
            rand69= random.randint (0,9)
            rand70= random.randint (0,9)
            rand71= random.randint (0,9)
            rand72= random.randint (0,9)
            rand73= random.randint (0,9)
            rand74= random.randint (0,9)
            rand75= random.randint (0,9)
            rand76= random.randint (0,9)
            rand77= random.randint (0,9)
            rand78= random.randint (0,9)
            rand79= random.randint (0,9)
            rand80= random.randint (0,9)
            rand81= random.randint (0,9)
            rand82= random.randint (0,9)
            rand83= random.randint (0,9)
            rand84= random.randint (0,9)
            rand85= random.randint (0,9)
            rand86= random.randint (0,9)
            rand87= random.randint (0,9)
            rand88= random.randint (0,9)
            rand89= random.randint (0,9)
            rand90= random.randint (0,9)
            rand91= random.randint (0,9)
            rand92= random.randint (0,9)
            rand93= random.randint (0,9)
            rand94= random.randint (0,9)
            rand95= random.randint (0,9)
            rand96= random.randint (0,9)
            rand97= random.randint (0,9)
            rand98= random.randint (0,9)
            rand99= random.randint (0,9)
            rand100= random.randint (0,9)
            rand101= random.randint (0,9)
            rand102= random.randint (0,9)
            rand103= random.randint (0,9)
            rand104= random.randint (0,9)
            rand105= random.randint (0,9)
            rand106= random.randint (0,9)
            rand107= random.randint (0,9)
            rand108= random.randint (0,9)
            rand109= random.randint (0,9)
            rand110= random.randint (0,9)
            rand111= random.randint (0,9)
            rand112= random.randint (0,9)
            rand113= random.randint (0,9)
            rand114= random.randint (0,9)
            rand115= random.randint (0,9)
            rand116= random.randint (0,9)
            rand117= random.randint (0,9)
            rand118= random.randint (0,9)
            rand119= random.randint (0,9)
            rand120= random.randint (0,9)
            rand121= random.randint (0,9)
            rand122= random.randint (0,9)
            rand123= random.randint (0,9)
            rand124= random.randint (0,9)
            rand125= random.randint (0,9)
            rand126= random.randint (0,9)
            rand127= random.randint (0,9)
            rand128= random.randint (0,9)
            rand129= random.randint (0,9)
            rand130= random.randint (0,9)
            rand131= random.randint (0,9)
            rand132= random.randint (0,9)
            rand133= random.randint (0,9)
            rand134= random.randint (0,9)
            rand135= random.randint (0,9)
            rand136= random.randint (0,9)
            rand137= random.randint (0,9)
            rand138= random.randint (0,9)
            rand139= random.randint (0,9)
            rand140= random.randint (0,9)
            rand141= random.randint (0,9)
            rand142= random.randint (0,9)
            rand143= random.randint (0,9)
            rand144= random.randint (0,9)
            rand145= random.randint (0,9)
            rand146= random.randint (0,9)
            rand147= random.randint (0,9)
    #a_n
            str = str.replace ("a",a_1[rand1])
            str = str.replace ("b",a_2[rand2])
            str = str.replace ("c",a_3[rand3])
            str = str.replace ("d",a_4[rand4])
            str = str.replace ("e",a_5[rand5])
            str = str.replace ("f",a_6[rand6])
            str = str.replace ("g",a_7[rand7])
            str = str.replace ("h",a_8[rand8])
            str = str.replace ("i",a_9[rand9])
            str = str.replace ("j",a_10[rand10])
            str = str.replace ("k",a_11[rand11])
            str = str.replace ("l",a_12[rand12])  #Замена каждого взятого символа из строки на символы из массива
            str = str.replace ("m",a_13[rand13])
            str = str.replace ("n",a_14[rand14])
            str = str.replace ("o",a_15[rand15])
            str = str.replace ("p",a_16[rand16])
            str = str.replace ("q",a_17[rand17])
            str = str.replace ("r",a_18[rand18])
            str = str.replace ("s",a_19[rand19])
            str = str.replace ("t",a_20[rand20])
            str = str.replace ("u",a_21[rand21])
            str = str.replace ("v",a_22[rand22])
            str = str.replace ("w",a_23[rand23])
            str = str.replace ("x",a_24[rand24])
            str = str.replace ("y",a_25[rand25])
            str = str.replace ("z",a_26[rand26])
            str = str.replace ("A",a_27[rand31])
            str = str.replace ("B",a_28[rand32])
            str = str.replace ("C",a_29[rand33])
            str = str.replace ("D",a_30[rand34])
            str = str.replace ("E",a_31[rand35])
            str = str.replace ("F",a_32[rand36])
            str = str.replace ("G",a_33[rand37])
            str = str.replace ("H",a_34[rand38])
            str = str.replace ("I",a_35[rand39])
            str = str.replace ("J",a_36[rand40])
            str = str.replace ("K",a_37[rand41])
            str = str.replace ("L",a_38[rand42])
            str = str.replace ("M",a_39[rand43])
            str = str.replace ("N",a_40[rand44])
            str = str.replace ("O",a_41[rand45])
            str = str.replace ("P",a_42[rand46])
            str = str.replace ("Q",a_43[rand47])
            str = str.replace ("R",a_44[rand48])
            str = str.replace ("S",a_45[rand49])
            str = str.replace ("T",a_46[rand50])
            str = str.replace ("U",a_47[rand51])
            str = str.replace ("V",a_48[rand52])
            str = str.replace ("W",a_49[rand53])
            str = str.replace ("X",a_50[rand54])
            str = str.replace ("Y",a_51[rand55])
            str = str.replace ("Z",a_52[rand56])
    #b_n
            str = str.replace (".",b_1[rand57])
            str = str.replace (",",b_2[rand58])
            str = str.replace ("?",b_3[rand59])
            str = str.replace ("-",b_4[rand60])
            str = str.replace ("_",b_5[rand61])
            str = str.replace ("1",b_6[rand62])
            str = str.replace ("2",b_7[rand63])
            str = str.replace ("3",b_8[rand64])
            str = str.replace ("4",b_9[rand65])
            str = str.replace ("5",b_10[rand66])
            str = str.replace ("6",b_11[rand67])
            str = str.replace ("7",b_12[rand68])
            str = str.replace ("8",b_13[rand69])
            str = str.replace ("9",b_14[rand70])
            str = str.replace ("0",b_15[rand71])
    #c_n
            str = str.replace ("а",c_1[rand72])
            str = str.replace ("б",c_2[rand73])
            str = str.replace ("в",c_3[rand74])
            str = str.replace ("г",c_4[rand75])
            str = str.replace ("д",c_5[rand76])
            str = str.replace ("е",c_6[rand77])
            str = str.replace ("ё",c_7[rand78])
            str = str.replace ("ж",c_8[rand79])
            str = str.replace ("з",c_9[rand80])
            str = str.replace ("и",c_10[rand81])
            str = str.replace ("й",c_11[rand82])
            str = str.replace ("к",c_12[rand83])
            str = str.replace ("л",c_13[rand84])
            str = str.replace ("м",c_14[rand85])
            str = str.replace ("н",c_15[rand86])
            str = str.replace ("о",c_16[rand87])
            str = str.replace ("п",c_17[rand88])
            str = str.replace ("р",c_18[rand89])
            str = str.replace ("с",c_19[rand90])
            str = str.replace ("т",c_20[rand91])
            str = str.replace ("у",c_21[rand92])
            str = str.replace ("ф",c_22[rand93])
            str = str.replace ("х",c_23[rand94])
            str = str.replace ("ц",c_24[rand95])
            str = str.replace ("ч",c_25[rand96])
            str = str.replace ("ш",c_26[rand97])
            str = str.replace ("щ",c_27[rand98])
            str = str.replace ("ъ",c_28[rand99])
            str = str.replace ("ы",c_29[rand100])
            str = str.replace ("ь",c_30[rand101])
            str = str.replace ("э",c_31[rand102])
            str = str.replace ("ю",c_32[rand103])
            str = str.replace ("я",c_33[rand104])
            str = str.replace ("А",c_34[rand105])
            str = str.replace ("Б",c_35[rand106])
            str = str.replace ("В",c_36[rand107])
            str = str.replace ("Г",c_37[rand108])
            str = str.replace ("Д",c_38[rand109])
            str = str.replace ("Е",c_39[rand110])
            str = str.replace ("Ё",c_40[rand111])
            str = str.replace ("Ж",c_41[rand112])
            str = str.replace ("З",c_42[rand113])
            str = str.replace ("И",c_43[rand114])
            str = str.replace ("Й",c_44[rand115])
            str = str.replace ("К",c_45[rand116])
            str = str.replace ("Л",c_46[rand117])
            str = str.replace ("М",c_47[rand118])
            str = str.replace ("Н",c_48[rand119])
            str = str.replace ("О",c_49[rand120])
            str = str.replace ("П",c_50[rand121])
            str = str.replace ("Р",c_51[rand122])
            str = str.replace ("С",c_52[rand123])
            str = str.replace ("Т",c_53[rand124])
            str = str.replace ("У",c_54[rand125])
            str = str.replace ("Ф",c_55[rand126])
            str = str.replace ("Х",c_56[rand127])
            str = str.replace ("Ц",c_57[rand128])
            str = str.replace ("Ч",c_58[rand129])
            str = str.replace ("Ш",c_59[rand130])
            str = str.replace ("Щ",c_60[rand131])
            str = str.replace ("Ъ",c_61[rand132])
            str = str.replace ("Ы",c_62[rand133])
            str = str.replace ("Ь",c_63[rand134])
            str = str.replace ("Э",c_64[rand135])
            str = str.replace ("Э",c_65[rand136])
            str = str.replace ("Я",c_66[rand137])
            qwe =str
            return qwe
    def decode(decoding_string):#Функция расшифровки
        qwer = decoding_string #Здесь ввод Нужно перевести строку сюда
        for non in range(10):
    #a_n
            qwer = qwer.replace(a_1[non], 'a')
            qwer = qwer.replace(a_2[non], 'b')
            qwer = qwer.replace(a_3[non], 'c')
            qwer = qwer.replace(a_4[non], 'd')
            qwer = qwer.replace(a_5[non], 'e')
            qwer = qwer.replace(a_6[non], 'f')
            qwer = qwer.replace(a_7[non], 'g')
            qwer = qwer.replace(a_8[non], 'h')
            qwer = qwer.replace(a_9[non], 'i')#Замена зашифрованного текста на символы
            qwer = qwer.replace(a_10[non], 'j')
            qwer = qwer.replace(a_11[non], 'k')
            qwer = qwer.replace(a_12[non], 'l')
            qwer = qwer.replace(a_13[non], 'm')
            qwer = qwer.replace(a_14[non], 'n')
            qwer = qwer.replace(a_15[non], 'o')
            qwer = qwer.replace(a_16[non], 'p')
            qwer = qwer.replace(a_17[non], 'q')
            qwer = qwer.replace(a_18[non], 'r')
            qwer = qwer.replace(a_19[non], 's')
            qwer = qwer.replace(a_20[non], 't')
            qwer = qwer.replace(a_21[non], 'u')
            qwer = qwer.replace(a_22[non], 'v')
            qwer = qwer.replace(a_23[non], 'w')
            qwer = qwer.replace(a_24[non], 'x')
            qwer = qwer.replace(a_25[non], 'y')
            qwer = qwer.replace(a_26[non], 'z')
            qwer = qwer.replace(a_27[non], 'A')
            qwer = qwer.replace(a_28[non], 'B')
            qwer = qwer.replace(a_29[non], 'C')
            qwer = qwer.replace(a_30[non], 'D')
            qwer = qwer.replace(a_31[non], 'E')
            qwer = qwer.replace(a_32[non], 'F')
            qwer = qwer.replace(a_33[non], 'G')
            qwer = qwer.replace(a_34[non], 'H')
            qwer = qwer.replace(a_35[non], 'I')
            qwer = qwer.replace(a_36[non], 'J')
            qwer = qwer.replace(a_37[non], 'K')
            qwer = qwer.replace(a_38[non], 'L')
            qwer = qwer.replace(a_39[non], 'M')
            qwer = qwer.replace(a_40[non], 'N')
            qwer = qwer.replace(a_41[non], 'O')
            qwer = qwer.replace(a_42[non], 'P')
            qwer = qwer.replace(a_43[non], 'Q')
            qwer = qwer.replace(a_44[non], 'R')
            qwer = qwer.replace(a_45[non], 'S')
            qwer = qwer.replace(a_46[non], 'T')
            qwer = qwer.replace(a_47[non], 'U')
            qwer = qwer.replace(a_48[non], 'V')
            qwer = qwer.replace(a_49[non], 'W')
            qwer = qwer.replace(a_50[non], 'X')
            qwer = qwer.replace(a_51[non], 'Y')
            qwer = qwer.replace(a_52[non], 'Z')
    #b_n
            qwer = qwer.replace(b_1[non], '.')
            qwer = qwer.replace(b_2[non], ',')
            qwer = qwer.replace(b_3[non], '?')
            qwer = qwer.replace(b_4[non], '-')
            qwer = qwer.replace(b_5[non], '_')
            qwer = qwer.replace(b_6[non], '1')
            qwer = qwer.replace(b_7[non], '2')
            qwer = qwer.replace(b_8[non], '3')
            qwer = qwer.replace(b_9[non], '4')
            qwer = qwer.replace(b_10[non], '5')
            qwer = qwer.replace(b_11[non], '6')
            qwer = qwer.replace(b_12[non], '7')
            qwer = qwer.replace(b_13[non], '8')
            qwer = qwer.replace(b_14[non], '9')
            qwer = qwer.replace(b_15[non], '0')
    #c_n
            qwer = qwer.replace(c_1[non], 'а')
            qwer = qwer.replace(c_2[non], 'б')
            qwer = qwer.replace(c_3[non], 'в')
            qwer = qwer.replace(c_4[non], 'г')
            qwer = qwer.replace(c_5[non], 'д')
            qwer = qwer.replace(c_6[non], 'е')
            qwer = qwer.replace(c_7[non], 'ё')
            qwer = qwer.replace(c_8[non], 'ж')
            qwer = qwer.replace(c_9[non], 'з')
            qwer = qwer.replace(c_10[non], 'и')
            qwer = qwer.replace(c_11[non], 'й')
            qwer = qwer.replace(c_12[non], 'к')
            qwer = qwer.replace(c_13[non], 'л')
            qwer = qwer.replace(c_14[non], 'м')
            qwer = qwer.replace(c_15[non], 'н')
            qwer = qwer.replace(c_16[non], 'о')
            qwer = qwer.replace(c_17[non], 'п')
            qwer = qwer.replace(c_18[non], 'р')
            qwer = qwer.replace(c_19[non], 'с')
            qwer = qwer.replace(c_20[non], 'т')
            qwer = qwer.replace(c_21[non], 'у')
            qwer = qwer.replace(c_22[non], 'ф')
            qwer = qwer.replace(c_23[non], 'х')
            qwer = qwer.replace(c_24[non], 'ц')
            qwer = qwer.replace(c_25[non], 'ч')
            qwer = qwer.replace(c_26[non], 'ш')
            qwer = qwer.replace(c_27[non], 'щ')
            qwer = qwer.replace(c_28[non], 'ъ')
            qwer = qwer.replace(c_29[non], 'ы')
            qwer = qwer.replace(c_30[non], 'ь')
            qwer = qwer.replace(c_31[non], 'э')
            qwer = qwer.replace(c_32[non], 'ю')
            qwer = qwer.replace(c_33[non], 'я')
            qwer = qwer.replace(c_34[non], 'А')
            qwer = qwer.replace(c_35[non], 'Б')
            qwer = qwer.replace(c_36[non], 'В')
            qwer = qwer.replace(c_37[non], 'Г')
            qwer = qwer.replace(c_38[non], 'Д')
            qwer = qwer.replace(c_39[non], 'Е')
            qwer = qwer.replace(c_40[non], 'Ё')
            qwer = qwer.replace(c_41[non], 'Ж')
            qwer = qwer.replace(c_42[non], 'З')
            qwer = qwer.replace(c_43[non], 'И')
            qwer = qwer.replace(c_44[non], 'Й')
            qwer = qwer.replace(c_45[non], 'К')
            qwer = qwer.replace(c_46[non], 'Л')
            qwer = qwer.replace(c_47[non], 'М')
            qwer = qwer.replace(c_48[non], 'Н')
            qwer = qwer.replace(c_49[non], 'О')
            qwer = qwer.replace(c_50[non], 'П')
            qwer = qwer.replace(c_51[non], 'Р')
            qwer = qwer.replace(c_52[non], 'С')
            qwer = qwer.replace(c_53[non], 'Т')
            qwer = qwer.replace(c_54[non], 'У')
            qwer = qwer.replace(c_55[non], 'Ф')
            qwer = qwer.replace(c_56[non], 'Х')
            qwer = qwer.replace(c_57[non], 'Ц')
            qwer = qwer.replace(c_58[non], 'Ч')
            qwer = qwer.replace(c_59[non], 'Ш')
            qwer = qwer.replace(c_60[non], 'Щ')
            qwer = qwer.replace(c_61[non], 'Ъ')
            qwer = qwer.replace(c_62[non], 'Ы')
            qwer = qwer.replace(c_63[non], 'Ь')
            qwer = qwer.replace(c_64[non], 'Э')
            qwer = qwer.replace(c_65[non], 'Ю')
            qwer = qwer.replace(c_66[non], 'Я')
        return qwer
    def copy_win1():
        copy_string = txt3.get(1.0, END)
        from tkinter import Tk
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(copy_string)
        r.update() 
        r.destroy()
    def paste_win2():
        paste_win = pyperclip.paste()
        txt2.insert(INSERT, paste_win)
        decrypt()
    def encrypt():
        coding_string = txt.get()
        string = code(coding_string)
        txt3.delete(1.0, END)
        txt3.insert(INSERT, string)
    def decrypt():
        decoding_string = txt2.get()
        string = decode(decoding_string)
        txt4.delete(1.0, END)
        txt4.insert(INSERT, string)
    def check_hash():
        def check():
            first_string = txt10.get()
            second_string = txt11.get()
            if first_string == second_string:
                mb.showinfo("Проверка хэш-суммы", 'Хэш-сумма совпадает!')
            else:
                mb.showwarning("Проверка хэш-суммы", 'Хэш-сумма не совпадает!')
        window2 = Tk()  
        window2.title("Проверка совпадения суммы")  
        window2.geometry('425x200')
        window2.resizable(width=False, height=False)
        lbl0 = Label(window2, text=" ", font=("Arial Bold", 12))
        lbl0.grid(column=0, row=1)
        lbl0 = Label(window2, text="    1ая сумма:", font=("Arial Bold", 12))
        lbl0.grid(column=0, row=2)
        txt10 = Entry(window2,width=40)  
        txt10.grid(column=1, row=3)
        lbl0 = Label(window2, text=" ", font=("Arial Bold", 12))
        lbl0.grid(column=0, row=4)
        lbl0 = Label(window2, text="    2ая сумма:", font=("Arial Bold", 12))
        lbl0.grid(column=0, row=5)
        txt11 = Entry(window2,width=40)  
        txt11.grid(column=1, row=6)
        lbl0 = Label(window2, text=" ", font=("Arial Bold", 12))
        lbl0.grid(column=0, row=7)
        btn3 = Button(window2, text="Сверить hash-суммы", font=("Arial Bold", 11), command=check)
        btn3.grid(column=1, row=8)
    def import_conf():
        mb.showinfo("Импорт/экспорт", '     Для импорта и экспорта\nконфигурации перенесите файл\n  logs.db в папку с программой!')
    def hash_def():
        fname = 'logs.db'
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        hash_sum = hash_md5.hexdigest()
        window3 = Tk()  
        window3.title("Проверка совпадения суммы")  
        window3.geometry('265x60')
        window3.resizable(width=False, height=False)
        lbl0 = Label(window3, text=" ", font=("Arial Bold", 12))
        lbl0.grid(column=0, row=1)
        txt12 = Entry(window3,width=40)  
        txt12.grid(column=1, row=3)
        txt12.insert(INSERT, hash_sum)
    def clear_button_win1():
        txt.delete(0, END)
        txt3.delete(1.0, END)
    def clear_button_win2():
        txt2.delete(0, END)
        txt4.delete(1.0, END)
    #____
    global password
    password = txt10.get()
#Основа окна Tkinter
    def password_reverse(string2):
        string = string2
        enter_number_str = ''
        enter_number_list = []
        for i in password:
            enter_number_str = enter_number_str + str(ord(i))

        for i in enter_number_str:
           enter_number_list.append(i)

        for i in range (len(enter_number_list)):
            key = string[:1]
            string = string[1:]
            pop = int(enter_number_list[i])
            string_1 = string[:pop]
            string_2 = string[pop:]
            string = string_1 + key + string_2
        return string
        #Сессия базы данных
    db = sqlite3.connect(r'logs.db')
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
    key TEXT,
    empty TEXT);
    """)
    cur.execute("SELECT * FROM users;")
    results = cur.fetchmany(10000)
    empty = ''
    if str(results) == '[]':
    #a_1
        a_1 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']    #Строчные буквы
        a_2 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_3 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_4 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_5 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_6 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_7 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_8 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_9 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_10 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_11 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_12 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_13 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_14 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_15 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_16 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_17 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_18 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_19 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_20 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_21 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_22 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_23 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_24 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_25 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_26 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_27 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_28 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_29 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_30 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_31 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_32 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_33 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_34 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_35 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_36 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_37 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_38 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_39 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_40 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_41 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_42 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_43 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_44 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_45 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_46 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_47 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_48 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_49 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_50 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_51 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        a_52 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
    #b_n
        b_1 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        b_2 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        b_3 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        b_4 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        b_5 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        b_6 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        b_7 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        b_8 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        b_9 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        b_10 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        b_11 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        b_12 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        b_13 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        b_14 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        b_15 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
    #c_n
        c_1 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_2 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_3 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_4 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_5 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_6 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_7 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_8 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_9 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_10 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_11 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_12 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_13 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_14 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_15 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_16 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_17 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_18 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_19 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_20 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_21 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_22 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_23 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_24 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_25 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_26 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_27 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_28 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_29 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_30 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_31 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_32 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_33 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_34 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_35 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_36 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_37 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_38 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_39 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_40 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_41 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_42 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_43 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_44 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_45 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_46 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_47 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_48 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_49 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_50 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_51 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_52 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_53 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_54 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_55 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_56 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_57 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_58 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_59 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_60 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_61 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_62 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_63 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_64 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_65 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        c_66 = ['not found','not found','not found','not found','not found','not found','not found','not found','not found','not found']
        random_dic()
    else:
    #a_n
        a_1 = eval(results[0][0])    #Строчные буквы
        for i in range (len (a_1)):
            string2 = a_1[i]
            a_1[i] = password_reverse(string2)
             
        a_2 = eval(results[1][0])
        for i in range (len (a_2)):
            string2 = a_2[i]
            a_2[i] = password_reverse(string2)
             
        a_3 = eval(results[2][0])
        for i in range (len (a_3)):
            string2 = a_3[i]
            a_3[i] = password_reverse(string2)
                     
        a_4 = eval(results[3][0])
        for i in range (len (a_4)):
            string2 = a_4[i]
            a_4[i] = password_reverse(string2)
                     
        a_5 = eval(results[4][0])
        for i in range (len (a_5)):
            string2 = a_5[i]
            a_5[i] = password_reverse(string2)
             
        a_6 = eval(results[5][0])
        for i in range (len (a_6)):
            string2 = a_6[i]
            a_6[i] = password_reverse(string2)
             
        a_7 = eval(results[6][0])
        for i in range (len (a_7)):
            string2 = a_7[i]
            a_7[i] = password_reverse(string2)
             
        a_8 = eval(results[7][0])
        for i in range (len (a_8)):
            string2 = a_8[i]
            a_8[i] = password_reverse(string2)
             
        a_9 = eval(results[8][0])
        for i in range (len (a_9)):
            string2 = a_9[i]
            a_9[i] = password_reverse(string2)
             
        a_10 = eval(results[9][0])
        for i in range (len (a_10)):
            string2 = a_10[i]
            a_10[i] = password_reverse(string2)
             
        a_11 = eval(results[10][0])
        for i in range (len (a_11)):
            string2 = a_11[i]
            a_11[i] = password_reverse(string2)
             
        a_12 = eval(results[11][0])
        for i in range (len (a_12)):
            string2 = a_12[i]
            a_12[i] = password_reverse(string2)
             
        a_13 = eval(results[12][0])
        for i in range (len (a_13)):
            string2 = a_13[i]
            a_13[i] = password_reverse(string2)
             
        a_14 = eval(results[13][0])
        for i in range (len (a_14)):
            string2 = a_14[i]
            a_14[i] = password_reverse(string2)
             
        a_15 = eval(results[14][0])
        for i in range (len (a_15)):
            string2 = a_15[i]
            a_15[i] = password_reverse(string2)
             
        a_16 = eval(results[15][0])
        for i in range (len (a_16)):
            string2 = a_16[i]
            a_16[i] = password_reverse(string2)
             
        a_17 = eval(results[16][0])
        for i in range (len (a_17)):
            string2 = a_17[i]
            a_17[i] = password_reverse(string2)
             
        a_18 = eval(results[17][0])
        for i in range (len (a_18)):
            string2 = a_18[i]
            a_18[i] = password_reverse(string2)
             
        a_19 = eval(results[18][0])
        for i in range (len (a_19)):
            string2 = a_19[i]
            a_19[i] = password_reverse(string2)
             
        a_20 = eval(results[19][0])
        for i in range (len (a_20)):
            string2 = a_20[i]
            a_20[i] = password_reverse(string2)
             
        a_21 = eval(results[20][0])
        for i in range (len (a_21)):
            string2 = a_21[i]
            a_21[i] = password_reverse(string2)
             
        a_22 = eval(results[21][0])
        for i in range (len (a_22)):
            string2 = a_22[i]
            a_22[i] = password_reverse(string2)
             
        a_23 = eval(results[22][0])
        for i in range (len (a_23)):
            string2 = a_23[i]
            a_23[i] = password_reverse(string2)
             
        a_24 = eval(results[23][0])
        for i in range (len (a_24)):
            string2 = a_24[i]
            a_24[i] = password_reverse(string2)
             
        a_25 = eval(results[24][0])
        for i in range (len (a_25)):
            string2 = a_25[i]
            a_25[i] = password_reverse(string2)
             
        a_26 = eval(results[25][0])
        for i in range (len (a_26)):
            string2 = a_26[i]
            a_26[i] = password_reverse(string2)
             
        a_27 = eval(results[26][0])    #Прописные буквы
        for i in range (len (a_27)):
            string2 = a_27[i]
            a_27[i] = password_reverse(string2)
             
        a_28 = eval(results[27][0])
        for i in range (len (a_28)):
            string2 = a_28[i]
            a_28[i] = password_reverse(string2)

        a_29 = eval(results[28][0])
        for i in range (len (a_29)):
            string2 = a_29[i]
            a_29[i] = password_reverse(string2)

        a_30 = eval(results[29][0])
        for i in range (len (a_30)):
            string2 = a_30[i]
            a_30[i] = password_reverse(string2)

        a_31 = eval(results[30][0])
        for i in range (len (a_31)):
            string2 = a_31[i]
            a_31[i] = password_reverse(string2)

        a_32 = eval(results[31][0])
        for i in range (len (a_32)):
            string2 = a_32[i]
            a_32[i] = password_reverse(string2)

        a_33 = eval(results[32][0])
        for i in range (len (a_33)):
            string2 = a_33[i]
            a_33[i] = password_reverse(string2)

        a_34 = eval(results[33][0])
        for i in range (len (a_34)):
            string2 = a_34[i]
            a_34[i] = password_reverse(string2)

        a_35 = eval(results[34][0])
        for i in range (len (a_35)):
            string2 = a_35[i]
            a_35[i] = password_reverse(string2)

        a_36 = eval(results[35][0])
        for i in range (len (a_36)):
            string2 = a_36[i]
            a_36[i] = password_reverse(string2)

        a_37 = eval(results[36][0])
        for i in range (len (a_37)):
            string2 = a_37[i]
            a_37[i] = password_reverse(string2)

        a_38 = eval(results[37][0])
        for i in range (len (a_38)):
            string2 = a_38[i]
            a_38[i] = password_reverse(string2)

        a_39 = eval(results[38][0])
        for i in range (len (a_39)):
            string2 = a_39[i]
            a_39[i] = password_reverse(string2)
 
        a_40 = eval(results[39][0])
        for i in range (len (a_40)):
            string2 = a_40[i]
            a_40[i] = password_reverse(string2)

        a_41 = eval(results[40][0])
        for i in range (len (a_41)):
            string2 = a_41[i]
            a_41[i] = password_reverse(string2)

        a_42 = eval(results[41][0])
        for i in range (len (a_42)):
            string2 = a_42[i]
            a_42[i] = password_reverse(string2)
        a_43 = eval(results[42][0])
        for i in range (len (a_43)):
            string2 = a_43[i]
            a_43[i] = password_reverse(string2)
        a_44 = eval(results[43][0])
        for i in range (len (a_44)):
            string2 = a_44[i]
            a_44[i] = password_reverse(string2)
        a_45 = eval(results[44][0])
        for i in range (len (a_45)):
            string2 = a_45[i]
            a_45[i] = password_reverse(string2)
        a_46 = eval(results[45][0])
        for i in range (len (a_46)):
            string2 = a_46[i]
            a_46[i] = password_reverse(string2)
        a_47 = eval(results[46][0])
        for i in range (len (a_47)):
            string2 = a_47[i]
            a_47[i] = password_reverse(string2)
        a_48 = eval(results[47][0])
        for i in range (len (a_48)):
            string2 = a_48[i]
            a_48[i] = password_reverse(string2)
        a_49 = eval(results[48][0])
        for i in range (len (a_49)):
            string2 = a_49[i]
            a_49[i] = password_reverse(string2)
        a_50 = eval(results[49][0])
        for i in range (len (a_50)):
            string2 = a_50[i]
            a_50[i] = password_reverse(string2)
        a_51 = eval(results[50][0])
        for i in range (len (a_51)):
            string2 = a_51[i]
            a_51[i] = password_reverse(string2)
        a_52 = eval(results[51][0])
        for i in range (len (a_52)):
            string2 = a_52[i]
            a_52[i] = password_reverse(string2)
    #b_n
        b_1 = eval(results[52][0])
        for i in range (len (b_1)):
            string2 = b_1[i]
            b_1[i] = password_reverse(string2)
        b_2 = eval(results[53][0])
        for i in range (len (b_2)):
            string2 = b_2[i]
            b_2[i] = password_reverse(string2)
        b_3 = eval(results[54][0])
        for i in range (len (b_3)):
            string2 = b_3[i]
            b_3[i] = password_reverse(string2)
        b_4 = eval(results[55][0])
        for i in range (len (b_4)):
            string2 = b_4[i]
            b_4[i] = password_reverse(string2)
        b_5 = eval(results[56][0])
        for i in range (len (b_5)):
            string2 = b_5[i]
            b_5[i] = password_reverse(string2)
        b_6 = eval(results[57][0])
        for i in range (len (b_6)):
            string2 = b_6[i]
            b_6[i] = password_reverse(string2)
        b_7 = eval(results[58][0])
        for i in range (len (b_7)):
            string2 = b_7[i]
            b_7[i] = password_reverse(string2)
        b_8 = eval(results[59][0])  #Цифры
        for i in range (len (b_8)):
            string2 = b_8[i]
            b_8[i] = password_reverse(string2)
        b_9 = eval(results[60][0])
        for i in range (len (b_9)):
            string2 = b_9[i]
            b_9[i] = password_reverse(string2)
        b_10 = eval(results[61][0])
        for i in range (len (b_10)):
            string2 = b_10[i]
            b_10[i] = password_reverse(string2)
        b_11 = eval(results[62][0])
        for i in range (len (b_11)):
            string2 = b_11[i]
            b_11[i] = password_reverse(string2)
        b_12 = eval(results[63][0])
        for i in range (len (b_12)):
            string2 = b_12[i]
            b_12[i] = password_reverse(string2)
        b_13 = eval(results[64][0])
        for i in range (len (b_13)):
            string2 = b_13[i]
            b_13[i] = password_reverse(string2)
        b_14 = eval(results[65][0])
        for i in range (len (b_14)):
            string2 = b_14[i]
            b_14[i] = password_reverse(string2)
        b_15 = eval(results[66][0])
        for i in range (len (b_15)):
            string2 = b_15[i]
            b_15[i] = password_reverse(string2)
    #c_n
        c_1 = eval(results[67][0])
        for i in range (len (c_1)):
            string2 = c_1[i]
            c_1[i] = password_reverse(string2)
        c_2 = eval(results[68][0])
        for i in range (len (c_2)):
            string2 = c_2[i]
            c_2[i] = password_reverse(string2)
        c_3 = eval(results[69][0])
        for i in range (len (c_3)):
            string2 = c_3[i]
            c_3[i] = password_reverse(string2)
        c_4 = eval(results[70][0])
        for i in range (len (c_4)):
            string2 = c_4[i]
            c_4[i] = password_reverse(string2)
        c_5 = eval(results[71][0])
        for i in range (len (c_5)):
            string2 = c_5[i]
            c_5[i] = password_reverse(string2)
        c_6 = eval(results[72][0])
        for i in range (len (c_6)):
            string2 = c_6[i]
            c_6[i] = password_reverse(string2)
        c_7 = eval(results[73][0])
        for i in range (len (c_7)):
            string2 = c_7[i]
            c_7[i] = password_reverse(string2)
        c_8 = eval(results[74][0])
        for i in range (len (c_8)):
            string2 = c_8[i]
            c_8[i] = password_reverse(string2)
        c_9 = eval(results[75][0])
        for i in range (len (c_9)):
            string2 = c_9[i]
            c_9[i] = password_reverse(string2)
        c_10 = eval(results[76][0])
        for i in range (len (c_10)):
            string2 = c_10[i]
            c_10[i] = password_reverse(string2)
        c_11 = eval(results[77][0])
        for i in range (len (c_11)):
            string2 = c_11[i]
            c_11[i] = password_reverse(string2)
        c_12 = eval(results[78][0])
        for i in range (len (c_12)):
            string2 = c_12[i]
            c_12[i] = password_reverse(string2)
        c_13 = eval(results[79][0])
        for i in range (len (c_13)):
            string2 = c_13[i]
            c_13[i] = password_reverse(string2)
        c_14 = eval(results[80][0])
        for i in range (len (c_14)):
            string2 = c_14[i]
            c_14[i] = password_reverse(string2)
        c_15 = eval(results[81][0])
        for i in range (len (c_15)):
            string2 = c_15[i]
            c_15[i] = password_reverse(string2)
        c_16 = eval(results[82][0])
        for i in range (len (c_16)):
            string2 = c_16[i]
            c_16[i] = password_reverse(string2)
        c_17 = eval(results[83][0])
        for i in range (len (c_17)):
            string2 = c_17[i]
            c_17[i] = password_reverse(string2)
        c_18 = eval(results[84][0])
        for i in range (len (c_18)):
            string2 = c_18[i]
            c_18[i] = password_reverse(string2)
        c_19 = eval(results[85][0])
        for i in range (len (c_19)):
            string2 = c_19[i]
            c_19[i] = password_reverse(string2)
        c_20 = eval(results[86][0])
        for i in range (len (c_20)):
            string2 = c_20[i]
            c_20[i] = password_reverse(string2)
        c_21 = eval(results[87][0])
        for i in range (len (c_21)):
            string2 = c_21[i]
            c_21[i] = password_reverse(string2)
        c_22 = eval(results[88][0])
        for i in range (len (c_22)):
            string2 = c_22[i]
            c_22[i] = password_reverse(string2)
        c_23 = eval(results[89][0])
        for i in range (len (c_23)):
            string2 = c_23[i]
            c_23[i] = password_reverse(string2)
        c_24 = eval(results[90][0])
        for i in range (len (c_24)):
            string2 = c_24[i]
            c_24[i] = password_reverse(string2)
        c_25 = eval(results[91][0])
        for i in range (len (c_25)):
            string2 = c_25[i]
            c_25[i] = password_reverse(string2)
        c_26 = eval(results[92][0])
        for i in range (len (c_26)):
            string2 = c_26[i]
            c_26[i] = password_reverse(string2)
        c_27 = eval(results[93][0])
        for i in range (len (c_27)):
            string2 = c_27[i]
            c_27[i] = password_reverse(string2)
        c_28 = eval(results[94][0])
        for i in range (len (c_28)):
            string2 = c_28[i]
            c_28[i] = password_reverse(string2)
        c_29 = eval(results[95][0])
        for i in range (len (c_29)):
            string2 = c_29[i]
            c_29[i] = password_reverse(string2)
        c_30 = eval(results[96][0])
        for i in range (len (c_30)):
            string2 = c_30[i]
            c_30[i] = password_reverse(string2)
        c_31 = eval(results[97][0])
        for i in range (len (c_31)):
            string2 = c_31[i]
            c_31[i] = password_reverse(string2)
        c_32 = eval(results[98][0])
        for i in range (len (c_32)):
            string2 = c_32[i]
            c_32[i] = password_reverse(string2)
        c_33 = eval(results[99][0])
        for i in range (len (c_33)):
            string2 = c_33[i]
            c_33[i] = password_reverse(string2)
        c_34 = eval(results[100][0])
        for i in range (len (c_34)):
            string2 = c_34[i]
            c_34[i] = password_reverse(string2)
        c_35 = eval(results[101][0])
        for i in range (len (c_35)):
            string2 = c_35[i]
            c_35[i] = password_reverse(string2)
        c_36 = eval(results[102][0])
        for i in range (len (c_36)):
            string2 = c_36[i]
            c_36[i] = password_reverse(string2)
        c_37 = eval(results[103][0])
        for i in range (len (c_37)):
            string2 = c_37[i]
            c_37[i] = password_reverse(string2)
        c_38 = eval(results[104][0])
        for i in range (len (c_38)):
            string2 = c_38[i]
            c_38[i] = password_reverse(string2)
        c_39 = eval(results[105][0])
        for i in range (len (c_39)):
            string2 = c_39[i]
            c_39[i] = password_reverse(string2)
        c_40 = eval(results[106][0])
        for i in range (len (c_40)):
            string2 = c_40[i]
            c_40[i] = password_reverse(string2)
        c_41 = eval(results[107][0])
        for i in range (len (c_41)):
            string2 = c_41[i]
            c_41[i] = password_reverse(string2)
        c_42 = eval(results[108][0])
        for i in range (len (c_42)):
            string2 = c_42[i]
            c_42[i] = password_reverse(string2)
        c_43 = eval(results[109][0])
        for i in range (len (c_43)):
            string2 = c_43[i]
            c_43[i] = password_reverse(string2)
        c_44 = eval(results[110][0])
        for i in range (len (c_44)):
            string2 = c_44[i]
            c_44[i] = password_reverse(string2)
        c_45= eval(results[111][0])
        for i in range (len (c_45)):
            string2 = c_45[i]
            c_45[i] = password_reverse(string2)
        c_46 = eval(results[112][0])
        for i in range (len (c_46)):
            string2 = c_46[i]
            c_46[i] = password_reverse(string2)
        c_47 = eval(results[113][0])
        for i in range (len (c_47)):
            string2 = c_47[i]
            c_47[i] = password_reverse(string2)
        c_48 = eval(results[114][0])
        for i in range (len (c_48)):
            string2 = c_48[i]
            c_48[i] = password_reverse(string2)
        c_49 = eval(results[115][0])
        for i in range (len (c_49)):
            string2 = c_49[i]
            c_49[i] = password_reverse(string2)
        c_50 = eval(results[116][0])
        for i in range (len (c_50)):
            string2 = c_50[i]
            c_50[i] = password_reverse(string2)
        c_51 = eval(results[117][0])
        for i in range (len (c_51)):
            string2 = c_51[i]
            c_51[i] = password_reverse(string2)
        c_52 = eval(results[118][0])
        for i in range (len (c_52)):
            string2 = c_52[i]
            c_52[i] = password_reverse(string2)
        c_53 = eval(results[119][0])
        for i in range (len (c_53)):
            string2 = c_53[i]
            c_53[i] = password_reverse(string2)
        c_54 = eval(results[120][0])
        for i in range (len (c_54)):
            string2 = c_54[i]
            c_54[i] = password_reverse(string2)
        c_55 = eval(results[121][0])
        for i in range (len (c_55)):
            string2 = c_55[i]
            c_55[i] = password_reverse(string2)
        c_56 = eval(results[122][0])
        for i in range (len (c_56)):
            string2 = c_56[i]
            c_56[i] = password_reverse(string2)
        c_57 = eval(results[123][0])
        for i in range (len (c_57)):
            string2 = c_57[i]
            c_57[i] = password_reverse(string2)
        c_58 = eval(results[124][0])
        for i in range (len (c_58)):
            string2 = c_58[i]
            c_58[i] = password_reverse(string2)
        c_59 = eval(results[125][0])
        for i in range (len (c_59)):
            string2 = c_59[i]
            c_59[i] = password_reverse(string2)
        c_60 = eval(results[126][0])
        for i in range (len (c_60)):
            string2 = c_60[i]
            c_60[i] = password_reverse(string2)
        c_61 = eval(results[127][0])
        for i in range (len (c_61)):
            string2 = c_61[i]
            c_61[i] = password_reverse(string2)
        c_62 = eval(results[128][0])
        for i in range (len (c_62)):
            string2 = c_62[i]
            c_62[i] = password_reverse(string2)
        c_63 = eval(results[129][0])
        for i in range (len (c_63)):
            string2 = c_63[i]
            c_63[i] = password_reverse(string2)
        c_64 = eval(results[130][0])
        for i in range (len (c_64)):
            string2 = c_64[i]
            c_64[i] = password_reverse(string2)
        c_65 = eval(results[131][0])
        for i in range (len (c_65)):
            string2 = c_65[i]
            c_65[i] = password_reverse(string2)
        c_66 = eval(results[132][0])
        for i in range (len (c_66)):
            string2 = c_66[i]
            c_66[i] = password_reverse(string2)
            
    pass_win.destroy()
    window = Tk()  
    window.title("Шифрование Андромеда")  
    window.geometry('410x340')
    window.resizable(width=False, height=False)
    tab_control = ttk.Notebook(window)  
    tab1 = ttk.Frame(tab_control)  
    tab2 = ttk.Frame(tab_control)
    tab3 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Зашифровать')  
    tab_control.add(tab2, text='Расшифровать')
    tab_control.add(tab3, text='Опции')
    #tab1 зашифровать
    lbl0 = Label(tab1, text="                 ", font=("Arial Bold", 12))
    lbl0.grid(column=0, row=0)
    lbl0 = Label(tab1, text="            ", font=("Arial Bold", 12))
    lbl0.grid(column=1, row=0)
    lbl = Label(tab1, text="Введите текст для зашифровки:", font=("Arial Bold", 12))
    lbl.grid(column=1, row=1)
    txt = Entry(tab1,width=40)  
    txt.grid(column=1, row=2)
    lbl1 = Label(tab1, text="      ", font=("Arial Bold", 5))
    lbl1.grid(column=1, row=3)
    btn = Button(tab1, text="Зашифровать!", font=("Arial Bold", 12), command=encrypt)
    btn.grid(column=1, row=4)
    lbl1 = Label(tab1, text="      ", font=("Arial Bold", 5))
    lbl1.grid(column=1, row=5)
    lbl1 = Label(tab1, text="Зашифрованный текст:", font=("Arial Bold", 12))
    lbl1.grid(column=1, row=6)
    txt3 = scrolledtext.ScrolledText(tab1, width=30, height=5)  
    txt3.grid(column=1, row=7)
    lbl0 = Label(tab1, text="            ", font=("Arial Bold", 12))
    lbl0.grid(column=1, row=8)
    btn = Button(tab1, text="Копировать!", font=("Arial Bold", 12), command=copy_win1)
    btn.grid(column=1, row=9)
    lbl1 = Label(tab1, text="  ", font=("Arial Bold", 5))
    lbl1.grid(column=2, row=2)
    btn = Button(tab1, text="✕", font=("Arial Bold", 12), command=clear_button_win1)
    btn.grid(column=3, row=2)
    #tab2 расшифровать
    lbl0 = Label(tab2, text="                 ", font=("Arial Bold", 12))
    lbl0.grid(column=0, row=0)
    lbl0 = Label(tab2, text="            ", font=("Arial Bold", 12))
    lbl0.grid(column=1, row=0)
    lbl1 = Label(tab2, text="Введите текст для расшифровки:", font=("Arial Bold", 12))
    lbl1.grid(column=1, row=1)
    txt2 = Entry(tab2,width=40)  
    txt2.grid(column=1, row=2)
    lbl1 = Label(tab2, text="      ", font=("Arial Bold", 5))
    lbl1.grid(column=1, row=3)
    btn1 = Button(tab2, text="Расшифровать!", font=("Arial Bold", 12), command=decrypt)
    btn1.grid(column=1, row=4)
    lbl1 = Label(tab2, text="      ", font=("Arial Bold", 5))
    lbl1.grid(column=1, row=5)
    lbl1 = Label(tab2, text="Расшифрованный текст:", font=("Arial Bold", 12))
    lbl1.grid(column=1, row=6)
    txt4 = scrolledtext.ScrolledText(tab2, width=30, height=5)  
    txt4.grid(column=1, row=7)
    lbl0 = Label(tab2, text="            ", font=("Arial Bold", 12))
    lbl0.grid(column=1, row=8)
    btn = Button(tab2, text="Вставить!", font=("Arial Bold", 12), command=paste_win2)
    btn.grid(column=1, row=9)
    lbl1 = Label(tab2, text="  ", font=("Arial Bold", 5))
    lbl1.grid(column=2, row=2)
    btn = Button(tab2, text="✕", font=("Arial Bold", 12), command=clear_button_win2)
    btn.grid(column=3, row=2)
    #tab3 опции
    lbl0 = Label(tab3, text="                           ", font=("Arial Bold", 9))
    lbl0.grid(column=0, row=0)
    lbl0 = Label(tab3, text=" ", font=("Arial Bold", 15))
    lbl0.grid(column=0, row=1)
    lbl = Label(tab3, text=" ", font=("Arial Bold", 2))
    lbl.grid(column=1, row=1)
    btn2 = Button(tab3, text="Импорт/экспорт конфигурации!", font=("Arial Bold", 11), command=import_conf)
    btn2.grid(column=1, row=4)
    lbl0 = Label(tab3, text="                 ", font=("Arial Bold", 1))
    lbl0.grid(column=0, row=5)
    lbl = Label(tab3, text="", font=("Arial Bold", 12))
    lbl.grid(column=1, row=6)
    btn3 = Button(tab3, text="                Hash-сумма!                ", font=("Arial Bold", 11), command=hash_def)
    btn3.grid(column=1, row=7)
    lbl0 = Label(tab3, text="                 ", font=("Arial Bold", 1))
    lbl0.grid(column=0, row=8)
    lbl = Label(tab3, text="", font=("Arial Bold", 12))
    lbl.grid(column=1, row=9)
    btn3 = Button(tab3, text="       Проверка hash-суммы         ", font=("Arial Bold", 11), command=check_hash)
    btn3.grid(column=1, row=10)
    lbl0 = Label(tab3, text="                 ", font=("Arial Bold", 1))
    lbl0.grid(column=0, row=11)
    lbl = Label(tab3, text="", font=("Arial Bold", 12))
    lbl.grid(column=1, row=12)
    btn3 = Button(tab3, text="           Изменить словарь!          ", font=("Arial Bold", 11), command=random_dic)
    btn3.grid(column=1, row=13)
    tab_control.pack(expand=1, fill='both')
    window.mainloop()

pass_win = Tk()
pass_win.title("")
pass_win.geometry('200x150')
lbl0 = Label(pass_win, text="    ", font=("Arial Bold", 12))
lbl0.grid(column=0, row=0)
lbl0 = Label(pass_win, text="Введите пароль:", font=("Arial Bold", 12))
lbl0.grid(column=1, row=1)
pass_win.resizable(width=False, height=False)
txt10 = Entry(pass_win,width=25)  
txt10.grid(column=1, row=2)
lbl0 = Label(pass_win, text="    ", font=("Arial Bold", 12))
lbl0.grid(column=1, row=3)
btn = Button(pass_win, text="Войти!", font=("Arial Bold", 12), command=enter_pass)
btn.grid(column=1, row=4)
pass_win.mainloop()

