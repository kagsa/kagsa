# Built Modules in Kagsa
we have some classes that help us to do many things in kagsa :
![](https://raw.githubusercontent.com/Zaky202/kagsa/main/built_modules.png)

## Random
**Randoming Module.<br><br>**

- **Random.oneOf( )** : choice one of items in a list :

```
// Random.oneOf( data:list )
Random.oneOf( list('pizza','salad','rise') )
```
- **Random.str( )** : random string :

```
// Random.str(length, abc=bool, cap=bool, num=bool, add=string)
Random.str(10, abc=true, cap=true, num=true, add='!@#$')
```
- **Random.int( )** : random integer :

```
// Random.int( min:int, max:int )
Random.int( 5, 10 )
```
## Code
**Encode\\Decode Module.**
- ### Base64 :

```
// Code.base64.encode( data:string )
// Code.base64.decode( data:string )

Code.base64.encode('some data')
Code.base64.decode('base64 data')
```

- ### Hex :

```
// Code.hex.encode( data:string )
// Code.hex.decode( data:string )

Code.hex.encode('some data')
Code.hex.decode('hex data')
```
- ### Binary :

```
// Code.binary.encode( data:string )
// Code.binary.decode( data:string )

Code.binary.encode('some data')
Code.binary.decode('binary data')
```
- ### Bytes :

```
// Code.utf_8.encode( data:string )
// Code.utf_8.decode( data:string )

Code.utf_8.encode('some data')
Code.utf_8.decode(bytes_data_string)
```
## JSON

**Dealing With Json Data**

- **JSON.toJson( )** : dict to JsonStr

```
// JSON.toJson( data:dict )
var my_dict = dict(name='mohammed', age=14)
write JSON.toJson(my_dict)
```
- **JSON.toDict( )** : JsonStr to dict

```
// JSON.toDict( data:string )
var my_json = '{"name":"mohammed", "age":14}'
write JSON.toDict(my_json)
```
- **JSON.parse( )** : parse a Json/Dict

```
// JSON.parse( data:(string/json) )
var json_str = '{"user_data": {"id": 123, "name": "mohammed"}}'
var JS = JSON.parse(json_str)
write JS.user_data.id
// 123


var json_str = dict( user_data= dict( id=123, name='mohammed' ) )
var JS = JSON.parse(json_str)
write JS.user_data.id
// 123
```
- **JSON.unParse( )** : unParse a parsed JSON

```
// JSON.unParse( data:parsed_json )
// i will use the json var that i write it up ( JS )
var un_parsed_JS = JSON.unParse( JS )
// now this var is a dict data

write get(un_parsed_JS, 'user_data')
// {'id': 123, 'name': 'mohammed'}
```
## HTTP 

**Create HTTP Requests Module**

**Step 1** : **HTTP( )** : create new session :
```
var session = HTTP()
```
**Step 2** : **.URL( )** : add URL :
```
// .URL( data:*string )
session.URL("https://api.ipify.org/")
// also it used like that
// .URL('https://example.com','path/to','page/')
```
**Step 3** : **.method( )** : choice method :
```
// .method( data:string )
session.method('get')
// Other Methods :
// GET, POST, PUT, HEAD, PATCH, DELETE, OPTIONS
```
**Step 4** : options :
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
**Step 5** : **.send( )** : send request :
```
// .send( data:dict )
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

**Use Regex to Get Data From Strings**

- **Regex( )** : call the module and set the regex code

```
// Regex( data:string )
var reg = Regex('".*?"')
```
- **Regex().isMatch( )** : if regex match string

```
// .isMatch( data:string )
var reg = Regex('mohammed')
write reg.isMatch('Hello my name is mohammed')
// True
```
- **Regex().findAll( )** : find all match

```
// .findAll( data:string )
var reg = Regex('z-[0-9]')
write reg.findAll('a-5 n-56 f-7 z-2 p-3 d-4 z-3')
// ['z-2', 'z-3']
```
- **Regex().indexStart( )\\.indexEnd()** : get the start\end of string index

```
// .indexStart( data:string )
// .indexEnd( data:string )
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

- **Regex().split( )** : split all the values

```
// .split( data:string )
var reg = Regex(',')
write reg.split('mohammed,ahmed,ali')
// ['mohammed', 'ahmed', 'ali']
```
- **Regex().split( )** : split values from (begin to `till`)

```
// .split( data:string, till=int )
var reg = Regex(',')
write reg.split('mohammed,ahmed,ali,sarah,abdallah', till=2)
// ['mohammed', 'ahmed', 'ali,sarah,abdallah']
```
- **Regex().replace( )** : replace values

```
// .replace( data:string, data:string )
var reg = Regex(',')
write reg.replace('mohammed,ahmed,ali,sarah,abdallah', ' - ')
// mohammed - ahmed - ali - sarah - abdallah
```
## System

**Dealing With The System**

- **System.argv** : get argv data

```
write System.argv
```
- **System.input( )** : get input line

```
write 'Write Any Thing :'
var any_thing = System.input()
```
- **System.write.err( )\\.out( )** : write data and errors

```
// System.write.out( data:*string )
// System.write.err( data:*string )

System.write.out('Hi there', ' , my name is mohammed')
System.write.err('Error')
```
- **System.exit( )** : exit program

```
// System.exit( data )
System.exit('program has stoped.')
```
- **System.cmd( )** : run commands

```
// System.cmd( data:string )
System.cmd('echo Hi Bro')
```
- **System.exec( )** : run commands and get output

```
// System.exec( data:string )
var cmd = System.exec('echo Hi Bro')
```
- **System.path( )** : get program path

```
write System.path()
```
- **System.informations( )** : get system informations

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

**Dealing With The Files**

- **File.Read( )** : read file

```
// File.Read( data:string, utf_8=bool )
var file = File.Read('data.txt')
// add utf_8=true in parameters to set encoding to utf-8
write file.getText()
file.end()
```
- **File.ReadBytes( )** : read bytes file

```
// File.ReadBytes( data:string )
var file = File.ReadBytes('image.png')
var data = file.get()
file.end()
```
- **File.Write( )** : write\\overwrite new file

```
// File.Write( data:string, utf_8=bool )
var file = File.Write('data.txt')
// add utf_8=true in parameters to set encoding to utf-8
file.write('data1', 'data2', 'data3')
file.end()
```
- **File.Add( )** : add data to a file

```
// File.Add( data:sring, utf_8=bool )
var file = File.Add('data.txt')
// add utf_8=true in parameters to set encoding to utf-8
file.write('data4', 'data5', 'data6')
file.end()
```
## Time

**Dealing With The Time**

- **Time.epoch( )** : get time from the epoch to now with seconds

```
Time.epoch()
```
- **Time.aEpoch( )** : get a time after epoch (use seconds)

```
// Time.aEpoch( data:string )
Time.aEpoch(0)      // Wed Dec 31 16:00:00 1969
Time.aEpoch(1000)   // Wed Dec 31 16:16:40 1969
```
- **Time.aEpoch( )** : get a time after epoch (get output as a obj)

```
// Time.aEpoch( data:string, obj=bool )
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
- **Time.now( )** : get the time now

```
write Time.now()
// Wed May 25 08:03:42 2022
```
- **Time.now( )** : get the time now (get output as a obj)

```
// Time.now( obj=bool )
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
- **Time.sleep( )** : stop the program for some seconds

```
// Time.sleep( data:(int\float) )
Time.sleep(5)  // stop for 5 sec
```
- **Time.count( )** : count time

```
var time = Time.count()
time.start()     // start counting
Time.sleep(1.5)  // make any thing
time.end()       // stop counter

write time.get   // get output
// 0:00:01.511142
```
- **Time.count( )** : count time and get output as obj

```
// Time.count( data:int )
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

**Math Functions**

Use the same functions of Python math lib (I'm not a mathematician)
```
Math.cos(1)
Math.sin(5)
Math.tan(10)
```


## Keyboard

**Dealing With Keyboard**


- **Keyboard.wait( )** : wait until the `'a'` key pressed

```
// Keyboard.wait( data:string )
Keyboard.wait('a')
```

- **Keyboard.write( )** : write somthing

```
// Keyboard.write( data:string )
Keyboard.write('github.com/kagsa/kagsa')
```

- **Keyboard.newHotkey( )** : create a new hotkey

```
// Keyboard.newHotkey( data:string , data:function )
func openGoogle () {
    System.cmd("start www.google.com")
}
Keyboard.newHotkey('ctrl + g', openGoogle)
```

-  **Keyboard.record( )** : record keys until `ESC` press

```
// Keyboard.record( until=string )
var data = Keyboard.record(until='esc')
```

- **Keyboard.record( ).get** : get data from record

```
data.get
```

- **Keyboard.record( ).playAll** : play the record

```
// .playAll( speed=(int\float)  )
data.playAll(speed=0.2) // defult speed : 0.5
```

- **Keyboard.press( )** : press some keys

```
// Keyboard.press( data:string )
Keyboard.press("ctrl + a, ctrl + c")
```

## Web
**Frontend framework for kagsa**,
You can find every thing on [kagsa/kagsa-web](http://github.com/kagsa/kagsa-web)