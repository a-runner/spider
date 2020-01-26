from die import Die
import pygal

die1 = Die()
die2 = Die(10)

result = []
for num in range(5000):
    s = die1.roll() + die2.roll()
    result.append(s)

fre = []
for c in range(1, 17):
    frequency = result.count(c)
    fre.append(frequency)


hist = pygal.Bar()
hist.x_labels = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
hist.y_labels = 'Frequency of the result'
hist.title = 'Result of rolling '
hist.add('D6 + D10', fre)
hist.render_to_file('die_visible.svg')