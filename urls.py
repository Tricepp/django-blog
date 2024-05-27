from django.contrib import admin
# <-- Make sure you have both of these imports.
from django.urls import path, include

urlpatterns = [
    path('polling/', include('polling.urls')),  # <-- Add this
    path('admin/', admin.site.urls),
]
