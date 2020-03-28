"""
Neste projeto é usado o pacote de visualização Pygal.
Útil para criar arquivos com gráficos vetoriais escaláveis.
Eles são úteis em visualizações apresentadas em telas de tamanhos diferentes, pois são
automaticamente escaladas para se adequar à tela de quem as estiver vendo

* Instalando o pacote :
 python -m pip install --user pygal 
 
 """

from random import randint

class Dice:
    # classe representa 1 dado de 6 lados
    def __init__(self, num_sides = 6):
        self.num_sides = num_sides

    def roll(self):
        # método de lançamento que gera um resultado aleatório entre 1 e 6
        return randint(1, self.num_sides)