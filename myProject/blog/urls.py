from django.urls import path,re_path
from . import views 

urlpatterns = [
    path('post/<int:post_id>/', views.post_details, name='post_details'),
    path('user/<str:username>/', views.user_details, name='user_details'),
    
    re_path(r'^article/(?P<year>[0-9]{4})/$', views.year_by_data, name='year_by_data'),
]