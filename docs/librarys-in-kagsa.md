# Librarys in Kagsa
library is a file with a group of functions.
## How To Craete Library ?
***
first we have to write the functions in `.kg` file<br>
this is sample functions for `ip_lib.kg` :
```
func getIP (){
    var session = HTTP()
    session.method('get')
    session.URL('https://api.ipify.org')
    var response = session.send()
    return response.text;
}

func isConnectToInternet () {
    try {
        var session = HTTP()
        session.method('get')
        session.URL('https://www.google.com')
        session.send()
        return true
    }catch{
        return false
    }
}
```
we will make a library from this functions<br>
now lets compile it.
```
kagsa -l ip_lib.kg -o IPLIB.kgl
```
`-l` for the functions file, should be `.kg`<br>
`-o` for output file, should be `.kgl`<br>
now we have the file `IPLIB.kgl` this is the translated kagsa codes encoded with base64
## How To Import Library ?
***
first create the importer file, importer is a json file used to import library<br>
```json
{"AnyNameForLibarary":"LibraryFile"}
```
We will create `import.json` :
```json
{"IPLib": "IPLIB.kgl"}
```
ok now the final step<br>
now lets try to use `IPLib` in my Codes<br>
to call library functions, should make like this
```
LibraryName__FunctionName()
```
add `__` in the middle<br>
My Code `file.kg` :
```
if IPLib__isConnectToInternet() {
    write 'Your IP is :';
    write IPLib__getIP()
}else{
    write 'No Internet Connection..!'
}
```
Now if i run the code i will get this
```
Error Catched in "file.kg", Out From Compiler :
    >> if IPLib__isConnectToInternet() {
    >> line 1
NameERR : name 'IPLib__isConnectToInternet' is not defined
```
we can fix it easly, just add `-m <YOUR-IMPORT-FILE>`<br>
Run it Like this :
```
kagsa file.kg -m import.json
```
The Output :
```
Your IP is :37.2**.***.***
```