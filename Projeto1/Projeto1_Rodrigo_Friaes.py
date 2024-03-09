# 1.2.1
def corrigir_palavra(s):
    i = 0
    while i < len(s)-1:
        if s[i] == chr(ord(s[i+1]) - ord('A') + ord('a')):    # se verificar um par mínuscula/maíscula da mesma letra
            s = s[:i] + s[i+2:]                               # remove o par e
            i = 0                                             # recomeça o ciclo
        elif s[i] == chr(ord(s[i+1]) - ord('a') + ord('A')):  # par maíscula/mínuscula da mesma letra
            s = s[:i] + s[i+2:]
            i = 0
        else:
            i += 1
    return s

# 1.2.2
def eh_anagrama(s1, s2):  # para verificar se duas palavras são anagramas, colocam-se com letras minusculas e
    s1, s2 = sorted(s1.lower()), sorted(s2.lower())  # e ordenam-se ambas
    return s1 == s2

# 1.2.3
def corrigir_doc(s):
    if not(type(s) == str and len(s) > 0):
        raise ValueError('corrigir_doc: argumento invalido')
    for c in s:
        if not ('a' <= c <= 'z' or 'A' <= c <= 'Z' or c == ' '):
            raise ValueError('corrigir_doc: argumento invalido')
    s = corrigir_palavra(s)
    s = s.split()
    res = []                    # 'frase resultante'
    encontrada = []             # "palavras ordenadas" encontradas
    for n in range(len(s)):
        p_ordenada = sorted(s[n].lower())
        if p_ordenada not in encontrada:
            encontrada += [p_ordenada]
            res.append(s[n])    # se uma certa "palavra ordenada" já tiver sido encontrada,
        elif s[n].lower() in " ".join(res).lower():  # verifica se esta 'palavra'
            res.append(s[n])    # já foi adicionada à 'frase resultante',pois caso já tiver sido adicionada,
    return " ".join(res)        # esta 'palavra' não é um anagrama duma palavra anterior

# 2.2.1
def obter_posicao(caracter, num):
    # para o num não exceder os limites nos movimentos:
    # ·para cima não deve exceder os valores da primeira linha
    if caracter == 'C' and num not in (1, 2, 3):
        num += -3
    # ·para baixo não deve exceder os valores da última linha
    elif caracter == 'B' and num not in (7, 8, 9):
        num += +3
    # ·para a esquerda não deve exceder os valores da primeira coluna
    elif caracter == 'E' and num not in (1, 4, 7):
        num += -1
    # ·para a direira não deve exceder os valores da última coluna
    elif caracter == 'D' and num not in (3, 6, 9):
        num += +1
    return num

# 2.2.2
def obter_digito(cadeia_de_caracteres, num):
    for mov in cadeia_de_caracteres:
        # obter posição em vários movimentos
        num = obter_posicao(mov, num)
    return num

# 2.2.3
def obter_pin(t):
    if not ((4 <= len(t) <= 10) and type(t) == tuple):
        raise ValueError('obter_pin: argumento invalido')
    pos = ((1, 2, 3), (4, 5, 6), (7, 8, 9))  # tuplo com os vários botões, sendo o n.º de cada linha e coluna
    pin = ()                                 # do painel de digitos reprensentado por pos[n.ºlinha][n.ºcoluna]
    num = 0
    linha, coluna = 1, 1  # começar no botão 5
    for s in t:
        if not (type(s) == str and len(s) > 0):
            raise ValueError('obter_pin: argumento invalido')
        i = 0
        while i < len(s):
            if not (s[i] in ('C','B','E','D')):
                raise ValueError('obter_pin: argumento invalido')
            elif s[i] == 'C' and 0 < linha < 3:
                linha += -1
                num = pos[linha][coluna]
            elif s[i] == 'B' and 0 <= linha < 2:
                linha += +1
                num = pos[linha][coluna]
            elif s[i] == 'E' and 0 < coluna < 3:
                coluna += -1
                num = pos[linha][coluna]
            elif s[i] == 'D' and 0 <= coluna < 2:
                coluna += +1
                num = pos[linha][coluna]
            i += 1
        pin += (num,)
    return pin

