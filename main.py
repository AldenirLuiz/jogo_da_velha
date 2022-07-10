from tkinter import Tk, Frame, Button
from random import choice
import os



class Window:
    # Construtor da janela.
    def __init__(self):
        self.numeros = [1,2,3,4,5,6,7,8,9]
        self.matrix = [[1,2,3],[4,5,6],[7,8,9]] # Lista de colunas e linhas Cada sublista uma coluna, cada numero um widget.
        self.sequencias = [
            {1,2,3}, {4,5,6}, {7,8,9},  # Lista de cobinacoes possiveis para um vencedor.
            {1,4,7}, {2,5,8}, {3,6,9},  # Necessario para a verificacao de combinacoes.
            {1,5,9}, {3,5,7}]
        
        self.widgets = dict() # container dos widgets.
        self.switch = True # switch de player, usado para alternar entre players
        self.player_1 = set() # container de jogadas player1, forma a sequencia numerica de jogadas.
        self.player_2 = set() # container de jogadas player2, forma a sequencia numerica de jogadas.
        self.caminho = f'{os.path.dirname(__file__)}\\tictac.ico'
        
        
    def layout(self):
        self.window = Tk() # Janela do Tkinter.
        self.window.geometry('800x800') # Tamanho da janela.
        self.window.iconbitmap(self.caminho) # Icone da janela.
        self.window.title('Jogo da Velha') # Titulo da janela
        self.mainframe = Frame(self.window) # Container principal do layout.
        self.mainframe.pack(expand='yes', fill='both') # gerenciador do container.
        self.but_clear = Button(self.mainframe, text='Recomecar', bg='white', font=('consolas', 16), command=lambda: self.clear())
        self.but_clear.pack(expand='no', fill='none')
        # Matriz da grade de widgets
        for coluna in self.matrix:
            self.frm_col = Frame(self.mainframe) # Container das colunas da grade.
            for numero in coluna: 
                self.frm_lin = Frame(self.frm_col) # Container dos botoes
                self.but_num = Button(self.frm_lin, text=' ', bg='white', font=('consolas', 32)) # Widget do botao.
                self.but_num.configure(command=lambda x=numero: self.comando(x)) # Configuracoes do botao.
                self.but_num.pack(expand='yes', fill='both') # gerenciador do widget.
                self.widgets[numero] = self.but_num # armazena os botoes para uso posterior.
                self.frm_lin.pack(side='left', expand='yes', fill='both') # os widgets sao distribuidos a esquerda a cada nova coluna.
            self.frm_col.pack(expand='yes', fill='both') # gerenciador do container.
        self.window.mainloop() # estado de loop da janela.
    # Fim da parte da janela.
    
    # Funcao de reset.
    def clear(self):
        self.player_1 = set()
        self.player_2 = set()
        self.numeros = [1,2,3,4,5,6,7,8,9]
        self.switch = True
        self.window.destroy()
        self.layout()
        
    # Funcao para verificar a sequencia, retorna caso nao haja correspondencia.
    def verificador(self, seqc, player):
        for sequencia in self.sequencias:
            temp = sequencia & seqc # filtra os numeros para encontrar uma sequencia correspondente.
            if temp in self.sequencias:
                if player:
                    print('Player 1 Vence!!!')
                    for k in self.widgets.keys():
                        self.desabilitar(k)
                    for n in temp:
                        self.widgets[n].configure(bg='cyan')
                    return True
                else:
                    print('Player 2 Vence!!!')
                    for k in self.widgets.keys():
                        self.desabilitar(k)
                    for n in temp:
                        self.widgets[n].configure(bg='red')
                    return True
            else:
                continue
        else: return False

    # Funcao de estado do widget, 'altera as propriedades dos botoes e faz a chamada de verificacao'
    def comando(self, num):
        self.desabilitar(num)
        self.numeros.remove(num)
        if self.switch: # Atende a condicao "True" do switch de players.
            self.widgets[num].configure(text='X') # configura o texto do botao para "X"
            self.widgets[num].configure(bg='blue') # configura a cor do botao para "azul"
            self.player_1.add(num) # adiciona o valor numerico correspondente na matriz ao container do player1
            if len(self.player_1) >= 2: # se houver 2 ou mais jogadas do player1, chama o verificador.
                if self.verificador(self.player_1, True):
                    return
                else:
                    self.player()
            else:
                self.switch = False # alterna entre players no switch.
                self.comando(self.computador())
                    
        else: # Atende a condicao "False" do switch de players.
            self.widgets[num].configure(text='O') # configura o texto do botao para "O"
            self.widgets[num].configure(bg='green') # configura a cor do botao para "verde"
            self.player_2.add(num) # adiciona o valor numerico correspondente na matriz ao container do player2
            self.switch = True # alterna entre players no switch.
            
            if len(self.player_2) > 2:# se houver mais de 2 jogadas do player2, chama o verificador.
                if self.verificador(self.player_2, False):
                    return
            else: return
            
    def computador(self) -> int: # BotPlayer
        str_temp_p = str_temp_c = list()
        if len(self.player_1) >= 2 or len(self.player_2) >= 2:
            for x in self.numeros:
                if self.verify(self.player_2, x):
                    return x
                elif self.verify(self.player_1, x):
                    str_temp_p.append(x)
            else:
                if len(str_temp_p) > 0:
                    return str_temp_c[0]
                else:
                    value = self.choicer()
                    return value
        else:
            value = self.choicer()
            return value
        
        
    def player(self) -> None:
        if len(self.numeros) > 0:
            self.switch = False # alterna entre players no switch.
            escolha = self.computador()
            self.player_2.add(escolha)
            self.comando(escolha)
        else:
            print('EMPATE')
            for widget in self.widgets.values():
                widget.configure(bg='yellow')
            return

    def verify(self, sec, num) -> bool:
        for sequencia in self.sequencias:
            temp = sequencia & sec
            temp.add(num)
            if temp == sequencia:
                return True
            else: continue
        else:
            return False

    def choicer(self) -> int:
        temp = ''
        for x in self.numeros:
            temp += temp+str(x)
        return int(choice(temp))

    def desabilitar(self, num) -> None:
        self.widgets[num].configure(activebackground='red', command=lambda: print('desabilitado'))
        return
        
        
janela = Window() # Instanciacao do objeto janela.
janela.layout()