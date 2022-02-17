from random import randint
from time import sleep
import emoji
import PySimpleGUI as sg 


class AdvinhaONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_maximo = 30
        self.valor_minimo = 1
        self.winner = False
        self.chance_adivinha = 4
        self.layout = [
            [sg.Text('          TENTE ADIVINHAR O NÚMERO    ')],
            [sg.Input(size=(5,0),key='ValorChute',expand_x=True),sg.Button('CHUTAR!',expand_x=True)],
            [sg.Output(size=(40,10))]
        ]
    

    def Iniciar(self):
        # Criar janela 
        self.janela = sg.Window('Jogo da Adivinhação',layout=self.layout)

        # Gera o valor Aleatório 
        self.GerarValorRandom()
    
        try:
            while True:  
                for c in range(self.chance_adivinha, -1, -1):
                    # Receber os valores
                    self.evento, self.valores = self.janela.Read()

                    # Condição com valores 
                    if self.evento == 'CHUTAR!':
                        self.valor_do_chute = self.valores['ValorChute']
                        if int(self.valor_do_chute) > self.valor_maximo or int(self.valor_do_chute) < self.valor_minimo:
                            print('ERRO! Só é permitido valores entre 1 e 30')
                            
                        elif int(self.valor_do_chute) > self.valor_aleatorio:
                            print(f'Seu chute foi acima!')
                            
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print(f'Seu chute foi abaixo!')
                            
                        else:
                            self.winner = True
                            self.FimJogo()
                            
                            
                if not self.winner:
                    self.GameOver()

                # Fecha a Janela
                if self.evento == sg.WINDOW_CLOSED:
                    break

        except ValueError:
            print('ERRO! Só é permitido números')
            self.Iniciar()


    def GerarValorRandom(self):
        self.valor_aleatorio = randint(self.valor_minimo, self.valor_maximo)


    def GameOver(self):
        print(f' Game Over! O número sorteado foi {self.valor_aleatorio} {emoji.emojize(":pensive:", use_aliases=True)}\n')
        print('Obrigado por participar!')


    def FimJogo(self):
        print(f'PARABÉNS!Você acertou!{emoji.emojize(":smile:", use_aliases=True)}\n')
        print('Fim de Jogo! Obrigado por participar')
        


adivinha_numero = AdvinhaONumero()
adivinha_numero.Iniciar()

