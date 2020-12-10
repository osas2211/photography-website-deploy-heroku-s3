from django.contrib import admin
from .models import home_page, showcase, about

# Register your models here.
models = [home_page, showcase, about]
for model in models:
    admin.site.register(model)
