# -*- coding: utf-8 -*-
# todo/app.py

bilans = 0
ile = int(raw_input("Wpłata: "))
bilans += ile
print "Stan konta", bilans

ile = int(raw_input("Wypłata: "))
bilans -= ile
print "Stan konta", bilans
return
