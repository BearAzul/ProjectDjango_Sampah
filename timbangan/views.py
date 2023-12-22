# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Timbangan

def timbangan_list(request):
    timbangan_data = Timbangan.objects.all()
    return render(request, 'timbangan_list.html', {'timbangan_data': timbangan_data})

def tambah_timbangan(request):
    if request.method == 'POST':
        nama = request.POST['Nama']
        alamat = request.POST['Alamat']
        tipe_sampah = request.POST['TipeSampah']
        jumlah_kilo = request.POST['JumlahKilo']

        # Menentukan harga per kilogram berdasarkan tipe sampah
        if tipe_sampah == 'Tipe A':
            harga_per_kilo = 1000  
        elif tipe_sampah == 'Tipe B':
            harga_per_kilo = 2000  
        elif tipe_sampah == 'Tipe C':
            harga_per_kilo = 3000  
        elif tipe_sampah == 'Tipe D':
            harga_per_kilo = 4000  
        else:
            harga_per_kilo = 0

        harga_keseluruhan = float(harga_per_kilo) * float(jumlah_kilo)

        Timbangan.objects.create(
            Nama=nama,
            Alamat=alamat,
            TipeSampah=tipe_sampah,
            HargaPerKilo=harga_per_kilo,
            JumlahKilo=jumlah_kilo,
            HargaKeseluruhan=harga_keseluruhan
        )
        return redirect('timbangan_list')

    return render(request, 'tambah_timbangan.html')

def edit_timbangan(request, id):
    timbangan = get_object_or_404(Timbangan, id=id)

    if request.method == 'POST':
        timbangan.Nama = request.POST['Nama']
        timbangan.Alamat = request.POST['Alamat']
        timbangan.TipeSampah = request.POST['TipeSampah']
        timbangan.JumlahKilo = request.POST['JumlahKilo']

        # Menentukan harga per kilogram berdasarkan tipe sampah
        if timbangan.TipeSampah == 'Tipe A':
            timbangan.HargaPerKilo = 1000
        elif timbangan.TipeSampah == 'Tipe B':
            timbangan.HargaPerKilo = 2000
        elif timbangan.TipeSampah == 'Tipe C':
            timbangan.HargaPerKilo = 3000
        elif timbangan.TipeSampah == 'Tipe D':
            timbangan.HargaPerKilo = 4000
        else:
            timbangan.HargaPerKilo = 0

        # Update harga keseluruhan
        timbangan.HargaKeseluruhan = float(timbangan.HargaPerKilo) * float(timbangan.JumlahKilo)

        timbangan.save()
        return redirect('timbangan_list')

    return render(request, 'edit_timbangan.html', {'timbangan': timbangan})

def hapus_timbangan(request, id):
    timbangan = get_object_or_404(Timbangan, id=id)

    if request.method == 'POST':
        timbangan.delete()
        return redirect('timbangan_list')

    return render(request, 'hapus_timbangan.html', {'timbangan': timbangan})
