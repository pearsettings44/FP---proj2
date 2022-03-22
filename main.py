############################################################
#             Projeto 2 de FP                              #
#             Nome: José Augusto Alves Pereira             #
#             Número: ist1103252                           #
#             Email: jose.a.pereira@tecnico.ulisboa.pt     #
#             Data: 15/11/2021                             #
############################################################

###############
# TAD Posicao #
###############

# Representacao: R[x, y] = {'x': x, 'y': y}
# cria_posicao: int , int -> posicao
# cria_copia_posicao: posicao -> posicao
# obter_pos_x: posicao -> int
# obter_pos_y: posicao -> int
# eh_posicao: universal -> booleano
# posicoes_iguais: posicao , posicao -> booleano
# posicao_para_str: posicao -> str
# obter_posicoes_adjacentes: posicao -> tuple
# ordenar_posicoes: tuple -> tuple


def cria_posicao(x, y):
    """
    cria_posicao(x, y): Recebe os valores correspondentes às coordenadas de uma posição e
    devolve a posição correspondente. Este contrustor verifica a validade dos seus argumentos.
    int, int ---> posicao
    """
    posicao = {"x": x, "y": y}
    if eh_posicao(posicao):
        return posicao
    raise ValueError("cria_posicao: argumentos invalidos")


def cria_copia_posicao(posicao):
    """
    cria_copia_posicao(posicao): Recebe uma posição e devolve uma cópia nova da posição.
    posicao ---> posicao
    """
    if eh_posicao(posicao):
        return dict(posicao)
    else:
        raise ValueError("cria_copia_posicao: argumentos invalidos")


def obter_pos_x(posicao):
    """
    obter_pos_x(posicao): Devolve a componente x da posição.
    posicao ---> int
    """
    return posicao["x"]


def obter_pos_y(posicao):
    """
    obter_pos_y(posicao): Devolve a componente y da posicao.
    posicao ---> int
    """
    return posicao["y"]


def eh_posicao(posicao):
    """
    eh_posicao(posicao): Devolve True caso o posicao seja um TAD posicao e False caso contrário.
    universal ---> bool
    """
    return isinstance(posicao, dict) and len(posicao) == 2 and "x" in posicao and "y" in posicao and \
        type(posicao["x"]) == int and type(posicao["y"]) == int and posicao["y"] >= 0 and posicao["x"] >= 0


def posicoes_iguais(pos1, pos2):
    """
    posicoes_iguais(pos1, pos2): Devolve True apenas se pos1 e pos2 são posições e são iguais.
    posicao, posicao ---> bool
    """
    return pos1 == pos2


def posicao_para_str(pos):
    """
    posicao_para_str(pos): Devolve a cadeia de caracteres '(x, y)' que representa
    o seu argumento (pos), sendo os valores de x e y as coordenadas de pos.
    posicao ---> str
    """
    return "(" + str(pos["x"]) + ", " + str(pos["y"]) + ")"


def obter_posicoes_adjacentes(pos):
    """
    obter_posicoes_adjacentes(p): Devolve um tuplo com as posições adjacentes
    à posicão de p, começando pela posição acima de p e seguindo no sentido horário.
    posicao ---> tuple
    """
    x, y = obter_pos_x(pos), obter_pos_y(pos)
    if x == 0 and y == 0:  # Caso não haja posicões adjacentes à esquerda e em baixo
        posicoes_adjacentes = (cria_posicao(x + 1, y), cria_posicao(x, y + 1))
    elif x == 0:  # Caso não haja posicões adjacentes à esquerda
        posicoes_adjacentes = (cria_posicao(x, y - 1), cria_posicao(x + 1, y), cria_posicao(x, y + 1))
    elif y == 0:  # Caso não haja posicões adjacentes em baixo
        posicoes_adjacentes = (cria_posicao(x + 1, y), cria_posicao(x, y + 1), cria_posicao(x - 1, y))
    else:
        posicoes_adjacentes = (cria_posicao(x, y - 1), cria_posicao(x + 1, y),
                               cria_posicao(x, y + 1), cria_posicao(x - 1, y))
    return posicoes_adjacentes


