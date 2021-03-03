from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


admin.site.site_header='Code with Rohit'
admin.site_title='Code with Rohit Admin Panel'
admin.site.index_title='Welcome to Code With Rohit'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myblog.urls')),
    path('my_project/',include('myproject.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),


]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

