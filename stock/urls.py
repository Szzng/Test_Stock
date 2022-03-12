from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/risingstock/', include('risingstock.urls')),
    path('api/accounts/', include('dj_rest_auth.urls')),
    path('api/accounts/registration/', include('dj_rest_auth.registration.urls'))
]