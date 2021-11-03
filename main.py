#Varbutibu kalkulators
# Autors: Oskar A.
# Datums: 03.11.2021 V2V
from datetime import date
import math

today = date.today()
print("Šodienas datums:","[",today,"]")
print ("Autors: Oskar A.")
txt = ('\033[94m{}\033[0m'.format("[Varbutibu kalkulators]"))
INF = txt.center(65)
print(INF)

def statistiska():

    valueM = int(input("notikumu skaits:"))
    valueK = int(input("eksperimentu skaits:"))

    w = valueM/valueK;

    print("\033[94m{}\033[0m".format("--------------------------------"))
    value_1 = w*100
    print("Tas bus " + format(value_1,",.2f")+"%"+" statistiskā varbūtība")
    print("\033[94m{}\033[0m".format("--------------------------------"))

def geometriksa():

    value_radiuss = int(input("Kada radius un tilpumi:"))
    value_malas = int(input("kada malas garumu:"))
    Pi = math.pi

    square = (math.pow(value_malas, 2)) / ((math.pow(value_radiuss, 2))) * Pi

    value_1 = square * 100
    print("\033[94m{}\033[0m".format("--------------------------------"))
    print("varbūtība ir " + format( value_1, ",.2f")+"%")
    if value_1>100:
        print("Varbūtība nekad nevar pārsniegt skaitli 1 (jeb 100%)")
    print("\033[94m{}\033[0m".format("--------------------------------"))


def klasiska():
    labveligo = float (input("labvēlīgo notikumu skaits:"))
    kopskaits = float (input("visu notikumu kopskaits:"))

    klasiska = labveligo/kopskaits

    print("\033[94m{}\033[0m".format("--------------------------------"))
    print("varbūtība ir =" + format( klasiska, ",.2f")+"%")
    print("\033[94m{}\033[0m".format("--------------------------------"))


if __name__ == '__main__':
        choice = input("Kada veida varbutibas aprekini Tev sodien padoma? \n"
                   "Ievadi burtu:\n"
                    "-K klasiska metode n no n\n"
                   "-G geometriksa varbutiba\n"
                   "-S statiska varbutiba k m reizes\n")
        if choice.lower() == 'k':
            klasiska()
        if choice.lower() == 'g':
            geometriksa()
        if choice.lower() == 's':
            statistiska()
        else:
            exit(0)