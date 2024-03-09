"""TAD posicao"""

# Construtor
def cria_posicao(x,y):
    if not (isinstance(x,int) and isinstance(y,int)
       and x >= 0 and y >= 0):
        raise ValueError('cria_posicao: argumentos invalidos')
    return x,y

def cria_copia_posicao(p):
    return cria_posicao(p[0],p[1])

# Seletores
def obter_pos_x(p):
    return p[0]
def obter_pos_y(p):
    return p[1]

# Reconhecedor
def eh_posicao(arg):
    if not (type(arg) == tuple and len(arg) == 2
       and isinstance(obter_pos_x(arg),int) and isinstance(obter_pos_y(arg),int)
       and obter_pos_x(arg) >= 0 and obter_pos_y(arg) >= 0):
        return False
    return True

# Teste
def posicoes_iguais(p1,p2):
    return p1 == p2 and eh_posicao(p1) and eh_posicao(p2)

# Transformador
def posicao_para_str(p):
    return str(p)

# Funções de alto nível
def obter_posicoes_adjacentes(p):
    pos_adjacentes = ()
    x = obter_pos_x(p)
    y = obter_pos_y(p)
    if y != 0:
        pos_adjacentes += ((x,y-1),)
    pos_adjacentes += ((x+1,y),)
    pos_adjacentes += ((x, y+1),)
    if x != 0:
        pos_adjacentes += ((x-1, y),)
    return pos_adjacentes

def ordenar_posicoes(t):
    return tuple(sorted(sorted(t), key=lambda x: obter_pos_y(x)))


"""TAD animal"""
# Construtor
def cria_animal(especie, reproducao, alimentacao):
    if not (type(especie) == str and type(reproducao) == int and type(alimentacao) == int
            and len(especie) > 0 and reproducao > 0 and alimentacao >= 0):
        raise ValueError('cria_animal: argumentos invalidos')
    return {'especie':especie, 'idade':0, 'fr_reprod':reproducao, 'fome':0, 'fr_aliment':alimentacao}

def cria_copia_animal(a):
    return a.copy()

# Seletores
def obter_especie(a):
    return a['especie']
def obter_freq_reproducao(a):
    return a['fr_reprod']
def obter_freq_alimentacao(a):
    return a['fr_aliment']
def obter_idade(a):
    return a['idade']
def obter_fome(a):
    return a['fome']

# Modificadores
def aumenta_idade(a):
    if obter_idade(a) < obter_freq_reproducao(a):
        a['idade'] += 1
    return a

def reset_idade(a):
    a['idade'] = 0
    return a

def aumenta_fome(a):
    if 0 < obter_freq_alimentacao(a) != obter_fome(a):
        a['fome'] += 1
    return a

def reset_fome(a):
    if obter_freq_alimentacao(a) > 0:
        a['fome'] = 0
    return a

# Reconhecedor
def eh_animal(a):
    d = ['especie','idade','fr_reprod','fome','fr_aliment']
    if type(a) != dict or len(a) != 5:
        return False
    for x in a:
        if x in d:
            d.remove(x)
        else:
            return False
    return True

def eh_predador(a):
    return eh_animal(a) and obter_freq_alimentacao(a) > 0
def eh_presa(a):
    return eh_animal(a) and obter_freq_alimentacao(a) == 0

# Teste
def animais_iguais(a1, a2):
    return a1 == a2 and eh_animal(a1) and eh_animal(a2)

# Transformadores
def animal_para_char(a):
    if obter_freq_alimentacao(a) == 0:
        return obter_especie(a)[0].lower()
    else:
        return obter_especie(a)[0].upper()

def animal_para_str(a):
    if obter_freq_alimentacao(a) == 0:
        return f'{obter_especie(a)} [{obter_idade(a)}/{obter_freq_reproducao(a)}]'
    else:
        return f'{obter_especie(a)} [{obter_idade(a)}/{obter_freq_reproducao(a)};\
{obter_fome(a)}/{obter_freq_alimentacao(a)}]'

# Funções de alto nível
def eh_animal_fertil(a):
    if obter_idade(a) == obter_freq_reproducao(a):
        return True
    return False

def eh_animal_faminto(a):
    if eh_predador(a) and obter_fome(a) == obter_freq_alimentacao(a):
        return True
    return False

def reproduz_animal(a):
    a = reset_idade(a)
    return cria_animal(obter_especie(a), obter_freq_reproducao(a), obter_freq_alimentacao(a))