def ordenar_posicoes(t_posicoes):
    """
    ordenar_posicoes(t): Devolve um tuplo contendo as mesmas posições do tuplo
    fornecido como argumento, ordenadas de acordo com a ordem de leitura do prado.
    tuple ---> tuple
    """
    t_posicoes = list(t_posicoes)
    flag = True
    while flag:
        flag = False
        for i in range(0, len(t_posicoes) - 1):
            # Ordenar posicões de acordo com o valor do seu y
            if obter_pos_y(t_posicoes[i]) > obter_pos_y(t_posicoes[i + 1]):
                t_posicoes[i], t_posicoes[i + 1] = t_posicoes[i + 1], t_posicoes[i]
                flag = True
            # Ordenar posicoes com y igual de acordo com o seu x
            if obter_pos_y(t_posicoes[i]) == obter_pos_y(t_posicoes[i + 1]) and \
                    obter_pos_x(t_posicoes[i]) > obter_pos_x(t_posicoes[i + 1]):
                t_posicoes[i], t_posicoes[i + 1] = t_posicoes[i + 1], t_posicoes[i]
    t_posicoes = tuple(t_posicoes)
    return t_posicoes


###############
# TAD Animal  #
###############

# Representacao: R[especie, frequeência de reprodução, frequência de alimentação, idade, fome] =
# Representacao: = {"especie": especie, "f_reproducao": reproducao, "f_alimentacao": alimentacao, "idade": 0, "fome": 0}
# cria_animal: str, str, int -> animal
# #cria_copia_animal: animal -> animal
# obter_especie: animal -> str
# obter_freq_reproducao: animal -> int
# obter_freq_alimentacao: animal -> int
# obter_idade: animal -> int
# obter_fome: animal -> int
# aumenta_idade: animal -> animal
# reset_idade: animal -> animal
# aumenta_fome: animal -> animal
# reset_fome: animal -> animal
# eh_animal: animal -> bool
# eh_predador: animal -> bool
# eh_presa: animal -> bool
# animais_iguais: animal -> bool
# animal_para_char: animal -> str
# animal_para_str: animal -> str
# eh_animal_fertil: animal -> bool
# eh_animal faminto: animal -> bool
# reproduz_animal: animal -> animal


def cria_animal(especie, reproducao, alimentacao):
    """
    cria_animal(especie, reproducao, alimentacao): Recebe uma cadeia de caracteres (especie) correspondente à
    espécie do animal e dois valores inteiros correspondentes à frequência de reprodução (reproducao) e à
    frequência de alimentação (alimentacao) e devolve o animal.
    str, int, int ---> animal
    """
    animal = {"especie": especie, "f_reproducao": reproducao, "f_alimentacao": alimentacao, "idade": 0, "fome": 0}
    if eh_animal(animal):
        return animal
    raise ValueError("cria_animal: argumentos invalidos")


def cria_copia_animal(animal):
    """
    cria_copia_animal(animal): Recebe um animal (animal), predador ou presa, e devolve
    uma nova cópia do animal.
    animal ---> animal
    """
    if eh_animal(animal):
        return dict(animal)
    else:
        raise ValueError("cria_animal: argumentos invalidos")


def obter_especie(animal):
    """
    obter_especie(animal): Devolve a cadeia de caracteres correspondente à espécie do animal.
    animal ---> str
    """
    return animal["especie"]


def obter_freq_reproducao(animal):
    """
    obter_especie(animal): Devolve a frequência de reprodução do animal (animal).
    animal ---> str
    """
    return animal["f_reproducao"]


def obter_freq_alimentacao(animal):
    """
    obter_freq_alimentacao(animal): Devolve a frequência de alimentação do animal (animal).
    animal ---> str
    """
    return animal["f_alimentacao"]


def obter_idade(animal):
    """
    obter_idade(animal): Devolve a idade do animal (animal).
    animal ---> int
    """
    return animal["idade"]


def obter_fome(animal):
    """
    obter_fome(animal): Devolve a fome do animal (animal).
    animal ---> int
    """
    return animal["fome"]


def aumenta_idade(animal):
    """
    aumenta_idade(animal):  Modifica destrutivamente o animal (animal) incrementando o
    valor da sua idade em uma unidade, e devolve o próprio animal.
    animal ---> animal
    """
    animal["idade"] += 1
    return animal


def reset_idade(animal):
    """
    reset_idade(animal): Modifica destrutivamente o animal (animal) definindo
    o valor da sua idade igual a 0, e devolve o próprio animal.
    animal ---> animal
    """
    animal["idade"] = 0
    return animal


def aumenta_fome(animal):
    """
    aumenta_fome(animal): modifica destrutivamente o animal predador (animal) incrementando
    o valor da sua fome em uma unidade, e devolve o próprio animal.
    animal ---> animal
    """
    if eh_predador(animal):
        animal["fome"] += 1
    return animal


def reset_fome(animal):
    """
    reset_fome(animal): modifica destrutivamente o animal predador (animal) definindo
    o valor da sua fome igual a 0, e devolve o próprio animal.
    animal ---> animal
    """
    if eh_predador(animal):
        animal["fome"] = 0
    return animal


