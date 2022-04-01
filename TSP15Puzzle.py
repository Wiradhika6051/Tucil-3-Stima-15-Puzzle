import re
import time
import copy
from operator import itemgetter

from numpy import array_equal
class TSP15Puzzle:
    def __init__(self,matrix):
        self.matrix = matrix
        self.startTime = time.time()*1000 # waktu mulai dalam ms
        self.endTime = None #waktu algoritma selesai
        self.solution = []
        self.endNode = None
        self.simpul = []#simpul yang sudah pernah dibangkitkan
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
        #struktur data simpul: simpul = (indeks,parent,isi, cost)->disimpan di atribut kelas
        #return (jumlah_simpul_yang_berhasil_dibangkitkan)
        simpul_hidup = []
        #inisialisasi simpul pertama
        i = 0
        first_node = [i,-1,self.matrix,0]
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
            temp[idx_kosong] = temp[idx_kosong-4]
            temp[idx_kosong-4] = 16
            node = [i,0,temp,self.getCost(temp)]
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
            temp[idx_kosong] = temp[idx_kosong+1]
            temp[idx_kosong+1] = 16
            node = [i,0,temp,self.getCost(temp)]
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
            temp[idx_kosong] = temp[idx_kosong+4]
            temp[idx_kosong+4] = 16
            node = [i,0,temp,self.getCost(temp)]
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
            temp[idx_kosong] = temp[idx_kosong-1]
            temp[idx_kosong-1] = 16
            node = [i,0,temp,self.getCost(temp)]
            simpul_hidup.append(node) 
            self.simpul.append(node)  
            i+=1   
            jumlah_simpul+=1
            if(self.g(node[2])==0):
                self.endNode = copy.deepcopy(node)
                #solusi ketemu
                found = True
        while(simpul_hidup and not found):#selama masih ada simpul hidup
            temp = copy.deepcopy(simpul_hidup)
            simpul_hidup = sorted(temp,key=itemgetter(3))#urutkan dari cost yang terkecil
            #print("before:")
            #print(simpul_hidup)
            node = simpul_hidup.pop(0)
            #print("after:")
            #print(simpul_hidup)
            print("panjang",len(simpul_hidup))
            print("aa")
            if(self.g(node[2])==0):
                print("ab")
                self.endNode = copy.deepcopy(node)
                #solusi ketemu
                break
            #generasikan simpul lain
            idx_kosong = node[2].index(16)
            # 1->ke atas
            print(idx_kosong)
            if(idx_kosong//4 > 0):#bukan di baris pertama
                temp = copy.deepcopy(node[2])
                temp[idx_kosong] = temp[idx_kosong-4]
                temp[idx_kosong-4] = 16
                jumlah_simpul+=1
                if self.checkUnique(temp):
                    node = [i,node[0],temp,self.getCost(temp)]
                    simpul_hidup.append(node)
                    self.simpul.append(node)
                    i+=1
            # 2->ke kanan
            if(idx_kosong%4 != 3):#bukan di kolom terakhir
                temp = copy.deepcopy(node[2])
                temp[idx_kosong] = temp[idx_kosong+1]
                temp[idx_kosong+1] = 16
                jumlah_simpul+=1
                if self.checkUnique(temp):
                    node = [i,node[0],temp,self.getCost(temp)]
                    simpul_hidup.append(node)
                    self.simpul.append(node)
                    i+=1
            # 3->ke bawah
            if(idx_kosong//4 != 3):#bukan di baris terakhir
                temp = copy.deepcopy(node[2])
                temp[idx_kosong] = temp[idx_kosong+4]
                temp[idx_kosong+4] = 16
                jumlah_simpul+=1
                if self.checkUnique(temp):
                    node = [i,node[0],temp,self.getCost(temp)]
                    simpul_hidup.append(node) 
                    self.simpul.append(node)
                    i+=1       
            # 4->ke kiri
            if(idx_kosong%4 != 0):#bukan di kolom pertama
                temp = copy.deepcopy(node[2])
                temp[idx_kosong] = temp[idx_kosong-1]
                temp[idx_kosong-1] = 16
                jumlah_simpul+=1
                if self.checkUnique(temp):
                    node = [i,node[0],temp,self.getCost(temp)]
                    simpul_hidup.append(node) 
                    self.simpul.append(node)  
                    i+=1   
            #print("asu")
        #mendapatkan path rute
        self.getPath(self.endNode)

        self.endTime = time.time()*1000
        return jumlah_simpul
    def getIDX(self,node_idx,matrix):
        #mendaptkan index suatu node
        i = 0
        print("anyink")
        print(matrix)
        print(node_idx)
        for elmt in matrix:
            if(elmt[0]==node_idx):#indeksnya sama
                return i
            i+=1
    def getPath(self,node):
        #mendapatkan path dari end node ke root
        #print("a")
        #print(node)
        #print(self.simpul)
        node_idx = self.getIDX(node[0],self.simpul)
        self.solution.append(self.simpul[node_idx])
        while(node_idx!=0):#bukan root,loop sampe ketemu loop
            node_idx = self.getIDX(node[1],self.simpul)
            node = self.simpul[node_idx]
            self.solution.append(node)
        self.solution = sorted(self.solution,key=itemgetter(0),reverse=True)
    def showStep(self):
        i = 1
        for idx in range(len(self.solution)-1,-1,-1):
            print("Langkah "+str(i)+":")
            self.cetakMatrix(self.solution[idx][2])
            i += 1
    def checkUnique(self,matrix):
    #memeriksa apakah suatu matrix sudah ada di self.simpul atau belum
        for simpul in self.simpul:
            if self.compareMatrix(simpul[2],matrix):
                return False
        return True

    def compareMatrix(self,mat1,mat2):
    #membandingkan 2 buah matrix
        lenmat = len(mat1)
        if(lenmat!=len(mat2)):
            return False
        for i in range(lenmat):
            if(mat1[i]!=mat2[i]):
                return False
        return True

if __name__ == '__main__':
    #array = [[1,1,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],200],[2,1,[1,2,3,4,5,7,6,8,9,10,11,12,13,14,15,16],100],[3,1,[1,2,4,3,5,6,7,8,9,10,11,12,13,14,15,16],150]]
    #array = sorted(array,key=itemgetter(3))
    #for item in array:
    #    print(item)
    import hashlib 
    array_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    str_1 = ""
    for char in array_1:
        str_1 = str_1 + "0" + str(char)
    print(str_1)
    array_2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,15]
    str_2 = ""
    for char in array_2:
        str_2 = str_2 + "0" + str(char)
    print(str_2)
    str_1.encode("utf-8")
    str_2.encode("utf-8")
    h1 = hashlib.sha3_512() # Python 3.6+
    h1.update(str_1)
    h1.hexdigest()
    h2 = hashlib.sha3_512() # Python 3.6+
    h2.update(str_2)
    h2.hexdigest()