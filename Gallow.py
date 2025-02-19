from tkinter import *
import random

main_win = Tk()
global error
global my_word
error = 0
my_word = []

def ClearWin():
    for widget in main_win.winfo_children():
        widget.destroy()

def CreateWin():
    main_win.title("Gallow")
    main_win.geometry("720x360")
    main_win.resizable(False, False)
    main_win.config(bg="black")

def random_word():
   with open('russian.txt', 'r') as file:
        words = file.readlines()
        words = [s.strip("\n") for s in words]
        return random.choice(words)
        
def GamePlay():
    ClearWin()
    word = random_word()
    i = 0

    canvas = Canvas(bg="white", width=200, height=200)
    canvas.place(anchor=CENTER, x = 200, y = 160)

    def draw():
        global error
        if error == 0:
            canvas.create_rectangle(5, 200, 200, 190, fill="#80CBC4", outline="#80CBC4")
            canvas.create_rectangle(165, 190, 180, 30, fill="#80CBC4", outline="#80CBC4")
            canvas.create_rectangle(165, 30, 95, 45, fill="#80CBC4", outline="#80CBC4")
            canvas.create_rectangle(95, 45, 110, 60, fill="#80CBC4", outline="#80CBC4")

    def Send():
        check = False
        letter = entry_word.get()
        letter = letter[0]
        entry_word.delete(0, END)
        print(letter)
        i = 0
        global error
        while i < len(word):
            if word[i] == letter:
                check = True
                my_word[i] = letter
            i = i+1
        if check == True:
            lbl_word["text"] = my_word
            return
        else:
            error+=1
            draw()
        
    draw()
    if error == 0:
        while i < len(word):
            my_word.append("_")
            i = i+1
        print(my_word)

    btn_start = Button(text="✅", width=5, height=2, command=Send)
    btn_start.place(anchor="c", y=140, x = 500)

    lbl_InputWord = Label(text="Введите букву",bg="black", fg="lime",font=("Arial", 18))
    lbl_InputWord.place(anchor="c", y=50, x = 500)

    entry_word = Entry(bg="white", justify = CENTER, font=("Arial", 18), width=5)
    entry_word.place(anchor="c", y=90, x = 500)

    lbl_word = Label(text=my_word,bg="black", fg="lime",font=("Arial", 22))
    lbl_word.place(anchor="c", y=250, x = 500)
        
def Play():
    error = 0
    my_word = []
    GamePlay()

def Info():
    ClearWin()

    lbl_leave = Label(text="Правила игры\nВам предстоит угадать словоЮ каждый раз угадывая по 1 букве\nЕсли вы не угадываете букву то человечек будет дорисовываться\nИгра заканчивается тогда:\n Когда человек полностью нарисован - поражение\nКогда слово угадано - победа", 
                      bg="black", fg = "lime", font=("Arial", 15))
    lbl_leave.place(anchor="c", y=90, x = 360)

    btn_menu = Button(text="В меню", width=10, height=2, command=MainMenu)
    btn_menu.place(anchor="c", y=200, x = 360)

def Leave():
    ClearWin()
    
    def click_yes():
        main_win.destroy()

    def click_no():
        MainMenu()

    lbl_leave = Label(text="Вы уверены что хотите выйти", bg="black", fg = "lime", font=("Arial", 16))
    lbl_leave.place(anchor="c", y=120, x = 360)

    btn_yes = Button(text="Да", width=10, height=2, command=click_yes)
    btn_yes.place(anchor="c",y=160,x=300)
    
    btn_no = Button(text="Нет", width=10, height=2, command=click_no)
    btn_no.place(anchor="c",y=160,x=420)

def MainMenu():
    ClearWin()

    btn_start = Button(text="Начать", width=10, height=2, command=Play)
    btn_start.place(anchor="c",y=120,x=360)

    btn_info = Button(text="Информация", width=10, height=2, command=Info)
    btn_info.place(anchor="c",y=180,x=360)

    btn_leave= Button(text="Выход", width=10, height=2, command=Leave)
    btn_leave.place(anchor="c",y=240,x=360)

CreateWin()
MainMenu()

main_win.mainloop()