# Сортировки

## Задача №3

### 3.1. Первые k элементов длинной последовательности.

Дана очень длинная последовательность целых чисел длины n.  
Требуется вывести в отсортированном виде её первые k элементов.  
Последовательность может не помещаться в память.  
Использовать слияние.  

**Время работы** O(n * log(k)).  
**Память** O(k).

| in | out |
| --------------------- | --------------------- |
| 9 4 <br> 3 7 4 5 6 1 15 4 2 | 1 2 3 4 |

### [Решение](./3.1.cpp)

### 3.2. Сортировка почти упорядоченной последовательности.

Дана последовательность целых чисел a1...an и натуральное число k, такое что для любых i, j:  
если j >= i + k, то a[i] <= a[j]  
Требуется отсортировать последовательность.  
Последовательность может быть очень длинной.  
Использовать слияние.  

**Время работы** O(n * log(k)).  
**Память** O(k).

| in | out |
| --------------------- | --------------------- |
| 10 4 <br> 0 4 3 2 1 8 7 6 5 9 | 0 1 2 3 4 5 6 7 8 9 |

### [Решение](./3.2.cpp)

### 3.3. Количество инверсий.

Дана последовательность целых чисел из диапазона (-10^9 .. 10^9).  
Длина последовательности не больше 10^6.  
Числа записаны по одному в строке.  
Количество чисел не указано.  
Пусть количество элементов n, и числа записаны в массиве a = a[i]: i из [0..n-1].  
Требуется напечатать количество таких пар индексов (i,j) из [0..n-1], что (i < j и a[i] > a[j]).  
Указание: количество инверсий может быть больше 4*10^9 - используйте int64_t.

| in | out |
| --------------------- | --------------------- |
| 1 <br> 2 <br> 3 <br> 4 | 0 |
| 4 <br> 3 <br> 1 <br> 2 | 6 |
| 3 <br> 2 <br> 2 | 2 |

### [Решение](./3.3.cpp)