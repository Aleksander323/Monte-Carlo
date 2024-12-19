import matplotlib.pyplot as plt

rc4_pairs_freq = [115, 96, 113, 109, 126, 92, 80, 90, 86, 93]
rc4_poker_freq = [88, 106, 86, 93, 87, 77, 97, 105, 128, 133]
expected_freq = [100]*10
x_ax = list(range(10))

# plt.bar(x_ax, rc4_pairs_freq, label='Otrzymany rozkład')
# plt.bar(x_ax, expected_freq, color='green', alpha=0.5, label='Przewidywany rozkład')
# plt.title('Frequency of pairs test - rozkłady p-wartości')
# plt.xlabel('Koszyki')
# plt.ylabel('Ilość p-wartości w koszyku')
# plt.legend()


plt.bar(x_ax, rc4_poker_freq, color='orange', label='Otrzymany rozkład')
plt.bar(x_ax, expected_freq, color='green', alpha=0.5, label='Przewidywany rozkład')
plt.title('Poker test - rozkłady p-wartości')
plt.xlabel('Koszyki')
plt.ylabel('Ilość p-wartości w koszyku')
plt.legend()


plt.show()
