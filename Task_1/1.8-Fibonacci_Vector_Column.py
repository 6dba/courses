from typing import Any
from numpy import matrix

def fibonacci(n: int) -> Any:
    """
    Вычисление n, n + 1 чисел Фибонначи при помощи вектор-столбца
    """
    # Исходная матрица [0,1] возводится в n степень для получения нужных значений матрицы 
    #                  [1,1]
    # и умножается на вектор-столбец со значениями F0 и F1
    # Таким образом мы получаем вектор-столбец со значениями Fn, Fn + 1

    # ХОД ВЫЧИЛСНИЙ
    # Возьводим матрицу в степень - умножаем саму на себя, к примеру 2 раза
    #  
    # c11 = a11 · a11 + a12 · a21 = 0 · 0 + 1 · 1 = 0 + 1 = 1

    # с12 = a11 · a12 + a12 · a22 = 0 · 1 + 1 · 1 = 0 + 1 = 1

    # с21 = a21 · a11 + a22 · a21 = 1 · 0 + 1 · 1 = 0 + 1 = 1

    # с22 = a21 · a12 + a22 · a22 = 1 · 1 + 1 · 1 = 1 + 1 = 2

    # Возвденную матрицу умножаем на вектор-стоблец
    # c11 = a11 · b11 + a12 · b21 = 1 · 1 + 1 · 1 = 1 + 1 = 2

    # c21 = a21 · b11 + a22 · b21 = 1 · 1 + 2 · 1 = 1 + 2 = 3

    print((666**777) % 5)

    return matrix([[0,1], [1,1]])**n * matrix([[1,1]]).T