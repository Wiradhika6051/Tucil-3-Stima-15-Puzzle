import tkinter as tk
#sumber template GUI:https://gist.github.com/RamonWill/0422b061464097a7a0162f33e4c13a2e
class GUI(tk.Tk):
    def __init__(self,solver, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("15 Puzzle Solver")
        self.geometry("700x400")
        self.configure(background="#57536E")
        self.solver = solver

        title_styles = {"font": ("Trebuchet MS Bold", 16),"foreground":"white","background":"#57536E"}
        input_text_styles =  {"font": ("Trebuchet MS Bold", 13),"foreground":"white","background":"#3f4fab"} 

        kurang_text_styles =  {"font": ("Trebuchet MS Bold", 13),"foreground":"white","background":"#3f8bab"} 
        kurang_normal_text_styles = {"font": ("Trebuchet MS Bold", 10),"foreground":"black","background":"#3f8bab"} 
        #main_frame = tk.LabelFrame(self, bg="#57536E",height=200,width=200)
        #main_frame.grid(row=0,column=0,columnspan=3)
        #judul
        title_text = tk.Label(self,title_styles,text="15 Puzzle Solver",justify="center")
        title_text.grid(row=0,column=0,columnspan=3)

        #frame input
        input_frame = tk.Frame(self,bg="#3f4fab",height=600,width=300,borderwidth=5)
        input_frame.grid(row=1,column=0)

        input_label = tk.Label(input_frame,input_text_styles,text="Pilih Input:",justify="center",width=18)
        input_label.grid(row=0,column=0)

        generate_button = tk.Button(input_frame,text="GENERATE")
        generate_button.grid(row=1,column=0)

        choose_from_button = tk.Button(input_frame,text="CHOOSE FROM FILE")
        choose_from_button.grid(row=2,column=0)

        #frame nilai fungsi kurang(i)
        kurang_frame = tk.Frame(self,bg="#3f8bab",height=600,width=300,borderwidth=5)
        kurang_frame.grid(row = 2,column=0)

        kurang_label_1 = tk.Label(kurang_frame,kurang_text_styles,text="Nilai fungsi KURANG(i)",justify="center")
        kurang_label_1.grid(row=0,column=0,columnspan=2)

        kurang_label_2 = tk.Label(kurang_frame,kurang_text_styles,text="untuk setiap i yang",justify="center")
        kurang_label_2.grid(row=1,column=0,columnspan=2)

        kurang_label_3 = tk.Label(kurang_frame,kurang_text_styles,text="bukan ubin kosong:",justify="center")
        kurang_label_3.grid(row=2,column=0,columnspan=2)

        self.filabel = []
        status_number = 0
        for i in range(1,16):
            kurang_number = self.solver.KURANG(i)
            status_number += kurang_number
            fi_label = tk.Label(kurang_frame,kurang_normal_text_styles,text="KURANG(%d) =  %d" % (i, kurang_number),justify="center")
            fi_label.grid(row=i+2,column=0)
            self.filabel.append(fi_label)
            

        #main_frame = tk.Frame(self, bg="#706d90", height=431, width=626)  # this is the background
        #main_frame.grid(row=0,column=0,rowspan=2)

        #self.geometry("700x500")  # Sets window size to 626w x 431h pixels
        #self.resizable(0, 0)  # This prevents any resizing of the screen
       # title_styles = {"font": ("Trebuchet MS Bold", 16), "background": "blue"}
        #title_styles = {"font": ("Trebuchet MS Bold", 16),"foreground":"blue"}

        #text_styles = {"font": ("Verdana", 14),
         #              "background": "blue",
         #              "foreground": "#E1FFFF"}

        #title = tk.ti
        #frame_login = tk.Frame(main_frame, bg="blue", relief="groove", bd=2)  # this is the frame that holds all the login details and buttons
        #frame_login.place(rely=0.30, relx=0.17, height=130, width=400)

        #label_title = tk.Label(frame_login, title_styles, text="Login Page")
        #label_title.grid(row=0, column=1, columnspan=1)

        #label_user = tk.Label(frame_login, text_styles, text="Username:")
        #label_user.grid(row=1, column=0)

        #label_pw = tk.Label(frame_login, text_styles, text="Password:")
        #label_pw.grid(row=2, column=0)

        #entry_user = tk.ttk.Entry(frame_login, width=45, cursor="xterm")
        #entry_user.grid(row=1, column=1)

       # entry_pw = tk.ttk.Entry(frame_login, width=45, cursor="xterm", show="*")
        #entry_pw.grid(row=2, column=1)

        #button = tk.ttk.Button(frame_login, text="Login", command=lambda: getlogin())
        #button.place(rely=0.70, relx=0.50)

        #signup_btn = tk.ttk.Button(frame_login, text="Register", command=lambda: get_signup())
        #signup_btn.place(rely=0.70, relx=0.75)


if __name__ == '__main__':
    from TSP15Puzzle import TSP15Puzzle
    solver = TSP15Puzzle([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
    gui = GUI(solver)
    gui.mainloop()