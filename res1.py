import numpy as np

with open('matrix_1.txt', 'r') as m_1:
    array_1 = m_1.readline().replace(" ", "")
    arr_1 = eval(array_1.split()[0])

with open('matrix_2.txt', 'r') as m_2:
    array_2 = m_2.readline().replace(" ", "")
    arr_2 = eval(array_2.split()[0])


a1 = np.array(arr_1, float).reshape((5, 5))
a2 = np.array(arr_2, float).reshape((5, 5))
re = np.dot(a1, a2)
print(re)
with open('result.txt', 'a') as r:
   r.write(str(re))
