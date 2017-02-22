# -*- coding: utf-8 -*-
# todo/app.py

def utworzKonto():
    return {'bilans': 0}

def wplata(konto,ile):
    konto['bilans'] += ile
    return konto['bilans']

def wyplata(konto,ile):
    konto['bilans'] -= ile
    return konto['bilans']

osoba1 = utworzKonto()
osoba2 = utworzKonto()

ile = int(raw_input("Wpłata 1: "))
print "Stan konta:", wplata(osoba1, ile)

ile = int(raw_input("Wpłata 2: "))
print "Stan konta:", wplata(osoba2, ile)

ile = int(raw_input("Wypłata 1: "))
print "Stan konta:", wyplata(osoba1, ile)

ile = int(raw_input("Wypłata 2: "))
print "Stan konta:", wyplata(osoba2, ile)
