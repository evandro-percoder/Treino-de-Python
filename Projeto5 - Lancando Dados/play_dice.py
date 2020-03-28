from dice import Dice
import pygal


# criando um dado (objeto)
d1  = Dice()

# lançando o dados e armazenando os resultados em uma lista
results = []
# lançando o dado 1000 vezes
for roll_num in range(1000):
    result = d1.roll()
    results.append(result)
print(results)

frequencies = []
for value in range(1, d1.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

# Este bloco, gera um código para ser aberto em um browser
hist = pygal.Bar()
hist.title = "Resultados dos lançamentos do dados 1000 vezes."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Resulatdo"
hist.y_title = "Frequencia do Resultado"
hist.add('D1', frequencies)
hist.render_to_file('lançamento_de_dado1.svg')
