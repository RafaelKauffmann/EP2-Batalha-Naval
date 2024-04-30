import random as rd

def mapao(mcpu,mplr):
    mp = []
    for i in range(len(mcpu)):
        mp.append([])
        mp[i].append(i+1)
        for j in range(len(mcpu)):
            mp[i].append(mcpu[i][j])
        mp[i].append(i+1)
        mp[i].append(i+1)
        for j in range(len(mplr)):
            mp[i].append(mplr[i][j])
        mp[i].append(i+1)
    return mp

def esc_humberto():
    paises = ['Brasil', 'França', 'Austrália', 'Rússia', 'Japão']
    return paises[rd.randint(0,4)]

def cria_mapa(n):
    mapa = []
    for i in range(n):
         mapa.append([])
         for j in range(n):
              mapa[i].append(' ')
    return mapa