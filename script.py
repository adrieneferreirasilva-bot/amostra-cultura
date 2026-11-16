import os
import random


def limpar_tela():
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
    personagens = [
        'YOICHI ISAGI',
        'MEGURU BACHIRA',
        'RENSUKE KUNIGAMI',
        'HYOMA CHIGIRI',
        'SHOEI BAROU',
        'SEISHIRO NAGI',
        'REO MIKAGE',
        'RIN ITOSHI',
        'SAE ITOSHI',
        'RYUSEI SHIDOU',
        'TABITO KARASU',
        'EITA OTOYA',
        'KENYU YUKIMIYA',
        'IKKI NIKO',
        'GIN GAGAMARU',
        'JINGO RAICHI',
        'ZANTETSU TSURUGI',
        'JYUBEI ARYU',
        'AOSHI TOKIMITSU',
        'OLIVER AIKU',
        'MICHAEL KAISER',
        'ALEXIS NESS',
        'JINPACHI EGO',
        'ANRI TEIERI',
        'NOEL NOA',
        'JULIAN LOKI',
        'LEONARDO LUNA',
        'CHRIS PRINCE',
        'MARC SNUFFY',
        'LAVINHO',
    ]

    personagem_secreto = random.choice(personagens)

    # Preenche com '_' apenas onde há letras; mantém espaços e hífens visíveis
    letras_descobertas = [
        letra if not letra.isalpha() else '_' for letra in personagem_secreto
    ]
    letras_erradas = []
    tentativas = 6

    while tentativas > 0 and '_' in letras_descobertas:
        limpar_tela()
        print('⚽ === JOGO DA FORCA: BLUE LOCK === ⚽')
        print(exibir_forca(tentativas))
        print('Personagem: ' + ' '.join(letras_descobertas))
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

        # Verifica se a letra está no nome do personagem
        if palpite in personagem_secreto:
            for index, letra in enumerate(personagem_secreto):
                if letra == palpite:
                    letras_descobertas[index] = palpite
        else:
            letras_erradas.append(palpite)
            tentativas -= 1

    # Tela final
    limpar_tela()
    print('⚽ === FIM DE JOGO === ⚽')
    print(exibir_forca(tentativas))

    if '_' not in letras_descobertas:
        print(
            f'🔥 GOLAÇO! Você provou seu ego e acertou: {personagem_secreto}'
        )
    else:
        print(f'🔒 LOCK OFF! Você perdeu. O personagem era: {personagem_secreto}')


if __name__ == '__main__':
    while True:
        jogar()
        jogar_novamente = (
            input('\nDeseja jogar novamente? (S/N): ').strip().upper()
        )
        if jogar_novamente != 'S':
            print('Encerrando o treino no Blue Lock. Até a próxima!')
            break
