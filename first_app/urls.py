from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views, viewscb, modelviewset

app_name = 'first_app'

# router = SimpleRouter()
# router.register('books', modelviewset.BookViewSet)
# urlpatterns=[
#     path('', include(router.urls))
# ]
urlpatterns = [
    # path('', views.hello),
    path('', views.index,  name='hello'),
    # path('<str:name>/<int:num>', views.helloo),
    path('', views.redirect),

    # path('books/', views.book_list, name='book-list'),
    # path('books/<int:pk>/', views.book_detail, name='book-details'),
    # path('publishers/', views.publisher_list, name='publisher-list'),
    # path('publishers/<int:pk>/', views.publisher_detail, name='publisher-detail'),

    path('books/', viewscb.BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', views.book_detail, name='book-details'),
    path('publishers/', views.publisher_list, name='publisher-list'),
    path('publishers/<int:pk>/', views.publisher_detail, name='publisher-detail'),

]
