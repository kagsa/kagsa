# Strings in Kagsa
String : the text data that writed between `' '` , `" "` or ` ``  `` `
## Examples :

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

format is a feature used inside string to add any value to the string.
### Examples :
```
var my_name = 'Mohammed';
write "Hello User, My Name is %{my_name}"
```
Format will read everything inside `%{}` and get the value of it and replace `%{something}` with the value.

## Methods :

Methods is a group of functions that help you to edit in any variable.

```
var example = 'kagsa is a new programming language';
```

- **toInt( )** : change from str to int

```
write toInt("5")
// output : 5
```

- **toFloat( )** : change from str to float

```
write toFloat("5")
// output : 5.0
```

- **replace( )** : replace 'new' with 'old'

```
write example.replace('new', 'old')
// or
write replace(example,"new",'old')
// output : kagsa is a old programming language
```

- **split( )** : split a value and change from str to list

```
write example.split(' ')
// or
write split(example,' ')
// output : ['kagsa','is','a','new','programming','language']
```

- **end( )** : check if string end with value

```
write example.end('abc')
// or
write end(example,'abc')
// output : False
```

- **start( )** : check if string start with value

```
write example.start('kagsa')
// or
write start(example,'kagsa')
// output : True
```

- **search( )** : search for value index

```
write example.serarch('is')
// or
write search(example,'is')
// output : 6
```

- **upcase( )** : change all letter to upcase

```
write example.upcase()
// or
write upcase(example)
// output : KAGSA IS A NEW PROGRAMMING LANGUAGE
```

- **downcase( )** : change all letter to downcase

```
write example.downcase()
// or
write downcase(example)
// output : kagsa is a new programming language
```

- **strip( )** : delete the space on right\left sides of string

```
write example.strip()
// or
write strip(example)
// output : kagsa is a new programming language
```

- **length( )** : count the string length

```
write example.length()
// or
write length(example)
// output : 35
```

- **get( )** : get index from str with 1 value

```
write example.get(0)
// or
write get(example,0)
// output : k
```

- **get( )** : get index from str with 2 value

```
write example.get(0,5)
write get(example,0,5)
// output : kagsa
````