def eh_animal(animal):
    """
    eh animal(animal): devolve True caso o seu argumento
    seja um TAD animal e False caso contrário
    universal --→ bool
    """
    argumentos = ["especie", "f_reproducao", "f_alimentacao", "idade", "fome"]
    return isinstance(animal, dict) and len(animal) == 5 and all(x in animal.keys() for x in argumentos) and \
        isinstance(animal["especie"], str) and len(animal["especie"]) != 0 and \
        isinstance(animal["f_reproducao"], int) and animal["f_reproducao"] > 0 and \
        isinstance(animal["f_alimentacao"], int) and animal["f_alimentacao"] >= 0 and \
        isinstance(animal["idade"], int) and animal["idade"] >= 0 and \
        isinstance(animal["fome"], int) and animal["fome"] >= 0


def eh_predador(animal):
    """
    eh_predador(animal): devolve True caso o seu argumento
    seja um TAD animal do tipo predador e False caso contrário.
    animal ---> bool
    """
    return eh_animal(animal) and obter_freq_alimentacao(animal) > 0


def eh_presa(animal):
    """
    eh_presa(animal): devolve True caso o seu argumento
    seja um TAD animal do tipo presa e False caso contrário.
    animal ---> bool
    """
    return eh_animal(animal) and obter_freq_alimentacao(animal) == 0


def animais_iguais(animal1, animal2):
    """
    animais_iguais(animal1, animal2): devolve True apenas se a1 e a2 são animais e são iguais.
    animal, animal ---> bool
    """
    if eh_animal(animal1) and eh_animal(animal2):
        if obter_especie(animal1) == obter_especie(animal2) and \
                obter_freq_alimentacao(animal1) == obter_freq_alimentacao(animal2) and \
                obter_freq_reproducao(animal1) == obter_freq_reproducao(animal2) and \
                obter_idade(animal1) == obter_idade(animal2) and \
                obter_fome(animal1) == obter_fome(animal2):
            return True
        else:
            return False
    return False


def animal_para_char(animal):
    """
    animal_para_char(animal): devolve a cadeia de caracteres dum único elemento
    correspondente ao primeiro carácter da espécie do animal passada por argumento,
    em maiúscula para animais predadores e em minúscula para animais presa.
    animal ---> str
    """
    if eh_predador(animal):
        return animal["especie"][0].upper()
    else:
        return animal["especie"][0].lower()


def animal_para_str(animal):
    """
    animal_para_str(animal): devolve a cadeia de caracteres que representa o animal.
    animal ---> str
    """
    if eh_predador(animal):
        return animal["especie"] + " [" + str(animal["idade"]) + "/" + str(animal["f_reproducao"]) + ";" + \
               str(animal["fome"]) + "/" + str(animal["f_alimentacao"]) + "]"
    else:
        return animal["especie"] + " [" + str(animal["idade"]) + "/" + str(animal["f_reproducao"]) + "]"


def eh_animal_fertil(animal):
    """
    eh_animal_fertil(animal): devolve True caso o animal a tenha atingido a idade de reprodução e False caso contrário.
    animal ---> bool
    """
    return obter_idade(animal) >= obter_freq_reproducao(animal)


def eh_animal_faminto(animal):
    """
    eh_animal_faminto(animal): devolve True caso o animal (animal) tenha atingindo um valor de
    fome igual ou superior á sua frequência de alimentação e False caso contrário. As
    presas devolvem sempre False.
    animal ---> bool
    """
    return 0 < obter_freq_alimentacao(animal) <= obter_fome(animal)


def reproduz_animal(animal):
    """
    reproduz_animal(animal): recebe um animal (animal) devolvendo um novo animal da mesma
    espécie com idade e fome igual a 0, e modificando destrutivamente o animal passado
    como argumento (animal) alterando a sua idade para 0.
    """
    animal_reproduzido = cria_copia_animal(animal)
    reset_fome(animal_reproduzido)
    reset_idade(animal_reproduzido)
    reset_idade(animal)
    return animal_reproduzido


#############
# TAD Prado #
#############

# cria_prado: posicao, tuple, tuple, tuple -> prado
# cria_copia_prado: prado -> prado
# obter_tamanho_x: prado -> int
# obter_tamanho_y: prado -> int
# obter_numero_predadores: prado -> int
# obter_numero_presas: prado -> int
# obter_posicao_animais: prado -> tuple posicoes
# obter_animal: prado, posicao -> animal
# eliminar_animal: prado, posicao -> prado
# mover_animal: prado, posicao, posicao -> prado
# inserir_animal: prado, animal, posicao -> prado
# eh_prado: universal -> bool
# eh_posicao_animal: prado, posicao -> bool
# eh_posicao_obstaculo: prado, posicao -> bool
# eh_posicao_livre: prado, posicao -> bool
# prados_iguais: prado, prado -> bool
# prado_para_str: prado -> str
# obter_valor_numerico: prado, posicao -> int
# obter_movimento: prado, posicao -> posicao


