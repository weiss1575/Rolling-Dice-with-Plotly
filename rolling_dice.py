from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline

class Die:
    """Representing a single die. """

    def __init__(self, num_sides = 6):
        """Default sides are 6 for a regular die"""
        self.num_sides = num_sides

    def roll(self):
        """Returns a random value between 1 and number of sides"""
        return randint(1, self.num_sides)


# Create two dice
die_1 = Die()
die_2 = Die()

# Make some rolls, store results in a list
results = []
for roll_num in range(100_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
# print(frequencies)

# Visualize the results
x_v = list(range(2, max_result + 1))
y_v = frequencies
data = [Bar(x=x_v, y=y_v)]
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title' : 'Frequency of Result'}
my_layout = Layout(title = 'Results of rolling two D6 dice 100,000 times', xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename = 'd6_d6.html')