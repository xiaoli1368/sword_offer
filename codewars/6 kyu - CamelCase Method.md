# 6 kyu - CamelCase Method


>## Detials
>
>Write simple .camelCase method (`camel_case` function in PHP, `CamelCase` in C# or `camelCase` in Java) for strings. All words must have their first letter capitalized without spaces.
>
>For instance:
>
>```python
>camelcase("hello case") => HelloCase
>camelcase("camel case word") => CamelCaseWord
>```
>
>Don't forget to rate this kata! Thanks :)



**原址：**[6 kyu - CamelCase Method](<https://www.codewars.com/kata/587731fda577b3d1b0001196>)



**说明：**

> 编写简单的.camelCase方法（PHP中的`camel_case`函数，C＃中的`CamelCase`或Java中的`camelCase`）。 所有单词的首字母必须没有空格。



**代码：**

```python
def camel_case(string):
    result = []
    sign = 1
    for i in string:
        if(i == ' '):
            sign = 1
        else:
            if(sign == 1):
                result.append(i.upper())
            else:
                result.append(i.lower())
            sign = 0
    return ''.join(result)
```

