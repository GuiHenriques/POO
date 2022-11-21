# Importar os módulos "turtle" e "math"
import turtle
import math

# Criar uma tartaruga e referenciá-la pelo nome "construtor"
construtor = turtle.Turtle()

#Definir o valor da variável x
x = 100

# Desenhar o corpo da casa (um retângulo)
for i in range(2):
    construtor.forward(2*x)
    construtor.left(90)
    construtor.forward(x)
    construtor.left(90)

#Desenhar a porta
construtor.forward(x/3)
construtor.left(90)

construtor.forward(2*x/3)
construtor.right(90)
construtor.forward(x/3)
construtor.right(90)
construtor.forward(2*x/3)

#Desenhar a janela
construtor.up()  # anda sem riscar
construtor.left(90)
construtor.forward(x/2)
construtor.left(90)
construtor.forward(x/3)
construtor.down()  # volta a riscar

for i in range(4):
    construtor.forward(x/3)
    construtor.right(90)

#Desenhar o telhado
construtor.up()  # anda sem riscar
construtor.forward(2*x/3)
construtor.right(90)
construtor.forward(x/3 + x/2)
construtor.left(135)
construtor.down()  # volta a riscar

construtor.forward(x * math.sqrt(2))
construtor.left(90)
construtor.forward(x * math.sqrt(2))

# Indicar que a tarefa foi concluída
turtle.done()



