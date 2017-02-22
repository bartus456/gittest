# -*- coding: utf-8 -*-
# todo/app.py
class Samochod(object):
    def __init__(self, marka="", model="", ileOsob=""):
        self.marka = marka
        self.model = model

    def laduj(self, ileOsob):
        self.bilans += ileOsob
        return self.
    def wyladuj(self, ileOsob):
        self.bilans -= ileOsob
        return self.bilans


sam = Samochod


ileOsob = int(raw_input("Wpłata 1: "))
print "Stan konta:", osoba1.wplata(ile)

ile = int(raw_input("Wpłata 2: "))
print "Stan konta:", osoba2.wplata(ile)

ile = int(raw_input("Wypłata 1: "))
print "Stan konta:", osoba1.wyplata(ile)

ile = int(raw_input("Wypłata 2: "))
print "Stan konta:", osoba2.wyplata(ile)
