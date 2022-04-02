from TSP15Puzzle import TSP15Puzzle

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
        puzzleSolver = TSP15Puzzle(matrix_awal)
        puzzleSolver.setStartTime()
        #lanjutkan program
        print("\nMatrix awal:")
        puzzleSolver.cetakMatrix()
        #menampilkan nilai kurang i masing masing indeks
        print("\nNilai fungsi KURANG(i) untuk setiap i yang bukan ubin kosong:")
        status_number = 0
        for i in range(1,16):
            kurang_number = puzzleSolver.KURANG(i)
            print("KURANG(%d) =  %d" % (i, kurang_number))
            status_number += kurang_number
        print()
        #menampilkan jumlah nilai status reachable
        get_1_position = [ 1, 3, 4, 6, 9, 11, 12, 14 ] #jika kotak kosong berada di indeks ini, maka nilai status_number += 1
        status_number += puzzleSolver.KURANG(16)
        if(matrix_awal.index(16) in get_1_position):
            status_number += 1
        print("Nilai dari nilai status reachable(sigma(i)+X):",status_number)
        #mengecek status reachable
        if(status_number % 2 != 0):#kalau ganjil maka tidak reachable
            print("\nPersoalan tidak bisa diselesaikan!")
        else:
            #menyelesaikan puzzle
            jumlah_simpul = puzzleSolver.solve()
            #menghandle kasus waktu penyelesaian terlalu lama
            if(jumlah_simpul==None):
                print("Persoalan membutuhkan waktu yang lama untuk diselesaikan! (melebihi 8 menit!)")
            else:
                #tampilkan urutan langkah
                print("Daftar Langkah:")
                puzzleSolver.showStep_CLI()
                #menampilkan waktu eksekusi program
                time_elapsed = puzzleSolver.getElapsedTime()
                print("\nWaktu eksekusi program: %s ms" % (time_elapsed))
                #menampilkan jumlah simpul yang dibangkitkan
                print("\nJumlah simpul yang dibangkitkan:",jumlah_simpul)


#tc: 1 2 3 4 5 6 16 8 9 10 7 11 13 14 15 12

#tc : 1 2 3 4 5 6 7 8 9 10 16 11 13 14 15 12
#1 2 3 4 
#5 6 7 8 
#9 10 11 12 
#13 14 15 16

#1 2 3 4 
#5 6 7 8 
#9 10 16 11 
#13 14 15 12

#1 2 3 4 
#5 6 16 8 
#9 10 7 11 (up)
#13 14 15 12

#1 2 3 4 
#5 6 7 8 
#9 10 11 16 (kanan)
#13 14 15 12

#1 2 3 4 
#5 6 7 8 
#9 10 15 11 (down)
#13 14 16 12

#1 2 3 4 
#5 6 7 8 
#9 16 10 11 (left)
#13 14 15 12


#1 2 3 4 
#5 6 7 8 
#9 10 11 16 (kanan)->base-1
#13 14 15 12

#1 2 3 4 
#5 6 7 16 
#9 10 11 12 (up?)->base-1
#13 14 15 8