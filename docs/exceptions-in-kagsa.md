# Exceptions in Kagsa
Exceptions is an important in all programming language<br>
Here we have to keywords : `try`, `catch`
## Example :
***
this is wrong kagsa code :
```
write toInt('abc')
```
if i run it i will get
```
Error Catched in "file.kg", Out From Compiler :
    >> write toInt('abc')
    >> line 1
ValueERR : can't change (abc) to int
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
    write 'There is a Error in Your Code',nl
    write 'Error Text',data.text
    write 'Error Line',data.line
    write 'Error Type',data.type
    write 'Error File',data.file
    
}
```
Output :
```
There is a Error in Your Code 
Error Text ValueERR : can't change (abc) to int 
Error Line 2
Error Type ValueERR
Error File file.kg
```
## How To Create Your Error ?
***
Use `NewERR` function to do it
```
// Create WiFiErr
var WiFiError = NewERR('WiFiError')

// Run it
WiFiError('NO Internet Connection..!')
```
Output :
```
Error Catched in "file.kg", Out From Compiler :
    >> WiFiError('NO Internet Connection..!')
    >> line 5
WiFiERR : NO Internet Connection..!
```
## Error in Kagsa :
You Can Use All Python Errors in Kagsa, Just replace `Error` with `ERR`
### Example :
```
SyntaxERR('Error Text')
```