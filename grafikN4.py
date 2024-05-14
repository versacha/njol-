import matplotlib.pyplot as plt

num_threads = [2, 4, 6, 8]
speedup_factors = [0.852706, 1.328117, 1.591187, 1.766731]

plt.plot(num_threads, speedup_factors, marker='o', linestyle='-')
plt.title('Ускорение от числа потоков')
plt.xlabel('Число потоков')
plt.ylabel('Коэффициент ускорения')
plt.grid(True)
plt.xticks(num_threads)
plt.show()
plt.savefig('график#4.png')
