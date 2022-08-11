# Classes in Kagsa
class is something like a function store, often used in libraries or in OOP.
## Example :
```
class app {
    func say (text) {
        write 'App : %{text}\n'
    }
    func close () {
        System.exit('')
    }
}

app.say('Hello')
app.say('This is my App')
app.say('This app use the OOP')

app.close()
```
### output :
```
App : Hello
App : This is my App      
App : This app use the OOP
```

## Constructor function :
constructor func is the main function in the class, to be clear, take a look at this example.
### Example :
```
class App {
    func @constructor (@this) {
        write 'Welcome To App\n'
        var @this.num = 0
    }
    func addOne (@this) {
        @this.num+=1
    }
    func takeOne (@this) {
        @this.num-=1
    }
}

var game = App()
game.addOne()
game.addOne()
game.addOne()
game.takeOne()

write game.num
```
### output :
```
Welcome To App
2
```
To be clear, the constructor function is like a session, so if you use it this way:
```
var game1 = App()
game1.addOne()
game1.addOne()
game1.addOne()
game1.takeOne()

var game2 = App()
game2.addOne()
game2.addOne()
game2.addOne()
game2.takeOne()
```
Unlike the first example, `game1` will be different and independent of `game2` and you can find many benefits yourselves.


**Ok good, but what does `@this` mean?**<br>
It is a variable that can be used within classes. It has several benefits, including:
- The ability to manipulate its variables (ex: `@this.num`) from within all functions in the class.
- It can also be used to use variables outside the class

## Repr function :
It is just a function that gives a value to the class, so that if you print the class, this value will printed.
### Example :
```
class Man {
    func @constructor (@this,name,age){
        string @this.name = name
        int @this.age = age
    }
    func @repr (@this){
        string name = @this.name
        int age  = @this.age
        return '<Man Class name="%{name}" age=%{age}>'
    }
}

write Man('mohammed',14) 
// <Man Class name="mohammed" age=14>
```
# String function :
It works in the same way as the repr function, but the value written in the (return) must be string.

**Note: If you find a `@string` function in the class, the `@repr` will be ignored.**