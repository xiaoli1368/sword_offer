# 7 kyu - Deodorant Evaporator


>## Detials
>
>This program tests the life of an evaporator containing a gas.
>
>We know the content of the evaporator (content in ml), the percentage of foam or gas lost every day (evap_per_day) and the threshold (threshold) in percentage beyond which the evaporator is no longer useful. All numbers are strictly positive.
>
>The program reports the nth day (as an integer) on which the evaporator will be out of use.
>
>**Note** : Content is in fact not necessary in the body of the function "evaporator", you can use it or not use it, as you wish. Some people might prefer to reason with content, some other with percentages only. It's up to you but you must keep it as a parameter because the tests have it as an argument.



**原址：**[7 kyu - Deodorant Evaporator](<https://www.codewars.com/kata/5506b230a11c0aeab3000c1f>)



**说明：**

> 该程序测试含有气体的蒸发器的寿命。
>
> 我们知道蒸发器的含量（以ml计的含量），每天损失的泡沫或气体的百分比（evap_per_day）和阈值（阈值），以百分比超过蒸发器不再有用。 所有数字都是严格正数。
>
> 该程序报告蒸发器将不使用的第n天（整数）。



**代码：**

```python
def evaporator(content, evap_per_day, threshold):
    day_spend = 0
    remain = 100
    while remain > threshold:
        day_spend += 1
        remain *= (1 - evap_per_day / 100)
    return day_spend
```

