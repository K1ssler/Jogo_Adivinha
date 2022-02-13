from random import randint
from time import sleep
import emoji


class AdvinhaONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_maximo = 30
        self.valor_minimo = 1
        self.winner = False
        self.chance_adivinha = 4

    def Iniciar(self):
        self.ApresentacaoJogo()
        self.GerarValorRandom()
    
        try:     
            for c in range(self.chance_adivinha, -1, -1):
                self.PedirValor()
                if self.valor_user > self.valor_maximo or self.valor_user < self.valor_minimo:
                    print('ERRO! Só é permitido valores entre 1 e 30')
                
                elif self.valor_user > self.valor_aleatorio:
                    print(f'Seu chute foi acima!')
                
                elif self.valor_user < self.valor_aleatorio:
                    print(f'Seu chute foi abaixo!')
                
                else:
                    self.winner = True
                    self.FimJogo()
                    break
            if not self.winner:
                self.GameOver()
        except ValueError:
            print('ERRO! Só é permitido números')
            self.Iniciar()


    def ApresentacaoJogo(self):
        print('BEM - VINDO!\n')
        print('Você tem 5 chances para adivinhar o número que a máquina está pensando, Boa Sorte!\n')
        print('Iniciando...')
        sleep(3)


    def PedirValor(self):
        self.valor_user = int(input('Digite um valor de 1 até 30:  '))
  

    def GerarValorRandom(self):
        self.valor_aleatorio = randint(self.valor_minimo, self.valor_maximo)


    def GameOver(self):
        print(f' \033[1;31mGame Over!\033[m O número sorteado foi {self.valor_aleatorio} {emoji.emojize(":pensive:", use_aliases=True)}\n')
        print('Obrigado por participar!')


    def FimJogo(self):
        print(f'\033[1;32mPARABÉNS!Você acertou \033[m{emoji.emojize(":smile:", use_aliases=True)}\n')
        print('Fim de Jogo! Obrigado por participar')


adivinha_numero = AdvinhaONumero()
adivinha_numero.Iniciar()

