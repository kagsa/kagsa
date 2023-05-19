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

KAGSA является новым интерпретируемым языком программирования, основанным на языке Python. KAGSA практичен и надежен в ваших проектах, с учетом всех его преимуществ.

## Преимущества

- 
    <h3>Легкость</h3>
        
    - **Kagsa считается одним из самых простых языков программирования. Если ты программист, не потребуется больше получаса для его изучения!**
        
    

- 
    <h3>Kagsa допускает некоторые запрещенные вещи при разработке программ</h3>
        
    - Kagsa позволяет многим вещам, которые запрещены другими языками, некоторые из них:
            
        - Допускает некоторые обозначения в переменном наименовании (`@$^~?`)
            
        - Изменение названия может начинаться с номера
            
        
        
    


## Недостатки

- 
    <h3>Скорость</h3>
        
    - Kagsa основан на Python, так что он немного медленнее, при запуске программы.
        
    


## История KAGSA
Конечно, KAGSA не была KAGSA с самого начала, я думал назвать его `PlusScript`. Его расширение было `.ps` и позднее я изменил его на `.pscript`. Когда я искал plusscript в гугле, я нашел два существующих языка программирования с этим названием и решил изменить его на **KAGSA**. Первая версия, с которой у меня были проблемы с публикацией ее на pip - это версия с номером `0.1.5` и она не содержала классы и содержала несколько глупых вещей, поэтому она был исключена, и мы получили новую ветку версий `1.x.x`.
## Версии

- [kagsa 1.1.1 (Hot Fix)](https://github.com/kagsa/kagsa/tree/1.1.1)
- [kagsa 1.1.0](https://github.com/kagsa/kagsa/tree/1.1.0)
- [kagsa 1.0.1](https://github.com/kagsa/kagsa/tree/1.0.1)
- [kagsa 0.1.5](https://github.com/kagsa/kagsa/tree/0.1.5)

## Как это работает?
**Здесь содержатся основные составные части KAGSA:**

- Лексер
        
    - Лексер переводит код в данные, содержащие ключ и значение:`['KEYWORD','var']`
        
    

- Синтаксический анализатор
        
    - Он проверяет синтакс данных из лексера.
        
    

- Парсер
        
    - Собирает все данные для кода на Python.
        
    

- Компилятор
        
    - Выполняет более чем одну задачу, наиболее важной из которых является то, что он готовит все для того, чтобы запустить код на Python выходящий из парсера.
        
    


## Загрузка
### PyPi (все OS)
Запустите эту команду в терминале:

    pip install kagsa

### Windows
Зайдите в [последние релизы](https://github.com/kagsa/kagsa/releases "") и загрузите `kagsa-win-1.1.0.zip`. Затем скопируйте папку `kagsa` в путь, который потом добавите в PATH:

`This PC` &gt; `Properties` &gt; `Advanced system settings` &gt; `Environment Variables` &gt; `System variables` &gt; `Path` &gt; `New` Введите путь `Ok` `Ok` `Ok`

*__<em>Примечание:</em>__ если команда `kagsa` не запускается в вашей командной строке, попытайтесь перезагрузить ваш компьютер.*

Сделайте так, чтобы файлы формата `.kg` всегда открывались `kagsa.exe`

### Linux
Зайдите в [последние релизы](https://github.com/kagsa/kagsa/releases "") и загрузите `kagsa-linux-1.1.0.zip`. Внимательно рассмотрите `readme.txt`.

*__<em>Примечание: Убедитесь, что вы установили</em>__`python3`.*

### Termux
Загрузите `kagsa-termux-1.1.0.zip`, затем прочитайте: `readme.txt`

*__<em>Примечание: Убедитесь, что вы установили</em>__`python3`.*

## Использование в командной строке
Запустить kagsa:

    kagsa file.kg

Скомпилировать библиотеку:

    kagsa -l lib.kg -o output.kgl

Проверка версии:

    kagsa -v
    kagsa --version

Проверка обновлений:

    kagsa -u
    kagsa --updates

Помощь:

    kagsa -h
    kagsa --help

## Примеры:
### Hello World
    write 'Hello World'

### ООП
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

### Факториал
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

## Документы
Вы можете найти полные документы в папке [docs](https://github.com/kagsa/kagsa/blob/main/docs/README.md "").
## Спасибо:
- [Redmads](https://github.com/RedMads/)
- [Hereioz](https://github.com/hereioz/)
- [Spooky](https://github.com/SpookySec/)
- [Samurai Coder](https://github.com/coder-samurai/)
