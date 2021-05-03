#libraray management
from tkinter import *
from tkinter import messagebox as msg


#setting
setup={
'width':'720',
'height':'1240',
'bg_color':'light grey',
'homepage_btn1_bg':'light blue',
'box bg':'blue',
'box fg':'white',
'canvas_button_bg':'blue'
}

root=Tk()
root.geometry(f"{setup['width']}x{setup['height']}")

import os
if os.path.isfile('books.data')==False:
	with open('books.data','w') as f:
		f.write('python,java,c++,node,frontend with kivy,networking,django,pygame,python OOPs')

class buttonFunctions:
	@staticmethod
	def issueok():
		try:
			which_book=listbox.curselection()
			msg.showinfo('info',books[which_book[0]]+' Isuued for \n till Next week .\nHopefully You enjoy \n(づ￣ ³￣)づ')
			with open('books.data','r') as f:
				b=f.readlines()
			instant_books=b[0].split(',')
			instant_books.remove(books[which_book[0]])
			with open('return.data','a') as f:
				f.write(','+books[which_book[0]])
			with open('books.data','w') as f:
				f.write(instant_books[0])
			instant_books.pop(0)
			with open('books.data','a') as f:
				for i in instant_books:
					f.write(','+i)
		except:
			msg.showwarning('Tip !','please Select a book \nfrom list !')
			buttonFunctions().issuebook()
		
	@staticmethod
	def ok():
		if msg.askquestion('library','Hope You liked books\n would you like to issue Book ??')=='yes':
			buttonFunctions().issuebook()
	def showbooks(self):
		issue=Toplevel()
		issue.title('Issue Centre')
		issue.geometry('650x1000+20+170')
		#books
		global books
		with open('books.data','r') as f:
			self.b=f.readlines()
		books=self.b[0].split(',')
		#list
		Label(issue,text='Select Your Book').place(x=20,y=20)
		global listbox
		listbox=Listbox(issue,width=31,height=15,fg=setup['box fg'],bg=setup['box bg'])
		for i in range(len(books)):
			listbox.insert(i,f' {i+1} | {books[i]}')
		listbox.place(x=50-30,y=70)
		Label(issue,text=f'Total Books : {len(books)}').place(x=30,y=700)
		Button(issue,text='OK',padx=130,bg='yellow',command=buttonFunctions.ok).place(x=170,y=800)

	@staticmethod
	def issuecancel():
		msg.showinfo('Soorry !','Felling sorry for not offering\n books that you like\n (╥╯﹏╰╥)ง')	
	def issuebook(self):
		issue=Toplevel()
		issue.title('Issue Centre')
		issue.geometry('650x1000+20+170')
		#books
		global books
		with open('books.data','r') as f:
			self.b=f.readlines()
		books=self.b[0].split(',')
		#list
		Label(issue,text='Select Your Book').place(x=20,y=20)
		global listbox
		listbox=Listbox(issue,width=31,fg=setup['box fg'],bg=setup['box bg'])
		for i in range(len(books)):
			listbox.insert(i,f' {i+1} | {books[i]}')
		listbox.place(x=50-30,y=70)
		Button(issue,text='issue',command=buttonFunctions.issueok).place(x=100,y=800)
		Button(issue,text='cancel',command=buttonFunctions().issuecancel).place(x=400,y=800)
		
	@staticmethod
	def save():
		bookname=book_name.get()
		with open('books.data','a') as f:
			f.write(f',{bookname}')
		msg.showinfo('Done',f'{bookname} is added \nin library.')
		
	def add_book(self):
		add_book=Toplevel()
		add_book.title('Add book')
		add_book.geometry('650x1000+20+170')
		Label(add_book,text='Book Name').place(x=20,y=20)
		global book_name
		book_name=StringVar()
		self.book_entry=Entry(add_book,textvariable=book_name,width=30).place(x=20,y=65)
		Button(add_book,text='save',bg='light green',command=buttonFunctions.save).place(x=30,y=800)
	@staticmethod
	def returncancel():
		msg.showinfo('info','Returning Process cancelled !')
	def returnok(self):
		which_book=listbox1.curselection()	
		try:
			msg.showinfo('returned',f'{retrn[which_book[0]]}\nreturned sucessfully.\nHope you enjoyed book!')
			with open('return.data','r') as f:
				b=f.readlines()
			instant_books=b[0].split(',')
			instant_books.remove(retrn[which_book[0]])
			with open('return.data','w') as f:
				f.write(instant_books[0])
			instant_books.pop(0)
			with open('return.data','a') as f:
				for i in instant_books:
					f.write(','+i)
			with open('books.data','a') as f:
				f.write(f',{retrn[which_book[0]]}')
		except:
			msg.showwarning('Tip !','please Select a book \nfrom list !')
			buttonFunctions().issuebook()
		
	def returnbook(self):
		try:
			rtrn=Toplevel()
			rtrn.title('Return Centre')
			rtrn.geometry('650x1000+20+170')
			with open('return.data','r') as f:
				ret=f.readlines()
			global retrn
			retrn=ret[0].split(',')
			retrn.pop(0)
		
			#list
			Label(rtrn,text='Select Your Book to return').place(x=20,y=20)
			global listbox1
			listbox1=Listbox(rtrn,width=31,fg='white',bg=setup['box bg'])
			for i in range(len(retrn)):
				listbox1.insert(i,f' {i+1} | {retrn[i]}')
			listbox1.place(x=50-30,y=70)
			Button(rtrn,text='return',command=buttonFunctions().returnok).place(x=100,y=800)
			Button(rtrn,text='cancel',command=buttonFunctions().returncancel).place(x=400,y=800)
		except:
			msg.showwarning('Info','please First issue a \n book from Libraray !')

		
