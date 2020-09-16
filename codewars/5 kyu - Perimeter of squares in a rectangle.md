# 5 kyu - Perimeter of squares in a rectangle


>The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. It's easy to see that the sum of the perimeters of these squares is : `4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80`
>
>Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1 squares disposed in the same manner as in the drawing:
>
>![alternative text](http://i.imgur.com/EYcuB1wm.jpg)
>
>\#Hint: See Fibonacci sequence
>
>\#Ref: <http://oeis.org/A000045>
>
>The function perimeter has for parameter n where n + 1 is the number of squares (they are numbered from 0 to n) and returns the total perimeter of all the squares.
>
>```
>perimeter(5)  should return 80
>perimeter(7)  should return 216
>```



**原址：**[5 kyu - Perimeter of squares in a rectangle](<https://www.codewars.com/kata/559a28007caad2ac4e000083>)



**说明：**

> 该图显示了6个正方形，其边长为1,1,2,3,5,8。很容易看出这些正方形的周长之和为：4 *（1 + 1 + 2 + 3 + 5 + 8）= 4 * 20 = 80。当有n + 1个方格以与图中相同的方式处理时，你能编写函数给出矩形中所有方块的周长之和。函数周长具有参数n，其中n + 1是正方形（它们从0到n编号）并返回所有正方形的总周长。
>



**代码：**

```python
def perimeter(n):
    a = [1, 1]
    for i in range(2, n + 1):
        a.append(a[i - 2] + a[i - 1])
    return 4 * sum(a)
```

