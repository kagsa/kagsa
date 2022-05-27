# Kagsa Programming Language
Kagsa is an Interpreted programming language written in Python, The language works by going through four stages:
## How it Works ?
***
![Kagsa White Bord](https://raw.githubusercontent.com/kagsa/kagsa/main/kagsa-white-bord.png)
* Lexer : converts codes into data that is easy to translate and consists of a key and a value. Example: `['KEYWORD','var']`
* Syntax Checker : checks the data out of Lexer and detects syntax errors.
* Parser : translates data out of Lexer into Python code with some errors detecting.
* Compiler : Runs the final code with a special error compiler that converts Python errors into Kagsa errors.

## Usage :
### Insalltion :<br>
**Downlaod Throw Pip :**
```
pip install kagsa
```
### How to Use it :
**Run Your Program :**
```
kagsa file.kg
```
_you can choice importer file : `-m import.json`_<br><br>
**Compile a Library :**
```
kagsa -l libcodes.kg -o output.kgl
```
_you can choice importer file : `-m import.json`_<br><br>
**Check Version :**
```
kagsa -v
or
kagsa --version
```
**Check For Updates :**
```
kagsa -u
or
kagsa --updates
```
**Show Usage :**
```
kagsa -h
or
kagsa --help
```

## Examples :
***
### Hello World Program
```
write 'Hello World'
```
### Factorial Program
```
func factorial (num) {
    if num < 0 {
        write 'error'
        return ''
    }elseif num == 0 {
        return 1
    }else{
        var data = 1
        for #i -> nlist(num, zero=false) {
            var data=data * #i;
        }
        return data;
        
    }
}
write factorial(10)
```

## Thanks To :
- [Redmads](https://github.com/RedMads/) : Continued support and Help