
from .views import BookList, BookViewSet
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
    # token authentication endpoint
     path('books/', BookList.as_view(), name='book-list'),
    #  read only endpoint
     path("", include(router.urls)),
    #  crud operations endpoint
     path("token/", obtain_auth_token, name ="api-token")
]


