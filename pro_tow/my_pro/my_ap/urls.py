from django.urls import path
from . import views

app_name = 'my_ap'
urlpatterns = [
    path('Home/', views.IndexView.as_view() , name = 'Home'),
    path('' , views.ProduiteListView.as_view() , name = 'produite'), # hada URL ta3 page Liste.html
    path('<int:pk>/', views.ProduiteDetialView.as_view(), name='detail'), # hna liykon pk ghadi yadini ll page detail.html
    path('creat/' ,views.ProduiteCreateView.as_view() , name = 'creat'),
    path('update/<int:pk>/', views.ProduiteUpdeat.as_view(), name='updeat'),
    path('delaite/<int:pk>/', views.ProduiteDelaite.as_view(), name='delaite'),

]


