import random as rd
def cria_mapa(dimensão):
    tabuleiro = []
    for i in range(0,dimensão):
        tabuleiro.append([])
        for e in range(0,dimensão):
            tabuleiro[i].append(' ')
    return tabuleiro

def posicao_suporta(mapa,blocos,linha,coluna,orientacao):
    m = mapa
    if linha >= len(mapa) or coluna >= len(mapa): return False
    if orientacao == 'h':
        if coluna+blocos > len(mapa): return False
    elif orientacao == 'v':
        if linha+blocos > len(mapa): return False
    for i in range(1,blocos):
        if orientacao == 'v':
            if m[linha+i][coluna] == 'N':
                return False
        else:
            if m[linha][coluna+i] == 'N':
                return False 
    return True

def aloca_navios_c(m,b):
    mapa = m
    for i in range(len(b)):
        n = b[i]
        alocado = False
        while not alocado:
            a = len(mapa)-1
            l = rd.randint(0,a)
            c = rd.randint(0,a)
            o = rd.choice(['h','v'])
            sup = posicao_suporta(mapa,n,l,c,o)
            if sup:
                alocado = True

        if o in ['v']:
                for i in range(n):
                        mapa[l+i][c] = 'N'

        else:
                for i in range(n):
                        mapa[l][c+i] = 'N'
    return mapa

def foi_derrotado(mapa):
    for i in range(0,len(mapa)):
        for e in mapa[i]:
            if e == 'N':
                return False
    return True