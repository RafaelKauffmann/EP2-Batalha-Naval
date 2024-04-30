    dificuldade_escolhida = False
    while not dificuldade_escolhida:
        if dif in [0,1]:
            dificuldade_escolhida = True
            print(f'\nHumberto (seu oponente) está alocando os navios de guerra do país {humb}...\n')
        elif dif in [2]:
            dificuldade_escolhida = True
            print(f'\nHumberto, Major da Morte, está alocando os navios de guerra do país {humb}...\n')
        else:
            dif = int(input('Selecione a dificuldade (0, 1 ou 2 por favor): '))
    print('Iniciando a gameplay envolvente em: ', end=' ')
    for i in range(4):
        t.sleep(1)
        print(3-i, end=' ')

    # listas e dicionários
    colunas = ['  ','A','B','C','D','E','F','G','H','I','J','  ','  ','A','B','C','D','E','F','G','H','I','J','  ']
    paises = ['Brasil','França','Austrália','Rússia','Japão']
    d1 = {'Brasil':{'cruzador':1,'torpedeiro':2,'destroyer':1,'couraçado':1,'porta-aviões':1},
          'França':{'cruzador':3,'porta-aviões':1,'destroyer':1,'submarino':1,'couraçado':1},
          'Austrália':{'couraçado':1,'cruzador':3,'submarino':1,'porta-aviões':1,'torpedeiro':1},
          'Rússia':{'cruzador':1,'porta-aviões':1,'couraçado':2,'destroyer':1,'submarino':1},
          'Japão':{'torpedeiro':2,'cruzador':1,'destroyer':2,'couraçado':1,'submarino':1},}
    gab = {'cruzador':2,'torpedeiro':3,'destroyer':3,'couraçado':4,'porta-aviões':5,'submarino':2}
    letras = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10}
    casas_atacadas = []