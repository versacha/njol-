import matplotlib.pyplot as plt

num_threads = [2, 4, 6, 8]
speedup_factors = [ 1.131480, 1.729722, 2.202082, 2.295656]

plt.plot(num_threads, speedup_factors, marker='o', linestyle='-')
plt.title('Ускорение от числа потоков')
plt.xlabel('Число потоков')
plt.ylabel('Коэффициент ускорения')
plt.grid(True)
plt.xticks(num_threads)
plt.show()
plt.savefig('график#2.png')
