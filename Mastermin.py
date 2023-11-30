import random

CORES = ["R", "G", "B", "Y", "W", "O"]
TENTATIVAS = 10
COMPRIMENTO_DO_CODIGO = 4

def gerar_codigo():
    codigo = []

    for _ in range(COMPRIMENTO_DO_CODIGO):
        cor = random.choice(CORES)
        codigo.append(cor)

    return codigo

def adivinhar_codigo():
    while True:
        palpite = input("Palpite: ").upper().split(" ")

        if len(palpite) != COMPRIMENTO_DO_CODIGO:
            print(f"Você deve adivinhar {COMPRIMENTO_DO_CODIGO} cores.")
            continue

        for cor in palpite:
            if cor not in CORES:
                print(f"Cor inválida: {cor}. Tente novamente.")
                break
        else:
            break

    return palpite    
        
def verificar_codigo(palpite, codigo_real):
    contagem_cores = {}
    posicao_correta = 0
    posicao_incorreta = 0

    for cor in codigo_real:
        if cor not in contagem_cores:
            contagem_cores[cor] = 0
        contagem_cores[cor] += 1    

    for cor_palpite, cor_real in zip(palpite, codigo_real):
        if cor_palpite == cor_real:
            posicao_correta += 1
            contagem_cores[cor_palpite] -= 1

    for cor_palpite, cor_real in zip(palpite, codigo_real): 
        if cor_palpite in contagem_cores and contagem_cores[cor_palpite] > 0:
            posicao_incorreta += 1
            contagem_cores[cor_palpite] -= 1

    return posicao_correta, posicao_incorreta      

def jogo():
    print(f"Bem-vindo ao mastermind, você tem {TENTATIVAS} para adivinhar o código...")
    print("As cores válidas são", *CORES)

    codigo = gerar_codigo()
    for tentativa in range(1, TENTATIVAS + 1):
        palpite = adivinhar_codigo()
        posicao_correta, posicao_incorreta = verificar_codigo(palpite, codigo)

        if posicao_correta == COMPRIMENTO_DO_CODIGO:
            print(f"Você acertou o código em {tentativa} tentativas!")
            break

        print(f"Posições Corretas: {posicao_correta} | Posições Incorretas: {posicao_incorreta}")

    else:
        print("Você acabou suas tentativas, o código era:", codigo)    

if __name__ == "__main__":
    jogo()
