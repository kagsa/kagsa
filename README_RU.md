<center>

<img src="https://raw.githubusercontent.com/Zaky202/kagsa/main/Logo.png" width="550"><br>
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
    
[
    ](https://mit-license.org/ "")![](https://img.shields.io/github/license/kagsa/kagsa "")[
](https://mit-license.org/ "")
[
    ](https://github.com/kagsa/kagsa/releases "")![](https://img.shields.io/github/v/release/kagsa/kagsa "")[
](https://github.com/kagsa/kagsa/releases "")
[
    ](https://pypi.org/project/kagsa "")![](https://img.shields.io/pypi/dm/kagsa "")[
](https://pypi.org/project/kagsa "")
[
    ](https://www.instagram.com/kagsa.kg "")![](https://img.shields.io/badge/Instagram-Up-blue "")[
](https://www.instagram.com/kagsa.kg "")
[
    ](https://discord.gg/q6ZmHU6DpM "")![](https://img.shields.io/badge/Discord-Up-green "")[
](https://discord.gg/q6ZmHU6DpM "")
# KAGSA Programming Language

</center>

KAGSA является новым интерпретированным программным языком, основанным на языке Python, язык будет практичным и надежным в ваших проектах, с учетом его преимуществ.
## преимущества

- 
    <h3>Легкость</h3>
        
    - **Кагса считается одним из самых простых языков, если ты программист, не потребуется больше получаса для его изучения!**
        
    

- 
    <h3>позволить некоторым запрещенным вещам при разработке программ</h3>
        
    - Kagsa позволяет многим вещам, которые запрещены другими языками, некоторые из них:
            
        - Допускает некоторые обозначения в переменном наименовании (`@$^~?`)
            
        - Изменение названия может начинаться с номера
            
        
        
    


## отрицательные последствия

- 
    <h3>скорость</h3>
        
    - Кагса основана на питоне, так что это немного медленнее, медленнее, когда начинается программа.
        
    


## История кагсы
Конечно, KAGSA не была КАГСА с самого начала, я думал назвать его `PlusScript`, а его распространение было продлево.`.ps`и позднее изменила его`.pscript`Когда я искала скидку в Гугле, я нашла два предыдущих языка программирования с этим названием и решила изменить ее до KAGSA, но в первом варианте у меня были проблемы с публикацией на трубопроводе, это первый вариант с номером`0.1.5`и он не содержал классы и содержал несколько глупых вещей, поэтому он был исключен, и мы получили новую версию`1.x.x`.
## варианты

- [kagsa 1.1.0](https://github.com/kagsa/kagsa/tree/1.1.0 "")
- [kagsa 1.0.1](https://github.com/kagsa/kagsa/tree/1.0.1 "")
- [kagsa 0.1.5](https://github.com/kagsa/kagsa/tree/0.1.5 "")

## Как это работает?
**Он содержит основные части:**

- Lexer
        
    - Он переводит коды кагсы в данные, содержащие ключ и значение:`['KEYWORD','var']`
        
    

- Syntax checker
        
    - Он проверяет синтакс данных из Лексера.
        
    

- Parser
        
    - Собирает все данные для кода Питона.
        
    

- Compiler
        
    - Она выполняет более чем одну задачу, наиболее важной из которых является то, что она готовит все для того, чтобы запустить коды Питона из прихода.
        
    


## Скачать
### PyPi (все ос)
Управляй этим командованием свой терминал:

    pip install kagsa

### Windows
Иди [Последний выброс кагсы](https://github.com/kagsa/kagsa/releases "")и загрузка`kagsa-win-1.1.0.zip`Принято.`kagsa`Обратите внимание на любой путь, который вы хотите, и добавите этот путь к изменениям окружающей среды:

`This PC` &gt; `Properties` &gt; `Advanced system settings` &gt; `Environment Variables` &gt; `System variables` &gt; `Path` &gt; `New` Введите путь `Ok` `Ok` `Ok`

*__<em>Примечание: если</em>__`kagsa`Команда не бежит к вашему компьютеру, попытается снова открыть тебе компьютер.*

Дела`.kg`файлы всегда открыты`kagsa.exe`
### Linux
Иди[Последний выброс кагсы](https://github.com/kagsa/kagsa/releases "")и загрузка`kagsa-linux-1.1.0.zip`Посмотри`readme.txt`

*__<em>Примечание: Убедитесь, что вы установили</em>__`python3`.*
### Termux
Загрузка`kagsa-termux-1.1.0.zip`, читать:`readme.txt`

*__<em>Примечание: Убедитесь, что вы установили</em>__`python3`.*
## Использование командной линии
Программа для кагсы:

    kagsa file.kg

сделать библиотеку:

    kagsa -l lib.kg -o output.kgl

Версия:

    kagsa -v
    kagsa --version

Проверка обновлений:

    kagsa -u
    kagsa --updates

Помогите:

    kagsa -h
    kagsa --help

## примеры:
### Привет.
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

### Фактор
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
Вы можете найти полные документы. [docs](https://github.com/kagsa/kagsa/blob/main/docs/README.md "") folder
## Благодаря:
- [Redmads](https://github.com/RedMads/)
- [Hereioz](https://github.com/hereioz/)
- [Spooky](https://github.com/SpookySec/)
- [Samurai Coder](https://github.com/coder-samurai/)