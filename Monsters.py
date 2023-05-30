import random
import math


def DangClass(dang):
    return dang / 5


def CalculStat(prior, DC):
    return 10 + random.randint(-2, 2) + prior * DC / 5


def Modifier(stat):
    return (stat - 10) // 2


def MakeStr(num):
    res = str(num)
    if len(res) < 3:
        res = " " * (3 - len(res)) + res
    return res


def MakeMod(num):
    num = Modifier(num)
    res = str(num)
    if num > 0:
        res = "+" + res
    if len(res) < 3:
        res = " " * (3 - len(res)) + res
    return res


def ConstructVampire(Class, Prior):
    return Monster(round(Class * 2.5), Prior)

class StatBoard:

    def __init__(self, Str, Dex, Con, Int, Wis, Cha):
        self.Str = Str
        self.Dex = Dex
        self.Con = Con
        self.Int = Int
        self.Wis = Wis
        self.Cha = Cha


class Monster:

    def __init__(self, dang, StatsPrior, Class):
        self.Class = Class

        self.Str = round(CalculStat(StatsPrior.Str, DangClass(dang)))
        self.Dex = round(CalculStat(StatsPrior.Dex, DangClass(dang)))
        self.Con = round(CalculStat(StatsPrior.Con, DangClass(dang)))
        self.Int = round(CalculStat(StatsPrior.Int, DangClass(dang)))
        self.Wis = round(CalculStat(StatsPrior.Wis, DangClass(dang)))
        self.Cha = round(CalculStat(StatsPrior.Cha, DangClass(dang)))

        self.AC = round(8 + Modifier(self.Dex) + min(DangClass(dang), 5))
        self.HP = round(
            (Modifier(self.Con) * DangClass(dang) + random.randint(4, 6 + (StatsPrior.Con + 1) // 3 * 2)) * 5)

        if StatsPrior.Dex <= 3 and StatsPrior.Str <= 3:
            self.Attacks = max(1, round(math.log(DangClass(dang), 4)))

            self.DiceNum = max(1, round(math.log(DangClass(dang), 4)))
            self.DamageDice = min(12, 6 + 2 * round(math.log(DangClass(dang), 5)))

            self.HitDamage = str(self.DiceNum) + "d" + str(self.DamageDice)

        else:
            self.Attacks = max(1, round(math.log(DangClass(dang), 2)))

            self.DiceNum = max(1, round(math.log(DangClass(dang), 2)))
            self.DamageDice = min(12, 6 + 2 * round(math.log(DangClass(dang), 2)))

            self.HitDamage = str(self.DiceNum) + "d" + str(self.DamageDice) + "+" + str(
                max(Modifier(self.Str), Modifier(self.Dex)))


    def get(self):
        print(" HP: " + str(self.HP) + " AC: " + str(self.AC))
        print(" Str  Dex  Con  Int  Wis  Cha")
        print(" " + MakeStr(self.Str) + "  " + MakeStr(self.Dex) + "  " + MakeStr(self.Con) + "  " + MakeStr(
            self.Int) + "  " + MakeStr(self.Wis) + "  " + MakeStr(self.Cha))
        print(" " + MakeMod(self.Str) + "  " + MakeMod(self.Dex) + "  " + MakeMod(self.Con) + "  " + MakeMod(
            self.Int) + "  " + MakeMod(self.Wis) + "  " + MakeMod(self.Cha))
        print(" AttacksNum: " + str(self.Attacks) + " Damage: " + self.HitDamage)


MonsterTypes = ["Mage", "Warior", "Rogue"]

StatPriorBook = {
    "Mage": StatBoard(1, 4, 5, 6, 2, 3),
    "Warior": StatBoard(6, 4, 5, 1, 2, 3),
    "Rogue": StatBoard(2, 6, 5, 4, 3, 1)
}

Mymonstr = Monster(50, StatPriorBook["Warior"], "Warior")
Mymonstr.get()