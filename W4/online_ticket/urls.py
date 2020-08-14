from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns


from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('user_profile.urls')),
    path('cinema/', include('cinema.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', index, name='home'),
    path('blog/', include('blog.urls'))

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
