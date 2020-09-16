# 7 kyu - Descending Order


>## Detials
>
>Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
>
>### Examples:
>
>Input: `21445` Output: `54421`
>
>Input: `145263` Output: `654321`
>
>Input: `1254859723` Output: `9875543221`



**原址：**[7 kyu - Descending Order](<https://www.codewars.com/kata/5467e4d82edf8bbf40000155>)



**说明：**

> 你的任务是创建一个函数，该函数可以将任何非负整数作为参数，并以其降序返回数字。 基本上，重新排列数字以创建尽可能高的数字。



**代码：**

```python
def Descending_Order(num):
    #Bust a move right here  
    return int(''.join(sorted(list(str(num)), reverse=True)))
```

