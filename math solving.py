from tkinter import *
from tkinter import ttk
import datetime
import random


# Генератор чисел. X и Y это пределы к примеру: от 2 до 4, где x=2 ,а y=4
def RandomDigit(x,y):
    return random.randint(x,y)


# Генератор примеров. Генерируются три числа x, y, z и из них составляется пример по формуле xy * z
def CreateExercise():
    global firstdigit
    global seconddigit
    global thirddigit
    global fourthdigit
    firstdigit = RandomDigit(1,9)
    seconddigit = RandomDigit(1,9)
    thirddigit = RandomDigit(1,9)
    fourthdigit = RandomDigit(1,9)
    exercise = str(firstdigit) + str(seconddigit) + 'x' + str(thirddigit) + str(fourthdigit) + '='
    return exercise


def GetAnswer():
    global firstdigit
    global seconddigit
    global thirddigit
    global fourthdigit
    global DraftAnswer
    DraftAnswer = int(str(firstdigit) + str(seconddigit)) * int(str(thirddigit) + str(fourthdigit))
    return DraftAnswer

def button(button_text):
    return Button(text = button_text, background='darkgray', font=('Comic Sans MS', 17, 'bold'))

            
root = Tk()
root.title("Math training")
root.geometry("400x400+760+340")
root.resizable(True, True)
task = CreateExercise()
write_answer_place = RandomDigit(1,4)
if write_answer_place == 1:
    answer1 = GetAnswer()
    answer2 = GetAnswer() + RandomDigit(50,250)
    answer3 = GetAnswer() + RandomDigit(50,250)
    answer4 = GetAnswer() + RandomDigit(50,250)
elif write_answer_place == 2:
    answer2 = GetAnswer()
    answer1 = GetAnswer() + RandomDigit(50,250)
    answer3 = GetAnswer() + RandomDigit(50,250)
    answer4 = GetAnswer() + RandomDigit(50,250)
elif write_answer_place == 3:
    answer3 = GetAnswer()
    answer2 = GetAnswer() + RandomDigit(50,250)
    answer1 = GetAnswer() + RandomDigit(50,250)
    answer4 = GetAnswer() + RandomDigit(50,250)
elif write_answer_place == 4:
    answer4 = GetAnswer()
    answer2 = GetAnswer() + RandomDigit(50,250)
    answer3 = GetAnswer() + RandomDigit(50,250)
    answer1 = GetAnswer() + RandomDigit(50,250)





answer_button1 = button(answer1)
answer_button2 = button(answer2)
answer_button3 = button(answer3)
answer_button4 = button(answer4)


math_label = ttk.Label(root, text = task, background='lightgray', anchor = 'center', font=('Comic Sans MS', 17, 'bold'))
math_label.grid(row = 0, column = 1, columnspan=2, sticky='wnes')


# Размещаем все кнопки по окну, а конкретно назначаем им поля и растягиваем в них
answer_button1.grid(row = 1, column = 1, sticky = 'wnes')
answer_button2.grid(row = 1, column = 2, sticky = 'wnes')
answer_button3.grid(row = 2, column = 1, sticky = 'wnes')
answer_button4.grid(row = 2, column = 2, sticky = 'wnes')

# Задаем размер всех колонок по Х
root.grid_columnconfigure(0, minsize = 100) 
root.grid_columnconfigure(1, minsize = 100)
root.grid_columnconfigure(2, minsize = 100)
root.grid_columnconfigure(3, minsize = 100)

# Задаем размер всех строчек по У
root.grid_rowconfigure(0, minsize = 100) 
root.grid_rowconfigure(1, minsize = 100)
root.grid_rowconfigure(2, minsize = 100)
root.grid_rowconfigure(3, minsize = 100)

# Запуск GUI TKinter
root.mainloop()
