# IO in Kagsa
inputs and outputs in Kagsa.
## write
***
`write` keyword let you print any data on **consle\terminal\cmd** , using this Syntaxs `write ELEMENTS` we can use `,` \ `+` between ELEMENTS.
### Examples :
```
// Example 1
var name='Mohammed'
write "My Name is "+name;
// My Name is Mohammed

// Example 2
write 'My Name is','Mohammed'
// My Name is Mohammed

// Example 3
write 34+2
// 36
```

## input
***
`input` keyword let you **get\read** data from user in command line , in `input` we have yo use this syntax `input ELEMENT`, you can't use `,` \ `+` in it.
### Examples :
```
// Example 1
var user=input'[+] Enter Your Username :'

// Example 2
write 'Hi, Welcome',input "Whats Your Name?"

// Example 1
var user = input'Username :'
var pass = input'Password :'
write user+':'+pass;
```
