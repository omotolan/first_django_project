from django.urls import path
from . import views

app_name = 'first_app'
urlpatterns = [
    # path('', views.hello),
    path('', views.index,  name='hello'),
    # path('<str:name>/<int:num>', views.helloo),
    path('', views.redirect)

]
