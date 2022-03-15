"""
PROJETO DE JOGO DE FORCA
"""

from tkinter import *   #ira criar a interface
import random   #servirá para selecionar aleatoriamente as palavras
import playsound    #tocará a música de fundo

def escolha_dificuldade():
    Label(interface_dificuldade, text ='Escolha sua dificuldade abaixo:', font = ('Arial',12), fg = 'black').pack()
    #o pack() fixa o label na interface_dificuldade
    Button(interface_dificuldade, text='Fácil - 10 erros permitidos', font=('Arial',12),fg='black',
           command=escolha_dificuldade_facil).pack()
    Button(interface_dificuldade, text='Médio - 8 erros permitidos', font=('Arial', 12), fg='black',
           command=escolha_dificuldade_medio).pack()
    Button(interface_dificuldade, text='Difícil - 6 erros permitidos', font=('Arial', 12), fg='black',
           command=escolha_dificuldade_dificil).pack()

#definição do número de erros e fechamento da janela de dificuldades
def escolha_dificuldade_facil():
    dificuldade.append(10)
    interface_dificuldade.destroy()

def escolha_dificuldade_medio():
    dificuldade.append(8)
    interface_dificuldade.destroy()

def escolha_dificuldade_dificil():
    dificuldade.append(6)
    interface_dificuldade.destroy()

def forca(event):   #event faz com que reconheça que deve esperar um evento (enter)
    cabeca_olhos_nariz = interface_forca.create_oval
    corpo = interface_forca.create_line
    boca = interface_forca.create_arc
    try:
        char = caracter.get().upper()[0] #pega a primeira letra digitada, independente de quantas forem digitadas
    except IndexError:  #caso o usuário não digite nada e der  enter, ele não irá travar o jogo
        pass
    else:
        try:
            int(char)   #conferencia de que char é uma letra
        except ValueError:
            if char not in letras_escolhidas:
                letras_escolhidas.append(char)  #atualiza a lista letras_escolhidas
                for indice in range(len(letras)): #percorre a lista para conferência
                    if char == letras[indice]:  #se o usuário acertou a letra, faça:
                        lista_traco[indice] = letras[indice] #atualiza o lista_traco recebendo a letra no indice que a encontrou
                        caracter_vazio['text'] = lista_traco
                        letras_conferencia.append(char)
                if char not in letras:
                    lista_erro.append(char)
                    caracteres_anteriores['text'] = lista_erro
    entrada_dados.set('')   #limpa a caixa de entrada do usuário
    if len(letras_conferencia) == len(letras):  #caso o usuário acerte todas as letras
        mensagem_final['text']= 'Jogo Ganho! Parabéns' #atualiza o texto da mensagem final
        mensagem_final['fg'] = 'green' #atualiza a cor da mensagem final
        caracter.destroy() #serve para retirar a caixinha, impedindo que o usuário continue incluindo letras
        Button(interface, text='Finalizar',font=('Arial',12),fg='red',command=quit).pack() #cria um botão para finalizar
    if len(lista_erro) == dificuldade[0]:
        mensagem_final['text'] ='Erros máximos atingido. Você perdeu!'
        mensagem_final['fg'] = 'red'
        Button(interface, text='Finalizar', font=('Arial', 12), fg='red', command=quit).pack()

    #desenhar o bonequuinho
    if len(lista_erro) == 1:    #cabeça
        cabeca_olhos_nariz(165,95,215,140, fill='grey',outline ='black')
    if len(lista_erro) == 2:    #corpo
        corpo(190,140,190,235)
    if len(lista_erro) == 3:    #braço 1
        corpo(190,140,130,190)
    if len(lista_erro) == 4:    #braço 2
        corpo(190,140,250,190)
    if len(lista_erro) == 5:    #perna 1
        corpo(190,235,125,300)
    if len(lista_erro) == 6:    #perna 2
        corpo(190,235,250,300)
    if len(lista_erro) == 7:    #olho 1
        cabeca_olhos_nariz(175,105,185,115, fill='white',outline ='black')
    if len(lista_erro) == 8:    #olho 2
        cabeca_olhos_nariz(195,105,205,115, fill='white',outline ='black')
    if len(lista_erro) == 9:    #nariz
        cabeca_olhos_nariz(187.5,117.5,192.5,122.5, fill='white',outline ='black')
    if len(lista_erro) == 10:   #boca
        boca(165,125,205,130, fill='white')

