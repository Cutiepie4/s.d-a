from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from mobile_model.views import MobileViewSet, MobileCategoryViewSet

router = DefaultRouter()
router.register(r'mobile', MobileViewSet)
router.register(r'mobilecategory', MobileCategoryViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
