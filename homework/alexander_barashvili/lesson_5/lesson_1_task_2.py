result_1 = 'результат операции: 42'

result_2 = 'результат операции: 514'

result_3 = 'результат работы программы: 9'

num_1 = int(result_1[result_1.index(':') + 1:].strip()) + 10
num_2 = int(result_2[result_2.index(':') + 1:].strip()) + 10
num_3 = int(result_3[result_3.index(':') + 1:].strip()) + 10

print(num_1, num_2, num_3)
