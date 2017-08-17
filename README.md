# Simple API demo.

Version:
 - Python 3.6.2
 - Django 1.11.4

How to install to main django settings.py file:
 - Add this app name to INSTALLED_APPS list

How to install to main django urls.py file:
 - Import the include() function: "from django.conf.urls import url, include"
 - Add a URL to urlpatterns:  "url(r'^simpleapi/', include('simpleapi.urls'))"
