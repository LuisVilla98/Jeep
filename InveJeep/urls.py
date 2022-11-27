from AppJeep.views import JeepTemplates, RegistroViews
from django.contrib import admin
from django.urls import path
from AppJeep import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('render/', JeepTemplates),
    path('Jeeps/', views.JeepTemplates),
    path('',RegistroViews),
    path('eliminarJeeps/<int:id>',views.eliminarJeeps),
    path('actualizarJeeps/<int:id>',views.actualizarJeeps)

]







