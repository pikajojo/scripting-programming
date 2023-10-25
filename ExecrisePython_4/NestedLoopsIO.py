def read_matrix(file_name):
    matrix = []
    file = open(file_name, encoding='utf-8')
    lines = file.readlines()

    for line in lines:
        inside_list = line.split()
        # split括号里面不需要加‘ ’空格， 否则求出来的list里面最后一个数字也会有空格
        matrix.append(inside_list)

    return matrix

def write_matrix(file_name, matrix):
    file = open(file_name, "w")
    for inner_list in matrix:
        for element in inner_list:
            temp = ''
            temp += str(element) + ' '
        file.write(temp)


def multiply_matrix(self, matrix_a, matrix_b):
    a_columns = len(matrix_a[0])
    a_rows = len(matrix_a)
    b_rows = len(matrix_b)
    b_columns = len(matrix_b[0])
    if a_columns != b_rows:
        return False
    else:
        n = a_columns
        res_matrix = []
        for i in range(a_rows):
            res_matrix.append([0] * b_columns)

        for i in range(a_rows):
            for j in range(b_columns):
                for k in range(n):
                    res_matrix[i][j] += int(matrix_a[i][k]) * int(matrix_b[k][j])

    return res_matrix

