import random
import tkinter as tk

# Cores já definidas
preta = "#000000"
azul = "#0000FF"
laranja = "#FF7F00"
branca = "#FFFFFF"

# Configurações do jogo
LARGURA = 600
ALTURA = 400
TAMANHO_QUADRADO = 20
VELOCIDADE = 120

class JogoCobrinha:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Jogo da Cobrinha")
        self.raiz.configure(bg=preta)
        self.raiz.resizable(False, False)
        self.jogo_ativo = False
        self.id_after = None

        self.canvas = tk.Canvas(
            self.raiz,
            width=LARGURA,
            height=ALTURA,
            bg=preta,
            highlightthickness=0
        )
        self.canvas.pack()

        self.pontuacao = 0
        self.texto_pontuacao = tk.Label(
        self.raiz,
          text="0",
          bg=preta,
          fg=branca,
          font=("Arial", 20, "bold")
)
        
        self.texto_pontuacao.pack()

        self.iniciar_jogo()

    def iniciar_jogo(self):
        if self.id_after is not None:
            self.raiz.after_cancel(self.id_after)
            self.id_after = None

        self.jogo_ativo = True
        self.direcao = "Direita"
        self.proxima_direcao = "Direita"

        self.cobra = [
            [LARGURA // 2, ALTURA // 2],
            [LARGURA // 2 - TAMANHO_QUADRADO, ALTURA // 2],
            [LARGURA // 2 - 2 * TAMANHO_QUADRADO, ALTURA // 2],
        ]

        self.comida = self.gerar_comida()
        self.pontuacao = 0
        self.texto_pontuacao.config(text="0")
        self.canvas.delete("all")

        self.atualizar_jogo()

    def gerar_comida(self):
        while True:
            x = random.randint(0, (LARGURA // TAMANHO_QUADRADO) - 1) * TAMANHO_QUADRADO
            y = random.randint(0, (ALTURA // TAMANHO_QUADRADO) - 1) * TAMANHO_QUADRADO
            pos = [x, y]
            if pos not in self.cobra:
                return pos

    def atualizar_jogo(self):
        if not self.jogo_ativo:
            return
        
        self.canvas.delete("all")

        # Desenhar comida
        self.canvas.create_rectangle(
            self.comida[0], self.comida[1],
            self.comida[0] + TAMANHO_QUADRADO, self.comida[1] + TAMANHO_QUADRADO,
            fill=laranja,
            outline=preta
        )

        # Desenhar cobra
        for parte in self.cobra:
            self.canvas.create_rectangle(
                parte[0], parte[1],
                parte[0] + TAMANHO_QUADRADO, parte[1] + TAMANHO_QUADRADO,
                fill=azul,
                outline=branca
            )

        self.mover_cobra()

        if self.jogo_ativo:
           self.id_after = self.raiz.after(
           VELOCIDADE,
           self.atualizar_jogo
           )

    def mover_cobra(self):
        self.direcao = self.proxima_direcao

        cabeca = self.cobra[0][:]
        if self.direcao == "Cima":
            cabeca[1] -= TAMANHO_QUADRADO
        elif self.direcao == "Baixo":
            cabeca[1] += TAMANHO_QUADRADO
        elif self.direcao == "Esquerda":
            cabeca[0] -= TAMANHO_QUADRADO
        elif self.direcao == "Direita":
            cabeca[0] += TAMANHO_QUADRADO

        self.cobra.insert(0, cabeca)

        if cabeca == self.comida:
            self.pontuacao += 1
            self.texto_pontuacao.config(text=str(self.pontuacao))
            self.comida = self.gerar_comida()
        else:
            self.cobra.pop()

        if (
            cabeca[0] < 0
            or cabeca[1] < 0
            or cabeca[0] + TAMANHO_QUADRADO > LARGURA
            or cabeca[1] + TAMANHO_QUADRADO > ALTURA
            or cabeca in self.cobra[1:]
        ):
            self.game_over()

    def game_over(self):
        self.jogo_ativo = False
        if self.id_after is not None:
            self.raiz.after_cancel(self.id_after)
            self.id_after = None

        self.canvas.create_text(
            LARGURA // 2,
            ALTURA // 2,
            text="Game Over",
            fill=branca,
            font=("Arial", 24, "bold")
        )
        self.canvas.create_text(
            LARGURA // 2,
            ALTURA // 2 + 30,
            text="Pressione Enter para jogar de novo",
            fill=branca,
            font=("Arial", 12)
        )

    def mudar_direcao(self, nova_direcao):
        oposto = {
            "Cima": "Baixo",
            "Baixo": "Cima",
            "Esquerda": "Direita",
            "Direita": "Esquerda"
        }

        if nova_direcao != oposto.get(self.direcao, ""):
            self.proxima_direcao = nova_direcao


if __name__ == "__main__":
    raiz = tk.Tk()
    jogo = JogoCobrinha(raiz)

    raiz.bind("<Up>", lambda event: jogo.mudar_direcao("Cima"))
    raiz.bind("<Down>", lambda event: jogo.mudar_direcao("Baixo"))
    raiz.bind("<Left>", lambda event: jogo.mudar_direcao("Esquerda"))
    raiz.bind("<Right>", lambda event: jogo.mudar_direcao("Direita"))
    raiz.bind("<Return>", lambda event: jogo.iniciar_jogo())

    raiz.mainloop()
