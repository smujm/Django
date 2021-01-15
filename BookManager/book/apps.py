from django.apps import AppConfig


class BookConfig(AppConfig):
    name = 'book'
    # admin中显示
    verbose_name = '后台相关'