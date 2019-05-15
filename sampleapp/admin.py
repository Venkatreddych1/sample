from django.contrib import admin
from .models import Reg

class Sample(admin.ModelAdmin):
      list_display = ['file','comment']



admin.site.register(Reg,Sample)


