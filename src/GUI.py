import tkinter as tk
from tkinter import filedialog
from TSP15Puzzle import TSP15Puzzle
import random
import os
import time
import threading
#sumber template GUI:https://gist.github.com/RamonWill/0422b061464097a7a0162f33e4c13a2e
class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("15 Puzzle Solver")
        self.geometry("700x700")
        self.configure(background="#57536E")
        self.matriks = None
        self.solver = None
        self.filabel = []#daftar label fungsi kurang(i)
        self.solution = None
        self.iteration = 0
        self.time_label = None
        self.node_label = None

        title_styles = {"font": ("Trebuchet MS Bold", 16),"foreground":"white","background":"#57536E"}
        input_text_styles =  {"font": ("Trebuchet MS Bold", 13),"foreground":"white","background":"#57536E"} 

        kurang_text_styles =  {"font": ("Trebuchet MS Bold", 13),"foreground":"white","background":"#57536E"} 
        self.kurang_normal_text_styles = {"font": ("Trebuchet MS Bold", 10),"foreground":"white","background":"#57536E"} 

        self.start_matrix_text_styles = {"font": ("Trebuchet MS Bold", 13),"foreground":"white","background":"#57536E"} 
        matrix_cell_text_styles = {"font": ("Trebuchet MS Bold", 10),"foreground":"black","background":"#dde4ec"} 

        sigma_text_styles = {"font": ("Trebuchet MS Bold", 13),"foreground":"white","background":"#57536E"}
        #judul
        title_text = tk.Label(self,title_styles,text="15 Puzzle Solver",justify="center")
        title_text.grid(row=0,column=0,columnspan=3)

        #frame input
        input_frame = tk.Frame(self,bg="#57536E",height=600,width=400,borderwidth=5)
        input_frame.grid(row=1,column=0)

        input_label = tk.Label(input_frame,input_text_styles,text="Pilih Input:",justify="center",width=18)
        input_label.grid(row=0,column=0,pady=6)

        generate_button = tk.Button(input_frame,text="GENERATE",command=lambda:self.generate())
        generate_button.grid(row=1,column=0,pady=5)

        choose_from_button = tk.Button(input_frame,text="CHOOSE FROM FILE",command=lambda:self.getMatrixFromFile())
        choose_from_button.grid(row=2,column=0,pady=5)

        #sigma frame
        self.sigma_frame = tk.Frame(self,bg="#57536E",height=600,width=300,borderwidth=5)
        self.sigma_frame.grid(row=1,column=1)

        self.sigma_label = tk.Label(self.sigma_frame,self.start_matrix_text_styles,text="Nilai dari nilai status reachable(sigma(i)+X): 0",justify="left")
        self.sigma_label.grid(row=0,column=0)

        self.warning_label = tk.Label(self.sigma_frame,self.start_matrix_text_styles,text="",justify="left")
        self.warning_label.grid(row=1,column=0)
        #frame nilai fungsi kurang(i)
        self.kurang_frame = tk.Frame(self,bg="#57536E",height=600,width=300,borderwidth=5)
        self.kurang_frame.grid(row = 2,column=0,rowspan=3)

        kurang_label_1 = tk.Label(self.kurang_frame,kurang_text_styles,text="Nilai fungsi KURANG(i)",justify="center")
        kurang_label_1.grid(row=0,column=0,columnspan=2)

        kurang_label_2 = tk.Label(self.kurang_frame,kurang_text_styles,text="untuk setiap i yang",justify="center")
        kurang_label_2.grid(row=1,column=0,columnspan=2)

        kurang_label_3 = tk.Label(self.kurang_frame,kurang_text_styles,text="bukan ubin kosong:",justify="center")
        kurang_label_3.grid(row=2,column=0,columnspan=2)

        #tombol solve
        solve_button = tk.Button(self,text="SOLVE",command=lambda:threading.Thread(target=self.solve()).start())
        solve_button.grid(row=2,column=1,pady=5)
       

        #menampilkan matriks awal
        start_matrix_frame = tk.Frame(self,bg="#57536E",height=600,width=300,borderwidth=5)
        start_matrix_frame.grid(row=3,column=1)

        start_matrix_label = tk.Label(start_matrix_frame,self.start_matrix_text_styles,text="Matrix awal:",justify="center")
        start_matrix_label.grid(row=0,column=0)
        
        matrix_frame = tk.Frame(start_matrix_frame,bg="#e3af74",height=200,width=200,borderwidth=5)
        matrix_frame.grid(row=1,column=0)

        self.startMatrixCell = []
        k = 0
        for i in range(4):
            for j in range(4):
                cell = tk.Label(matrix_frame,matrix_cell_text_styles,text=" ",justify="center",relief="raised",padx=5,pady=1,width=2)
                cell.grid(row=i,column=j)
                self.startMatrixCell.append(cell)
                k+=1
        #template buat nampilin matriks akhir
        self.end_matrix_frame = tk.Frame(self,bg="#57536E",height=600,width=300,borderwidth=5)
        self.end_matrix_frame.grid(row=4,column=1)

        self.end_matrix_label = tk.Label(self.end_matrix_frame,self.start_matrix_text_styles,text="Matrix Akhir:",justify="center")
        self.end_matrix_label.grid(row=0,column=0,columnspan=2)

        self.iteration_label = tk.Label(self.end_matrix_frame,self.start_matrix_text_styles,text="Iterasi Ke-0",justify="center")
        self.iteration_label.grid(row=1,column=0,columnspan=2)
        
        self.e_matrix_frame = tk.Frame(self.end_matrix_frame,bg="#e3af74",height=200,width=200,borderwidth=5)
        self.e_matrix_frame.grid(row=2,column=0,columnspan=2)

        self.endMatrixCell = []
        k = 0
        for i in range(4):
            for j in range(4):
                cell = tk.Label(self.e_matrix_frame,matrix_cell_text_styles,text=" ",justify="center",relief="raised",padx=5,pady=1,width=2)
                cell.grid(row=i,column=j)
                self.endMatrixCell.append(cell)
                k+=1
        #prev button
        self.prev_button = tk.Button(self.end_matrix_frame,text="PREV MOVE",command=lambda:self.prev(),state="disabled")
        self.prev_button.grid(row=3,column=0)        
        #next button
        self.next_button = tk.Button(self.end_matrix_frame,text="NEXT MOVE",command=lambda:self.next(),state="disabled")
        self.next_button.grid(row=3,column=1)
    def generate(self):
        #menghasilkan matriks 15 puzzle acak
        self.matriks = [0 for i in range(16)]
        for i in range(16):
            angka = random.randint(1,16)
            while angka in self.matriks:
                angka = random.randint(1,16)
            self.matriks[i] = angka
        self.solver = TSP15Puzzle(self.matriks)
        for k in range(16):
            if(self.matriks[k]==16):
                self.startMatrixCell[k]['text'] = " "
            else:
                self.startMatrixCell[k]['text'] = str(self.matriks[k])
        if(len(self.filabel)>0):
            for i in range(len(self.filabel)):
                self.filabel[i]['text'] = ""
        if(self.time_label!=None):
            self.time_label['text'] = ""
        if(self.node_label!=None):
            self.node_label['text'] = ""
        self.sigma_label['text'] = "Nilai dari nilai status reachable(sigma(i)+X): 0"
        for i in range(16):
            self.endMatrixCell[i]['text'] = " "
        self.warning_label['text'] = ""
        self.iteration_label['text'] = "Iterasi Ke-0"
        self.next_button['state'] = "disabled"
        self.prev_button['state'] = "disabled"
    def getMatrixFromFile(self):
        #memilih file input dari file
        filename = filedialog.askopenfilename(initialdir=os.getcwd())
        if(filename!=None):
            self.matriks = [0 for i in range(16)]
            i = 0
            f = open(filename, "r")
            for line in f:
                subarr = line.rstrip('\n').split(" ")
                for num in subarr:
                    self.matriks[i] = int(num)
                    i+=1
            f.close()
            self.solver = TSP15Puzzle(self.matriks)        
            for k in range(16):
              #  print(type(self.startMatrixCell[k]))
                if(self.matriks[k]==16):
                    self.startMatrixCell[k]['text'] = " "
                else:
                    self.startMatrixCell[k]['text'] = str(self.matriks[k])
            if(len(self.filabel)>0):
                for i in range(len(self.filabel)):
                    self.filabel[i]['text'] = ""
            if(self.time_label!=None):
                self.time_label['text'] = ""
            if(self.node_label!=None):
                self.node_label['text'] = ""    
            self.sigma_label['text'] = "Nilai dari nilai status reachable(sigma(i)+X): 0"   
            for i in range(16):
                self.endMatrixCell[i]['text'] = " "
            self.warning_label['text'] = ""
            self.iteration_label['text'] = "Iterasi Ke-0"
            self.next_button['state'] = "disabled"
            self.prev_button['state'] = "disabled"
    def solve(self):
        #menyelesaikan puzzle
        if(self.matriks!=None and self.solver!=None):
            self.warning_label['text'] = ""
            self.iteration_label['text'] = "Iterasi Ke-0"
            self.solver.setStartTime()
            #hitung yang kurang(i)
            status_number = 0
            for i in range(1,16):
                kurang_number = self.solver.KURANG(i)
                status_number += kurang_number
                fi_label = tk.Label(self.kurang_frame,self.kurang_normal_text_styles,text="KURANG(%d) =  %d" % (i, kurang_number),justify="center")
                fi_label.grid(row=i+2,column=0)
                self.filabel.append(fi_label)
            #Hitung nilai sigma(kurang-i)+x
            get_1_position = [ 1, 3, 4, 6, 9, 11, 12, 14 ] #jika kotak kosong berada di indeks ini, maka nilai status_number += 1
            status_number += self.solver.KURANG(16)
            if(self.matriks.index(16) in get_1_position):
                status_number += 1
            self.sigma_label['text'] = "Nilai dari nilai status reachable(sigma(i)+X): "+str(status_number)
            #mengecek status reachable
            if(status_number % 2 != 0):#kalau ganjil maka tidak reachable
                self.warning_label['text'] = "Persoalan tidak bisa diselesaikan!"
            else:
                #menyelesaikan puzzle
                jumlah_simpul = self.solver.solve()
                #menghandle kasus waktu penyelesaian terlalu lama(dinonaktifkan secara default, bisa diaktifkan dengan menghilangkan
                # tanda # di file TSP15Puzzle.py pada line 15,134,135,136)
                if(jumlah_simpul==None):
                    self.warning_label['text'] = "Persoalan membutuhkan waktu yang lama untuk diselesaikan! (melebihi 8 menit!)"
                else:
                    #menampilkan waktu eksekusi program
                    time_elapsed = self.solver.getElapsedTime()
                    if(time_elapsed<1000):#kurang dari 1 detik
                        self.time_label = tk.Label(self.sigma_frame,self.start_matrix_text_styles,text="Waktu eksekusi program: %s ms" % (round(time_elapsed,3)),justify="left")
                    elif(time_elapsed<1000*60):#kurang dari 1 menit
                        self.time_label = tk.Label(self.sigma_frame,self.start_matrix_text_styles,text="Waktu eksekusi program: %d detik %s ms" % (time_elapsed//1000,round(time_elapsed%1000,3)),justify="left")
                    elif(time_elapsed<1000*60*60):#kurang dari 1 jam
                        menit = time_elapsed//(1000*60)
                        remainder = time_elapsed%(1000*60)
                        detik = remainder //1000
                        ms = round(remainder % 1000,3)
                        self.time_label = tk.Label(self.sigma_frame,self.start_matrix_text_styles,text="Waktu eksekusi program: %d menit %d detik %s ms" % (menit,detik,ms),justify="left")
                    else: #lebih dari 1 jam
                        jam = time_elapsed//(1000*60*60)
                        rem_1 = time_elapsed%(1000*60*60)
                        menit = rem_1//(1000*60)
                        remainder = rem_1%(1000*60)
                        detik = remainder //1000
                        ms = round(remainder % 1000,3)
                        self.time_label = tk.Label(self.sigma_frame,self.start_matrix_text_styles,text="Waktu eksekusi program: %d jam %d menit %d detik %s ms" % (jam,menit,detik,ms),justify="left")                        
                    self.time_label.grid(row=1,column=0)
                    #menampilkan jumlah simpul yang dibangkitkan
                    self.node_label = tk.Label(self.sigma_frame,self.start_matrix_text_styles,text="Jumlah simpul yang dibangkitkan: %d" % (jumlah_simpul))
                    self.node_label.grid(row=2,column=0)
                    self.solution = self.solver.get_solution()
                    self.iteration = 0
                    initial_action = self.solution[self.iteration]
                    for k in range(16):
                        if(initial_action[2][k]==16):
                            self.endMatrixCell[k]['text'] = " "
                        else:
                            self.endMatrixCell[k]['text'] = str(initial_action[2][k])
                    self.prev_button['state'] = "disabled"
                    if(len(self.solution)==1):
                        self.next_button['state'] = "disabled"
                    else:
                        self.next_button['state'] = "active"
    def next(self):
        #menuju move selanjutnya
        if(self.solution!=None):
            if(self.iteration<len(self.solution)):
                self.iteration+=1
                action = self.solution[self.iteration]
                self.iteration_label['text'] = "Iterasi Ke-"+str(self.iteration)
                for k in range(16):
                    if(action[2][k]==16):
                        self.endMatrixCell[k]['text'] = " "
                    else:
                        self.endMatrixCell[k]['text'] = str(action[2][k])
                if(self.iteration==len(self.solution)-1):
                    self.next_button['state'] = "disabled"
                    if(len(self.solution)>1):
                        self.prev_button['state'] = "active"
                else:
                    self.next_button['state'] = "active"
                    self.prev_button['state'] = "active"
    def prev(self):
        #menuju move sebelumnya
        if(self.solution!=None):
            if(self.iteration>0):
                self.iteration-=1
                action = self.solution[self.iteration]
                self.iteration_label['text'] = "Iterasi Ke-"+str(self.iteration)
                for k in range(16):
                    if(action[2][k]==16):
                        self.endMatrixCell[k]['text'] = " "
                    else:
                        self.endMatrixCell[k]['text'] = str(action[2][k])
                if(self.iteration==0):
                    self.prev_button['state'] = "disabled"
                    self.next_button['state'] = "active"
                else:
                    self.prev_button['state'] = "active"
                    self.next_button['state'] = "active"