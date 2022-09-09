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

KAGSA هي لغة برمجة مترجمة جديدة تعتمد على Python ، ستكون اللغة عملية وموثوقة في مشاريعك ، ألق نظرة على مزاياها.

## مزايا

- ### السهولة
  - تعتبر **Kagsa** من أسهل اللغات ، فإذا كنت مبرمجًا فلن تحتاج إلى أكثر من نصف ساعة لتتعلمها !! :)
- ### السماح ببعض الممنوعات في البرمجة
  -   يسمح Kagsa بالعديد من الأشياء التي تحظرها اللغات الأخرى ، بعضها:

      - السماح ببعض الرموز في اسم المتغير ( `@$^~?` )
      - يمكن أن يبدأ اسم المتغير برقم

## السلبيات

- ### سرعة
  - يعتمد Kagsa على Python ، لذا فهو أبطأ قليلاً ، ويكون بطيئًا في البداية عند بدء تشغيل البرنامج.

## قصة كاجسا

بالطبع ، **KAGSA** لم تكن **KAGSA** منذ البداية ، كنت أفكر في تسميتها **PlusScript وامتداد** ملفها كان `.ps` ثم قمت بتغييره لاحقًا إلى `.pscript` ، عندما بحثت عن plusscript في Google وجدت لغتي برمجة سابقتين بهذا الاسم و قررت تغييره إلى **KAGSA** ، ولكن في الإصدار الأول واجهت مشاكل في النشر على Pip ، كانت النسخة الأولى برقم `0.1.5` ولا تحتوي على فئات وتحتوي على بعض الأشياء الغبية لذا تم حذفها وحصلنا على الجديد الإصدار `1.xx`

## إصدارات
- [kagsa 1.1.1 (Hot Fix)](https://github.com/kagsa/kagsa/tree/1.1.1)
- [kagsa 1.1.0](https://github.com/kagsa/kagsa/tree/1.1.0)
- [kagsa 1.0.1](https://github.com/kagsa/kagsa/tree/1.0.1)
- [kagsa 0.1.5](https://github.com/kagsa/kagsa/tree/0.1.5)

## كيف تعمل ؟

**يحتوي على أجزاء رئيسية** :

- **ليكسر**
  - يترجم رموز kagsa إلى بيانات تحتوي على مفتاح وقيمة: `['KEYWORD','var']`
- **مدقق النحو**
  - يتحقق من بناء جملة البيانات الصادرة من Lexer.
- **محلل**
  - يرتب جميع البيانات لتكون كود Python.
- **مترجم**
  - يقوم بأكثر من مهمة ، أهمها أنه يعد كل شيء لتشغيل أكواد Python الصادرة من المحلل اللغوي.

## التنصيب

### PyPi (جميع أنظمة التشغيل)

شغّل هذا الأمر على جهازك :

    pip install kagsa

### وندوز

انتقل إلى [إصدارات kagsa الأخيرة وقم](https://github.com/kagsa/kagsa/releases) بتنزيل `kagsa-win-1.1.0.zip` ، وانسخ مجلد `kagsa` إلى أي مسار تريده وأضف هذا المسار إلى متغيرات البيئة:

`This PC` > `Properties` > `Advanced system settings` > `Environment Variables` `System variables` > `Path` > `New` > لصق المسار> `Ok` > `Ok` > `Ok`

_**ملاحظة** : إذا لم يتم تشغيل أمر `kagsa` على CMD ، فحاول إعادة تشغيل جهاز الكمبيوتر_

اجعل ملفات `.kg` مفتوحة دائمًا باستخدام `kagsa.exe`

### لينكس

انتقل إلى [إصدارات kagsa الأخيرة وقم](https://github.com/kagsa/kagsa/releases) بتنزيل `kagsa-linux-1.1.0.zip` ، ألق نظرة على `readme.txt`

_**ملاحظة** : تأكد من تثبيت `python3` ._

### ترموكس

قم بتنزيل `kagsa-termux-1.1.0.zip` ، واقرأ `readme.txt`

_**ملاحظة** : تأكد من تثبيت `python3` ._

## استخدام سطر الأوامر

قم بتشغيل برنامج kagsa:

    kagsa file.kg

تجميع مكتبة:

    kagsa -l lib.kg -o output.kgl

الاصدار الحالي:

    kagsa -v
    kagsa --version

تحقق من وجود تحديثات :

    kagsa -u
    kagsa --updates

مساعدة :

    kagsa -h
    kagsa --help

## أمثلة :

### مرحبا بالعالم

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

### المضروب الحسابي
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

## وثائق

يمكنك العثور على المستندات الكاملة في مجلد [المستندات](https://github.com/kagsa/kagsa/blob/main/docs/README.md)

## شكرا ل:
- [Redmads](https://github.com/RedMads/)
- [Hereioz](https://github.com/hereioz/)
- [Spooky](https://github.com/SpookySec/)
- [Samurai Coder](https://github.com/coder-samurai/)
