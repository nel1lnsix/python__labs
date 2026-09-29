"""ЛР2, задание B — матрицы (списки списков)."""


def transpose(mat: list[list[float | int]]) -> list[list]:
    
    if not mat:
        return []

    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("матрица рваная — строки разной длины")

    result = []
    for col_idx in range(row_length):
        new_row = []
        for row in mat:
            new_row.append(row[col_idx])
        result.append(new_row)

    return result


def row_sums(mat: list[list[float | int]]) -> list[float]:
    
    if not mat:
        return []

    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("матрица рваная — строки разной длины")

    return [sum(row) for row in mat]


def col_sums(mat: list[list[float | int]]) -> list[float]:
    
    if not mat:
        return []

    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("матрица рваная — строки разной длины")

    result = []
    for col_idx in range(row_length):
        col_sum = 0
        for row in mat:
            col_sum += row[col_idx]
        result.append(col_sum)

    return result


if __name__ == "__main__":
    print("--- transpose ---")
    print(transpose([[1, 2, 3]]))          
    print(transpose([[1], [2], [3]]))      
    print(transpose([[1, 2], [3, 4]]))     
    print(transpose([]))                   
    try:
        print(transpose([[1, 2], [3]]))
    except ValueError as e:
        print("ValueError:", e)            

    print("--- row_sums ---")
    print(row_sums([[1, 2, 3], [4, 5, 6]]))   
    print(row_sums([[-1, 1], [10, -10]]))     
    print(row_sums([[0, 0], [0, 0]]))         
    try:
        print(row_sums([[1, 2], [3]]))
    except ValueError as e:
        print("ValueError:", e)               

    print("--- col_sums ---")
    print(col_sums([[1, 2, 3], [4, 5, 6]]))   
    print(col_sums([[-1, 1], [10, -10]]))     
    print(col_sums([[0, 0], [0, 0]]))         
    try:
        print(col_sums([[1, 2], [3]]))
    except ValueError as e:
        print("ValueError:", e)               
