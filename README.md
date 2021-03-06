# 💻 PyLocalHost
[![image](https://img.shields.io/pypi/pyversions/pipenv.svg)](https://www.python.org/downloads/) 
[![image](https://img.shields.io/pypi/v/flask?label=FLASK)](https://github.com/pallets/flask) 
[![image](https://img.shields.io/pypi/l/pipenv.svg)](LICENSE)

------------------------------------------------------------------------

### السلام عليكم ورحمة الله وبركاته

مرحبا بك في مشروعي الأول في عالم الـ Open source لقد أطلقت على هذا البرنامج اسم PyLocalHost. الهدف من إنشاء هذا البرنامج هو لحل مشكلة يعاني منها الكثيرون وهي في الطريقة التي يقوم بها المحاضر في نقل ملف او مجموعة من الملفات بين الطلبة. أتذكر جيدا هذه المشكلة وانا على مقاعد الدراسة أتذكر كيف يستغرق الامر وقتا طويلا.

### ماهو PyLocaLHost ؟

هو عبارة عن تطبيق ويب لنقل الملفات بين مجموعة من المستخدمين في نفس الشبكة وذلك عن طريق استخدام بروتوكول HTTP.

## كيف يعمل البرنامج ؟ 

يقوم البرنامج بتحويل جهازك إلى موقع ويب ثم يسمح للجهزة المتصلة في نفس الشبكة بالوصول إلى التطبيق


# المتطلبات
يعتمد هذا البرنامج على لغة البايثون 🐍 لذلك يجب تنصيب اللغة في الجهاز قبل البدا بعملية التنصيب.

يمكن لك تنصيب البايثون عن طريق هذا الربط https://www.python.org/downloads/
# التنصيب
بعد تحميل الملف, قم بفك ضغط الملف ثم ادخل عليه وفتح نافذة cmd 

الخطوة الاولى: إنشاء بيئة افتراضية للبرنامج

```bash
 python -m venv venv
```

الخطوة الثانية: تفعيل البيئة الافتراضية

```bash
venv\Scripts\activate.bat 
```

الخطوة الثالثة: تنصيب المكتبات الخاصة بالبرنامج

```bash
pip install -r requirements.txt
```

# تشغيل البرنامج

```bash
python app.py
```

![me](https://github.com/mohammed-aladi/PyLocalHost/blob/master/static/img/pylocalhost.gif)


## بعد تشغيل البرنامج, الخطوة الاولى إنشاء كلمة مرور

سوف يطلب منك إنشاء كلمة مرور لصفحة المستفيدين. لن يستطيع أي زائر من الوصول إلى الملفات بدون إدخال كلمة المرور.

![me](https://github.com/mohammed-aladi/PyLocalHost/blob/master/static/img/1.PNG)


## الخطوة الثانية رفع ملف

![me](https://github.com/mohammed-aladi/PyLocalHost/blob/master/static/img/website.gif)

# معلومات الاتصال

عنوان البرنامج مع كلمة المرور سوف تظهر في صفحة الادمن

![me](https://github.com/mohammed-aladi/PyLocalHost/blob/master/static/img/2.PNG)


# رخصة الاستخدام

[MIT License](LICENSE)
