import random
import art
import palavras
print(art.logo)
print("Esse é um jogo da forca sobre as principais frutas brasileiras.\nTeste seu conhecimento e boa sorte!")

fim_de_jogo = False
lista_palavras = palavras.palavras
palavra_escolhida = random.choice(lista_palavras)
tamanhao_letra = len(palavra_escolhida)
vidas = 5
espacos = []

for i in range(tamanhao_letra):
    espacos.append("_")

while not fim_de_jogo:
    palpite = input('Digite uma letra: ').lower()
    for posicao in range(tamanhao_letra):
        letra = palavra_escolhida[posicao]
        if letra == palpite:
            espacos[posicao] = letra
    print(art.etapas[vidas])
    print(espacos)
    if palpite in espacos:
        print("\nVocê já acertou essa palavra!")
    else:
        print(f"\nVocê digitou: {palpite} e não tem na palavra\nPedeu uma vida!")

        if palpite not in palavra_escolhida:
            vidas -= 1
            if vidas == 0:
                fim_de_jogo = True
                print(f"\nAcabaram as vidas! a palavra era: {palavra_escolhida}")
        if "_" not in espacos:
            fim_de_jogo = True
            print("\nParabéns, você ganhou!")
