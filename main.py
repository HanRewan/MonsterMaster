from tkinter import *
import threading
import random
import Monsters
from Monsters import MakeStr

root = Tk()
root.title("MonsterMaster")
root.geometry("240x155")
label = Label(root, text=str(0))

process = []

def createMonsterWindow(Mnstr):
    NewWindow = Tk()
    NewWindow.title("Monster")
    NewWindow.geometry("200x110")
    label5 = Label(NewWindow, text=" Тип монстра: " + Mnstr.Class)
    label6 = Label(NewWindow, text=" HP: " + str(Mnstr.HP) + " AC: " + str(Mnstr.AC))
    label7 = Label(NewWindow, text=" Str  Dex  Con  Int  Wis  Cha")
    label8 = Label(NewWindow, text=" " + MakeStr(Mnstr.Str) + "  " + MakeStr(Mnstr.Dex) + "  " + MakeStr(Mnstr.Con) + "  " + MakeStr(Mnstr.Int) + "  " + MakeStr(Mnstr.Wis) + "  " + MakeStr(Mnstr.Cha))
    label9 = Label(NewWindow, text=" Кількість атак: " + str(Mnstr.Attacks) + " Урон: " + Mnstr.HitDamage)
    label5.place(x=5, y=5)
    label6.place(x=5, y=25)
    label7.place(x=5, y=45)
    label8.place(x=5, y=65)
    label9.place(x=5, y=85)
    NewWindow.mainloop()



def count():
    global label
    try:
        charnum = int(Enter1.get())
        charlvl = int(Enter2.get())
        charcorelvl = int(Enter3.get())
        EnemysNum = Enter4.get().split()

        coml = charnum*charlvl*(1.325**charcorelvl)

        Enemys = []
        types = []
        for num in EnemysNum:
            type = Monsters.MonsterTypes[random.randint(0, len(Monsters.MonsterTypes) - 1)]
            dng = round(coml / len(EnemysNum) / int(num))
            tp = Monsters.StatPriorBook[type]
            Mnstr = Monsters.Monster(dng, tp, type)
            types.append(type)
            Enemys.append(Mnstr)


        for i in range(0, len(Enemys), 1):
            threading.Thread(target=createMonsterWindow, args=(Enemys[i],)).start()
            print(" Тип монстрів: " + types[i])
            print(" Кількість монстрів: " + str(EnemysNum[i]))
            Enemys[i].get()

    except ValueError:
        coml="Будь ласка введіть коректні дані."


    label.destroy()
    label = Label(root, text="Загальна сила групи: " + str(coml))
    label.place(x=5, y=130)


button1 = Button(root, text="Порахувати", command=count)
label1 = Label(root, text="Розмір паті:")
label2 = Label(root, text="Середній рівень:")
label3 = Label(root, text="Рівень GU:")
label4 = Label(root, text="Вороги:")
Enter1 = Entry(root)
Enter2 = Entry(root)
Enter3 = Entry(root)
Enter4 = Entry(root)


label1.place(x=5, y=5)
label2.place(x=5, y=25)
label3.place(x=5, y=45)
label4.place(x=5, y=65)

button1.place(x=80, y=100)
Enter1.place(x=110, y=7)
Enter2.place(x=110, y=27)
Enter3.place(x=110, y=47)
Enter4.place(x=110, y=67)
root.mainloop()