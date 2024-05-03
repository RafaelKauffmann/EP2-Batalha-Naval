import random as rd
import time as t
def main():
    # head
    print(' ================== x_x ========================== x_x ==================')
    print('|                                                                        |')
    print('| Bem-vindo ao SUPER BATALHA NAVAL HUMBERTO REDUX LIMITED DELUXE EDITION |')
    print('|                                                                        |')
    print(' ====================== ( °ㅁ°) ========== (°ㅁ° ) ======================\n')

    # memes e aviso ao jogador
    t.sleep(1)
    print('Lembre-se de jogar em tela cheia para maior Humbersã... quer dizer, imersão!')

    # seletor de dificuldade e escolha do país de Humberto
    print('Dificuldades:')
    print('"Tá fácil a vida??" [1] / "Normal... sem graça..." [2] / "Vejo vocês no quiz de quarta-feira..." [3]')
    dif = int(input('Selecione a dificuldade: '))
    humb = esc_humberto()
    dificuldade_escolhida = False
    while not dificuldade_escolhida:
        if dif in [1,2]:
            dificuldade_escolhida = True
            print(f'\nHumberto (seu oponente) está alocando os navios de guerra do país {humb}...\n')
        elif dif in [3]:
            dificuldade_escolhida = True
            print(f'\nHumberto, Major da Morte, está alocando os navios de guerra do país {humb}...\n')
        else:
            dif = int(input('Selecione a dificuldade (0, 1 ou 2 por favor): '))
    print('Iniciando a gameplay envolvente em: ', end=' ')
    for i in range(4):
        t.sleep(1)
        print(3-i, end=' ')

    # listas e dicionários
    colunas = ['  ','A','B','C','D','E','F','G','H','I','J','    ','A','B','C','D','E','F','G','H','I','J']
    paises = ['Brasil','França','Austrália','Rússia','Japão']
    d1 = {'Brasil':{'cruzador':1,'torpedeiro':2,'destroyer':1,'couraçado':1,'porta-aviões':1},
          'França':{'cruzador':3,'porta-aviões':1,'destroyer':1,'submarino':1,'couraçado':1},
          'Austrália':{'couraçado':1,'cruzador':3,'submarino':1,'porta-aviões':1,'torpedeiro':1},
          'Rússia':{'cruzador':1,'porta-aviões':1,'couraçado':2,'destroyer':1,'submarino':1},
          'Japão':{'torpedeiro':2,'cruzador':1,'destroyer':2,'couraçado':1,'submarino':1},}
    gab = {'cruzador':2,'torpedeiro':3,'destroyer':3,'couraçado':4,'porta-aviões':5,'submarino':2}
    letras = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10}
    nums = [1,2,3,4,5,6,7,8,9,10]
    letras_lista = ['a','b','c','d','e','f','g','h','i','j']
    jogadas_plr = []
    jogadas_cpu = []

    # alocação de navios - Humberto e criação de mapas
    frota_cpu = d1[humb]
    blocos_cpu = []
    for navio in frota_cpu:
        for i in range(frota_cpu[navio]):
            blocos_cpu.append(gab[navio])
    mapa_cpu = (aloca_navios(cria_mapa(10),blocos_cpu))
    mapa_player = cria_mapa(10)
    mapa_oculto = cria_mapa(10)

    # alocação de navios - player
    if dif in [0,1]:
        print('Humberto já está aguardando em posição de batalha!\n')
    else:
        print('\nHumberto já está aguardando sua rendição!\n')
    print('1: Brasil\n   1 cruzador\n   2 torpedeiro\n   1 destroyer\n   1 couraçado\n   1 porta-aviões\n\n\
2: França\n   3 cruzador\n   1 porta-aviões\n   1 destroyer\n   1 submarino\n   1 couraçado\n\n\
3: Austrália\n   1 couraçado\n   3 cruzador\n   1 submarino\n   1 porta-aviões\n   1 torpedeiro\n\n\
4: Rússia\n   1 cruzador\n   1 porta-aviões\n   2 couraçado\n   1 destroyer\n   1 submarino\n\n\
5: Japão\n   2 torpedeiro\n   1 cruzador\n   2 destroyer\n   1 couraçado\n   1 submarino\n')
    while True:
        e = int(input('Escolha o país da sua frota: [1/2/3/4/5]: '))
        if e not in [1,2,3,4,5]:
            print('Escolha inválida. Por favor escolha um país entre 1 e 5.')
        else:
            break
    print(f'Você escolheu o país {paises[e-1]}.')
    print('Agora é sua vez de alocar seus navios de guerra!')
    print('')
    frota_plr = d1[paises[e-1]]
    pais_plr = paises[e-1]
    for navio in frota_plr:
        for i in range(frota_plr[navio]):
            mapa_oculto = cor(mapa_oculto,'cpu')
            mapa_display = cor(mapa_player,'plr')
            print(f'      HUMBERTO - {humb}                                       JOGADOR - {pais_plr}')
            for i in range(len(colunas)):
                if i == len(colunas)-1:
                    print(colunas[i],end='\n')
                else:
                    print(colunas[i],end='    ')
            for linha in mapao(mapa_oculto,mapa_display):
                for e in linha:
                    if e in [1,2,3,4,5,6,7,8,9]:
                        print(' ',end='')
                        print(e,end='  ')
                    elif e in [10]:
                        print(e,end='  ')
                    else:
                        print(e,end='')
                print('')
            for i in range(len(colunas)):
                if i == len(colunas)-1:
                    print(colunas[i],end='\n')
                else:
                    print(colunas[i],end='    ')
            print('')
        
            print(f'Alocar {navio}, ({gab[navio]} blocos)')
            escolhido = False
            while not escolhido:
                col = str(input('Escolha a letra da coluna: '))
                li = int(input('Escolha o número da linha: '))
                ori = str(input('Escolha a orientação [v,h]: '))
                print('')
                if posicao_suporta(mapa_player,gab[navio],li-1,letras[col]-1,ori):
                    mapa_player = aloca_player(mapa_player,gab[navio],li-1,letras[col]-1,ori)
                    escolhido = True
                else:
                    print('Posição inválida! Por favor escolha outra.')

    # jogo começando
    mapa_oculto = cor(mapa_oculto,'cpu')
    mapa_display = cor(mapa_player,'plr')
    print(f'      HUMBERTO - {humb}                                       JOGADOR - {pais_plr}')
    for i in range(len(colunas)):
        if i == len(colunas)-1:
            print(colunas[i],end='\n')
        else:
            print(colunas[i],end='    ')
    for linha in mapao(mapa_oculto,mapa_display):
        for e in linha:
            if e in [1,2,3,4,5,6,7,8,9]:
                print(' ',end='')
                print(e,end='  ')
            elif e in [10]:
                print(e,end='  ')
            else:
                print(e,end='')
        print('')
    for i in range(len(colunas)):
        if i == len(colunas)-1:
            print(colunas[i],end='\n')
        else:
            print(colunas[i],end='    ')
    print('')


    while not foi_derrotado(mapa_cpu) or not foi_derrotado(mapa_player):
        t.sleep(1)
        mapa_oculto = cor(mapa_oculto,'cpu')
        mapa_display = cor(mapa_player,'plr')
        print(f'      HUMBERTO - {humb}                                       JOGADOR - {pais_plr}')
        for i in range(len(colunas)):
            if i == len(colunas)-1:
                print(colunas[i],end='\n')
            else:
                print(colunas[i],end='    ')
        for linha in mapao(mapa_oculto,mapa_display):
            for e in linha:
                if e in [1,2,3,4,5,6,7,8,9]:
                    print(' ',end='')
                    print(e,end='  ')
                elif e in [10]:
                    print(e,end='  ')
                else:
                    print(e,end='')
            print('')
        for i in range(len(colunas)):
            if i == len(colunas)-1:
                print(colunas[i],end='\n')
            else:
                print(colunas[i],end='    ')
        print('')
        
        print('Escolha uma cordenada para bombardear!')
        esc = False
        while not esc:
            a = str(input('Escolha o letra da coluna: '))
            b = input('Escolha o número da linha: ')
            if a in letras_lista and b in [1,2,3,4,5,6,7,8,9,10,'1','2','3','4','5','6','7','8','9','10']:
                coord_plr = a + str(b)
                b = int(b)
                if coord_plr not in jogadas_plr:
                    jogadas_plr.append(coord_plr)
                    esc = True
                else:
                    print('Essa coordenada já foi atacada! Escolha novamente.')
            else:
                print('Coordenada inválida! Escolha novamente.')
        
        print(f'Você atirou em {coord_plr}:', end=' ')
        t.sleep(1.5)
        if mapa_cpu[b-1][letras[a]-1] == 'N':
            mapa_cpu[b-1][letras[a]-1] = 'X'
            print('BOOM!')
        else:
            mapa_cpu[b-1][letras[a]-1] = 'A'
            print('Água')

        t.sleep(1)
        valida = False
        while valida == False:
            l_cpu = rd.choice(letras_lista)
            n_cpu = rd.randint(0,len(mapa_player))
            if l_cpu in letras_lista and n_cpu in nums:
                coord_cpu = l_cpu + str(n_cpu)
                if coord_cpu not in jogadas_cpu:
                    jogadas_cpu.append(coord_cpu)
                    valida = True
        
        print(f'Humberto atirou em {coord_cpu}:', end=' ')
        t.sleep(1.5)
        if mapa_player[n_cpu-1][letras[l_cpu]-1] == 'N':
            mapa_player[n_cpu-1][letras[l_cpu]-1] = 'X'
            print('BOOM!')
        else:
            mapa_player[n_cpu-1][letras[l_cpu]-1] = 'A'
            print('Água')
    
    if foi_derrotado(mapa_cpu) and not foi_derrotado(mapa_player):
        print('Você procurou coisa pra fazer e derrotou Humberto, Major da morte!')
    
    elif foi_derrotado(mapa_player) and not foi_derrotado(mapa_cpu):
        print('Humberto, Major da morte, derrotou você e te aprisionou no reino amaldiçoado da DP!')
    
    else:
        print('Vocês empataram, fizeram as pazes e foram viver juntos na Alemanha!')

    denovo = str(input('Jogar de novo? [s/n] '))
    resp = False
    while not resp:
        if denovo in ['s','S']:
            resp = True
            main()
            break
        elif denovo not in ['n','N']:
            print('Resposta inválida')
            denovo = str(input('Jogar de novo? [s/n] '))
        else:
            print('TCHAU (Dito com a voz do Humberto)')

