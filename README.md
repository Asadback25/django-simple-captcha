# 🛡️ Django Simple CAPTCHA Integration

Bu loyiha **Django** ilovasida spam va botlardan himoya qilish uchun `django-simple-captcha` paketini qanday o‘rnatish va ishlatishni ko‘rsatadi.

---

## 📦 O‘rnatish

```bash
pip install django-simple-captcha
```

---

## ⚙️ Sozlash (settings.py)

`INSTALLED_APPS` ga qo‘shing:

```python
INSTALLED_APPS = [
    ...
    'captcha',
]
```

Migratsiya qiling:

```bash
python manage.py migrate
```

---

## 🔗 URL sozlash

`urls.py` fayliga qo‘shing:

```python
from django.urls import path, include

urlpatterns = [
    ...
    path('captcha/', include('captcha.urls')),
]
```

---

## 📝 Formada ishlatish

```python
from django import forms
from captcha.fields import CaptchaField

class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    captcha = CaptchaField()
```

---

## 🎨 Template (HTML)

```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```

---

## ⚡ Qanday ishlaydi?

- Foydalanuvchiga rasm + kod ko‘rsatiladi  
- U kodni to‘g‘ri kiritsa → form o‘tadi  
- Noto‘g‘ri bo‘lsa → xatolik qaytariladi  

---

## 🔧 Qo‘shimcha sozlamalar

`settings.py` ichida:

```python
CAPTCHA_LENGTH = 5
CAPTCHA_FONT_SIZE = 50
CAPTCHA_IMAGE_SIZE = (150, 50)
```

---

## 🚀 Ishlatish sabablari

- Spamni kamaytiradi  
- Botlardan himoya qiladi  
- Oson integratsiya qilinadi  
- Django bilan to‘liq mos  

---

## ❗ Eslatma

Agar CAPTCHA chiqmasa:

- `captcha` app qo‘shilganini tekshiring  
- `migrate` qilinganini tekshiring  
- `urls.py` to‘g‘ri ulanganini tekshiring  

---

## 📚 Foydali maslahat

Development vaqtida tez-tez CAPTCHA yangilash uchun:

```python
CAPTCHA_TIMEOUT = 1  # minut
```
