# Something Need to Know in Kagsa
Something Need to Know Before Start Programming
## nl
this is a variable we can use it in kagsa<br>
his value is `\n` (New Line)
```
write 'Hello',nl,nl,nl
```
Output :
```
Hello



```

# nlist()
This fucntion is for create a number list, for example you can use it in for loop
```
write nlist(5)
// [0,1,2,3,4,5]
// from 0 to 5

write nlist(5,zero=false)
// [1,2,3,4,5]
// from 1 to 5
```

# none
his value is nothing
```
write none
// None
```

# is..()
this group of fuctions is to check datatype of var
```
isStr()
isInt()
isFloat()
isList()
isDict()

// if yes it will return 1
// if no it will return 0
```

# not()
This function takes Boolean data and gives the opposite of its true result.
```
write not(5==5)
// False

string name = 'user'
if not(name == 'admin'){
    write 'You Are NOT The Admin !!'
}
```
