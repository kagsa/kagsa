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



KAGSA は、Python に基づく新しい解釈型プログラミング言語です。この言語は、プロジェクトで実用的で信頼性が高くなります。その利点をご覧ください。
## 利点
- ### 容易さ
    - **Kagsa** は最も簡単な言語の 1 つと考えられています。プログラマーであれば、学習に 30 分以上は必要ありません。 :)
- ### プログラミングで禁止されていることを許可する
    - Kagsa では、他の言語で禁止されている多くのことが許可されています。
        - 変数名に一部の記号を許可する (@$^~?)
        - 変数名は数字で始めることができます

## ネガ
- ### スピード
    - Kagsa は Python をベースにしているので少し遅く、プログラムを起動した当初は遅いです。

## Kagsa 物語
もちろん、KAGSA は最初から KAGSA ではありませんでした。私はそれを `PlusScript` と呼ぶことを考えていました。そのファイル拡張子は `.ps` で、後で `.pscript` に変更しました。Google で `plusscript` を検索すると、この名前の以前のプログラミング言語が 2 つ見つかりました。 KAGSA に変更することにしましたが、最初のバージョンで pip での公開に問題があり、番号が `0.1.5` の最初のバージョンであり、クラスが含まれておらず、いくつかの愚かなものが含まれていたため、削除され、新しいものを取得しました バージョン `1.x.x`.

## バージョン
- [kagsa 1.1.1 (Hot Fix)](https://github.com/kagsa/kagsa/tree/1.1.1)
- [kagsa 1.1.0](https://github.com/kagsa/kagsa/tree/1.1.0)
- [kagsa 1.0.1](https://github.com/kagsa/kagsa/tree/1.0.1)
- [kagsa 0.1.5](https://github.com/kagsa/kagsa/tree/0.1.5)

## それはどのように実行されますか？
**それは主要な部品を含んでいます**:

* **Lexer**
    - これは、kagsa コードをキーと値を含むデータに変換します。
    
    `['KEYWORD','var']`
* **Syntax Checker**
    - レクサーから出力されるデータの構文をチェックします。
* **Parser**
    - すべてのデータを Python コードに配置します。
* **Compiler**
    - 複数のタスクを実行しますが、その中で最も重要なのは、パーサーから出てくる Python コードを実行するためのすべてを準備することです。

## ダウンロード
### PyPi ( すべての OS )
このコマンドを端末で実行します :
```
pip install kagsa
```
### Windows

に行く [last kagsa releases](https://github.com/kagsa/kagsa/releases) `kagsa-win-1.1.0.zip` をダウンロードし、`kagsa` フォルダーを任意のパスにコピーし、このパスを環境変数に追加します。

`This PC` > `Properties` > `Advanced system settings` > `Environment Variables` > `System variables` > `Path` > `New` > Paste The Path > `Ok` > `Ok` > `Ok`

_**注** : CMD で `kagsa` コマンドが実行されていない場合は、コンピューターを再起動してみてください_

`.kg` ファイルを常に `kagsa.exe` で開くようにする

### Linux
に行く [last kagsa releases](https://github.com/kagsa/kagsa/releases) `kagsa-linux-1.1.0.zip` をダウンロードし、`readme.txt` を見てください。

_**注** : `python3` がインストールされていることを確認してください。

### Termux
に行く [last kagsa releases](https://github.com/kagsa/kagsa/releases) `kagsa-termux-1.1.0.zip` をダウンロードし、`readme.txt` を見てください。

_**注** : `python3` がインストールされていることを確認してください。

## コマンドラインの使用法
kagsa プログラムを実行します。:
```
kagsa file.kg
```
ライブラリをコンパイルします:
```
kagsa -l lib.kg -o output.kgl
```
バージョンの確認 :
```
kagsa -v
kagsa --version
```
アップデートを確認 ：
```
kagsa -u
kagsa --updates
```
ヘルプ ：
```
kagsa -h
kagsa --help
```

## 例 :
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

## ドキュメント
[docs](https://github.com/kagsa/kagsa/blob/main/docs/README.md) フォルダで完全なドキュメントを見つけることができます

## ありがとう:
- [Redmads](https://github.com/RedMads/)
- [Hereioz](https://github.com/hereioz/)
- [Spooky](https://github.com/SpookySec/)
- [Samurai Coder](https://github.com/coder-samurai/)
