# Dict in Kagsa
dict is datatype like JSON, its used to saved a data within `key` and `value`

## Examples :

```
var users = dict(admin="password123")

add(users, 'ahmed' , 'mypass734')
add(users, 'ali' , 'asd12345')
add(users, 'aslooj' , 'pass321')

write 'Aslooj Password is : ' + get(users, 'aslooj')
```
## Methods :

Methods is a group of functions that help you to edit in any variable.

- **dict( )** : create dict

```
var dct = dict(name='mohammed')
```

- **toStr( )** : change dict to str

```
write toStr(dct)
// output : {'name':'mohammed'}
```

- **length( )** : get length

```
write dct.length()
// or
write length(dct)
// output : 1
```

- **get( )** : get value by key

```
write dct.get('name')
// or
write get(dct, 'name')
// output : mohammed
```

- **append( )** : add data to dict

```
dct.append(age,1000)
// or
append(dct,'age', 1000)
// dict will be : {'name':'mohammed', 'age':1000}
```

- **clear( )** : clear everythings

```
dct.clear()
// or
clear(dct)
// dict will be : {}
```
- **add( )** : add data to dict

```
dct.add('name','mhmd')
// or
add(dct, 'age', 100)
add(dct, 'job', 'student')
add(dct, 'github', 'kagsa')
// dict will be : {'name':'mhmd','age':100,'job':'student','github':'kagsa'}
```
- **delete( )** : delete data

```
dct.delete('age')
// or
delete(dct, 'age')
// dict will be : {'name':'mhmd','job':'student','github':'kagsa'}
```

- **keys( )** : get all keys as a list

```
write dct.keys()
// or
write keys(dct)
// output : ['name','job','github']
```

- **values( )** : get all values as a list

```
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