# Conditions in Kagsa

We Have 3 conditions word in kagsa : `if`, `elseif`, `else`.
The conditions sentences help to deal with the data and give programming great ease with decision-making
conditions writted in this syntax :
```
condition-name  statements  {
    line of codes..
}
```
## Example :
***
```
var i = 5;

if i > 7 {
    write 'Number is Big Than 7'
}elseif i > 15 {
    write 'Number is Big Than 15';
}else{
    write 'Number is Small Than 7'
}

// output :
// Number is Small Than 7
```

## Statements :
***
you can use this separators in the statements :<br>
`==` is equal, Example `5 == 5` = true<br>
`!=` is not equal, Example `5 != 2` = true<br>
`>` is big than, Example `5 < 2` = false<br>
`<` is small than, Example `2 < 10` = true<br>
`->` is in, Example `'hi' -> "i am mohammed"` =  false<br>
`>=` is big than or equal to, Example `5 >= 2` = true<br>
`<=` is small than or equal to, Example `3 <= 3` = true<br>
`||` or, example `(4.0 == 5) || (4.0 == 4)` = true<br>
`&&` and, Example `('h' -> 'hi') && ('p' -> 'mohammed')` = false<br>
`flase` its clear, right? Example `0 == false` = true<br>
`true` its clear too, Example `1 == true` = true<br>
and more !!<br>
You can use a functions as a statements too, just make your function return `1` or `true` for Yes and `0` or `false` for No, example :
```
var str = "abcdefgh"
if str.start('abc') {
    // str is started with 'abc'
    write 'string startrd with "abc"'
}else{
    write 'string didn\'t started with "abc"'
}
```
some times we have to use a function returns with a separator, example :
```
// i will make a str var wit value : 'mohammed'
// the length of 'mohammed' is 8
var str = 'mohammed'

if str.length() < 5 {
    write 'the length of %{str} is less than 5'
}

else{
    write 'the length of %{str} is more than 5'
}
```
in this example we use `length(str) < 5` as statement, this mean we use (function +separator + int)

## How it Works ?
***
the condition word will read the statement and if `statement = true` the lines of code will run , example
```
// the statement is :
// (5 > 3) = (5 is big than 3)
// is 5 big than 3 ??
// YES !!, then the program will print "yes"
if 5 > 3 {
    write 'yes'
}else{
    write 'no'
}
```