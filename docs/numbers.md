# Integer-Float in Kagsa
**integer** : a number data saved in var or else.<br>
**float** : it just a float :) .
## Examples :

```
var my_age_int = 1000;
write my_age_int + 500
// 1500

var my_age_float = 1000.5
write my_age_float + 0.5
// 1001
```
## Math :

we have to learn how to use math in kagsa, right?
<br>**Plus** : `+`
<br>**Minus** : `-`
<br>**Times** : `*`
<br>**Divide** : `/`
<br>**Power** : `**`
<br>**Remainder of Division** : `%`
### Examples :
```
var a = 5;
var b = 2.5

write a + b
// 7.5

write a - b
// 2.5

write a * b
// 12.5

write a / b
// 2

write a ** 2
// 25

write a % b
// 0
```
## Methods :

Methods is a group of functions that help you to edit in any variable.
```
var num = 55;
```
- **toStr( )** : change from int\float to str

```
write toStr(num)
// output : 55
```

- **toFloat( )** : change from int\str to float

```
write toFloat(num)
// output : 55.0
```

- **toInt( )** : change from str\float to int

```
write toInt('453')
// output : 453
```

## Math on Variable
lets take a example that we have a variable named `num` and equal `5` how we add `5` on it ? you have to do this
```
var num = num+5
```
just a joke, you can use this short way :
```
num+=5
```
you can use `-` , `/` , `*` , `**` , `%`