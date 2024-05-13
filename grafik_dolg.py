import matplotlib.pyplot as plt

x1 = [2, 4, 6, 8]
y1 = [2.165126, 4.028101, 5.088920, 6.600093]

x2 = [2, 4, 6, 8]
y2 = [2.675305, 4.169788, 5.229280, 6.275507]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5), subplot_kw=dict(xlabel='Число потоков', ylabel='Коэффициент ускорения'))

ax1.plot(x1, y1, marker='o', label='Данные', color='blue')
ax1.plot(x1, x1, color='red')
ax1.set_title('Монте-Карло')
ax1.grid(True)
ax1.legend(['10^7'])

ax2.plot(x2, y2, marker='o', label='Данные2', color='green')
ax2.plot(x2, x2, color='red')
ax2.set_title('Монте-Карло')
ax2.grid(True)
ax2.legend(['10^8'])

plt.savefig('график2.png')

plt.tight_layout()
plt.show()
