def ative_ataque():
    print("Isso roda quando a função é chamada")

    Ataque = "Brute Force"
    print("foi esse tipo de ataque que teve: " + Ataque)

    Numeros_ataque_sucessivos = 5
    print(Numeros_ataque_sucessivos)

    Impacto_do_incidente = 20.0
    print(Impacto_do_incidente)

    bool_ataque = True
    bool_defesa = False
    print("o ataque teve algum dano no servidor", bool_defesa , "o ataque teve algum dano na maquina", bool_ataque )

    indicador_de_impacto = 5 * 20.0
    print("a variavel Numeros_ataque_sucessivos multiplicado pela variavel Impacto_do_incidente")
    print(indicador_de_impacto)

    Numeros_ataque_sucessivos += Impacto_do_incidente
    print("Minha bool_defesa", Numeros_ataque_sucessivos ,"adição a minha bool_ataque resulta em", Impacto_do_incidente)

    Numeros_ataque_sucessivos -= Impacto_do_incidente
    print("Minha bool_defesa", Numeros_ataque_sucessivos ,"subtração a minha bool_ataque resulta em", Impacto_do_incidente)

    Numeros_ataque_sucessivos /= Impacto_do_incidente
    print("Minha bool_defesa", Numeros_ataque_sucessivos ,"divisão a minha bool_ataque resulta em", Impacto_do_incidente)

    Numeros_ataque_sucessivos *= Impacto_do_incidente
    print("Minha bool_defesa", Numeros_ataque_sucessivos ,"multiplicação a minha bool_ataque resulta em", Impacto_do_incidente)

    print(Ataque, Numeros_ataque_sucessivos, Impacto_do_incidente)

def mostrar_mensagem():
    print("Olá! O sistema de segurança está rodando.")


mostrar_mensagem()
ative_ataque()
