from django.db import models

class DataPamong(models.Model):
    nik = models.CharField(max_length=16, unique=True)
    nip = models.CharField(max_length=18, unique=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    nama = models.CharField(max_length=255)
    tempat_lahir = models.CharField(max_length=255)
    tanggal_lahir = models.DateField()
    alamat = models.TextField()
    status_kawin = models.CharField(max_length=50)
    pekerjaan = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=100)
    golongan_darah = models.CharField(max_length=2)
    agama = models.CharField(max_length=50)
    jenis_kelamin = models.CharField(max_length=10)
    periode_masa_jabatan = models.CharField(max_length=100)
    pendidikan_terakhir = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Kegiatan(models.Model):
    id_user = models.ForeignKey(DataPamong, on_delete=models.CASCADE)
    nama_perangkat_desa = models.CharField(max_length=255)
    jabatan_perangkat_desa = models.CharField(max_length=100)
    jenis_kegiatan = models.CharField(max_length=100)
    keterangan = models.TextField()
    tanggal_pelaporan = models.DateField()
    status = models.BooleanField(default=False)
    foto_kegiatan = models.ImageField(upload_to='foto_kegiatan/', null=True, blank=True)

    def __str__(self):
        return self.nama_perangkat_desa

class AgendaKegiatan(models.Model):
    kegiatan = models.ForeignKey(Kegiatan, on_delete=models.CASCADE)
    tgl_mulai = models.DateField()
    ket = models.TextField()
    user_id = models.ForeignKey(DataPamong, on_delete=models.CASCADE)

    def __str__(self):
        return f"Agenda {self.kegiatan} mulai {self.tgl_mulai}"
