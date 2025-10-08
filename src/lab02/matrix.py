def is_valid_matr(mat: list[list[float | int]]) -> bool:
    for i in range (len(mat)):
        if len(mat[i])!=0 and len(mat[0])!=len(mat[i]):
            return False
    return True 

def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat)==0:
        return []
    if is_valid_matr(mat)==False:
        return ValueError

    result = []
    for columns in range (len(mat[0])):
        new_row=[]
        for row in range (len(mat)):
            new_row.append(mat[row][columns])
        result.append(new_row)

    return result 

#print(transpose([[1, 2, 3]]), transpose([[1], [2], [3]]), transpose([[1, 2], [3,4]]), transpose([]), transpose([[1, 2], [3]])) #Тест-кейс transpose




def row_sums(mat: list[list[float | int]]) -> list[float]:
    if is_valid_matr(mat)==False:
        return ValueError
    
    result=[]
    for row in mat:
        result.append(sum(row))
    
    return result

#print(row_sums([[1,2,3], [4,5,6]]), row_sums([[-1,1], [10,-10]]), row_sums([[0,0], [0,0]]), row_sums([[1,2], [3]])) #Тест-кейс row_sums


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if is_valid_matr(mat)==False:
        return ValueError
    
    new_mat=(transpose(mat))
    result=(row_sums(new_mat))

    return result

#print(col_sums([[1,2,3], [4,5,6]]), col_sums([[-1,1], [10,-10]]), col_sums([[0,0], [0,0]]), col_sums([[1,2], [3]])) #Тест-кейс col_sums


