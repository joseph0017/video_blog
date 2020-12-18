from django.contrib import admin

# Register your models here.
from .models import Videos,Images

admin.site.register(Videos)

admin.site.register(Images)