# Built Modules in Kagsa
we have some classes that help us to do many things in kagsa :
## Random
***
**Random Things Module.<br><br>**
Choice one of :
```
Random.oneOf( list('choice1','choice2','choice3') )
```
Random String :
```
Random.str(length, abc=true, cap=true, num=true, add="-*/+")
```
Random Integer :
```
Random.int(5,10) // from 5 to 10
```
## Code
***
**Encode\\Decode Module.**
### Base64 :
```
Code.base64.encode('some data')
Code.base64.decode('base64 data')
```
### Hex :
```
Code.hex.encode('some data')
Code.hex.decode('hex data')
```
### Binary :
```
Code.binary.encode('some data')
Code.binary.decode('binary data')
```
## JSON
***
**Json Data encoder and decoder.**
<br><br>Dict to JsonStr
```
var my_dict = dict(name='mohammed', age=14)
write JSON.toJson(my_dict)
```
JsonStr to Dict
```
var my_json = '{"name":"mohammed", "age":14}'
write JSON.toDict(my_json)
```
## HTTP 
***
**Create HTTP Requests Module**
<br><br>Step 1 : Create New Session :
```
var session = HTTP()
```
Step 2 : Add URL :
```
session.URL("https://api.ipify.org/")
```
Step 3 : Choice Method (POST\\GET) :
```
session.method('get') // or 'GET'
```
Step 4 : Options :
```
// --Optional--
// update header
session.headers( headers_dict )

// set auth
session.auth( auth_data )

// update cookies
session.cookies( cookies_dict )
```
Step 5 : Send Request :
```
var response = session.send() // or session.send( params_data )
```
Step 6 : Get Output :
```
write response.cookies
write response.headers
write response.text
write response.content
write response.code
```
## Regex
***
**Use Regex to Get Data From Strings**
<br><br>first create call the module
```
var re = Regex('".*?"')
```
Now use the functions<br>
if regex match string
```
re.isMatch(' a  fkld  "a string"  ') // true
```
find all match
```
re.findAll('  "abc"   lefd 98jd  3 "def"   erk4  "ghi"')
// ['"abc"', '"def"', '"ghi"']
```
get the start of index of ("def")
```
re.indexStart('  lefd 98jd  3 "def"   erk4 ') // 15
```
get the end of index of ("def")
```
re.indexEnd('  lefd 98jd  3 "def"   erk4 ') // 20
```
split all the values
```
re.split('  "abc"   lefd 98jd  3 "def"   erk4  "ghi"')
// ['  ', '   lefd 98jd  3 ', '   erk4  ', '']
```
split values from (1 to on)
```
re.split('  "abc"   lefd 98jd  3 "def"   erk4  "ghi"',on=1)
// ['  ', '   lefd 98jd  3 "def"   erk4  "ghi"']
```
replace values
```
re.replace('adf "fg" ghg hfj "f65" 54 hgf "65g" fgd','000')
// adf 000 ghg hfj 000 54 hgf 000 fgd
```
## System
***
**Dealing With The System**
<br><br>get argv data
```
write System.argv
```
Get input line
```
write 'Write Any Thing :'
var dd = System.input()
```
write data and errors
```
System.write.out('Hi', ' There')
System.write.err('Error')
```
exit program
```
System.exit('goodbey')
```
Run Commands
```
System.cmd('echo Hi Bro')
```
Run Commands and get Outputs
```
var out = System.exec('echo Hi Bro')
// with Shell
var out = System.exec('echo Hi Bro',shell=true)
```
Get Program Path
```
write System.path()
```
Get System Informations
```
var Sys = System.informations()
write get(Sys,'system')
write get(Sys,'node')
write get(Sys,'release')
write get(Sys,'version')
write get(Sys,'machine')
write get(Sys,'processor')
```
## File
***
**Dealing With The Files**
<br><br>
Read File
```
var file = File.Read('data.txt')
write file.getText()
file.end()
```
Write New File of OverWrite
```
var file = File.Write('data.txt')
file.write('data1', 'data2', 'data3')
file.end()
```
Add Data to a File
```
var file = File.Add('data.txt')
file.write('data4', 'data5', 'data6')
file.end()
```
## Time
***
**Dealing With The Time**
<br><br>
get time from the epoch to now with seconds
```
Time.epoch()
```
get a time after epoch (use seconds)
```
Time.aEpoch(0)      // Wed Dec 31 16:00:00 1969
Time.aEpoch(1000)   // Wed Dec 31 16:16:40 1969
```
get a time after epoch (get output as a obj)
```
var data = Time.aEpoch(1000, obj=true)
write data.year ,nl;
write data.mon ,nl;
write data.mday ,nl;
write data.hour ,nl;
write data.min ,nl;
write data.sec ,nl;
write data.wday ,nl;
write data.yday ,nl;
write data.isdst ,nl;
```
get the time now
```
write Time.now()
// Wed May 25 08:03:42 2022
```
get the time now (get output as a obj)
```
var data = Time.now(obj=true)
write data.year ,nl;
write data.mon ,nl;
write data.mday ,nl;
write data.hour ,nl;
write data.min ,nl;
write data.sec ,nl;
write data.wday ,nl;
write data.yday ,nl;
write data.isdst ,nl;
```
stop the program for some seconds
```
Time.sleep(5)  // stop for 5 sec
```