# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 17:16:41 2021

@author: dell
"""

odds = [['2.47', '1.48'], ['1.20', '4.04'], ['1.38', '2.81'], ['2.89', '1.36'], ['1.65', '2.11'], ['5.55', '1.11'], ['1.30', '3.21'], ['2.89', '1.36'], ['1.42', '2.65'], ['2.73', '1.40'], ['3.73', '1.23'], ['2.99', '1.34'], ['2.36', '1.52'], ['1.61', '2.17'], ['21+', '2.16']]

Date =  ['Mon 27.09', 'Mon 27.09', 'Mon 27.09', 'Mon 27.09', 'Mon 27.09', 'Mon 27.09', 'Mon 27.09', 'Mon 27.09', 'Mon 27.09', 'Mon 27.09', 'Mon 27.09', 'Mon 27.09', 'Mon 27.09', 'Mon 27.09', 'Mon 27.09']

team = ['Baptiste, Hailey\nPaolini, Jasmine', 'Azarenka, Victoria\nZhang, Shuai', 'Anisimova, Amanda\nGolubic, Viktorija', 'Osorio Serrano, Maria Camila\nMartincova, Tereza', 'Cornet, Alize\nYastremska, Dayana', 'Brengle, Madison\nKontaveit, Anett', 'Bouzkova, Marie\nDoi, Misaki', 'Vandeweghe, Coco\nLinette, Magda', 'Teichmann, Jil\nKanepi, Kaia', 'Sasnovich, Aliaksandra\nKeys, Madison', 'Ruse, Elena-Gabriela\nGiorgi, Camila', 'Tomljanovic, Ajla\nVondrousova, Marketa', 'Clijsters, Kim\nHsieh, Su-Wei', 'Stephens, Sloane\nZidansek, Tamara', 'Vekic, Donna\nLI, Ann']

time = ['15:00', '15:00', '15:00', '15:00', '15:00', '15:00', '15:00', '15:00', '15:00', '15:00', '15:00', '15:00', '15:00', '15:00', '15:00']

team1 = []
team2 = []

odds1 = []
odds2 = []

final = []
final_list = []

#for t in team:
    #print(t.split("\n"))
#    team1.append(t.split("\n")[0])
 #   team2.append(t.split("\n")[1])
    #fla
for o in odds:
    if '+' in o[0]:
        print(o[0])
        #odds1.append(o[0])
        #odds2.append(o[1])
    
#for i,t1 in enumerate(team1):
#    final = [time[i],team1[i],team2[i],odds1[i],odds2[i],Date[i]]
#    final_list.append(final)
    
#print(team1)
#print(team2)
#print(odds1)
#print(odds2)
#print(final_list)



