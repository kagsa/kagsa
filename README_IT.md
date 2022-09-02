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

<h1 align="center" >linguaggio di programmazione KAGSA</h1>

KAGSA è un nuovo linguaggio di programmazione interpretato basato su Python, il linguaggio sarà pratico e affidabile nei vostri progetti, date un'occhiata ai suoi vantaggi.
## vantaggi

- 
    <h3>la facilità</h3>
        
    - **Kagsa è considerata una delle lingue più facili, se sei un programmatore non avrà bisogno di più di mezz'ora per impararlo!**
        
    

- 
    <h3>consentire alcune cose proibite nella programmazione</h3>
        
    - Kagsa permette molte cose che altre lingue proibiscono, alcune di loro:
            
        - Consentire alcuni simboli in nome variabile (`@$^~?`)
            
        - Il nome variabile può iniziare con il numero
            
        
        
    


## negativi

- 
    <h3>velocità</h3>
        
    - Kagsa si basa su Python, quindi è un po 'più lento, lento è all'inizio quando il programma è iniziare.
        
    


## storia di kagsa
Naturalmente, KAGSA non era KAGSA dall'inizio, stavo pensando di chiamarlo PlusScript e la sua estensione file era`.ps`e poi lo cambiò`.pscript`, quando ho cercato plusscript in Google ho trovato due precedenti linguaggi di programmazione con questo nome e ho deciso di cambiare a KAGSA , ma nella prima versione ho avuto problemi di pubblicazione su pip , è stata la prima versione con il numero`0.1.5`e non contiene lezioni e conteneva alcune cose stupide quindi è stato cancellato e abbiamo ottenuto la nuova versione`1.x.x`.
## versioni

- [kagsa 1.1.0](https://github.com/kagsa/kagsa/tree/1.1.0 "")
- [kagsa 1.0.1](https://github.com/kagsa/kagsa/tree/1.0.1 "")
- [kagsa 0.1.5](https://github.com/kagsa/kagsa/tree/0.1.5 "")

## come funziona?
**Contiene una parte principale :**

- **Lexer** :
        
    - Traduce codici kagsa in dati che contengono una chiave e un valore:`['KEYWORD','var']`
        
    

- **Controller della sintassi** :
        
    - Controlla la sintassi dei dati provenienti dalla Lexer.
        
    

- **Parser** :
        
    - Organizza tutti i dati per essere codice Python.
        
    

- **Compilatore del compilatore** :
        
    - Fa più di un compito, il più importante è che prepara tutto per eseguire codici Python uscendo dal parser.
        
    


## installazione
### PyPi (tutto os)
Eseguire questo comando il terminale :

    pip install kagsa

### Windows
Vai a[ultimo rilascio di kagsa](https://github.com/kagsa/kagsa/releases "") e scaricare`kagsa-win-1.1.0.zip`, Copia , Copia`kagsa`cartella su qualsiasi percorso che si desidera e aggiungere questo percorso alle variabili Ambiente :

`This PC` &gt; `Properties` &gt; `Advanced system settings` &gt; `Environment Variables` &gt; `System variables` &gt; `Path` &gt; `New` `Ok` `Ok` `Ok`

*__<em>Nota: se</em>__`kagsa` comando non è eseguito sul vostro CMD, provare a riavviare il computer*

Make `.kg`file sempre aperti con`kagsa.exe`
### Linux
Vai a[ultimo rilascio di kagsa](https://github.com/kagsa/kagsa/releases "") e scaricare`kagsa-linux-1.1.0.zip`, Date un'occhiata`readme.txt`

*__<em>Nota: Assicurarsi di aver installato</em>__`python3`.*
### Termux
Scarica il download Download`kagsa-termux-1.1.0.zip`, leggere , leggere`readme.txt`

*__<em>Nota: Assicurarsi di aver installato</em>__`python3`.*
## uso riga di comando
Eseguire il programma kagsa :

    kagsa file.kg

Compilare una biblioteca :

    kagsa -l lib.kg -o output.kgl

Controlla la versione :

    kagsa -v
    kagsa --version

Controllare gli aggiornamenti :

    kagsa -u
    kagsa --updates

Aiuto :

    kagsa -h
    kagsa --help

## esempi :
### ciao mondo
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
## documenti
È possibile trovare documenti completi in [docs](https://github.com/kagsa/kagsa/blob/main/docs/README.md "") cartella
## grazie a :
- [Redmads](https://github.com/RedMads/)
- [Hereioz](https://github.com/hereioz/)
- [Spooky](https://github.com/SpookySec/)
- [Samurai Coder](https://github.com/coder-samurai/)
