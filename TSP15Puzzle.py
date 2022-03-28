import time
import copy
class TSP15Puzzle:
    def __init__(self,matrix):
        self.matrix = matrix
        self.startTime = time.Time()*1000 # waktu mulai dalam ms
        self.endTime = None #waktu algoritma selesai
        self.solution = []
    def getElapsedTime(self):
        #mengembalikan waktu algoritma dalam ms
        return self.endTime-self.startTime
    def cetakMatrix(self):
        #mencetak matriks awal
        for i in range(16):
            print(self.matrix[i],end=" ")
            if(i==3 or i==7 or i==11):
                print()
        print()
    def KURANG(self,i):
        #menghitung jumlah nilai di depan posisi nomor i yang nilainya lebih kecil dari i
        count = 0
        start_idx = self.matrix.index(i)
        for n in range(start_idx+1,16):
            if(self.matrix[n]<i and self.matrix[n]!=0):
                count += 1
        return count
    def getCost(self, tempMatrix):
        #mendapatkan cost suatu cabang
        cost = 1    #f(i)
        for i in range(16):
            if(tempMatrix[i] != 16 and tempMatrix[i]!=i+1):
                cost+=1
        return cost
    def sort(self, listOfMatrix):
        #mengurutkan daftar matriks dari cost terkecil 
        temp = copy.deepcopy(listOfMatrix)
        pass
    def solve(self):
        #menyelesaikan puzzle dengan algoritma branch and bound
        #struktur data simpul: simpul = (indeks,parent,isi, cost)->disimpan di atribut kelas
        #return (jumlah_simpul_yang_berhasil_dibangkitkan)
        jumlah_simpul = 0
        simpul_hidup = []
        #inisialisasi simpul pertama
        i = 1
        first_node = [i,None,self.matrix,0]
        self.solution.append(first_node)
        i+=1
        # melakukan algoritma branch and bound
        # inisialisasi simpul awal
        idx_kosong = self.matrix.index(16)
        # 1->ke atas
        if(idx_kosong//4 > 0):#bukan di baris pertama
            temp = copy.deepcopy(self.matrix)
            temp[idx_kosong] = temp[idx_kosong-4]
            temp[idx_kosong-4] = 16
            node = [i,1,temp,self.getCost(temp)]
            simpul_hidup.append(node)
            i+=1
        # 2->ke kanan
        if(idx_kosong%4 != 3):#bukan di kolom terakhir
            temp = copy.deepcopy(self.matrix)
            temp[idx_kosong] = temp[idx_kosong+1]
            temp[idx_kosong+1] = 16
            node = [i,1,temp,self.getCost(temp)]
            simpul_hidup.append(node)
            i+=1
        # 3->ke bawah
        if(idx_kosong//4 != 3):#bukan di baris terakhir
            temp = copy.deepcopy(self.matrix)
            temp[idx_kosong] = temp[idx_kosong+4]
            temp[idx_kosong+4] = 16
            node = [i,1,temp,self.getCost(temp)]
            simpul_hidup.append(node) 
            i+=1       
        # 4->ke kiri
        if(idx_kosong%4 != 0):#bukan di kolom pertama
            temp = copy.deepcopy(self.matrix)
            temp[idx_kosong] = temp[idx_kosong-1]
            temp[idx_kosong-1] = 16
            node = [i,1,temp,self.getCost(temp)]
            simpul_hidup.append(node)   
            i+=1   
        simpul_hidup = self.sort(simpul_hidup)#urutkan dari cost yang terkecil
        self.endTime = time.time()*1000
        return jumlah_simpul
