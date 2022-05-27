# List is Kagsa
lists is one of datatypes it like memory for a data.
## Example :
***
```
// make a new list
var users = list()

append(users, 'mohammed')
append(users, 'ali')
append(users, 'aslooj')
append(users, 'ahmed')
append(users, 'awad')

write users;
// output :
// ['mohammed', 'ali', 'aslooj', 'ahmed', 'awad']
```

## Methods :
***
Methods is a group of functions that help you to edit in any variable.
```

var LIST = list(1,2,3)
// change from list to str
write toStr(LIST)
// output : '[1, 2, 3]'

// length of the list
write length(LIST)
// output : 3

// get a index from list
write get(LIST,0)
// output : 1

// get from index to another
write get(LIST,0,2)
// output : [1, 2]

// clear the list
clear(LIST)
// the list will be : []

// add a item to list
append(LIST,'a')
append(LIST,'b')
append(LIST,'b')
append(LIST,'c')
// the list will be : ['a', 'b', 'b', 'c']

// delete item throw index
delete(LIST,0,idx=true)
// the list will be : ['b', 'b', 'c']

// delete item by name
delete(LIST, 'b')
// the list will be : ['c']

// add\edit items throw index 
add(LIST, 0, 'b')
add(LIST, 0, 'a')
add(LIST, 0, '0')
// the list will be : ['0', 'a', 'b', 'c']

// search for a item
write index(LIST,'c')
// output : 4

// add a items of list to another list
var lst2 = list('d','e','f')
applist(LIST, lst2)
// the list will be : ['0', 'a', 'b', 'c', 'd', 'e', 'f']

// count a item in the list
write count(LIST, '0')
// output : 1

// join all list items
write join(LIST, '-')
// output : 0-a-b-c-d-e-f
```
## Loop with List :
***
### Example :
```
var list_var = list(45245,454,5554,45,2345,43)
for ii -> list_var{
    write ii,nl
}
// This will Print Every Thing
```