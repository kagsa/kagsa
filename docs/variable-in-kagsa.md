# Variable in Kagsa
variables is some names saved im program memory and each of them have a value or elements
## Create
***
in kagsa we use `var` keyword to **create\edit** variabes, and use this syntax :<br>
`var VAR_ID = VAR_ELEMENTS`
### Examples :
```
var my_name = 'Mohammed';
var this_year = 2022
```

## ID
***
to make a variable id thats from more than 1 letter use the common way :
```
var my_name = 'Mohammed';
```
if you want to name the id with 1 letter use `#` before id :
```
var #i = "ABC"
```

## Global
***
use `global` keyword to create a new Global Variable and use `var` to edit it.
### Example :
```
// use "global" to create
global my_var
// use "var" to edit value
var my_var = 'This is Global Varable.'
```

## Delete
***
use `delvar` keyword to delete any variable
### Example :
```
var my_name = 'Mohammed';
delvar my_name
// Now The Variable (my_name) is Deleted.
```