def cria_prado(canto_inf_dt, rochedos, animais, pos_animais):
    """
    Devolve o prado que representa internamente o mapa e os animais presentes.
    posicao, tuple, tuple, tuple ---> prado
    """
    prado = {"canto_inf_dt": canto_inf_dt, "rochedos": rochedos, "animais": animais, "pos_animais": pos_animais}
    if eh_prado(prado):
        return prado
    raise ValueError("cria_prado: argumentos invalidos")


def cria_copia_prado(prado):
    """
    cria_copia_prado: Recebe um prado e devolve uma nova c ́opia do prado.
    prado ---> prado
    """
    if eh_prado(prado):
        return dict(prado)
    else:
        raise ValueError("cria_animal: argumentos invalidos")


def obter_tamanho_x(prado):
    """
    obter_tamanho_x(prado): Devolve o valor inteiro que corresponde à dimensâo N(x) do prado.
    prado ---> int
    """
    return obter_pos_x(prado["canto_inf_dt"]) + 1


def obter_tamanho_y(prado):
    """
    obter_tamanho_y(prado): Devolve o valor inteiro que corresponde à dimensâo N(y) do prado.
    prado ---> int
    """
    return obter_pos_y(prado["canto_inf_dt"]) + 1


def obter_numero_predadores(prado):
    """
    obter_numero_predadores(prado): Devolve o número de animais predadores no prado.
    prado ---> int
    """
    numero_predadores = 0
    for animal in prado["animais"]:
        if eh_predador(animal):
            numero_predadores += 1
    return numero_predadores


def obter_numero_presas(prado):
    """
    obter_numero_presas(prado): Devolve o número de animais presas no prado.
    prado ---> int
    """
    numero_presas = 0
    for animal in prado["animais"]:
        if eh_presa(animal):
            numero_presas += 1
    return numero_presas


def obter_posicao_animais(prado):
    """
    obter_posicao_animais(prado): devolve um tuplo contendo as posições do prado
    ocupadas por animais, ordenadas em ordem de leitura do prado.
    prado ---> tuple posicoes
    """
    posicoes = ()
    for posicao_animal in prado["pos_animais"]:
        posicoes += (posicao_animal,)
    return ordenar_posicoes(posicoes)


def obter_animal(prado, posicao):
    """
    obter_animal(prado, posicao): devolve o animal do prado que se encontra na posição (posicao).
    prado, posicao ---> animal
    """
    posicoes = prado["pos_animais"]
    for index, posicao_animal in enumerate(posicoes):
        if posicoes_iguais(posicao_animal, posicao):
            return prado["animais"][index]


def eliminar_animal(prado, posicao):
    """
    eliminar_animal(prado, posicao): Modifica destrutivamente o prado (prado) eliminando o
    animal da posição (posicao) deixando-a livre. Devolve o próprio prado.
    prado, posicao ---> prado
    """
    for index, posicao_animal in enumerate(prado["pos_animais"]):
        if posicoes_iguais(posicao_animal, posicao):
            lista_posicoes_animais, lista_animais = list(prado["pos_animais"]), list(prado["animais"])
            del lista_posicoes_animais[index]
            del lista_animais[index]
            prado["animais"], prado["pos_animais"] = tuple(lista_animais), tuple(lista_posicoes_animais)
            return prado


def mover_animal(prado, posicao1, posicao2):
    """
    mover_animal(prado, posicao1, posicao2): Modifica destrutivamente o prado (prado) movimentando
    o animal da posição posicao1 para a nova posição posicao2, deixando livre a posição onde
    se encontrava. Devolve o próprio prado.
    prado, posicao, posicao ---> prado
    """
    posicoes = list(prado["pos_animais"])
    for index, posicao in enumerate(posicoes):
        if posicoes_iguais(posicao, posicao1):
            posicoes[index] = posicao2
    posicoes = tuple(posicoes)
    prado["pos_animais"] = posicoes
    return prado


def inserir_animal(prado, animal, posicao):
    """
    inserir_animal(prado, animal, posicao): Modifica destrutivamente o prado (prado) acrescentando
    na posição (posicao) do prado o animal (animal) passado com argumento. Devolve o próprio prado.
    prado, animal, posicao ---> prado
    """
    posicoes, animais = list(prado["pos_animais"]), list(prado["animais"])
    posicoes.append(posicao)
    animais.append(animal)
    posicoes, animais = tuple(posicoes), tuple(animais)
    prado["animais"], prado["pos_animais"] = animais, posicoes
    return prado


