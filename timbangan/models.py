# models.py
from django.db import models

class Timbangan(models.Model):
    Nama = models.CharField(max_length=255)
    Alamat = models.CharField(max_length=255)
    TipeSampah = models.CharField(max_length=255)
    HargaPerKilo = models.DecimalField(max_digits=10, decimal_places=2)
    JumlahKilo = models.DecimalField(max_digits=10, decimal_places=2)
    HargaKeseluruhan = models.DecimalField(max_digits=10, decimal_places=2)
  
    def __str__(self):
        return self.Nama