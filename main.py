# Aldenir Luiz 03/10/2021

from tkinter import Label, Tk, Frame, Button, PhotoImage
from time import sleep
import funcoes


class Janela:
    def __init__(self):
        # widgets da janela principal.
        self.window = Tk()
        self.window.geometry("600x600")
        self.frame = Frame(self.window)
        self.frame.pack(expand="yes", fill="both")
        self.digitados = list() # Histórico de escolhidos.
        self.numeros = [1,2,3,4,5,6,7,8,9]
        
        img_0 = PhotoImage(file="img_O.png")
        img_1 = PhotoImage(file="img_X.png")
        # Containers que compoem as linhas.
        self.frame_0 = Frame(self.frame, bg="green")
        self.frame_0.pack(expand="yes", fill="both")
        self.frame_1 = Frame(self.frame, bg="yellow")
        self.frame_1.pack(expand="yes", fill="both")
        self.frame_2 = Frame(self.frame, bg="red")
        self.frame_2.pack(expand="yes", fill="both")
       

        # Primeira Linha de botoes -> armazenados no container: frame_0
        self.bttLine_00 = Button(self.frame_0, relief="raised", width=3, height=4, highlightbackground="black", borderwidth=4, command=lambda: layout(1, self.bttLine_00, "pl"))
        self.bttLine_00.pack(side="left", expand="yes", fill="both")
        self.bttLine_01 = Button(self.frame_0, relief="raised",width=3, height=4, border=4, command=lambda: layout(2, self.bttLine_01, "pl"))
        self.bttLine_01.pack(side="left", expand="yes", fill="both")
        self.bttLine_02 = Button(self.frame_0, relief="raised",width=3, height=4, border=4, command=lambda: layout(3, self.bttLine_02, "pl"))
        self.bttLine_02.pack(side="left", expand="yes", fill="both")
        
        # Segunda Linha de botoes -> armazenados no container: frame_1
        self.bttLine_03 = Button(self.frame_1, relief="raised",width=3, height=4, border=4, command=lambda: layout(4, self.bttLine_03, "pl"))
        self.bttLine_03.pack(side="left", expand="yes", fill="both")
        self.bttLine_04 = Button(self.frame_1, relief="raised",width=3, height=4, border=4, command=lambda: layout(5, self.bttLine_04, "pl"))
        self.bttLine_04.pack(side="left", expand="yes", fill="both")
        self.bttLine_05 = Button(self.frame_1, relief="raised",width=3, height=4, border=4, command=lambda: layout(6, self.bttLine_05, "pl"))
        self.bttLine_05.pack(side="left", expand="yes", fill="both")

        # Terceira Linha de botoes -> armazenados no container: frame_2
        self.bttLine_06 = Button(self.frame_2, relief="raised",width=3, height=4, border=4, command=lambda: layout(7, self.bttLine_06, "pl"))
        self.bttLine_06.pack(side="left", expand="yes", fill="both")
        self.bttLine_07 = Button(self.frame_2, relief="raised",width=3, height=4, border=4, command=lambda: layout(8, self.bttLine_07, "pl"))
        self.bttLine_07.pack(side="left", expand="yes", fill="both")
        self.bttLine_08 = Button(self.frame_2, relief="raised",width=3, height=4, border=4, command=lambda: layout(9, self.bttLine_08, "pl"))
        self.bttLine_08.pack(side="left", expand="yes", fill="both")


        def layout(numero, widget, jogador):
            """Captura O Nome e o Valor do Widget Clicado
                a fim de Gerar um Evento de Configuracao no Widget
                em Seguida Envia o Valor do Widget para Verfificacao.
                :PARAM: numero; recebe o valor do widget.
                :PARAM: widget; recebe o nome do widget a que foi atribuido a variavel.
                :FUNCT: verificado(): Invoca a Função de verificação disparada por clic do botão
                """
            if numero not in self.numeros: # Verifica no histórico se o numero ja foi escolhido anteriormente.
                print("escolha outro")
                return False # Sai da função sem fazer alterações.
            else:
                self.numeros.remove(numero) # Adiciona o número escolhido ao histórico

            if jogador == "cmp": # Verifica se o jogador e a maquina
                 # Reconfigura o widget para a cor vermelha.
                widget.configure(image=img_0, width=24, height=24) # Reconfigura o widget para a cor vermelha.
            else:
                 # Reconfigura o widget para a cor azul.
                widget.configure(image=img_1, width=24, height=24)
            veirficado = funcoes.verify(numero, jogador) # Chama a função de verificação, verifica se há combinação.
            if veirficado: # Dispara o evento de fim de jogo caso a função retorne True.
                sleep(0.5)
                if jogador == "pl":
                    nome = "VOCÊ"
                    fim_jogo(nome)
                else:
                    nome = "Computador"
                    fim_jogo(nome)
            else: # continua o jogo se a função retornar False.
                if jogador == "cmp":
                    pass
                else:
                    botplayer()


        def botplayer():
            sleep(0.6)
            escolha = funcoes.intelit()
            print("escolhido: ", escolha)
            widgets = {
            1: self.bttLine_00, 2: self.bttLine_01, 3: self.bttLine_02,
            4: self.bttLine_03, 5: self.bttLine_04, 6: self.bttLine_05,
            7: self.bttLine_06, 8: self.bttLine_07, 9: self.bttLine_08}
            try:
                wid = widgets[escolha]
                layout(escolha, wid, "cmp")
            except KeyError:
                fim_jogo("EMPATOU", True)


        def fim_jogo(nome, empate=False):
            if empate:
                condicao = ""
            else:
                condicao = "VENCEU!!"

            
            # self.frame.forget() # Limpa todos os widgets do jogo.
            self.frame_F = Frame(self.window, bg=None) # Container subtitudo
            
            self.text = Label(self.frame_F, text=f"{nome} {condicao}") # Mensagem de fim de jogo.
            self.text.pack(expand="yes", fill="both")  # Construtor do widget text.
            self.bt_R = Button(self.frame_F, text="JOGAR NOVAMENTE", command=lambda: Reiniciar())
            self.bt_R.pack() # Construtor do widget bt_R.
            self.frame_F.pack(expand="yes", fill="both")
            if nome == "VOCÊ":
                self.frame_F.configure(bg="green")
                self.text.configure(bg="green")
            

    
        def Reiniciar():
            self.window.destroy()
            funcoes.clear()
            Janela()

            
        self.window.mainloop() # Mantem a janela.


Janela()
