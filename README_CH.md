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
KAGSA 是一种基于Python的新的解释编程语言、这种语言在您的项目中是实用和可靠的、看看它的优点。

## 优势优势

- 
    <h3>轻松</h3>
        
    - **卡格萨被认为是最简单的语言之一、如果你是一个程序员不需要超过半小时才能学会它!**
        
    

- 
    <h3>允许一些禁止的事情编程</h3>
        
    - 卡格萨允许许许多其他语言禁止的东西、其中一些是:
            
        - 允许一些可变名称的符号(`@$^~?`)
            
        - 可变名字可以从数字开始
            
        
        
    


## 否定

- 
    <h3>速速速速速速速</h3>
        
    - 卡格萨是基于Python、所以它是一个有点慢、缓慢的开始时程序开始。
        
    


## 卡格萨的故事
当然、KAGSA从一开始就不是KAGSA、我想称之为 `pluscript`、文件扩展是 `.ps` 然后把它变成`.pscript`当我搜索谷歌的⁇语时、我发现两种以前的编程语言有这个名字、并决定将它改为KAGSA、但在第一版中出版。`0.1.5` 它不包含类、它包含一些愚蠢的东西、所以删除它、我们得到了新版本 `1.x.x`.
## 版本版本

- [kagsa 1.1.0](https://github.com/kagsa/kagsa/tree/1.1.0)
- [kagsa 1.0.1](https://github.com/kagsa/kagsa/tree/1.0.1)
- [kagsa 0.1.5](https://github.com/kagsa/kagsa/tree/0.1.5)

## 如何工作?
**其主要部分:**

- **Lexer** :
        
    - 它将kagsa代码翻译成包含键和值的数据:
    
    `['KEYWORD','var']`
        
    

- **Syntax Checker** :
        
    - 它检查从Lexer出来的数据的语法。
        
    

- **Parser** :
        
    - 所有数据都是Python代码
        
    

- **Compiler** :
        
    - 它完成的任务不止一项、其中最重要的任务是它准备从解析器中运行Python代码。
        
    


## 安装安装安装
### PyPi ( 所有操作系统 )
运行这个命令你的终点站

    pip install kagsa

### Windows
去吧 [最后的卡格萨释放](https://github.com/kagsa/kagsa/releases "") 并下载`kagsa-win-1.1.0.zip`收到`kagsa`文件夹到任何你想要的路径、添加这条路径到环境变量:

`This PC` &gt; `Properties` &gt; `Advanced system settings` &gt; `Environment Variables` &gt; `System variables` &gt; `Path` &gt; `New` `Ok` `Ok` `Ok`

*__<em>注:如果</em>__`kagsa`指令不是在你的CMD上运行、试着重新启动你的计算机*

化妆`.kg`文件总是打开`kagsa.exe`
### Linux
去吧[最后的卡格萨释放](https://github.com/kagsa/kagsa/releases "")并下载`kagsa-linux-1.1.0.zip`看看`readme.txt`

*__<em>注:确保你安装了</em>__`python3`.*
### Termux
下载`kagsa-termux-1.1.0.zip`阅读`readme.txt`

*__<em>注:确保你安装了</em>__`python3`.*
## 命令行使用
运行卡格萨计划

    kagsa file.kg

汇编图书馆:

    kagsa -l lib.kg -o output.kgl

检查版:

    kagsa -v
    kagsa --version

检查更新:

    kagsa -u
    kagsa --updates

帮忙:

    kagsa -h
    kagsa --help

## 实例:
### 你好世界
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

## 文件文件
您可以在 [doc](https://github.com/kagsa/kagsa/blob/main/docs/README.md "") 文件中找到所有文档
## 感谢:
- [Redmads](https://github.com/RedMads/)
- [Hereioz](https://github.com/hereioz/)
- [Spooky](https://github.com/SpookySec/)
- [Samurai Coder](https://github.com/coder-samurai/)
