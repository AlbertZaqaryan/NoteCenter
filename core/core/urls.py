"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from main import views
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

router = routers.DefaultRouter()

router.register(r'category', views.CategoryView)
router.register(r'subcategory', views.SubCategoryView)
router.register(r'brand', views.BrandView)
router.register(r'product', views.ProductView)
router.register(r'product_cpu', views.CPUView)
router.register(r'product_gpu', views.GPUView)
router.register(r'product_ram', views.RamView)
router.register(r'product_memory', views.MemoryView)
router.register(r'product_display', views.DisplayView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('', include(router.urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += i18n_patterns(path('', include(router.urls)))