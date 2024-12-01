import customtkinter as ctk
from customtkinter import CTkButton as btn
import threading
import win10toast

        

class App():
    class standart(ctk.CTk):
        def __init__(self):
            super().__init__()
            self.geometry('700x500')
            self.title('Text Editor')

            #Переменные проверки работы фреймов
            self.frame = False#Для проверки главного фрейма
            self.work = False#Проверка побочного фрейма при нажатии кнопки сохранения 
            self.work2 = False#Проверка фрейма 2 при открытии
            self.op = False

            self.button = ctk.CTkButton(self, text='file', height=10, width=50, command=self.create_and_del_frame)

            self.text = ctk.CTkTextbox(self, height=500, width=700)
            

            self.button.pack(padx=10, pady=10, side='left', anchor='nw') 
            self.text.pack(padx=10, pady=10, expand=True, fill=ctk.BOTH)

           

            

        def create_and_del_frame(self):
            #self.text.get('0.0', 'end')
            if self.frame:
                self.frm.destroy()
                self.frame = False
                 #условие при котором проверяется создан ли фрейм для кнопки сохранения или нет если да то его нужно уничтожить
                if self.work:
                    self.save_frame.destroy()
                    self.work = False# переменная для отслеживания работы фрейма при нажатии кнопки сохранения

                if self.work2:
                    self.open_frame.destroy()
                    self.work2 = False

            else:
                 self.frm = ctk.CTkFrame(self, width=150, height=100, fg_color='gray')
                 self.buttons_for_btn_file()
                 #self.frm.pack(side='left', padx=10, pady=50, anchor='w')
                 self.frm.place(x=5, y=50)
                 self.frame = True

        def buttons_for_btn_file(self):
            #характеристики кнопок
            width = 20
            height = 10
            color = 'gray'

            #создание кнопок
            self.save_file = btn(self.frm, text='save file', width=width, height=height, fg_color=color, command=self.save)
            self.what_save_file = btn(self.frm, text='save with...', width=width, height=height, fg_color=color)
            self.open = btn(self.frm, text='open file', width=width, height=height, fg_color=color, command=self._open_)
            #self.options = btn(self.frm, text='options', width=width, height=height, fg_color=color, command=self._options_)
            #self.new_window = btn(self.frm, text='new window', width=width, height=height, fg_color=color, command=self.new)
            self.exit = btn(self.frm, text='exit', width=width, height=height, fg_color=color, command=lambda:exit())
        
             
            #отрисовка кнопок
            #self.new_window.pack(padx=10, pady=10)
            self.save_file.pack(padx=10, pady=10)
            #self.what_save_file.pack(padx=10, pady=10)
            self.open.pack(padx=10, pady=10)
            #self.options.pack(padx=10, pady=10)
            self.exit.pack(padx=10, pady=10)

        def save(self):#данная функция находиться в  1 кнопке сохранения файла
            try:
                
                if self.work:
                    self.save_frame.destroy()
                    self.work = False
                else:
                    self.save_frame = ctk.CTkFrame(self, fg_color='gray')
                    self.btn = btn(self.save_frame, height=30, width=20, text='save', fg_color='gray', command=self.save_file_)
                    self.entry = ctk.CTkEntry(self.save_frame, width=100, height=30)

                    self.save_frame.place(x=85, y=55)
                    self.btn.pack(side='right')
                    self.entry.pack()

                    self.work = True

            except Exception as ex:
                print(ex)    
        
        def save_file_(self):
            try:               
                with open(self.entry.get(), 'w') as file:
                    file.write(self.text.get('0.0', 'end'))
                    thread = threading.Thread(daemon=True, target=lambda:win10toast.ToastNotifier().show_toast('WRITTEN', 'WRITTEN'))
                    thread.start()
            except Exception as ex:
                try:
                    thread = threading.Thread(daemon=True, target=lambda:win10toast.ToastNotifier().show_toast('ERROR', str(ex)))
                    thread.start()
                except:pass

            

        def _open_(self):
            
                
                if self.work2:
                    self.open_frame.destroy()
                    
                    self.work2 = False
                else:
                    self.open_frame = ctk.CTkFrame(self, fg_color='gray')
                    self.btn2 = btn(self.open_frame, height=30, width=20, text='open', fg_color='gray', command=self.open_file)
                    self.entry2 = ctk.CTkEntry(self.open_frame, width=100, height=30)

                    self.open_frame.place(x=85, y=95)
                    self.btn2.pack(side='right')
                    self.entry2.pack()

                    self.work2 = True

                


        def open_file(self):
            try:
                with open(self.entry2.get(), 'r') as file:
                    read = file.read()  
                    self.text.delete('1.0', ctk.END)    
                    self.text.insert('0.0', read)
            except Exception as ex:
                try:
                    thread = threading.Thread(daemon=True, target=lambda:win10toast.ToastNotifier().show_toast('ERROR', str(ex)))
                    thread.start()                   
                except:pass


                

                       
                
                
                
if __name__ == '__main__':
    App.standart().mainloop()