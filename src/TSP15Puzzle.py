import time
import copy
from operator import itemgetter

from numpy import array_equal
class TSP15Puzzle:
    def __init__(self,matrix):
        self.matrix = matrix
        self.startTime = None # waktu mulai dalam ms
        self.endTime = None #waktu algoritma selesai
        self.solution = []
        self.endNode = None
        self.simpul = []#simpul yang sudah pernah dibangkitkan
        self.MAXTIME = 8*60*1000 #waktu maksimum komputasi (dalam ms)
    def get_matrix(self):
        return self.matrix
    def getElapsedTime(self):
        #mengembalikan waktu algoritma dalam ms
        return self.endTime-self.startTime
    def cetakMatrix(self,matrix=None):
        if(matrix == None):
            matrix = self.matrix
        #mencetak matriks awal
        for i in range(16):
            print(matrix[i],end=" ")
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
    def g(self,matrix):
        #mengembalikan cost mencapai simpul tujuan dari simpul i
        #dihitung dengan menghitung jumlah label yang tidak berada di posisi akhirnya
        cost = 0
        for i in range(1,17):
            if(matrix[i-1]!=i):
                cost += 1
        return cost

    def solve(self):
        #menyelesaikan puzzle dengan algoritma branch and bound
        #struktur data simpul: simpul = (indeks,parent,isi, cost,hash_value)->disimpan di atribut kelas
        #return (jumlah_simpul_yang_berhasil_dibangkitkan)
        simpul_hidup = []
        self.solution = []
        #inisialisasi simpul pertama
        i = 0
        first_node = [i,-1,self.matrix,0,self.hashing(self.matrix)]
        self.simpul.append(first_node)
        jumlah_simpul = 1
        if(self.g(first_node[2])==0):
            self.endNode = copy.deepcopy(first_node)
            self.endTime = time.time()*1000
            self.getPath(self.endNode)
            return jumlah_simpul
        i+=1
        # melakukan algoritma branch and bound
        # inisialisasi simpul awal
        idx_kosong = self.matrix.index(16)
        found = False
        # 1->ke atas
        if(idx_kosong//4 > 0 and not found):#bukan di baris pertama
            temp = copy.deepcopy(self.matrix)
            temp[idx_kosong],temp[idx_kosong-4] = temp[idx_kosong-4],temp[idx_kosong]
            node = [i,0,temp,self.getCost(temp),self.hashing(temp)]
            simpul_hidup.append(node)
            self.simpul.append(node)
            i+=1
            jumlah_simpul+=1
            if(self.g(node[2])==0):
                self.endNode = copy.deepcopy(node)
                #solusi ketemu
                found = True
        # 2->ke kanan
        if(idx_kosong%4 != 3 and not found):#bukan di kolom terakhir
            temp = copy.deepcopy(self.matrix)
            temp[idx_kosong],temp[idx_kosong+1] = temp[idx_kosong+1],temp[idx_kosong]
            node = [i,0,temp,self.getCost(temp),self.hashing(temp)]
            simpul_hidup.append(node)
            self.simpul.append(node)
            i+=1
            jumlah_simpul+=1
            if(self.g(node[2])==0):
                self.endNode = copy.deepcopy(node)
                #solusi ketemu
                found = True
        # 3->ke bawah
        if(idx_kosong//4 != 3 and not found):#bukan di baris terakhir
            temp = copy.deepcopy(self.matrix)
            temp[idx_kosong],temp[idx_kosong+4] = temp[idx_kosong+4],temp[idx_kosong]
            node = [i,0,temp,self.getCost(temp),self.hashing(temp)]
            simpul_hidup.append(node) 
            self.simpul.append(node)
            i+=1       
            jumlah_simpul+=1
            if(self.g(node[2])==0):
                self.endNode = copy.deepcopy(node)
                #solusi ketemu
                found = True
        # 4->ke kiri
        if(idx_kosong%4 != 0 and not found):#bukan di kolom pertama
            temp = copy.deepcopy(self.matrix)
            temp[idx_kosong],temp[idx_kosong-1] = temp[idx_kosong-1],temp[idx_kosong]
            node = [i,0,temp,self.getCost(temp),self.hashing(temp)]
            simpul_hidup.append(node) 
            self.simpul.append(node)  
            i+=1   
            jumlah_simpul+=1
            if(self.g(node[2])==0):
                self.endNode = copy.deepcopy(node)
                #solusi ketemu
                found = True
        while(simpul_hidup and not found):#selama masih ada simpul hidup
            temp_time = time.time()*1000
            if(temp_time-self.startTime>self.MAXTIME):
                return None
            temp = copy.deepcopy(simpul_hidup)
            simpul_hidup = sorted(temp,key=itemgetter(3))#urutkan dari cost yang terkecil
            node = simpul_hidup.pop(0)
            time.sleep(1)
            if(self.g(node[2])==0):
                self.endNode = copy.deepcopy(node)
                #solusi ketemu
                break
            #generasikan simpul lain
            idx_kosong = node[2].index(16)
            # 1->ke atas
            if(idx_kosong//4 > 0):#bukan di baris pertama
                temp = copy.deepcopy(node[2])
                temp[idx_kosong],temp[idx_kosong-4] = temp[idx_kosong-4],temp[idx_kosong]
                jumlah_simpul+=1
                hash_value = self.hashing(temp)
                if self.checkUnique(hash_value):
                    temp_node = [i,node[0],temp,self.getCost(temp),hash_value]
                    simpul_hidup.append(temp_node)
                    self.simpul.append(temp_node)
                    i+=1
            # 2->ke kanan
            if(idx_kosong%4 != 3):#bukan di kolom terakhir
                temp = copy.deepcopy(node[2])
                temp[idx_kosong],temp[idx_kosong+1] = temp[idx_kosong+1],temp[idx_kosong]
                jumlah_simpul+=1
                hash_value = self.hashing(temp)
                if self.checkUnique(hash_value):
                    temp_node = [i,node[0],temp,self.getCost(temp),hash_value]
                    simpul_hidup.append(temp_node)
                    self.simpul.append(temp_node)
                    i+=1
            # 3->ke bawah
            if(idx_kosong//4 != 3):#bukan di baris terakhir
                temp = copy.deepcopy(node[2])
                temp[idx_kosong],temp[idx_kosong+4] = temp[idx_kosong+4],temp[idx_kosong]
                jumlah_simpul+=1
                hash_value = self.hashing(temp)
                if self.checkUnique(hash_value):
                    temp_node = [i,node[0],temp,self.getCost(temp),hash_value]
                    simpul_hidup.append(temp_node) 
                    self.simpul.append(temp_node)
                    i+=1       
            # 4->ke kiri
            if(idx_kosong%4 != 0):#bukan di kolom pertama
                temp = copy.deepcopy(node[2])
                temp[idx_kosong],temp[idx_kosong-1] = temp[idx_kosong-1],temp[idx_kosong]
                jumlah_simpul+=1
                hash_value = self.hashing(temp)
                if self.checkUnique(hash_value):
                    temp_node = [i,node[0],temp,self.getCost(temp),hash_value]
                    simpul_hidup.append(temp_node) 
                    self.simpul.append(temp_node)  
                    i+=1   
        #mendapatkan path rute
        self.getPath(self.endNode)
        self.endTime = time.time()*1000
        return jumlah_simpul
    def getIDX(self,node_idx,matrix):
        #mendapatkan index suatu node
        i = 0
        for elmt in matrix:
            if(elmt[0]==node_idx):#indeksnya sama
                return i
            i+=1
    def getPath(self,node):
        #mendapatkan path dari end node ke root
        node_idx = self.getIDX(node[0],self.simpul)
        self.solution.append(self.simpul[node_idx])
        while(node_idx!=0):#bukan root,loop sampe ketemu loop
            node_idx = self.getIDX(node[1],self.simpul)
            node = self.simpul[node_idx]
            self.solution.append(node)
        self.solution = sorted(self.solution,key=itemgetter(0))
    def showStep_CLI(self):
        i = 1
        for idx in range(len(self.solution)):
            print("Langkah "+str(i)+":")
            self.cetakMatrix(self.solution[idx][2])
            i += 1
    def checkUniquePakeMatrix(self,matrix):
    #memeriksa apakah suatu matrix sudah ada di self.simpul atau belum dengan cek manual isi matriks
        for simpul in self.simpul:
            if self.compareMatrix(simpul[2],matrix):
                return False
        return True
    def checkUnique(self,hash_matriks):
        #memeriksa apakah suatu matrix sudah ada di self.simpul atau belum
        for simpul in self.simpul:
            if simpul[4]==hash_matriks:
                return False
        return True
    def compareMatrix(self,mat1,mat2):
    #membandingkan 2 buah matrix
        for i in range(len(mat1)):
            if(mat1[i]!=mat2[i]):
                return False
        return True
    def setStartTime(self):
        #mengassign nilai waktu mulai
        self.startTime = time.time()*1000
    def get_solution(self):
        #mendapatkan solusi 15 puzzle
        return self.solution
    def hashing(self,object):
        #combine tiap element di object jadi sebuah string
        string = ""
        for char in object:
            string+= "0"
            string+= str(char)
        return hash(string)