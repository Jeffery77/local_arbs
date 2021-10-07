# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 18:33:14 2021

@author: dell
"""

p = [['22:55', 'Basilashvili, Nikoloz - Opelka, Reilly', '2.47', '1.55', '2.21', '1.67', '2.21', '1.67', '+36', '23:00', 'Harris, Lloyd - Shapovalov, Denis', '2.44', '1.56', '2.19', '1.69', '2.19', '1.69', '+36', 'Tennis - ATP - US Open', 'Sep 04, 2021'], ['11:00', 'Den Ouden, Guy - Veldheer, Mick', '1.52', '2.16', '+2', 'Tennis - ITF Men - Germany', 'Sep 05, 2021'], ['08:00', 'Malla, Bastian - Marozsan, Fabian', '1.67', '1.92', '+2', 'Tennis - ITF Men - Slovakia', 'Sep 05, 2021'], ['09:00', 'Frech, Magdalena - Smitkova, Tereza', '1.44', '2.35', '+2', 'Tennis - ITF Women - Czech Republic', 'Sep 05, 2021'], ['08:30', 'Kraus, Sinja - Dinu, Cristina', '2.61', '1.36', '+2', 'Tennis - ITF Women - Austria', 'Sep 05, 2021'], ['10:00', 'Melnikova, Marina - Park, Sohyun', '1.64', '1.96', '+2', 'Tennis - ITF Women - Spain', 'Sep 05, 2021']]
k = [['15:00', 'Ivashka, Ilya - Berrettini, Matteo', '2.71', '1.47', '2.33', '1.61', '2.33', '1.61', '+36', '16:00', 'Seppi, Andreas - Otte, Oscar', '2.09', '1.75', '2.01', '1.81', '2.01', '1.81', '+36', '17:30', 'Djokovic, Novak - Nishikori, Kei', '1.03', '12.62', '1.16', '5.33', '1.16', '5.33', '+36', '17:30', 'Monfils, Gael - Sinner, Jannik', '2.37', '1.59', '2.18', '1.69', '2.18', '1.69', '+36', '19:15', 'Karatsev, Aslan - Brooksby, Jenson', '1.96', '1.85', '1.94', '1.87', '1.94', '1.87', '+36', '22:00', 'Basilashvili, Nikoloz - Opelka, Reilly', '2.82', '1.44', '2.39', '1.58', '2.39', '1.58', '+36', '23:00', 'Harris, Lloyd - Shapovalov, Denis', '2.57', '1.51', '2.25', '1.65', '2.25', '1.65', '+36', 'Tennis - ATP - US Open', 'Sep 04, 2021'], ['12:00', 'Den Ouden, Guy - Rosenkranz, Mats', '1.58', '2.05', '+2', 'Tennis - ITF Men - Germany', 'Sep 04, 2021'], ['15:00', 'Minnen, Greet - Andreescu, Bianca Vanessa', '3.48', '1.31', '2.84', '1.43', '2.84', '1.43', '+28', '16:00', 'Kvitova, Petra - Sakkari, Maria', '1.92', '1.89', '1.92', '1.89', '1.92', '1.89', '+28', '16:15', 'Bencic, Belinda - Pegula, Jessica', '1.76', '2.08', '1.80', '2.02', '1.80', '2.02', '+28', '17:00', 'Kontaveit, Anett - Swiatek, Iga', '1.97', '1.85', '1.95', '1.86', '1.95', '1.86', '+28', '18:00', 'Sorribes Tormo, Sara - Raducanu, Emma', '1.86', '1.95', '1.87', '1.94', '1.87', '1.94', '+28', '19:00', 'Pliskova, Karolina - Tomljanovic, Ajla', '1.28', '3.71', '1.41', '2.93', '1.41', '2.93', '+28', '23:00', 'Barty, Ashleigh - Rogers, Shelby', '1.10', '7.06', '1.22', '4.36', '1.22', '4.36', '+28', 'Tennis - WTA - US Open', 'Sep 04, 2021']]
#temp_a = []
temp_b = []
for l in k:
    temp_a = []
    counter = 0
    print("lenl ",len(l))
    for i,v in enumerate(l):
        if (v[0].isalpha() and (i != (len(l) - 2) and (i != (len(l) - 1) ))):
            inde = l.index(v)
            print(inde)
            print("i:",i)
            print("e",len(l) - 2 )
            temp_a = [l[inde - 1],l[inde],l[inde + 1],l[inde + 2],l[-2],l[-1]]
            print("count:",counter)
            print("v",v)
            counter = counter + 1
            temp_b.append(temp_a)
            temp_a = []
        if counter == 2:
            counter = 0
print(temp_b)