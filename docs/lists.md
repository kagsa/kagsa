# List is Kagsa
lists is one of datatypes, its somthing like memory for any data.
## Example :

```
// make a new list
var users = list()

users.append('mohammed')
users.append('ali')
users.append('aslooj')
users.append('ahmed')
users.append('awad')

write users;
// output :
// ['mohammed', 'ali', 'aslooj', 'ahmed', 'awad']
```

## Methods :

Methods is a group of functions that help you to edit in any variable.

- **list( )** : create new list

```
var LIST = list(1,2,3)
```
- **toStr( )** : convert from list to str

```
write toStr(LIST)
// output : '[1, 2, 3]'
```
- **length( )** : length of the list

```
write LIST.length()
// or
write length(LIST)
// output : 3
```
- **get( )** : get a index from list

```
write LIST.get(0)
// or
write get(LIST,0)
// output : 1
```

- **get( )** : get from index to another

```
write LIST.get(0,2)
// or
write get(LIST,0,2)
// output : [1, 2]
```

- **clear( )** : clear the list

```
LIST.clear()
// or
clear(LIST)
// the list will be : []
```

- **append( )** : add a item to list

```
LIST.append('a')
// or
append(LIST,'b')
append(LIST,'b')
append(LIST,'c')
// the list will be : ['a', 'b', 'b', 'c']
```

- **delete( )** : delete item throw index

```
delete(LIST,0,idx=true)
// or
LIST.delete(0,idx=true)
// the list will be : ['b', 'b', 'c']
```
- **delete( )** : delete item by name

```
delete(LIST, 'b')
// or
LIST.delete('b')
// the list will be : ['c']
```

- **add( )** : add\edit items throw index

```
LIST.add(0, 'b')
// or
add(LIST, 0, 'a')
add(LIST, 0, '0')
// the list will be : ['0', 'a', 'b', 'c']
```

- **index( )** : search for a item

```
write LIST.index('c')
// or
write index(LIST,'c')
// output : 4
```

- **applist( )** : add a items of list to another list

```
var lst2 = list('d','e','f')
applist(LIST, lst2)
// or
LIST.applist(lst2)
// the list will be : ['0', 'a', 'b', 'c', 'd', 'e', 'f']
```

- **count( )** : count a item in the list

```
write LIST.count('0')
// or
write count(LIST, '0')
// output : 1
```
- **join( )** : join all list items

```
write LIST.join('-')
write join(LIST, '-')
// output : 0-a-b-c-d-e-f
```
## Loop with List :

### Example :
```
var list_var = list(45245,454,5554,45,2345,43)
for ii -> list_var{
    write ii,nl
}
// This will Print Every Thing
```