from tkinter import *
from tkinter import ttk, messagebox #กล่องข้อความ

GUI = Tk() #ทีตัวใหญ่ เคตัวเล็ก
GUI.title('โปรแกรมคำนวณราคาปลา')
GUI.geometry('600x600')

bg = PhotoImage(file="Fish.png")
# bg = PhotoImage(file= r'C:\Users\Uncle Engineer\Desktop\Basic Python\car.png')

BG = Label(GUI, image=bg)
BG.pack()

L = Label(GUI,text='กรุณากรอกราคาปลาต่อกิโลกรัม',font=("Angsana New",20))
L.pack()

j_quantity = StringVar() # เป็นตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI, textvariable=j_quantity, font=("Sarabun",20))
E1.pack(ipadx=10,ipady=5,pady=5)

L = Label(GUI,text='กรุณากรอกน้ำหนักปลา (กิโลกรัม)',font=("Angsana New",20))
L.pack()

j_quantity2 = StringVar() # เป็นตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้วอันที่2
E2 = ttk.Entry(GUI, textvariable=j_quantity2, font=("Sarabun",20))
E2.pack(ipadx=10,ipady=5,pady=5)

def Cal():
	try:
		quan = float(j_quantity.get()) #ตัวแปรราคาปลา
		B = float(j_quantity2.get()) #สร้างตัวแปรจำนวนปลาต่อกิโล
		calc = quan * B # บาทต่อกิโล * จำนวนปลาที่กรอกมา
		messagebox.showinfo('ราคาทั้งหมด','ราคาปลาทั้งหมด {} บาท'.format(calc) )
		j_quantity.set('')
		j_quantity2.set('')
		E1.focus()

	except:
		messagebox.showwarning('กรอกผิด','กรุณากรอกเฉพาะตัวเลขเท่านั้น')
		j_quantity.set('1')
		E1.focus()

B = ttk.Button(GUI, text='คำนวณ',command=Cal)
B.pack(ipadx=30,ipady=20,pady=20) #ipadx ขยายความกว้าง x/y


GUI.mainloop() # เพื่อให้โปรแกรมรันตลอดเวลา