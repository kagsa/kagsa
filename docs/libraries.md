# Libraries in Kagsa
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
`-l` for the lib codes file, should be `.kg`<br>
`-o` for output file, should be `.kgl`<br>
now we have the file `IPLIB.kgl` this file is our new library
## How To Import Library ?
***
now we will use the `include` kewword.
```
include "IPLIB.kgl"
// in include feel free to use full path or somthing like this :
// c:\\projects\kagsa\file.kgl
// myFloder\file.kgl
```
now you can use the library functions/classes
```
if IPLIB.isConnectToInternet() {
    write 'Connected'
}else{
    write 'Not Connected'
}
```

sample output :
```
Connected
```