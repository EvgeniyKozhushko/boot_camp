"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from books import views as books_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', books_views.books_home, name='home'),

    path('home_books/', books_views.HomeBookListView.as_view(), name='home-books'),
    path('book/<int:pk>', books_views.BookDetailView.as_view(), name='book'),
    path('book_create/', books_views.BookCreateView.as_view(), name='book-create'),
    path('book_update/<int:pk>/', books_views.BookUpdateView.as_view(), name='book-update'),
    path('book_delete/<int:pk>/', books_views.BookDeleteView.as_view(), name='book-delete'),


    path('home_authors/', books_views.AuthorListView.as_view(), name='home-authors'),
    path('author/<int:pk>/', books_views.AuthorDetailView.as_view(), name='author'),
    path('author_create/', books_views.AuthorCreateView.as_view(), name='author-create'),
    path('author_update/<int:pk>/', books_views.AuthorUpdateView.as_view(), name='author-update'),
    path('author_delete/<int:pk>/', books_views.AuthorDeleteView.as_view(), name='author-delete')
]
