Django Simple Captcha Integration
1. O'rnatish
Bash
pip install django-simple-captcha
2. settings.py
INSTALLED_APPS ro'yxatiga qo'shing:

Python
INSTALLED_APPS = [
    # ...
    'captcha',
]
3. urls.py
Asosiy urls.py fayliga marshrutni qo'shing:

Python
from django.urls import path, include

urlpatterns = [
    # ...
    path('captcha/', include('captcha.urls')),
]
4. Migratsiya
Bash
python manage.py migrate
5. forms.py
Formaga CaptchaField ni qo'shing:

Python
from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()
6. views.py
is_valid() metodidan foydalaning (u captchani avtomatik tekshiradi):

Python
def login_user(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # Captcha to'g'ri, login mantiqi shu yerda
            pass
    return render(request, 'login.html', {'form': form})
7. login.html
HTML
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Kirish</button>
</form>
