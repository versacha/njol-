import matplotlib.pyplot as plt

num_threads = [2, 4, 6, 8]
speedup_factors = [1.494883, 2.426474, 2.944409, 2.390247]

plt.plot(num_threads, speedup_factors, marker='o', linestyle='-')
plt.title('Ускорение от числа потоков')
plt.xlabel('Число потоков')
plt.ylabel('Коэффициент ускорения')
plt.grid(True)
plt.xticks(num_threads)
plt.show()
plt.savefig('график#5.png')
