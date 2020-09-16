# 4 kyu - Next bigger number with the same digits


>You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:
>
>```js
>12 ==> 21
>513 ==> 531
>2017 ==> 2071
>```
>
>If no bigger number can be composed using those digits, return `-1`:
>
>```js
>9 ==> -1
>111 ==> -1
>531 ==> -1
>```



**原址：**[4 kyu - Next bigger number with the same digits](<https://www.codewars.com/kata/55983863da40caa2c900004e>)



**说明：**

> 您必须创建一个带有正整数的函数，并返回由相同数字组成的下一个更大的数字。如果使用这些数字不能组成更大的数字，则返回-1。



**代码：**

```python
def next_bigger(n):
    result = []    
    list_n = list(str(n))
    min_n = sorted(list_n, reverse=True)
    length = len(list_n)
    if(n == int(''.join(min_n))):
        return(-1)
    else:
        for i in range(length - 2, -1, -1):
            for j in range(length - 1, i, -1):
                if(list_n[i] < list_n[j]):
                    list_n[i], list_n[j] = list_n[j], list_n[i]
                    return(int(''.join(list_n[:i + 1]) + ''.join(sorted(list_n[i + 1:]))))
```

