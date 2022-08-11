# Dict in Kagsa
dict is datatype like JSON, its used to saved a data within `key` and `value`
## Examples :
***
```
var users = dict(admin="password123")

add(users, 'ahmed' , 'mypass734')
add(users, 'ali' , 'asd12345')
add(users, 'aslooj' , 'pass321')

write 'Aslooj Password is : ' + get(users, 'aslooj')
```
## Methods :
***
Methods is a group of functions that help you to edit in any variable.
```
var dct = dict(name='mohammed')

// change dict to str
write toStr(dct)
// output : {'name':'mohammed'}

// get length
write length(dct)
// output : 1

// get value by key
write get(dct, 'name')
// output : mohammed

// add data to dict
append(dct,'age', 1000)
// dict will be : {'name':'mohammed', 'age':1000}

// clear everythings
clear(dct)
// dict will be : {}

// add data to dict
add(dct, 'name', 'mhmd')
add(dct, 'age', 100)
add(dct, 'job', 'student')
add(dct, 'github', 'kagsa')
// dict will be : {'name':'mhmd','age':100,'job':'student','github':'kagsa'}

// delete data
delete(dct, 'age')
// dict will be : {'name':'mhmd','job':'student','github':'kagsa'}

// get all keys as a list
write keys(dct)
// output : ['name','job','github']

// get all values as a list
write values(dct)
// output : ['mhmd','student','kagsa']
```
## Loop with Dict :
### Example :
```
var dict_var = dict(name='zaky',age=100)
for ii -> keys(dict_var){
    write 'key :',ii,'  value :',get(dict_var,ii),nl
}
// This will Print Every Thing
```
## Dict & JSON
You can use dict data as json :<br>
Change from dict to Json String :
```
var dct = dict( user_data= dict( id=123, name='mohammed' ) )
var json = JSON.toJson(dct)
write json;
// {"user_data": {"id": 123, "name": "mohammed"}}
```
Read Json String
```
var json_str = '{"user_data": {"id": 123, "name": "mohammed"}}'
var out = JSON.toDict(json_str)
// out is a Dict Data
```
Parse a Json/Dict
```
var json_str = '{"user_data": {"id": 123, "name": "mohammed"}}'
// you can use this -> dict( user_data= dict( id=123, name='mohammed' ) )
var JS = JSON.parse(json_str)
write JS.user_data.id
// 123
```
UnParse a Parsed JSON
```
// i will use the json var that i write it up ( JS )
var un_parsed_JS = JSON.unParse( JS )
// now this var is a dict data

write get(un_parsed_JS, 'user_data')
// {'id': 123, 'name': 'mohammed'}
```