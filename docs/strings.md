# Strings in Kagsa
String : the text data that writed between `' '` , `" "` or ` ``  `` `
## Examples :
***
```
var this_is_my_string = 'Any Text Data, this str is writed in \'\' '

var ss = "this is another string , writed in \"\" "

var many_lines_string = ``
string here
another line 
another line x2
this str is writed in \``
end of str -> ``
```

## Format :
***
format is a feature used inside string to add any values (from variables) to str.
### Examples :
```
var my_name = 'Mohammed';
write "Hello User, My Name is %{my_name}"
```
Format will search for `%{}` and get the variable value in it and replace `%{value}` with the value.

## Methods :
***
Methods is a group of functions that help you to edit in any variable.
```
// make variable to test the methods
var example = 'kagsa is a new programming language';

// change from str to int
write toInt("5")
// output : 5

// change from str to float
write toFloat("5")
// output : 5.0

// replace 'new' with 'old'
write replace(example,"new",'old')
// output : kagsa is a old programming language

// split a value and change from str to list
write split(example,' ')
// output : ['kagsa','is','a','new','programming','language']

// check if string end with value
write end(example,'abc')
// output : False

// check if string start with value
write start(example,'kagsa')
// output : True

// search for value index
write search(example,'is')
// output : 6

// change all letter to upcase
write upcase(example)
// output : KAGSA IS A NEW PROGRAMMING LANGUAGE

// change all letter to downcase
write downcase(example)
// output : kagsa is a new programming language

// delete the space on right\left sides of string
write strip(example)
// output : kagsa is a new programming language

// count the string length
write length(example)
// output : 35

// get index from str with 1 value
write get(example,0)
// output : k

// get index from str with 2 value
write get(example,0,5)
// output : kagsa
```