"""TAD prado"""
# Construtor
def cria_prado(d, r, a, p):
    if not eh_posicao(d) or type(r) != tuple or\
       type(a) != tuple or type(p) != tuple or\
       True in [not eh_posicao(pos) for pos in p + r] +\
       [not eh_animal(animal) for animal in a]\
       or obter_pos_x(d) <= 1 or obter_pos_y(d) <= 1 or\
       len(a) != len(p) or len(a) == 0:
        raise ValueError('cria_prado: argumentos invalidos')
    posicoes1 = r + p
    posicoes2 = posicoes1
    for i in range(len(posicoes1)):
        if not(0 < posicoes1[i][0] < d[0] and 0 < posicoes1[i][1] < d[1]):
            raise ValueError('cria_prado: argumentos invalidos')
        if posicoes1[i] in posicoes2[i+1:]:
            raise ValueError('cria_prado: argumentos invalidos')
        else:
            posicoes2 = posicoes2[i+1:]
    return {'dim':d,'rochedos':r,'animais':a,'posicoes':p}

def cria_copia_prado(m):
    ans = ()
    for animal in m['animais']:
        ans += (cria_copia_animal(animal),)
    copia_prado = m.copy()
    copia_prado['animais'] = ans
    return copia_prado

# Seletores
def obter_tamanho_x(m):
    return m['dim'][0] + 1
def obter_tamanho_y(m):
    return m['dim'][1] + 1

def obter_numero_predadores(m):
    n_predadores = 0
    for animal in m['animais']:
        if eh_predador(animal):
            n_predadores += 1
    return n_predadores

def obter_numero_presas(m):
    n_presas = 0
    for animal in m['animais']:
        if eh_presa(animal):
            n_presas += 1
    return n_presas

def obter_posicao_animais(m):
    return ordenar_posicoes(m['posicoes'])

def obter_animal(m, p):
    for i in range(len(m['posicoes'])):
        if p == m['posicoes'][i]:
            return m['animais'][i]
    return {}

# Modificadores
def eliminar_animal(m, p):
    ans = ()
    pos = ()
    for i in range(len(m['animais'])):
        if p != m['posicoes'][i]:
            ans += (m['animais'][i],)
            pos += (m['posicoes'][i],)
    m['animais'], m['posicoes'] = ans, pos
    return m

def inserir_animal(m, a, p):
    m['animais'] += (a,)
    m['posicoes'] += (p,)
    return m

def mover_animal(m, p1, p2):
    inserir_animal(m, obter_animal(m, p1), p2)
    eliminar_animal(m, p1)
    return m

# Recohecedores
def eh_prado(arg):
    d = ['dim','rochedos','animais','posicoes']
    if not (type(arg) == dict and len(arg) == 4):
        return False
    for x in arg:
        if x in d:
            d.remove(x)
        else:
            return False
    return True

def eh_posicao_animal(m, p):
    if obter_animal(m,p):
        return True
    return False

def eh_posicao_obstaculo(m, p):
    if p in m['rochedos']\
       or obter_pos_x(p) in (0,obter_tamanho_x(m)-1)\
       or obter_pos_y(p) in (0,obter_tamanho_y(m)-1):
        return True
    return False

def eh_posicao_livre(m, p):
    if not eh_posicao_obstaculo(m,p)\
       and not eh_posicao_animal(m,p):
        return True
    return False

# Testes
def prados_iguais(p1, p2):
    return p1 == p2 and eh_prado(p1) and eh_prado(p2)

# Transformador
def prado_para_str(m):
    linha_sup = '+' + '-' * (obter_tamanho_x(m)-2) + '+\n'
    prado = linha_sup
    for linha_n in range(1,obter_tamanho_y(m)-1):
        prado += '|' + '.' * (obter_tamanho_x(m) - 2) + '|\n'
        for pos in obter_posicao_animais(m):
            if pos[1] == linha_n:
                prado = prado[:obter_valor_numerico(m,pos)+linha_n] +\
                        animal_para_char(obter_animal(m,pos)) +\
                        prado[obter_valor_numerico(m,pos)+linha_n+1:]
        for obs in m['rochedos']:
            if obs[1] == linha_n:
                prado = prado[:obter_valor_numerico(m,obs)+linha_n] +\
                        '@'+prado[obter_valor_numerico(m,obs)+linha_n+1:]
    prado += '+'+'-' * (obter_tamanho_x(m) - 2)+'+'
    return prado

