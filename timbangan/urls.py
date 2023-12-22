# urls.py
from django.urls import path
from .views import timbangan_list, tambah_timbangan, edit_timbangan, hapus_timbangan

urlpatterns = [
    path('timbangan/', timbangan_list, name='timbangan_list'),
    path('tambah_timbangan/', tambah_timbangan, name='tambah_timbangan'),
    path('edit_timbangan/<int:id>/', edit_timbangan, name='edit_timbangan'),
    path('hapus_timbangan/<int:id>/', hapus_timbangan, name='hapus_timbangan'),
    # Tambahkan pattern URL lainnya jika diperlukan
]
