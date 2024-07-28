from django.contrib import admin
from django.utils.html import format_html
from .models import DataPamong, Kegiatan, AgendaKegiatan

@admin.register(DataPamong)
class DataPamongAdmin(admin.ModelAdmin):
    list_display = (
        'nik', 'nip', 'nama', 'tempat_lahir', 'tanggal_lahir', 
        'alamat', 'status_kawin', 'pekerjaan', 'jabatan', 
        'golongan_darah', 'agama', 'jenis_kelamin', 
        'periode_masa_jabatan', 'pendidikan_terakhir', 'photo_tag'
    )
    search_fields = ('nik', 'nama', 'nip')
    list_filter = ('status_kawin', 'jenis_kelamin', 'agama', 'pendidikan_terakhir')

    def photo_tag(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.photo.url))
        return '-'
    photo_tag.short_description = 'Photo'

@admin.action(description='Mark selected activities as completed')
def make_completed(modeladmin, request, queryset):
    queryset.update(status=True)

@admin.register(Kegiatan)
class KegiatanAdmin(admin.ModelAdmin):
    list_display = (
        'id_user', 'nama_perangkat_desa', 'jabatan_perangkat_desa', 
        'jenis_kegiatan', 'keterangan', 'tanggal_pelaporan', 
        'status', 'foto_kegiatan'
    )
    search_fields = ('nama_perangkat_desa', 'jabatan_perangkat_desa', 'jenis_kegiatan')
    list_filter = ('jenis_kegiatan', 'status')
    actions = [make_completed]

@admin.register(AgendaKegiatan)
class AgendaKegiatanAdmin(admin.ModelAdmin):
    list_display = ('kegiatan', 'tgl_mulai', 'ket', 'user_id')
    search_fields = ('kegiatan__nama_perangkat_desa', 'user_id__nama')
    list_filter = ('tgl_mulai',)
