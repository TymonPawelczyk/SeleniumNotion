import io
import csv
import re
import pandas as pd

kolumny = []
komorki = []


with open("pytania.txt", "r", encoding="utf-8") as file1:
    read_content = file1.readlines()
    for i in read_content:
        
        try:
            x = int(i[0:1])
            if isinstance(x, int):
                # print('komorki')
                komorki.append(i)
        except:
            # print('Kolumna')
            if re.match('[^a-z]',i[0:2]):
                kolumny.append(i)
            else:
                komorki.append(i)
    
data = {key: [] for key in kolumny}
data['Architektura komputerów\n'].extend(komorki[:8])
data['Systemy operacyjne i programowanie systemowe\n'].extend(komorki[8:16])
data['Sieci komputerowe\n'].extend(komorki[16:24])
data['Algorytmy i struktury danych\n'].extend(komorki[24:44])
data['Programowanie\n'].extend(komorki[44:59])
data['Bazy danych\n'].extend(komorki[59:70])
data['Elementy grafiki komputerowej\n'].extend(komorki[70:80])
data['Podstawy Sztucznej Inteligencji\n'].extend(komorki[80:90])


# for x in data.keys():
#     print(x)
#     for i in data[x]:
#         print(i)

# for i in range(8):
#     data['Architektura komputerów\n'] = komorki[i]
# print(data)
# print(kolumny)
# print(komorki)
# for i in komorki:
#     print(i)
    
df = pd.DataFrame(komorki)
df[1] = df[0]
df.loc[:8,1] = 'Architektura komputerów'
df.loc[8:16,1] = 'Systemy operacyjne i programowanie systemowe'
df.loc[16:24,1] = 'Sieci komputerowe'
df.loc[24:44,1] = 'Algorytmy i struktury danych'
df.loc[44:59,1] = 'Programowanie'
df.loc[59:70,1] = 'Bazy danych'
df.loc[70:80,1] = 'Elementy grafiki komputerowej'
df.loc[80:90,1] = 'Podstawy Sztucznej Inteligencji'

print(df)

print(kolumny)