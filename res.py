import numpy as np

with open('matrix_1.txt', 'r') as m_1:
    array_1 = m_1.readline().replace(" ", "")
    arr_1 = eval(array_1.split()[0])

with open('matrix_2.txt', 'r') as m_2:
    array_2 = m_2.readline().replace(" ", "")
    arr_2 = eval(array_2.split()[0])
res = list()
for i in range(5):
    for j in range(5):
        res.append(arr_1[i][j] * arr_2[i][j])

final_res = np.array(res)
final_res = final_res.reshape([5, 5])
with open('result.txt', 'w') as r:
    r.write(str(final_res))
