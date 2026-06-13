from django.contrib import admin
from django.urls import path, include  # Не забудь додати include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_app.urls')),  # Підключаємо маршрути з нашого додатку
]