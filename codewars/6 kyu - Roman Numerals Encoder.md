# 6 kyu - Roman Numerals Encoder


>## Detials
>
>Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.
>
>Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
>
>Example:
>
>```python
>solution(1000) # should return 'M'
>```



**原址：**[6 kyu - Roman Numerals Encoder](https://www.codewars.com/kata/51b62bf6a9c58071c600001b)



**说明：**

> 创建一个以正整数作为参数并返回包含该整数的罗马数字表示的字符串的函数。
>
> 现代罗马数字是通过从最左边的数字开始分别表示每个数字并跳过值为零的任何数字来编写的。 在罗马数字中，呈现1990：1000 = M，900 = CM，90 = XC; 导致MCMXC。 2008年写成2000 = MM，8 = VIII; 或MMVIII。 1666按降序使用每个罗马符号：MDCLXVI。



**代码：**

```python
def solution(n):
    # TODO convert int to roman string
    result = []
    string = list(str(n))
    length = len(string)
    ref = [['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
           ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
           ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
           ['M', 'MM', 'MMM', 'MM', 'M', 'MM', 'MMM', 'MMMM', 'MM']
        ]
    for i in range(length):
        if string[i] == '0':
            continue
        else:
            result.append(ref[length - 1 - i][int(string[i]) - 1])      
    return ''.join(result)
```

