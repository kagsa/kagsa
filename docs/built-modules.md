# Built Modules in Kagsa
we have some classes that help us to do many things in kagsa :
## Random
***
**Randoming Module.<br><br>**

- Choice one of items in a list :

```
Random.oneOf( list('choice1','choice2','choice3') )
```
- Random String :

```
Random.str(length, abc=true, cap=true, num=true, add="-*/+")
```
- Random Integer :

```
Random.int(5,10) // from 5 to 10
```
## Code
***
**Encode\\Decode Module.**
- ### Base64 :
```
Code.base64.encode('some data')
Code.base64.decode('base64 data')
```
- ### Hex :
```
Code.hex.encode('some data')
Code.hex.decode('hex data')
```
- ### Binary :
```
Code.binary.encode('some data')
Code.binary.decode('binary data')
```
- ### Bytes :
```
Code.utf_8.encode('some data')
Code.utf_.decode(bytes_data_string)
```
## JSON
***
**Dealing With Json Data**
<br><br>
- Dict to JsonStr

```
var my_dict = dict(name='mohammed', age=14)
write JSON.toJson(my_dict)
```
- JsonStr to Dict

```
var my_json = '{"name":"mohammed", "age":14}'
write JSON.toDict(my_json)
```
- Parse a Json/Dict

```
var json_str = '{"user_data": {"id": 123, "name": "mohammed"}}'
var JS = JSON.parse(json_str)
write JS.user_data.id
// 123


var json_str = dict( user_data= dict( id=123, name='mohammed' ) )
var JS = JSON.parse(json_str)
write JS.user_data.id
// 123
```
- UnParse a Parsed JSON

```
// i will use the json var that i write it up ( JS )
var un_parsed_JS = JSON.unParse( JS )
// now this var is a dict data

write get(un_parsed_JS, 'user_data')
// {'id': 123, 'name': 'mohammed'}
```
## HTTP 
***
**Create HTTP Requests Module**
<br><br>
**Step 1** : Create New Session :
```
var session = HTTP()
```
**Step 2** : Add URL :
```
session.URL("https://api.ipify.org/")
```
**Step 3** : Choice Method :
```
session.method('get')
// Other Methods :
// GET, POST, PUT, HEAD, PATCH, DELETE, OPTIONS
```
**Step 4** : Options :
```
// --Optional--
// update header
session.headers( headers_dict )

// set auth
session.auth( auth_data )

// update cookies
session.cookies( cookies_dict )

// set output encoding
session.encoding('utf-8')
```
**Step 5** : Send Request :
```
var response = session.send() // or session.send( params_data )
```
**HTTP Request Response**
```
response.cookies
response.headers
response.text
response.content
response.code
response.redirect
response.url
```
## Regex
***
**Use Regex to Get Data From Strings**
<br><br>
- call the module and set the regex code

```
var reg = Regex('".*?"')
```
- if regex match string

```
var reg = Regex('mohammed')
write reg.isMatch('Hello my name is mohammed')
// True
```
- find all match

```
var reg = Regex('z-[0-9]')
write reg.findAll('a-5 n-56 f-7 z-2 p-3 d-4 z-3')
// ['z-2', 'z-3']
```
- get the start\end of string index

```
var reg = Regex('ahmed')
write reg.indexStart('ali ahmed')
// 4
write reg.indexEnd('ali ahmed')
// 9

// this mean :
// ali ahmed
//     |   |
//     4   9
```

- split all the values

```
var reg = Regex(',')
write reg.split('mohammed,ahmed,ali')
// ['mohammed', 'ahmed', 'ali']
```
- split values from (begin to `till`)

```
var reg = Regex(',')
write reg.split('mohammed,ahmed,ali,sarah,abdallah', till=2)
// ['mohammed', 'ahmed', 'ali,sarah,abdallah']
```
- replace values

```
var reg = Regex(',')
write reg.replace('mohammed,ahmed,ali,sarah,abdallah', ' - ')
// mohammed - ahmed - ali - sarah - abdallah
```
## System
***
**Dealing With The System**
<br><br>
- get argv data

```
write System.argv
```
- get input line

```
write 'Write Any Thing :'
var any_thing = System.input()
```
- write data and errors

```
System.write.out('Hi there', ' , my name is mohammed')
System.write.err('Error')
```
- exit program

```
System.exit('program has stoped.')
```
- run Commands

```
System.cmd('echo Hi Bro')
```
- run Commands and get Outputs

```
var cmd = System.exec('echo Hi Bro')
// withot Shell
var cmd = System.exec('echo Hi Bro',shell=false)
// if the command is wrong it will raise a error
```
- get Program Path

```
write System.path()
```
- get System Informations

```
var Sys = System.informations()
// dict data
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
- Read File

```
var file = File.Read('data.txt')
write file.getText()
file.end()
```
- Read Btytes File

```
var file = File.ReadBytes('image.png')
var data = file.get
```
- Write New File of OverWrite

```
var file = File.Write('data.txt')
file.write('data1', 'data2', 'data3')
file.end()
```
- Add Data to a File

```
var file = File.Add('data.txt')
file.write('data4', 'data5', 'data6')
file.end()
```
## Time
***
**Dealing With The Time**
<br><br>
- get time from the epoch to now with seconds

```
Time.epoch()
```
- get a time after epoch (use seconds)

```
Time.aEpoch(0)      // Wed Dec 31 16:00:00 1969
Time.aEpoch(1000)   // Wed Dec 31 16:16:40 1969
```
- get a time after epoch (get output as a obj)

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
- get the time now

```
write Time.now()
// Wed May 25 08:03:42 2022
```
- get the time now (get output as a obj)

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
- stop the program for some seconds

```
Time.sleep(5)  // stop for 5 sec
```
- count time

```
var time = Time.count()
time.start()     // start counting
Time.sleep(1.5)  // make any thing
time.end()       // stop counter

write time.get   // get output
// 0:00:01.511142
```
- count time and get output as obj

```
var time = Time.count(obj=1)
time.start()
Time.sleep(1.5)
time.end()

write time.days , nl
write time.min , nl
write time.seconds , nl
write time.microseconds , nl
write time.total_seconds , nl

// 0 
// -999999999 days, 0:00:00 
// 1
// 502204
// 1.502204
```
## Math
***
**Some Math Functions**<br>
Use the same functions of Python math lib (I'm not a mathematician)
```
Math.cos(1)
Math.sin(5)
Math.tan(10)
```


## Keyboard
***
**Dealing With Keyboard**


- Wait Until The `'a'` Key Press

```
Automation.Keyboard.wait('a')
```

- Write Somthing

```
Automation.Keyboard.write('github.com/kagsa/kagsa')
```

- Create a New Hotkey

```
func openGoogle () {
    System.cmd("start www.google.com")
}
Automation.Keyboard.newHotkey('ctrl + g', openGoogle)
```

-  Record Keys until `ESC` press

```
var data = Automation.Keyboard.record(until='esc')
```

- Get Data From Record

```
data.get
```

- Play The Record

```
data.playAll(speed=0.2) // defult speed : 0.5
```

- Press Some Keys

```
Automation.Keyboard.press("ctrl + a, ctrl + c")
```
