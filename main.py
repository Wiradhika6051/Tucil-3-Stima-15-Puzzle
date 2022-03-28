def cetakMatrix(matrix):
    for i in range(16):
        print(matrix[i],end=" ")
        if(i==3 or i==7 or i==11):
            print()

if __name__ == "__main__":
    matrix_awal = input("Masukkan matriks(tulis 0 untuk sel kosong): ").strip().split(" ")
    #saring masukan
    try:
        matrix_awal = list(map(lambda x: int(x),matrix_awal))
        for element in matrix_awal:
            if(element>15 or element < 0 ):
                raise IndexError("Masukkan hanya boleh 1-15!")
        if(len(set(matrix_awal))!=len(matrix_awal)):# ada yang gak unik
                raise Exception("Semua elemen harus unik!")
    except ValueError:
        print("Masukkan hanya boleh angka!")
    except IndexError:
        print("Masukkan hanya boleh 1-15!")
    except Exception:
        print("Semua elemen harus unik!")
    else:
        #lanjutkan program
        print("Matrix awal:")
        cetakMatrix(matrix_awal)