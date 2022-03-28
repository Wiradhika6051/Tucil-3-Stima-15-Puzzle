from matplotlib.pyplot import get


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
        print("\nMatrix awal:")
        cetakMatrix(matrix_awal)
        #menampilkan nilai kurang i masing masing indeks
        print("\nNilai fungsi KURANG(i) untuk setiap i yang bukan ubin kosong:")
        status_number = 0
        for i in range(1,16):
            kurang_number = KURANG(matrix_awal,i)
            print("KURANG(%d) =  %d" % (i, kurang_number))
            status_number += kurang_number
        print()
        #menampilkan jumlah nilai status reachable
        get_1_position = [ 1, 3, 4, 6, 9, 11, 12, 14 ] #jika kotak kosong berada di indeks ini, maka nilai status_number += 1
        status_number += KURANG(matrix_awal,16)
        if(matrix_awal.index(16) in get_1_position):
            status_number += 1
        print("Nilai dari nilai status reachable(sigma(i)+X):",status_number)
        #mengecek status reachable
        if(status_number % 2 != 0):#kalau ganjil maka tidak reachable
            print("\nPersoalan tidak bisa diselesaikan!")
        else:
            print("aman")