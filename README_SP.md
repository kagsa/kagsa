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

KAGSA es un nuevo idioma de programación interpretado basado en Python, el idioma será práctico y fiable en sus proyectos, echa un vistazo a sus ventajas.
## ventajas

- 
    <h3>fácil</h3>
        
    - **Kagsa se considera uno de los idiomas más fáciles, si eres un programador no necesitará más de media hora para aprenderlo!**
        
    

- 
    <h3>permitir algunas cosas prohibidas en la programación</h3>
        
    - Kagsa permite muchas cosas que otros idiomas prohíben, algunas de ellas:
            
        - Permitir algunos símbolos en nombre variable (`@$^~?`)
            
        - El nombre variable puede empezar con el número
            
        
        
    


## negativos

- 
    <h3>velocidad de velocidad</h3>
        
    - Kagsa se basa en Python, así que es un poco más lento, es lento al principio cuando el programa está empezando.
        
    


## historia de Kagsa
Por supuesto, KAGSA no fue KAGSA desde el principio, estaba pensando en llamarlo PlusScript y su extensión de archivo fue`.ps` y más tarde lo cambió`.pscript`, cuando busqué el plusscript en Google encontré dos idiomas anteriores de programación con este nombre y decidí cambiarlo a KAGSA , pero en la primera versión tuve problemas para publicar en pip, fue la primera versión con el número`0.1.5` y no contenía clases y contenía algunas cosas estúpidas así que fue borrado y conseguimos la nueva versión`1.x.x`.
## versiones
- [kagsa 1.1.0](https://github.com/kagsa/kagsa/tree/1.1.0 "")
- [kagsa 1.0.1](https://github.com/kagsa/kagsa/tree/1.0.1 "")
- [kagsa 0.1.5](https://github.com/kagsa/kagsa/tree/0.1.5 "")

## ¿Cómo funciona?
**Contiene partes principales:**

- **Lexer** :
        
    - Se traduce códigos kagsa en datos que contienen una clave y un valor:`['KEYWORD','var']`
        
    

- **Syntax Checker** :
        
    - Comprueba la sintaxis de los datos que salen del Lexer.
        
    

- **Parser** :
        
    - Arregla todos los datos para ser código Python.
        
    

- **Compiler** :
        
    - Hace más de una tarea, la más importante de la cual es que prepara todo para ejecutar códigos Python saliendo del parser.
        
    


## instalación de instalación
### PyPi ( Todos los sistemas operativos )
Dirija este comando su terminal:

    pip install kagsa

### Windows
Ir a ir[último lanzamiento de kagsa](https://github.com/kagsa/kagsa/releases "") y descarga`kagsa-win-1.1.0.zip`, Copiado ,`kagsa`carpeta a cualquier camino que quieras y añade este camino a las variables ambientales:

`This PC` &gt; `Properties` &gt; `Advanced system settings` &gt; `Environment Variables` &gt; `System variables` &gt; `Path` &gt; `New` `Ok` `Ok` `Ok`

*__<em>Nota : si</em>__`kagsa`El comando no se ejecuta en su CMD, tratar de reiniciar la computadora*

Hacerlo hacer`.kg`archivos siempre abiertos con`kagsa.exe`
### Linux
Ir a ir[último lanzamiento de kagsa](https://github.com/kagsa/kagsa/releases "")y descarga`kagsa-linux-1.1.0.zip`, Echa un vistazo`readme.txt`

*__<em>Nota : Asegúrese de haber instalado</em>__`python3`.*
### Termux
Descargar Descargar Descargar Descargar`kagsa-termux-1.1.0.zip`, leer ,`readme.txt`

*__<em>Nota : Asegúrese de haber instalado</em>__`python3`.*
## uso de la línea de mando
Ejecutar programa de kagsa:

    kagsa file.kg

Compilar una biblioteca:

    kagsa -l lib.kg -o output.kgl

Ver versión :

    kagsa -v
    kagsa --version

Compruebe las actualizaciones :

    kagsa -u
    kagsa --updates

Ayuda :

    kagsa -h
    kagsa --help

## ejemplos:
### Hola mundo
    write 'Hello World'

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

### factorial
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

## documentos
Puede encontrar documentos completos en [Docs](https://github.com/kagsa/kagsa/blob/main/docs/README.md "") de la carpeta
## gracias a:
- [Redmads](https://github.com/RedMads/)
- [Hereioz](https://github.com/hereioz/)
- [Spooky](https://github.com/SpookySec/)
- [Samurai Coder](https://github.com/coder-samurai/)