FUN=buttonFunctions()
def exit():
	quit()
class Library:
	def __init__(self):
		self.can=Canvas(root,width=setup['width'],height=setup['height'],bg=setup['bg_color']).place(x=0,y=0)
		self.quote='"Literacy is the most basic currency, of the knowledge economy" ,—Barack Obama'.split(',')
	def homepage(self):
		Label(self.can,text='COMPUTER SCIENCE LIBRARY',font='vardana 11 bold',bg=setup['bg_color']).place(x=30,y=30)
		Label(self.can,text='owner - DURGESH RAWAT',font='vardana 6 italic',bg=setup['bg_color']).place(x=210,y=90)
		Label(self.can,text='_'*67,font='vardana 4 bold',bg=setup['bg_color']).place(x=20,y=136)
		self.placex,self.placey=[100,260,340],[200,240,280]
		for i in range(len(self.quote)):
			Label(self.can,text=self.quote[i],font='vardana 7 italic',bg=setup['bg_color'],fg='red').place(x=self.placex[i],y=self.placey[i])
		Label(self.can,text='_'*67,font='vardana 4 bold',bg=setup['bg_color']).place(x=20,y=336)
		color=Canvas(self.can,height=420,width=400,bg=setup['canvas_button_bg']).place(x=120,y=575)
		Button(color,text='show BOOK',padx=100,bg=setup['homepage_btn1_bg'],command=FUN.showbooks).place(x=175,y=860-120-10-120)
		Button(color,text='Issue BOOK',padx=100,bg=setup['homepage_btn1_bg'],command=FUN.issuebook).place(x=175,y=860-120-60)
		Button(color,text='return BOOK',padx=97,bg=setup['homepage_btn1_bg'],command=FUN.returnbook).place(x=175,y=870-60-60)
		Button(color,text='add BOOK',padx=112,bg=setup['homepage_btn1_bg'],command=FUN.add_book).place(x=175,y=940-60-60)
		Button(color,text='  Exit  ',padx=144,bg=setup['homepage_btn1_bg'],command=exit).place(x=175,y=1010-60-60)
		
library=Library()
library.homepage()
root.mainloop()