def nao_e_montanha(limite, posicoes):
    """
    nao_e_montanha(limite, posicoes): Função auxiliar á função eh_prado. Devolve True caso nenhuma posição recebida
    como argumento corresponda a uma posição de montanha. Devolve False caso contrário.
    posicao, posicao ---> bool
    """
    return all(obter_pos_x(posicao) != 0 for posicao in posicoes) and \
        all(obter_pos_x(posicao) != obter_pos_x(limite) for posicao in posicoes) and \
        all(obter_pos_y(posicao) != 0 for posicao in posicoes) and \
        all(obter_pos_y(posicao) != obter_pos_y(limite) for posicao in posicoes)


def eh_prado_representacao_valida(prado):
    """
    eh_prado_representacao_valida(prado): Função auxiliar à função eh_prado. Devolve True caso
    a representação geral do TAD eh_prado esteja correta, caso contrário devolve False
    prado ---> bool
    """
    argumentos = ["canto_inf_dt", "rochedos", "animais", "pos_animais"]
    return isinstance(prado, dict) and len(prado) == 4 and \
        all(argumento in prado.keys() for argumento in argumentos)


def eh_prado_rochedos_validos(prado):
    """
    eh_prado_rochedos_validos(prado): Função auxiliar à função eh_prado. Devolve True caso
    os rochedos sejam válidos, caso contrário devolve False
    prado ---> bool
    """
    return isinstance(prado["rochedos"], tuple) and isinstance(prado["rochedos"], tuple) and \
        all(eh_posicao(posicao) for posicao in prado["rochedos"]) and \
        nao_e_montanha(prado["canto_inf_dt"], prado["rochedos"]) and \
        all(obter_pos_x(rochedo) <= obter_pos_x(prado["canto_inf_dt"]) for rochedo in prado["rochedos"])


def eh_prado_animais_validos(prado):
    """
    eh_prado_animais_validos(prado): Função auxiliar à função eh_prado. Devolve True caso
    os animais sejam válidos, caso contrário devolve False
    prado ---> bool
    """
    return isinstance(prado["animais"], tuple) and len(prado["animais"]) >= 1 and \
        all(eh_animal(animal) for animal in prado["animais"])


def eh_prado_pos_animais_valido(prado):
    """
    eh_prado_pos_animais_valido(prado): Função auxiliar à função eh_prado. Devolve True caso
    as posições dos animais sejam válidas, caso contrário devolve False
    prado ---> bool
    """
    return isinstance(prado["pos_animais"], tuple) and \
        len(prado["animais"]) == len(prado["pos_animais"]) and \
        all(eh_posicao(posicao) for posicao in prado["pos_animais"]) and \
        nao_e_montanha(prado["canto_inf_dt"], prado["pos_animais"]) and not \
        any(posicao in prado["rochedos"] for posicao in prado["pos_animais"])


def eh_prado(prado):
    """
    eh_prado(prado): devolve True caso o seu argumento seja um TAD prado e False caso contrário.
    prado ---> bool
    """
    return eh_prado_representacao_valida(prado) and eh_posicao(prado["canto_inf_dt"]) and \
        eh_prado_rochedos_validos(prado) and eh_prado_animais_validos(prado) and \
        eh_prado_pos_animais_valido(prado)


def eh_posicao_animal(prado, posicao):
    """
    eh_posicao_animal(prado, posicao): Devolve True apenas no caso
    da posição (posicao) do prado estar ocupada por um animal.
    prado, posicao ---> bool
    """
    return any(posicoes_iguais(posicao, posicao_animal) for posicao_animal in prado["pos_animais"])


def eh_posicao_obstaculo(prado, posicao):
    """
    eh_posicao_obstaculo(prado, posicao): Devolve True apenas no caso
    da posição (posicao) do prado corresponder a uma montanha ou rochedo.
    prado, posicao ---> bool
    """
    return any(posicoes_iguais(posicao, posicao_obstaculo) for posicao_obstaculo in prado["rochedos"]) or \
        not nao_e_montanha(prado["canto_inf_dt"], (posicao,))


def eh_posicao_livre(prado, posicao):
    """
    eh_posicao_livre(prado, posicao): Devolve True apenas no caso da posição (posicao) do prado
    corresponder a um espaço livre (sem animais, nem obstáculos).
    prado, posicao ---> bool
    """
    return not eh_posicao_obstaculo(prado, posicao) and not eh_posicao_animal(prado, posicao)


def obter_posicao_rochedos(prado):
    """
    obter_posicao_rochedos(prado): Função auxiliar á função prados_iguais. Devolve as posições ordenadas dos rochedos.
    prado ---> tuple posicoes
    """
    posicoes = ()
    for posicao_rochedo in prado["rochedos"]:
        posicoes += (posicao_rochedo,)
    return ordenar_posicoes(posicoes)


