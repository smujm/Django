from django.contrib import admin

# Register your models here.
# 注册模型
# admin.site.register(模型类)
from book.models import BookInfo

admin.site.register(BookInfo)