# funções
def cor(m,id):
    red = '\u001b[31m▇▇▇▇▇\u001b[0m'
    green = '\u001b[32m▇▇▇▇▇\u001b[0m' 
    blue = '\u001b[34m▇▇▇▇▇\u001b[0m'
    mapa_novo = m
    if id == 'plr':
        for i in range(len(m)):
            for j in range(len(m)):
                if m[i][j] == ' ':
                    mapa_novo[i][j] = '     '
                elif m[i][j] == 'N':
                    mapa_novo[i][j] = green
                elif m[i][j] == 'X':
                    mapa_novo[i][j] = red
                elif m[i][j] == 'A':
                    m[i][j] = blue
    if id == 'cpu':
        for i in range(len(m)):
            for j in range(len(m)):
                if m[i][j] == ' ':
                    mapa_novo[i][j] = '     '
                elif m[i][j] == 'X':
                    mapa_novo[i][j] = red
                elif m[i][j] == 'A':
                    m[i][j] = blue
    return mapa_novo

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

def posicao_suporta(mapa,blocos,linha,coluna,orientacao):
    if mapa[linha][coluna] == 'N':
        return False
    for i in range(0,blocos):
        if orientacao == 'v':
            if linha + i > len(mapa)-1:
                return False
            if mapa[linha+i][coluna] == 'N':
                return False
        else:
            if coluna + i > len(mapa)-1:
                return False
            if mapa[linha][coluna+i] == 'N':
                return False 
    return True

def aloca_navios(m,b):
    mapa = m
    for i in range(len(b)):
        n = b[i]
        alocado = False
        while not alocado:
            l = rd.randint(0,len(mapa)-1)
            c = rd.randint(0,len(mapa)-1)
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

def foi_derrotado(m):
    derrotado = True
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] == 'N':
                derrotado = False
                break
    return derrotado

def aloca_player(m,n,l,c,o):
    m_novo = m
    if o in ['v']:
        for i in range(n):
            m_novo[l+i][c] = 'N'
    else:
        for i in range(n):
            m_novo[l][c+i] = 'N'
    return m_novo

main()