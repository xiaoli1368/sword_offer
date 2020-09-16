# 5 kyu - Did I Finish my Sudoku


>Write a function done_or_not/`DoneOrNot` passing a board (list[list_lines]) as parameter. If the board is valid return 'Finished!', otherwise return 'Try again!'
>
>Sudoku rules:
>
>Complete the Sudoku puzzle so that each and every row, column, and region contains the numbers one through nine only once.
>
>Rows:
>
>![img](http://www.sudokuessentials.com/images/Row.gif)
>
>There are 9 rows in a traditional Sudoku puzzle. Every row must contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. There may not be any duplicate numbers in any row. In other words, there can not be any rows that are identical.
>
>In the illustration the numbers 5, 3, 1, and 2 are the "givens". They can not be changed. The remaining numbers in black are the numbers that you fill in to complete the row.
>
>Columns:
>
>![img](http://www.sudokuessentials.com/images/Column.gif)
>
>
>
>There are 9 columns in a traditional Sudoku puzzle. Like the Sudoku rule for rows, every column must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. Again, there may not be any duplicate numbers in any column. Each column will be unique as a result.
>
>In the illustration the numbers 7, 2, and 6 are the "givens". They can not be changed. You fill in the remaining numbers as shown in black to complete the column.
>
>Regions
>
>![img](http://www.sudokuessentials.com/images/Region.gif)
>
>A region is a 3x3 box like the one shown to the left. There are 9 regions in a traditional Sudoku puzzle.
>
>Like the Sudoku requirements for rows and columns, every region must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. Duplicate numbers are not permitted in any region. Each region will differ from the other regions.
>
>In the illustration the numbers 1, 2, and 8 are the "givens". They can not be changed. Fill in the remaining numbers as shown in black to complete the region.
>
>Valid board example:
>
>![img](http://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/364px-Sudoku-by-L2G-20050714_solution.svg.png)
>
>For those who don't know the game, here are some information about rules and how to play Sudoku: <http://en.wikipedia.org/wiki/Sudoku> and <http://www.sudokuessentials.com/>



**原址：**[5 kyu - Did I Finish my Sudoku](<https://www.codewars.com/kata/53db96041f1a7d32dc0004d2>)



**说明：**

> 检测是否完成数独



**代码：**

```python
def done_or_not(board): #board[i][j]
    a = list(range(9))
    for i in range(9):
        my_dict1 = dict(zip(board[i], a))
        if(len(my_dict1) != 9):
            return('Try again!')
        my_dict2 = dict(zip([j[i] for j in board], a))
        if(len(my_dict2) != 9):
            return('Try again!')
        x = i % 3 * 3
        y = i // 3 * 3
        my_dict3 = dict(zip(board[y][x:x+3] + board[y+1][x:x+3] + board[y+2][x:x+3], a))
        if(len(my_dict3) != 9):
            return('Try again!') 
    return('Finished!')
```

