# 💻 PyLocalHost

قمنا بإنشاء هذا البرنامج ليكون حلا لمشكلة يعاني منها المحاضرين الذين يرغبون في مشاركة الملفات بين الطلبة. جرت العادة باستخدام اجهزة التخزين الخارجية في نقل الملفات بين الطلبة والذي بدورة يعد غير آمن غير انه يأخذ وقت أطول في النقل. لذلك جاء هذا البرنامج ليحل هذه المشكلة وذلك عن طريق استخدام بروتوكول HTTP  في نقل الملفات في نفس الشبكة.


## كيف يعمل البرنامج ؟ 

يقوم البرنامج بتحويل جهازك إلى موقع ويب ثم يسمح للجهزة المتصلة في نفس الشبكة بالوصول إلى التطبيق


# المتطلبات
يعتمد هذا البرنامج على لغة البايثون 🐍 لذلك يجب تنصيب اللغة في الجهاز قبل البدا بعملية التنصيب.

يمكن لك تنصيب البايثون عن طريق هذا الربط https://www.python.org/downloads/
# التنصيب
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