def quit():
    interface.destroy()


playsound.playsound('musica_fundo.mp3', block=False)

#leitura do arquivo linha por linha e selecionando aleatóriamente uma palavara
with open('Palavras.txt') as arq:
    leitura = arq.readlines()
    palavra = random.choice(leitura).split('\n')[0].upper() #o indice zero é pq o split cria uma lista separando pelo \n e portanto
    #o índice 0 trará somente a palavra em si.
    print(palavra)

#criação de listas para armazenar dados
letras = [] #letras da palavra escolhida aleatoriamente
lista_traco = []   #traços para mostrar o tamanho da palavra na interface
lista_erro = [] #letras erradas que o usuário já escolheu
letras_escolhidas = []  #todas as letras escolhidas pelo usuario
letras_conferencia = [] #lista para conferir se o usuário ganhou
dificuldade = []    #número maximo de erros de acordo com a dificuldade escolhida

#armazenando dados nas listas
for indice in range(len(palavra)):
    letras.append(palavra[indice])
    lista_traco.append(' ___ ')

interface_dificuldade =Tk() #cria o objeto de interface Tk
escolha_dificuldade()   #chama a função para a interface da escolha da dificuldade
interface_dificuldade.mainloop()

if len(dificuldade) == 1:   #vai para outra janela somente após escolher uma dificuldade
    interface = Tk()
    #para organizar melhor a interface, será utilizado o CAnvas()
    interface_titulo = Canvas(interface)    #é uma classe otimizada para construção e organização de formas geométricas
    interface_titulo.pack(side=TOP) #definimos qe o título está localizado no topo
    interface_forca = Canvas(interface, width=400,height=400) #primeiro parâmetro é comprimento e o outro altura
    interface_forca.pack(side=TOP)
    interface_texto = Canvas(interface, width=400,height=400)
    interface_texto.pack(side=TOP)

    #criação das astes e da forca
    #criação de retângulos recebendo coordenadas
    interface_forca.create_rectangle(10,400,400,390,fill='yellow') #criamos um retãngulo passando coordenadas finais,
    # iniciais e a cor
    interface_forca.create_rectangle(10, 400, 20, 30, fill='yellow')
    interface_forca.create_rectangle(10, 30, 200, 40, fill='yellow')
    interface_forca.create_rectangle(180, 40, 200, 50, fill='red')
    interface_forca.create_rectangle(187.5, 50, 192.5, 90, fill='black')
    interface_forca.create_oval(160, 90, 220, 145, fill='black')
    interface_forca.create_oval(165, 95, 215, 140, fill='white')

    #entrada do texto inicial
    Label(interface_titulo,text = 'Bem Vindo ao Jogo da Forca',font=('Arial',12),fg='black').pack()
    Label(interface_texto,text='Digite sua letra abaixo:\n',font=('Arial',12),fg='black').pack()

    entrada_dados=StringVar()   #variável responsável por receber a string letra do usuário
    caracter =Entry(interface_texto,textvariable=entrada_dados) #usa o Entry() para reconhecer a entrada de dados
    # do usuário, passando interface_texto como norteador de onde a caixa de entrada de dados vai ficar e também passa
    #a variável que será utilizada para armazenar o dado
    caracter.pack() #adiciona a caixa de entrada à interface
    caracter.bind('<Return>', forca) #Bind realiza a ligação do caracter à função forca a partir de um evento (ex:Enter)

    #criar a interface de caracteres vazios
    caracter_vazio = Label(interface_texto,text=lista_traco)
    caracter_vazio.pack()

    #bloco para letras erradas escolhidas pelo usuário
    Label(interface_texto, text='Letras erradas:').pack()
    caracteres_anteriores = Label(interface_texto,text=lista_erro)
    caracteres_anteriores.pack()

    #mensagem final de vitória ou derrota
    mensagem_final = Label(interface_texto,text='')
    mensagem_final.pack()
    interface.mainloop()

