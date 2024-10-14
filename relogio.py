from tkinter import * 
from time import strftime 

#funçao para atualizar o relogio
def atualizar_relogio():
    horario_atual = strftime("%H:%M:%S %p")
    rotulo_relogio.config(text=horario_atual)
    rotulo_relogio.after(1000, atualizar_relogio)
    
#criaçao da janela principal
janela = Tk()
janela.title("relogio digital simples")

#criaçao do rotulo para exibir o relogio 
rotulo_relogio = Label(
    janela,
    font=("Arial", 40, "bold"),
    background=" purple",
    foreground="dark blue"
)
#posiciona o rotulo para o centro da janela 
rotulo_relogio.pack(anchor="center")
#inicia a atualizaçao do relogio
atualizar_relogio()
#inicia o loop principal da interface grafica
janela.mainloop()
