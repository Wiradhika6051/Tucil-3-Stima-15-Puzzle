def cetakMatrix(matrix):
    #mencetak matriks awal
    for i in range(16):
        print(matrix[i],end=" ")
        if(i==3 or i==7 or i==11):
            print()
    print()

def KURANG(list,i):
    #menghitung jumlah nilai di depan posisi nomor i yang nilainya lebih kecil dari i
    count = 0
    start_idx = list.index(i)
    for n in range(start_idx+1,16):
        if(list[n]<i and list[n]!=0):
            count += 1
    return count

if __name__ == "__main__":
    matrix_awal = input("Masukkan matriks(tulis 16 untuk sel kosong): ").strip().split(" ")
    #saring masukan
    try:
        matrix_awal = list(map(lambda x: int(x),matrix_awal))
        for element in matrix_awal:
            if(element>16 or element < 1 ):
                raise IndexError("Masukkan hanya boleh 1-16!")
        if(len(set(matrix_awal))!=len(matrix_awal)):# ada yang gak unik
                raise Exception("Semua elemen harus unik!")
    except ValueError:
        print("Masukkan hanya boleh angka!")
    except IndexError:
        print("Masukkan hanya boleh 1-16!")
    except Exception:
        print("Semua elemen harus unik!")
    else:
        #lanjutkan program
        print("Matrix awal:")
        cetakMatrix(matrix_awal)
        #menampilkan nilai kurang i masing masing indeks
        for i in range(1,16):
            print("KURANG(%d) =  %d" % (i,KURANG(matrix_awal,i)) )