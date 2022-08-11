# Loops in Kagsa
Loops is the process of repeating a block of codes with a specified number or an infinite number, we have 2 types of loop :

## For
***
This type of loop is used to read a dict, a list, etc.
### Example :
```
var list_var = list(45245,454,5554,45,2345,43)
for ii -> list_var{
    write ii,nl
}
// every time the codes is run ii will have another value
// in first time the ii value will be 45245
// in second time the ii value will be 454
// until end
```
and dict :
```
var dict_var = dict(name='zaky',age=100)
for ii -> keys(dict_var){
    write 'key :',ii,'  value :',get(dict_var,ii),nl
}
// every time the codes is run ii will have another value
// in first time the ii value will be "name"
// in second time the ii value will be "age"
```
and you can use it on string , that will read every letter inside string

ok, now something wow, `nlist()` function :
```
for dd -> nlist(10,zero=false) {
    write "Count : %{dd}\n"
}
```
## While
***
This type of loop reads the condition and if it is real, it will continue to iterate<br>
it works like the conditions word (`if`)
### Example :
```
var num = 0;
while num < 11 {
    num+=1
    write num , nl
}
```
this with print numbers from 0 to 10
## Break
***
break is not a type of loop but its a keyword that used to stop loop
### Example :
```
var #n = 0
while true {
    write #n
    #n+=1
    if #n == 10 {
        break // if the variable equal 10 stop the loop
    }
}
```