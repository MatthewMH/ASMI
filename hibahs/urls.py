from django.urls import path
from .admin import UploadedFile_list  # Import your custom admin class
from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .views import print_item_view, delete_item_view, print_mikroskopik_view, delete_mikroskopik_view





urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('print/<int:item_id>', print_item_view, name='print_item_view'), 
    path('delete/<int:item_id>', delete_item_view, name='delete_item_view'),
    path('print-mikroskopik/<int:item_id>', print_mikroskopik_view, name='print_mikroskopik_view'), 
    path('delete-mikroskopik/<int:item_id>', delete_mikroskopik_view, name='delete_mikroskopik_view'), 
    # path('uploadedfile', print_item_view, name='print_item_view'),
    # *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),

    


   ]