# 6 kyu - Give me a Diamond


>## Detials
>
>Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since James doesn't know how to make this happen, he needs your help.
>
>## Task
>
>You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (`*`) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (`\n`).
>
>Return `null/nil/None/...` if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.
>
>## Examples
>
>A size 3 diamond:
>
>```
> *
>***
> *
>```
>
>...which would appear as a string of `" *\n***\n *\n"`
>
>A size 5 diamond:
>
>```
>  *
> ***
>*****
> ***
>  *
>```
>
>...that is: `" *\n ***\n*****\n ***\n *\n"`



**原址：**[6 kyu - Give me a Diamond](<https://www.codewars.com/kata/5503013e34137eeeaa001648>)



**说明：**

> 您需要使用星号（`*`）字符返回在屏幕上打印时看起来像钻石形状的字符串。 应删除尾随空格，并且每行必须以换行符（`\ n`）终止。



**代码：**

```python
def diamond(n):
    # Make some diamonds!
    result = []
    if (n < 0 or n % 2 == 0):
        return None
    else:
        for i in range(1, n + 1):
            y = (n + 1) // 2     # 中间的行
            x = (y - abs(y -i))  # i的等价的行
            result.append(' ' * (y - x) + '*' * (x * 2 -1) + '\n')
        return ''.join(result)
```

