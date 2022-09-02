# Variable in Kagsa
variables is some names saved in program memory and each of them have a value or elements
## Create

in kagsa we use `var` keyword as the main way to **create\edit** variabes, and use this syntax :<br>
`var ID = ELEMENTS`

### Examples :
```
var my_name = 'Mohammed';
var this_year = 2022
```
There is many another keywords to make a string :
- **string**

```
string my_name = 10+10
// value will be : "20"
// the orginal value is 20 ,but string keyword change it to string
```
- **int**

```
int num = "5"
// value will be : 5
// the orginal value is "5" ,but int keyword change it to int
```
- **float**

```
float num = 5
// value will be : 5.0
// the orginal value is 5 ,but float keyword change it to float
```
- **list**

```
list my_name = "ali"
// value will be : ['a','l','i]
// the orginal value is "ali" ,but list keyword change it to list
```
- **dict**

```
dict data = '{"name":"ali"}'
// value will be : {"name":"ali"}
// the orginal value is "{"name":"ali"}" ,but dict keyword change it to dict
```


## Variable Name
You can use `abc..` or `ABC..` or `_` or `_@$^~?` or `123..` to write the var name<br>
### Examples :
```
var my_name = 'Mohammed';
```
```
var i = "ABC"
```

## Global

use `global` keyword to create a new global variable and use `var` to edit it.
### Example :
```
// use "global" to create
global my_var
// use "var" to edit value
var my_var = 'This is Global Varable.'
```

## Delete

use `delvar` keyword to delete any variable
### Example :
```
var my_name = 'Mohammed';
delvar my_name
// Now The Variable (my_name) is Deleted.
```