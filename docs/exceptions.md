# Exceptions in Kagsa
Exceptions is an important in all programming language<br>
Here we have to keywords : `try`, `catch`
## Example :

this is wrong kagsa code because you can't covert `abc` to an integer :
```
write toInt('abc')
```
if i run it i will get
```
error catched [ test.kg/ValueERR ]
   |
 1 | write toInt('abc')
   |
error : can't change (abc) to int
```
the error file is : `file.kg`<br>
the error line no : `1`<br>
the error line  : `write toInt('abc')`<br>
the error type : `ValueERR`<br>
the error text : `can't change (abc) to int`<br><br>
**How We Can Run it Without get an Error ?**
we can use try and catch
```
try {
    write toInt('abc')
}
catch {
    write 'There is a Error in Your Code'
}
```
Output :
```
There is a Error in Your Code
```
Ok its Clear<br><br>
**How To Get Error Data Under Catch Command ?**
```
try {
    write toInt('abc')
}
catch {
    var data = getError()
    write 'There is a Error in Your Code' , nl
    write 'Error Text',data.text , nl
    write 'Error Line',data.line , nl
    write 'Error LineNo',data.lineno , nl
    write 'Error Type',data.type , nl
    write 'Error File',data.file , nl

}
```
Output :
```
There is a Error in Your Code 
Error Text can't change (abc) to int 
Error Line write toInt('abc')
Error LineNo 2
Error Type ValueERR
Error File test.kg
```
## How To Create Your Error ?
Use `NewERR` function to do it
```
// Create WiFiErr
var WiFiError = NewERR('WiFiError')

// Run it
WiFiError('NO Internet Connection..!')
```
Output :
```
error catched [ test.kg/WiFiERR ]
   |
 5 | WiFiError('NO Internet Connection..!')
   |
error : NO Internet Connection..!
```
You can add a details to your error text just add `\n` and the details :
```
WiFiError('NO Internet Connection..!\nCheck Your Internet Connection')
```

Output :
```
error catched [ test.kg/WiFiERR ]
   |
 5 | WiFiError('NO Internet Connection..!\nCheck Your Internet Connection')
   |
error : NO Internet Connection..!
details : Check Your Internet Connection
```

## Errors in Kagsa :
You Can Use All Python Errors in Kagsa, Just replace `Error` with `ERR`
### Example :
```
SyntaxERR('Error Text')
```