# Functions in Kagsa
function is a way to shorten a block of codes and call it anywhere in the program.
we use this syntax to write a function :
```
func name (parameters) {
    // block of codes..
}
```
## Example :
***
```
// create function
func print_cv (name,age,job){
    write "Hi My Name is %{name}, My age is %{age} , i am %{job}\n"
}
// call it
print_cv('Mohammed', 14, 'student')
print_cv('Aslooj', 14, 'student')
```
## Return
***
return is a keyword that help to return data for fucntions
### Example :
```
func say_my_name (name) {
    return 'your name is %{name}'; // this func = 'your name is %{name}'
}

var something = say_my_name('mhmd')
// this var is equal 'your name is mhmd'
```
you can return any type of data str,int,float,dict,list....