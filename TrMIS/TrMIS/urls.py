
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('', include('TrMISApp.urls')),
    path('reverse/', include('reverserelation.urls')),
    path('multiplemodelquery/', include('multiplemodelquery.urls')),
    path('attendance/', include('attendance.urls')),
    path('hyperlinkedmodelserializer/', include('hyperlinkedmodelserializer.urls')),

]
