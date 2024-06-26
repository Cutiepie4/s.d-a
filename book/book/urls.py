from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from book_model.views import BookViewSet, BookCategoryViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'bookcategory', BookCategoryViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
