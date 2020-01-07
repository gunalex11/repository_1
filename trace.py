n = int(input()) # вводим размерность матрицы

mat = [ [] for i in range(n) ] # создаём пустую матрицу

for i in range(n):
    mat[i] = input().split(' ') # заполняем её, разбивая введённые строки на части
    for j in range(n):
        mat[i][j] = int(mat[i][j]) # переводим каждый элемент матрицы из строки в число

sum = 0
for i in range(n): # считаем сумму сразу двух диагоналей
    sum += mat[i][i]
    sum += mat[i][n - 1 - i]

if n % 2 == 1: # вычитаем центральный элемент из суммы, если он есть
    sum -= mat[n//2][n//2]

print(sum)