# 3.2.1
def eh_entrada(entrada_bdb):
    if not(type(entrada_bdb) == tuple and len(entrada_bdb) == 3 and type(entrada_bdb[0]) == str
       and type(entrada_bdb[1]) == str and type(entrada_bdb[2]) == tuple and len(entrada_bdb[2]) > 1):
        return False
    for a in entrada_bdb[0]:
        if not('a' <= a <= 'z' or a == '-'):
            return False
    for b in entrada_bdb[1][1:-1]:
        if not('a' <= b <= 'z' and entrada_bdb[1][0] == '[' and entrada_bdb[1][-1] == ']'
           and len(entrada_bdb[1][1:-1]) == 5):
            return False
    for c in entrada_bdb[2]:
        if not (type(c) == int and c > 0):
            return False
    return True

# 3.2.2
def validar_cifra(s1, s2):
    ocorrencias = {}
    ctrl = ''              # sequencia de controlo
    for i in s1:           # contar numero de ocorrências de cada caracter excluindo '-'
        if i != '-' and i not in ocorrencias:
            ocorrencias[i] = 1
        elif i in ocorrencias:
            ocorrencias[i] += 1
    for j in ocorrencias:  # comparar n.º de ocorrências entre caracteres da cifra
        k = 0              # caracter da sequencia de controlo
        while k < len(ocorrencias):
            if len(ctrl) == 0:        # se nenhum caracter da cifra tiver sido adicionado
                ctrl = j
                k = len(ocorrencias)  # avança para o próximo caracter da cifra
            elif k == len(ctrl):      # se o caracter já tiver sido comparado com todos os caracteres
                ctrl += j             # da sequencia de controlo, este é o que tem menor n.º de ocorrencias
                k = len(ocorrencias)
            elif ocorrencias[j] > ocorrencias[ctrl[k]]:   # se tiver mais ocorrencias que k é adicionado antes de k
                ctrl = ctrl[:k] + j + ctrl[k:]
                k = len(ocorrencias)
            elif ocorrencias[j] == ocorrencias[ctrl[k]]:  # mesmo n.º de ocorrencias
                if j > ctrl[k]:                           # se não estiverem por ordem alfabética:
                    k += 1                                # avança para o próximo caracter da sequencia de controlo.
                else:
                    ctrl = ctrl[:k] + j + ctrl[k:]        # se estiver por ordem alfabética o caracter é
                    k = len(ocorrencias)                  # adicionado antes de k
            elif ocorrencias[j] < ocorrencias[ctrl[k]]:   # se tiver menos ocorrencias que k
                k += 1                                    # avança para o próximo k
    controlo = '[' + ctrl[:5] + ']'
    if controlo == s2:
        return True
    return False

# 3.2.3
def filtrar_bdb(lista_bdb):
    entradas_invalidas = []
    if not (type(lista_bdb) == list and len(lista_bdb) > 0):
        raise ValueError('filtrar_bdb: argumento invalido')
    for entrada in lista_bdb:
        if not eh_entrada(entrada):
            raise ValueError('filtrar_bdb: argumento invalido')
        if not validar_cifra(entrada[0], entrada[1]):
            entradas_invalidas += [entrada]
    return entradas_invalidas

# 4.2.2
def obter_num_seguranca(t):
    subtracao = abs(t[0]-t[1])
    j = 0
    i = 1
    while i <= len(t):
        if i == len(t):  # comparar a subtração absoluta
            j += 1       # entre todos os elemetos do tuplo
            i = j + 1
        elif abs(t[j] - t[i]) <= subtracao:
            subtracao = abs(t[j] - t[i])
        i += 1
    return subtracao

