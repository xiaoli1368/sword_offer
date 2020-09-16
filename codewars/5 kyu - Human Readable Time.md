# 5 kyu - Human Readable Time


>## Detials
>
>Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (`HH:MM:SS`)
>
>- `HH` = hours, padded to 2 digits, range: 00 - 99
>- `MM` = minutes, padded to 2 digits, range: 00 - 59
>- `SS` = seconds, padded to 2 digits, range: 00 - 59
>
>The maximum time never exceeds 359999 (`99:59:59`)
>
>You can find some examples in the test fixtures.



**原址：**[5 kyu - Human Readable Time](<https://www.codewars.com/kata/52685f7382004e774f0001f7>)



**说明：**

> 编写一个函数，它以非负整数（秒）作为输入，并以人类可读的格式返回时间（`HH：MM：SS`）。



**代码：**

```python
def make_readable(seconds):
    hh = seconds // 3600
    mm = (seconds - hh * 3600) // 60
    ss = seconds - hh * 3600 - mm * 60
    time = [hh, mm, ss]
    for i in range(3):
        time[i] = '0' + str(time[i]) if time[i] < 10 else str(time[i])
    return ':'.join(time)
```

