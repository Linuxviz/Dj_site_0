from django.urls import path
from .views import news, view_category

urlpatterns = [
    path('', news, name='home'),
    path('category/<int:index>/', view_category, name='category')
]
