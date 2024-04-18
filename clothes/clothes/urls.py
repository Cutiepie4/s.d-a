from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from clothes_model.views import ClothesViewSet, ClothesCategoryViewSet

router = DefaultRouter()
router.register(r'clothes', ClothesViewSet)
router.register(r'clothescategory', ClothesCategoryViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
