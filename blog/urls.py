from blog import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('blog', views.article_list),
    path('contact', views.contact),
    path('article/<int:article_id>', views.article),
    path('email', views.email)
]