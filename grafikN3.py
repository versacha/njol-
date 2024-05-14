import matplotlib.pyplot as plt

num_threads = [2, 4, 6, 8]
speedup_factors = [1.057420, 1.460956, 1.910733, 1.917740]

plt.plot(num_threads, speedup_factors, marker='o', linestyle='-')
plt.title('Ускорение от числа потоков')
plt.xlabel('Число потоков')
plt.ylabel('Коэффициент ускорения')
plt.grid(True)
plt.xticks(num_threads)
plt.show()
plt.savefig('график#3.png')
