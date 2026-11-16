import os
import random


def limpar_tela():
    # Limpa o terminal de acordo com o sistema operacional
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_forca(tentativas):
    estagios = [
        # 0 tentativas restantes (Game Over)
        """
           --------

           |      |
           |      O

           |     \\|/
           |      |
           |     / \\
          ---
        """,
        # 1 tentativa restante
        """
           --------

           |      |
           |      O

           |     \\|/
           |      |
           |     / 
          ---
        """,
        # 2 tentativas restantes
        """
           --------

           |      |
           |      O

           |     \\|/
           |      |
           |      
          ---
        """,
        # 3 tentativas restantes
        """
           --------

           |      |
           |      O

           |     \\|
           |      |
           |     
          ---
        """,
        # 4 tentativas restantes
        """
           --------

           |      |
           |      O

           |      |
           |      |
           |     
          ---
        """,
        # 5 tentativas restantes
        """
           --------

           |      |
           |      O
           |    
           |      
           |     
          ---
        """,
        # 6 tentativas restantes (Início)
        """
           --------

           |      |
           |      
           |    
           |      
           |     
          ---
        """,
    ]
    return estagios[tentativas]


def jogar():
    palavras = [
        'PYTHON',
        'ALGORITMO',
        'COMPUTADOR',
        'TECLADO',
        'PROGRAMACAO',
        'INTERNET',
        'DESENVOLVEDOR',
        'SISTEMA',
        'VARIAVEL',
        'FUNCAO',
        'ABACAXI',
        'ELEFANTE',
        'ASTRONAUTA',
        'MONTANHA',
        'OCEANO',
    ]

    palavra_secreta = random.choice(palavras)
    letras_descobertas = ['_' for _ in palavra_secreta]
    letras_erradas = []
    tentativas = 6

    while tentativas > 0 and '_' in letras_descobertas:
        limpar_tela()
        print('=== JOGO DA FORCA ===')
        print(exibir_forca(tentativas))
        print('Palavra: ' + ' '.join(letras_descobertas))
        print(
            f"Letras erradas: {', '.join(letras_erradas) if letras_erradas else 'Nenhuma'}"
        )
        print(f'Tentativas restantes: {tentativas}\n')

        palpite = input('Digite uma letra: ').strip().upper()

        # Validações de entrada
        if len(palpite) != 1 or not palpite.isalpha():
            input(
                'Entrada inválida! Digite apenas UMA letra. Pressione Enter...'
            )
            continue

        if palpite in letras_descobertas or palpite in letras_erradas:
            input('Você já tentou essa letra! Pressione Enter...')
            continue

        # Verifica se a letra está na palavra
        if palpite in palavra_secreta:
            for index, letra in enumerate(palavra_secreta):
                if letra == palpite:
                    letras_descobertas[index] = palpite
        else:
            letras_erradas.append(palpite)
            tentativas -= 1

    # Tela final de Vitória ou Derrota
    limpar_tela()
    print('=== FIM DE JOGO ===')
    print(exibir_forca(tentativas))

    if '_' not in letras_descobertas:
        print(f'🎉 PARABÉNS! Você acertou a palavra: {palavra_secreta}')
    else:
        print(f'💀 VOCÊ PERDEU! A palavra era: {palavra_secreta}')


if __name__ == '__main__':
    while True:
        jogar()
        jogar_novamente = (
            input('\nDeseja jogar novamente? (S/N): ').strip().upper()
        )
        if jogar_novamente != 'S':
            print('Obrigado por jogar! Até a próxima.')
            break

