print("Become the programmer you're meant to be!")

def is_mini_sudoku(sudoku):
    is_sudoku=True
    list_of_total_elements=[]
    for row in sudoku:
        for i in row:
            list_of_total_elements.append(i)
    for element in list_of_total_elements:
        print(list_of_total_elements.count(element))
        if list_of_total_elements.count(element)>1:
            
            is_sudoku=False
    
    return is_sudoku



sudoku=[]
for i in range(3):
    list_a=input().split()
    sudoku.append(list_a)

is_sudoku=is_mini_sudoku(sudoku)
print(is_sudoku)