# Funções de alto nível
def obter_valor_numerico(m, p):
    return obter_pos_x(p) +\
           obter_pos_y(p) * obter_tamanho_x(m)

def obter_movimento(m,p):
    if eh_animal(obter_animal(m,p)):
        pos_livres = tuple(x for x in obter_posicoes_adjacentes(p)
                           if eh_posicao_livre(m,x))
        pos_animais = tuple(x for x in obter_posicoes_adjacentes(p)
                            if eh_posicao_animal(m,x))
        pos_presas = tuple(x for x in pos_animais
                           if eh_presa(obter_animal(m,x)))
        if eh_predador(obter_animal(m,p)):
            if len(pos_presas) != 0:
                indice = obter_valor_numerico(m, p) % len(pos_presas)
                return pos_presas[indice]
        if len(pos_livres) == 0:
            return p
        else:
            indice = obter_valor_numerico(m, p) % len(pos_livres)
            return pos_livres[indice]


"""Funções adicionais"""
def geracao(m):
    for pos in obter_posicao_animais(m):  # posicoes
        animal = obter_animal(m, pos)
        mov = obter_movimento(m, pos)
        aumenta_idade(animal)
        aumenta_fome(animal)
        if eh_animal_fertil(animal) and not posicoes_iguais(pos,mov):  # reproducao
            novo_animal = reproduz_animal(animal)
            if eh_predador(animal) and eh_animal_faminto(animal):  # faminto
                eliminar_animal(m, pos)
                inserir_animal(m, novo_animal, pos)
            else:
                mover_animal(m, pos, mov)
                inserir_animal(m, novo_animal, pos)
        elif eh_posicao_animal(m,mov) and eh_presa(obter_animal(m,mov))\
                and eh_predador(animal):  # encontrou presa
            eliminar_animal(m,mov)
            reset_fome(animal)
            mover_animal(m, pos, mov)
        elif eh_animal_faminto(animal):  # faminto
            eliminar_animal(m,pos)
        elif not posicoes_iguais(pos,mov):
            mover_animal(m,pos,mov)
    return m


def simula_ecossistema(f,g,v):
    with open(f, 'r') as file:
        lines = file.readlines()
        lines = [eval(line.rstrip()) for line in lines]
        dim = cria_posicao(lines[0][0],lines[0][1])
        obs = tuple(cria_posicao(x[0],x[1]) for x in lines[1])
        an = ()
        pos = ()
    for animal in lines[2:]:
        an += (cria_animal(animal[0], animal[1], animal[2]),)
        pos += (cria_posicao(animal[3][0], animal[3][1]),)
    m = cria_prado(dim, obs, an, pos)

    def simula_ecossistema_aux(m,acc):
        n_predadores = obter_numero_predadores(m)
        n_presas = obter_numero_presas(m)
        prado = cria_copia_prado(m)
        geracao(prado)
        n_maximo = obter_valor_numerico(m,dim)+1-len(obs)\
                   -2*obter_tamanho_x(m)-2*obter_tamanho_y(m)+4
        if v:
            if acc == 0:
                print('Predadores:', n_predadores,
                      'vs Presas:',n_presas,
                      '(Gen. '+str(acc)+')')
                print(prado_para_str(m))
                return simula_ecossistema_aux(m, acc + 1)
            elif n_predadores != obter_numero_predadores(prado)\
                 or n_presas != obter_numero_presas(prado):
                print('Predadores:',obter_numero_predadores(prado),
                      'vs Presas:',obter_numero_presas(prado),
                      '(Gen. '+str(acc)+')')
                print(prado_para_str(geracao(m)))
                return simula_ecossistema_aux(m, acc + 1)
            elif n_predadores == n_maximo or n_presas == n_maximo or acc == g:
                return n_predadores,n_presas
            else:
                return simula_ecossistema_aux(geracao(m), acc + 1)
        else:
            if acc == g:
                print('Predadores:',n_predadores,
                      'vs Presas:',n_presas,
                      '(Gen. '+str(acc)+')')
                print(prado_para_str(m))
                return n_predadores,n_presas
            else:
                if acc == 0:
                    print('Predadores:',n_predadores,
                          'vs Presas:',n_presas,
                          '(Gen. '+str(acc)+')')
                    print(prado_para_str(m))
                return simula_ecossistema_aux(geracao(m), acc + 1)
    return simula_ecossistema_aux(m,0)
