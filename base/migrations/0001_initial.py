# Generated by Django 5.0.6 on 2024-07-20 13:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataPamong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nik', models.CharField(max_length=16, unique=True)),
                ('nip', models.CharField(max_length=18, unique=True)),
                ('nama', models.CharField(max_length=255)),
                ('tempat_lahir', models.CharField(max_length=255)),
                ('tanggal_lahir', models.DateField()),
                ('alamat', models.TextField()),
                ('status_kawin', models.CharField(max_length=50)),
                ('pekerjaan', models.CharField(max_length=100)),
                ('jabatan', models.CharField(max_length=100)),
                ('golongan_darah', models.CharField(max_length=2)),
                ('agama', models.CharField(max_length=50)),
                ('jenis_kelamin', models.CharField(max_length=10)),
                ('periode_masa_jabatan', models.CharField(max_length=100)),
                ('pendidikan_terakhir', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Kegiatan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_perangkat_desa', models.CharField(max_length=255)),
                ('jabatan_perangkat_desa', models.CharField(max_length=100)),
                ('jenis_kegiatan', models.CharField(max_length=100)),
                ('keterangan', models.TextField()),
                ('tanggal_pelaporan', models.DateField()),
                ('status', models.BooleanField(default=False)),
                ('foto_kegiatan', models.ImageField(blank=True, null=True, upload_to='foto_kegiatan/')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.datapamong')),
            ],
        ),
        migrations.CreateModel(
            name='AgendaKegiatan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgl_mulai', models.DateField()),
                ('ket', models.TextField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.datapamong')),
                ('kegiatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.kegiatan')),
            ],
        ),
    ]
