import turtle
import random

def desenhar_roda_de_cores():
    # Configuração inicial da tela
    tela = turtle.Screen()
    tela.title("Roda de Cores")
    tela.bgcolor("black")
    tela.setup(width=800, height=700)

    # Criar o objeto Turtle
    pincel = turtle.Turtle()
    pincel.speed(0)
    pincel.hideturtle()

    # Configurar o número de segmentos
    num_segmentos = 36
    angulo = 360 / num_segmentos
    raio = 200  # Raio da roda

    for _ in range(num_segmentos):
        # Gerar duas cores aleatórias para o gradiente
        cor1 = (random.random(), random.random(), random.random())
        cor2 = (random.random(), random.random(), random.random())
        tela.colormode(1.0)  # Modo RGB entre 0 e 1

        # Desenhar o segmento
        pincel.fillcolor(cor1)
        pincel.penup()
        pincel.goto(0, 0)
        pincel.pendown()
        pincel.begin_fill()
        pincel.forward(raio)
        pincel.left(90)
        pincel.circle(raio, extent=angulo)
        pincel.left(90)
        pincel.forward(raio)
        pincel.end_fill()

        # Girar o pincel para o próximo segmento
        pincel.right(180 - angulo)

    # Manter a tela aberta
    tela.mainloop()

# Executar o programa
desenhar_roda_de_cores()
