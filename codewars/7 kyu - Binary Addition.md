# 7 kyu - Binary Addition


>## Detials
>
>Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.
>
>The binary number returned should be a string.



**原址：**[7 kyu - Binary Addition](<https://www.codewars.com/kata/551f37452ff852b7bd000139>)



**说明：**

> 实现一个将两个数字相加并以二进制形式返回其总和的函数。 转换可以在添加之前或之后完成。返回的二进制数应为字符串。
>


**代码：**

```python
def add_binary(a,b):
    #your code here
    c      = a + b
    result = []
    shang  = 1
    yushu  = 1
    while(shang != 0):
        shang = c // 2
        yushu = c % 2
        result.append(str(yushu))
        c     = shang
    return ''.join(result[::-1])
```

