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

    canvas = Canvas(bg="black", highlightbackground = "black", width=200, height=200)
    canvas.place(anchor=CENTER, x = 200, y = 160)

    def draw():
        global error
        if error == 0:
            canvas.create_rectangle(5, 200, 200, 190, fill="#80CBC4", outline="#80CBC4")
            canvas.create_rectangle(165, 190, 180, 30, fill="#80CBC4", outline="#80CBC4")
            canvas.create_rectangle(165, 30, 95, 45, fill="#80CBC4", outline="#80CBC4")
            canvas.create_rectangle(95, 45, 110, 60, fill="#80CBC4", outline="#80CBC4")
        elif error == 1:
            canvas.create_oval(87, 60,117, 90, fill="#ece5cb", outline="#ece5cb")
        elif error == 2:
            canvas.create_rectangle(99, 90, 105, 130, fill="#ece5cb", outline="#ece5cb")
        elif error == 3:
            canvas.create_polygon(105, 105,  130, 70, 135, 75,  105, 115, fill="#ece5cb", outline="#ece5cb")
        elif error == 4:
            canvas.create_polygon(99, 105,   74, 70,  69, 75,    99, 115, fill="#ece5cb", outline="#ece5cb")
        elif error == 5:
            canvas.create_polygon(105, 130,  135, 170, 130, 175, 99, 130, fill="#ece5cb", outline="#ece5cb")
        elif error == 6:
            canvas.create_polygon(99, 130,  69, 170, 74, 175, 105, 130, fill="#ece5cb", outline="#ece5cb")
            Lose()

    def Lose():
        lbl_word.destroy()
        entry_word.destroy()
        btn_start.destroy()
        lbl_InputWord.destroy()

        lbl_lose = Label(text="Вы проиграли",bg="black", fg="lime",font=("Arial", 18))
        lbl_lose.place(anchor="c", y=90, x = 500)

        lbl_word1 = Label(text=f"Слово было {word}",bg="black", fg="lime",font=("Arial", 18))
        lbl_word1.place(anchor="c", y=190, x = 500)

        btn_restart = Button(text="Рестарт", width=10, height=2, command=Play)
        btn_restart.place(anchor="c", y=140, x = 450)

        btn_menu = Button(text="В меню", width=10, height=2, command=MainMenu)
        btn_menu.place(anchor="c", y=140, x = 550)

    def Win():
        ClearWin()
        lbl_lose = Label(text="Вы победили",bg="black", fg="lime",font=("Arial", 18))
        lbl_lose.place(anchor="c", y=90, x = 360)

        lbl_word = Label(text=my_word,bg="black", fg="lime",font=("Arial", 22))
        lbl_word.place(anchor="c", y=250, x = 360)

        btn_restart = Button(text="Рестарт", width=10, height=2, command=Play)
        btn_restart.place(anchor="c", y=160, x = 290)

        btn_menu = Button(text="В меню", width=10, height=2, command=MainMenu)
        btn_menu.place(anchor="c", y=160, x = 430)

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
        word1 = ""
        for letter in my_word:
            word1 = word1 + letter

        if word1==word:
            Win()
            return
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
    global error
    global my_word
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