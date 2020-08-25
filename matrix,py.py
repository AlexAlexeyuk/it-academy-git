import random

def cr_array(x):
    x = random.randint(1, 100)
    return x
    

def create_matrix(cr_array, rows, col):
    return [[cr_array(x)  
             for x in range(rows)]
             for x in range(col)]

m1 = create_matrix(cr_array, 5, 5)
m2 = create_matrix(cr_array, 5, 5)




for i in range(5):
    for j in range(5):
        print(m1[i][j] * m2[i][j], end = ' ')
        
        
with open('matrix_1.txt', 'w') as m_1:
    def cr_array(x):
        x = random.randint(1, 100)
        return x
    

    def create_matrix(cr_array, rows, col):
        return [[cr_array(x)  
                 for x in range(rows)]
                for x in range(col)]

    m1 = create_matrix(cr_array, 5, 5)
    m_1.write(str(m1))
    
with open('matrix_2.txt', 'w') as m_2:
    def cr_array(x):
        x = random.randint(1, 100)
        return x
    

    def create_matrix(cr_array, rows, col):
        return [[cr_array(x)  
                 for x in range(rows)]
                for x in range(col)]

    m2 = create_matrix(cr_array, 5, 5)
    m_2.write(str(m2))