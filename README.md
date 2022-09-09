<p align="center" >
    <br>
    <img src="https://raw.githubusercontent.com/Zaky202/kagsa/main/Logo.png" width="550">
    
<br>    
    
<a href="https://github.com/kagsa/kagsa/blob/main/README.md">
    English
</a>-
<a href="https://github.com/kagsa/kagsa/blob/main/README_AR.md">
    عربي
</a>-
<a href="https://github.com/kagsa/kagsa/blob/main/README_RU.md">
    русский
</a>-
<a href="https://github.com/kagsa/kagsa/blob/main/README_JP.md">
    日本語
</a>-
<a href="https://github.com/kagsa/kagsa/blob/main/README_CH.md">
    官话
</a><br>
<a href="https://github.com/kagsa/kagsa/blob/main/README_SP.md">
    español
</a>-
<a href="https://github.com/kagsa/kagsa/blob/main/README_IN.md">
    हिंदी
</a>-
<a href="https://github.com/kagsa/kagsa/blob/main/README_IT.md">
    italiano
</a><br><br>
    

<a href="https://mit-license.org/" >
    <img src="https://img.shields.io/github/license/kagsa/kagsa">
</a>
<a href="https://github.com/kagsa/kagsa/releases" >
    <img src="https://img.shields.io/github/v/release/kagsa/kagsa">
</a>
<a href="https://pypi.org/project/kagsa">
    <img src="https://img.shields.io/pypi/dm/kagsa">
</a>
<a href="https://www.instagram.com/kagsa.kg">
    <img src="https://img.shields.io/badge/Instagram-Up-blue">
</a>
<a href="https://discord.gg/q6ZmHU6DpM">
    <img src="https://img.shields.io/badge/Discord-Up-green">
</a>

</p>
<h1 align="center" >KAGSA Programming Language</h1>



KAGSA is a new Interpreted programming language based on Python, the language will be practical and reliable in your projects, take a look at its advantages.
## Advantages
- ### The Ease
    - **Kagsa** is considered one of the most easy languages, if you are a programmer will not need more than half an hour to learn it !! :)
- ### Allow some forbidden things in programming
    - Kagsa allows many things that other languages prohibit, some of them :
        - Allow some symbols in variable name (`@$^~?`)
        - Variable name can start with number

## Negatives
- ### Speed
    - Kagsa is based on Python, so it is a little slower, slow is at the beginning when the program is start.

## Kagsa Story
Of course, **KAGSA** was not **KAGSA** from the beginning, I was thinking of calling it **PlusScript** and its file extension was `.ps` and later changed it to `.pscript`, when I searched for plusscript in Google I found two previous programming languages with this name and decided to change it to **KAGSA** , but in The first version I had problems publishing on pip, was the first version with the number `0.1.5` and it did not contain classes and it contained some stupid things so it was deleted and we got the new version `1.x.x`.     

## Versions
- [kagsa 1.1.1 (Hot Fix)](https://github.com/kagsa/kagsa/tree/1.1.1)
- [kagsa 1.1.0](https://github.com/kagsa/kagsa/tree/1.1.0)
- [kagsa 1.0.1](https://github.com/kagsa/kagsa/tree/1.0.1)
- [kagsa 0.1.5](https://github.com/kagsa/kagsa/tree/0.1.5)

## How it Works ?
**It contains a main parts** :
* **Lexer**
    - It translates kagsa codes into data that contains a key and a value : `['KEYWORD','var']`
* **Syntax Checker**
    - It checks the syntax of the data coming out of the Lexer.
* **Parser**
    - Arranges all data to be Python code.
* **Compiler**
    - It does more than one task, the most important of which is that it prepares everything to run Python codes coming out of the parser.

## Installation
### PyPi ( All OS )
Run this command your terminal :
```
pip install kagsa
```
### Windows

Go to [last kagsa releases](https://github.com/kagsa/kagsa/releases) and download `kagsa-win-1.1.0.zip`, Copy `kagsa` folder to any path you want and add this path to Environment Variables :

`This PC` > `Properties` > `Advanced system settings` > `Environment Variables` > `System variables` > `Path` > `New` > Paste The Path > `Ok` > `Ok` > `Ok`

_**Note** : if `kagsa` command isn't run on your CMD, try to restart you computer_

Make `.kg` files always open with `kagsa.exe`

### Linux
Go to [last kagsa releases](https://github.com/kagsa/kagsa/releases) and download `kagsa-linux-1.1.0.zip`, Take a look at `readme.txt`

_**Note** : Make sure you have installed `python3`._

### Termux
Download `kagsa-termux-1.1.0.zip`, read `readme.txt`

_**Note** : Make sure you have installed `python3`._

## Command Line Usage
Run kagsa program :
```
kagsa file.kg
```
Compile a library :
```
kagsa -l lib.kg -o output.kgl
```
Check version :
```
kagsa -v
kagsa --version
```
Check for updates :
```
kagsa -u
kagsa --updates
```
Help :
```
kagsa -h
kagsa --help
```

## Examples :
### Hello World
```
write 'Hello World'
```
### OOP
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
### Factorial
```
func factorial (num) {
    if num < 0 {
        write 'error'
        return ''
    }elseif num == 0 {
        return 1
    }else{
        var data = 1
        for i -> nlist(num, zero=false) {
            var data=data * i;
        }
        return data;
        
    }
}
write factorial(10)
```
## Documents
You can find full documents in [docs](https://github.com/kagsa/kagsa/blob/main/docs/README.md) folder
## Thanks To :
- [Redmads](https://github.com/RedMads/)
- [Hereioz](https://github.com/hereioz/)
- [Spooky](https://github.com/SpookySec/)
- [Samurai Coder](https://github.com/coder-samurai/)