def obter_animais(prado):
    """
    obter_posicao_animais(prado): Função auxiliar á função prados_iguais. Devolve os animais.
    """
    animais = ()
    for posicao in obter_posicao_animais(prado):
        animais += (obter_animal(prado, posicao),)
    return animais


def prados_iguais(prado1, prado2):
    """
    prados_iguais(prado1, prado2):devolve True apenas se prado1 e prado2 forem prados e forem iguais.
    prado, prado ---> bool
    """
    if eh_prado(prado1) and eh_prado(prado2):
        if obter_tamanho_y(prado1) == obter_tamanho_y(prado2) and \
                obter_tamanho_x(prado1) == obter_tamanho_x(prado2) and \
                obter_posicao_animais(prado1) == obter_posicao_animais(prado2) and \
                obter_posicao_rochedos(prado1) == obter_posicao_rochedos(prado2) and \
                obter_animais(prado1) == obter_animais(prado2):
            return True
        else:
            return False
    return False


def eh_canto(prado, posicao):
    """
    eh_canto(prado, posicao): Função auxiliar á função prado_para_str. Recebe um prado e uma posição e
    devolve True se a posição recebida corresponde a um dos cantos do prado, False caso contrário.
    prado, posicao ---> bool
    """
    canto_sup_esq, canto_sup_dt = cria_posicao(0, 0), cria_posicao(obter_tamanho_x(prado) - 1, 0)
    canto_inf_esq, canto_inf_dt = cria_posicao(0, obter_tamanho_y(prado) - 1), prado["canto_inf_dt"]
    return posicoes_iguais(posicao, canto_inf_dt) or posicoes_iguais(posicao, canto_inf_esq) or \
        posicoes_iguais(posicao, canto_sup_esq) or posicoes_iguais(posicao, canto_sup_dt)


def eh_cima_ou_baixo(prado, posicao):
    """
    eh_cima_ou_baixo(prado, posicao): Função auxiliar á função prado_para_str. Recebe um prado e uma posição e
    devolve True se a posição recebida corresponde a uma posição na extremidade superior ou inferior do prado,
    devolvendo False caso contrário.
    prado, posicao ---> bool
    """
    return obter_pos_y(posicao) == 0 or obter_pos_y(posicao) == obter_tamanho_y(prado) - 1


def eh_esq_ou_dt(prado, posicao):
    """
    eh_esq_ou_dt(prado, posicao): Função auxiliar á função prado_para_str. Recebe um prado e uma posição e
    devolve True se a posição recebida corresponde a uma posição na extremidade esquerda ou direita do prado,
    devolvendo False caso contrário.
    prado, posicao ---> bool
    """
    return obter_pos_x(posicao) == 0 or obter_pos_x(posicao) == obter_tamanho_x(prado) - 1


def decide_simbolo(prado, x, y):
    """
    decide_simbolo(prado, x, y): Função auxiliar à função prado_para_str. Recebe um prado e o x e y de uma posição,
    e utiliza outras funções auxiliares para definir a representação da posição dependendo da posição que se trata.
    prado, int, int ---> str
    """
    if eh_canto(prado, cria_posicao(x, y)):
        return "+"  # Simbolo "+" corresponde a uma posição num dos cantos do prado.
    elif eh_cima_ou_baixo(prado, cria_posicao(x, y)):
        return "-"  # Simbolo "-" corresponde a uma posição numa das extremidades superiores ou inferior do prado.
    elif eh_esq_ou_dt(prado, cria_posicao(x, y)):
        return "|"  # Simbolo "|" corresponde a uma posição numa das extremidades laterais do prado.
    elif eh_posicao_obstaculo(prado, cria_posicao(x, y)) and \
            nao_e_montanha(prado["canto_inf_dt"], (cria_posicao(x, y),)):
        return "@"  # Simbolo "@" corresponde a uma posição ocupada por um rochedo do prado.
    elif eh_posicao_animal(prado, cria_posicao(x, y)):  # Animais representam-se pelo primeiro caracter da sua especie
        return animal_para_char(obter_animal(prado, cria_posicao(x, y)))
    else:
        return "."  # Simbolo "." corresponde a uma posição livre do prado.


def prado_para_str(prado):
    """
    prado_para_str(prado): Devolve uma cadeia de caracteres que representa o prado
    prado ---> str
    """
    prado_str = ""
    for y in range(0, obter_tamanho_y(prado)):
        for x in range(0, obter_tamanho_x(prado)):
            simbolo = decide_simbolo(prado, x, y)
            prado_str += simbolo
        prado_str += "\n"
    return prado_str[:-1]


