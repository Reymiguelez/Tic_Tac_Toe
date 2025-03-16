def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vencedor(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(celula == jogador for celula in linha):
            return True
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

def verificar_empate(tabuleiro):
    return all(celula != " " for linha in tabuleiro for celula in linha)

def jogar():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogadores = ["X", "O"]
    jogador_atual = 0

    print("Bem-vindo ao Jogo da Velha!")
    exibir_tabuleiro(tabuleiro)

    while True:
        print(f"Jogador {jogadores[jogador_atual]}, é sua vez!")
        try:
            linha = int(input("Digite a linha (0, 1 ou 2): "))
            coluna = int(input("Digite a coluna (0, 1 ou 2): "))
            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = jogadores[jogador_atual]
                exibir_tabuleiro(tabuleiro)
                if verificar_vencedor(tabuleiro, jogadores[jogador_atual]):
                    print(f"Parabéns! Jogador {jogadores[jogador_atual]} venceu!")
                    break
                if verificar_empate(tabuleiro):
                    print("Empate! O tabuleiro está cheio.")
                    break
                jogador_atual = 1 - jogador_atual
            else:
                print("Essa posição já está ocupada. Tente novamente.")
        except (ValueError, IndexError):
            print("Entrada inválida. Certifique-se de digitar números entre 0 e 2.")

if __name__ == "__main__":
    jogar()
