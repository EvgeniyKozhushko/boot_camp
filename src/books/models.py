from django.db import models
from django.urls import reverse

# Create your models here.

class Author(models.Model):
    name = models.CharField(verbose_name='Имя автора', max_length=60)
    author_discription = models.TextField(verbose_name= 'Описание', blank=True, null=True)
    #picture_author = models.ImageField(verbose_name="Картинка", upload_to = 'author/%Y/%m/%d/',blank=True, null=True)

    def __str__(self) -> str:
        return f'Автор {self.name}'

class Book(models.Model):
    title_book = models.CharField(verbose_name="Название книги", max_length= 200)
    #picture_book = models.ImageField(verbose_name="Картинка", upload_to = 'author/%Y/%m/%d/')
    book_author = models.ManyToManyField(Author, default='Автор', related_name='authors') # должен быть справочник
    book_series = models.CharField(verbose_name="Серия книг", max_length= 50)
    book_genre = models.CharField(verbose_name="Жанр", max_length= 20)
    year_publishing = models.IntegerField(verbose_name= "Год издания")
    number_pages = models.IntegerField(verbose_name="Количество страниц")
    size = models.CharField(verbose_name="Формат", max_length= 100)
    ISBN = models.CharField(verbose_name="ISBN",max_length= 100)
    publishing_house = models.CharField(verbose_name="Издательство", max_length= 40)
    # in_stock = models.IntegerField(verbose_name="Количество в наличии")
    # available_to_order = models.BooleanField(verbose_name="Доступна к заказу", default=True)
    rating = models.IntegerField(verbose_name="Рейтинг (0-10)", blank=True, null=True)
    date_inclusion = models.DateTimeField(verbose_name="Дата внесения в каталог", auto_now_add=True, auto_now=False)
    date_change = models.DateTimeField(verbose_name="Дата последнего изменения карточки", auto_now_add=False, auto_now=True)

    def __str__(self) -> str:
        return f"{self.title_book}"