def obter_valor_numerico(prado, posicao):
    """
    obter_valor_numerico(prado, posicao): Devolve o valor numérico da
    posição (posicao) correspondente à ordem de leitura no prado (prado).
    prado, posicao ---> int
    """
    contador = 0
    for y in range(0, obter_tamanho_y(prado)):
        for x in range(0, obter_tamanho_x(prado)):
            if x == obter_pos_x(posicao) and y == obter_pos_y(posicao):
                return contador
            contador += 1


def obter_movimento_presa(prado, posicao):
    """
    obter_movimento_presa(prado, posicao):Função auxiliar à função obter_movimento.  Devolve a posição seguinte do
    animal presa na posição (posicao) dentro do prado (prado) de acordo com as regras de movimento dos animais no prado.
    prado, posicao ---> posicao
    """
    posicoes_adjacentes_livres = []
    for posicao_adjacente in obter_posicoes_adjacentes(posicao):
        # guardar as posicoes livres adjacentes
        if eh_posicao_livre(prado, posicao_adjacente):
            posicoes_adjacentes_livres.append(posicao_adjacente)
    return posicoes_adjacentes_livres


def obter_movimento(prado, posicao):
    """
    obter_movimento(prado, posicao): Devolve a posição seguinte do animal na posição (posicao) dentro
    do prado (prado) de acordo com as regras de movimento dos animais no prado.
    prado, posicao ---> posicao
    """
    posicoes_adjacentes_livres = []
    # No caso de ser uma presa
    if eh_presa(obter_animal(prado, posicao)):
        posicoes_adjacentes_livres = obter_movimento_presa(prado, posicao)
    # No caso de ser um predador
    if eh_predador(obter_animal(prado, posicao)):
        posicoes_adjacentes_presas = []
        for posicao_adjacente in obter_posicoes_adjacentes(posicao):
            # guardar as posicoes livres adjacentes
            if eh_posicao_livre(prado, posicao_adjacente):
                posicoes_adjacentes_livres.append(posicao_adjacente)
            # guardar as posicoes ocupadas por presas adjacentes.
            if eh_posicao_animal(prado, posicao_adjacente) and eh_presa(obter_animal(prado, posicao_adjacente)):
                posicoes_adjacentes_presas.append(posicao_adjacente)
        # Caso haja presas nas posicoes adjacentes
        if posicoes_adjacentes_presas:
            posicao_escolhida = posicoes_adjacentes_presas[(obter_valor_numerico(prado, posicao) %
                                                            len(posicoes_adjacentes_presas))]
            return posicao_escolhida
    # Caso nao haja posicoes adjacentes livres, o animal fica na mesma posição.
    if not posicoes_adjacentes_livres:
        return posicao
    posicao_escolhida = posicoes_adjacentes_livres[(obter_valor_numerico(prado, posicao) %
                                                    len(posicoes_adjacentes_livres))]
    return posicao_escolhida


def aconteceu_movimento_geracao(prado, posicao, animal, proxima_posicao):
    """
    aconteceu_movimento_geracao(prado, posicao, animal,proxima_posicao): Função auxiliar à função geracao.
    Devolve a posição seguinte do animal, e verifica se o animal está em condições de se reproduzir.
    prado, posicao, animal, posicao ---> posicao
    """
    if eh_animal_fertil(animal):
        filho = reproduz_animal(animal)
        inserir_animal(prado, filho, posicao)
    return proxima_posicao


def geracao(prado):
    """
    geracao(prado): É a função auxiliar que modifica o prado (prado) fornecido como argumento de
    acordo com a evolução correspondente a uma geração completa, e devolve o próprio
    prado. Isto  é, seguindo a ordem de leitura do prado, cada animal (vivo) realiza o seu
    turno de ação de acordo com as regras descritas.
    prado ---> prado
    """
    posicoes_movidas = []
    for y in range(0, obter_tamanho_y(prado)):
        for x in range(0, obter_tamanho_x(prado)):
            # posicao atual.
            posicao = cria_posicao(x, y)
            # caso a posicao atual seja um animal, incrementar a idade,
            if eh_posicao_animal(prado, posicao) and \
                    not any(posicoes_iguais(posicao, posicao_movida) for posicao_movida in posicoes_movidas):
                animal = obter_animal(prado, posicao)
                aumenta_idade(animal)
                # caso esse animal seja um prepador, incrementar a fome.
                if eh_predador(animal):
                    aumenta_fome(animal)
                # mover o animal da posição atual.
                proxima_posicao = obter_movimento(prado, posicao)
                if eh_posicao_animal(prado, proxima_posicao) and eh_predador(obter_animal(prado, posicao)):
                    eliminar_animal(prado, proxima_posicao)
                    reset_fome(animal)
                mover_animal(prado, posicao, proxima_posicao)
                # caso tenha acontecido um movimento (equivale a que o animal não fique na mesma posição).
                if eh_posicao_livre(prado, posicao):
                    posicoes_movidas.append(aconteceu_movimento_geracao(prado, posicao, animal, proxima_posicao))
                if eh_predador(animal) and eh_animal_faminto(animal):
                    eliminar_animal(prado, proxima_posicao)
    return prado


