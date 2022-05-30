from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('acervo/', include('acervo.urls')),
    path('', include('usuarios.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('emprestimo/', include('emprestimo.urls')),
    path('funcionarios/', include('funcionarios.urls')),
]
