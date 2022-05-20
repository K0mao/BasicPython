#GUI-calculator.py

from tkinter import *
from tkinter import ttk,messagebox

GUI = Tk() #ทีตัวใหญ่ เคตัวเล็ก
GUI.title('โปรแกรมคำนวณราคาผัก')
GUI.geometry('700x600')

bg = PhotoImage(file='car1.png')
BG = Label(GUI,image=bg)
BG.pack()

L = Label(GUI,text='กรุณากรอกจำนวนผัก(กิโลกรัมละ28บาท)',font=(None,20))
L.pack()


V_quantity = StringVar() #เป็นตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI,textvariable=V_quantity,font=(None,20))
E1.pack()

def Cal():
    try :
        quan =float( V_quantity.get())
        calc = quan * 28 # 28บาทต่อกิโล * จำนวนปลาที่กรอกมา
        messagebox.showinfo('ราคาทั้งหมด','ราคาผักทั้งหมด {} บาท'.format(calc))
        V_quantity.set('')
        E1.focus()
    except:
        messagebox.showwarning('กรอกผิด','กรุณากรอกเฉพาะตัวเลขเท่านั้น')
        V_quantity.set('1')
        E1.focus()

B = ttk.Button(GUI,text='คำนวณ',command=Cal)
B.pack(ipadx=30,ipady=20,pady=20) #ipadx ขยายความกว้าง x/y

GUI.mainloop() #เพื่อให้โปรแกรมรันตลอดเวลา