# 4.2.3
def decifrar_texto(s, num):
    s = list(s)
    while num >= 26:  # retirar o excesso do numero de segurança
        num += -26   # retirando sucessivamente 26 (n.º de letras do alfabeto)
    for i in range(len(s)):
        if s[i] == '-':
            s[i] = ' '
        # indice par
        elif i % 2 == 0 and ord(s[i]) + num + 1 > ord('z'):  # se a adição do elemento de indice par
            s[i] = chr(ord(s[i]) + num + 1 - 26)             # e do número de segurança
        elif i % 2 == 0:                                     # ultrapassar 'z' retira o excesso
            s[i] = chr(ord(s[i]) + num + 1)
        # indice impar
        elif ord(s[i]) + num - 1 > ord('z'):
            s[i] = chr(ord(s[i]) + num - 1 - 26)
        elif ord(s[i]) + num - 1 < ord('a'):
            s[i] = chr(ord(s[i]) + num - 1 + 26)
        else:
            s[i] = chr(ord(s[i]) + num - 1)
    return "".join(s)

# 4.2.4
def decifrar_bdb(lista_bdb):
    decifrado = []
    if not (type(lista_bdb) == list and len(lista_bdb) > 0):
        raise ValueError('decifrar_bdb: argumento invalido')
    for entrada in lista_bdb:
        if not eh_entrada(entrada):
            raise ValueError('decifrar_bdb: argumento invalido')
        decifrado += [decifrar_texto(entrada[0], obter_num_seguranca(entrada[2]))]
    return decifrado

# 5.2.1
def eh_utilizador(dic):
    if not (type(dic) == dict and len(dic) == 3):
        return False
    for info in ('name','pass','rule'):
        if not(info in dic and type(dic['name']) == str and len(dic['name']) > 0
           and type(dic['pass']) == str and len(dic['pass']) > 0):
            return False
    for rule in ('vals','char'):
        if not(rule in dic['rule'] and type(dic['rule']) == dict and len(dic['rule']) == 2
           and type(dic['rule']['vals']) == tuple and len(dic['rule']['vals']) == 2
           and type(dic['rule']['char']) == str and len(dic['rule']['char']) == 1
           and ('a' <= dic['rule']['char'] <= 'z')):
            return False
    return True

# 5.2.2
def eh_senha_valida(senha,regra):
    minimo = regra['vals'][0]  # numero minimo de vezes que uma determinada letra minuscula deve aparecer
    maximo = regra['vals'][1]  # numero maximo
    contagem = {}
    num_vogais = 0
    for caracter in senha:  # contagem dos caracteres da senha
        if caracter not in contagem:
            contagem[caracter] = 1
        else:
            contagem[caracter] += 1
    for vogal in contagem:  # contagem das vogais para validar a regra geral em que a senha deve conter
        if vogal in ('a','e','i','o','u'):  # pelo menos três vogais minusculas
            num_vogais += contagem[vogal]
    if regra['char'] not in contagem or num_vogais < 3:
        return False
    return minimo <= contagem[regra['char']] <= maximo and letras_consecutivas(senha)

def letras_consecutivas(senha):
    valor = False
    i = 0
    while i < len(senha) - 1:  # validar a regra geral em que a senha deve conter
        if senha[i] == senha[i + 1]:  # pelo menos um caracter que apareça duas vezes consecutivas.
            valor = True
        i += 1
    return valor

# 5.2.3
def filtrar_senhas(lista_dic):
    utilizadores_invalidos = []
    if not (type(lista_dic) == list and len(lista_dic) > 0):
        raise ValueError('filtrar_senhas: argumento invalido')
    for info in lista_dic:
        if not eh_utilizador(info):
            raise ValueError('filtrar_senhas: argumento invalido')
        if not eh_senha_valida(info['pass'],info['rule']):
            utilizadores_invalidos += [info['name']]
    return sorted(utilizadores_invalidos)