def simula_ecossistema_verboso(prado, num_geracoes):
    """
    simula_ecossistema_verboso(prado, num_geracoes): Função auxiliar à função simula_ecossistema.
    Realiza o modo verboso.
    prado, int ---> None
    """
    i = 0
    while i <= num_geracoes:
        numero_presas, numero_predadores = obter_numero_presas(prado), obter_numero_predadores(prado)
        # Geracao 0
        if i == 0:
            print(f"Predadores: {obter_numero_predadores(prado)} vs Presas: {obter_numero_presas(prado)} (Gen. {i})")
            print(prado_para_str(prado))
        else:
            geracao(prado)
        if numero_presas != obter_numero_presas(prado) or numero_predadores != obter_numero_predadores(prado):
            print(f"Predadores: {obter_numero_predadores(prado)} vs Presas: {obter_numero_presas(prado)} (Gen. {i})")
            print(prado_para_str(prado))
        i += 1


def simula_ecossistema_nao_verboso(prado, num_geracoes):
    """
    simula_ecossistema_nao_verboso(prado, num_geracoes): Função auxiliar à função simula_ecossistema.
    Realiza o modo não verboso.
    prado, int ---> None
    """
    i = 0
    while i <= num_geracoes:
        # Geracao 0
        if i == 0:
            print(f"Predadores: {obter_numero_predadores(prado)} vs Presas: {obter_numero_presas(prado)} (Gen. {i})")
            print(prado_para_str(prado))
            i += 1
        # Ultima geracao
        elif i == num_geracoes:
            geracao(prado)
            print(f"Predadores: {obter_numero_predadores(prado)} vs Presas: {obter_numero_presas(prado)} (Gen. {i})")
            print(prado_para_str(prado))
            i += 1
        else:
            geracao(prado)
            i += 1


def simula_ecossistema_configuracao(ficheiro):
    """
    simula_ecossitema_configuracao(ficheiro): Função auxiliar à função simula_ecossistema.
    Obtem o prado conforme as configurações recebidas pelo (ficheiro).
    str ---> prado
    """
    with open(ficheiro, "r") as config:
        linhas = config.readlines()
        # Obter a posicao do canto inferior do prado.
        linha_dimensao = eval(linhas[0])
        canto_inf_dt = cria_posicao(linha_dimensao[0], linha_dimensao[1])
        # Obter a posicao dos rochedos do prado.
        rochedos = ()
        if len(linhas[1]) > 1:
            linhas_rochedos = eval(linhas[1])
            for rochedo in linhas_rochedos:
                rochedos += (cria_posicao(rochedo[0], rochedo[1]),)
        # Obter os animais do prado e as suas posicoes no prado.
        animais_raw, animais = (), ()
        posicoes_animais_raw, posicoes_animais = (), ()
        for linha_animal in linhas[2:]:
            linha_animal = eval(linha_animal)
            animal, posicao = linha_animal[0:3], linha_animal[3]
            animais_raw += (animal,)
            posicoes_animais_raw += (posicao,)
        for posicao in posicoes_animais_raw:
            posicoes_animais += (cria_posicao(posicao[0], posicao[1]),)
        for animal in animais_raw:
            animais += (cria_animal(animal[0], animal[1], animal[2]),)
    return cria_prado(canto_inf_dt, rochedos, animais, posicoes_animais)


def simula_ecossistema(ficheiro, num_geracoes, modo_verboso):
    """
    simula_ecossistema(ficheiro, num_geracoes, modo_verboso): É a função principal que permite simular o ecossistema
    de um prado. A cadeia de caracteres (ficheiro) passada por argumento corresponde ao nome do ficheiro de
    configuração da simulação. O valor inteiro g corresponde ao número de gerações a simular. O argumento
    booleano (modo_verboso) ativa o modo verboso (True) ou o modo quiet (False).
    str, int, bool ---> tuple
    """
    prado = simula_ecossistema_configuracao(ficheiro)
    if modo_verboso:
        simula_ecossistema_verboso(prado, num_geracoes)
    else:
        simula_ecossistema_nao_verboso(prado, num_geracoes)
    return obter_numero_predadores(prado), obter_numero_presas(prado)


print(simula_ecossistema("C:\\Users\\josea\\Desktop\\public_test_config-3.txt", 35, True))
