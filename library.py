from tkinter import *
from sqlalchemy import create_engine
root = Tk()
class Library:
	def __init__(self, master):
		master.config(bg = "#238")
		master.title("Library Management System")
		master.geometry("620x500")


		#____________________Admin login menu___________________________
		self.warning_label = Label(master, text="To use this app you must authorized admin", bg ="#238", fg="#984", font =('Arial', 15,))
		self.admin_name_label = Label(master, text="Admin name", bg ="#238", fg="white", font =('Arial', 15))
		self.admin_name_entry = Entry(master, fg = "white", bg="#121", font=("Arial", 12), relief='flat')
		self.admin_password_label = Label(master, text="Admin password", bg ="#238", fg="white", font =('Arial', 15))
		self.admin_password_entry = Entry(master, fg = "white", bg="#121", font=("Arial", 12), relief='flat')
		self.login_button = Button(master, text = "Login", bg = '#432', fg='green', font=('verdana', 15), command=self.admin_verify)
		self.invalid_label = Label(master, text="Invalid username or password", bg ="#238", fg="red", font =('verdana', 15,))


		#____________________student registration menu___________________________
		self.student_welcome_label = Label(master, text="Registration of Legal student", bg ="#238", fg="#984", font =('Arial', 15,))
		self.student_firstname_label = Label(master, text="student name", bg ="#238", fg="white", font =('Arial', 15))
		self.student_firstname_entry = Entry(master, fg = "white", bg="#121", font=("Arial", 12), relief='flat')
		self.student_lastname_label = Label(master, text="student lastaname", bg ="#238", fg="white", font =('Arial', 15))
		self.student_lastname_entry = Entry(master, fg = "white", bg="#121", font=("Arial", 12), relief='flat')
		self.add_button = Button(master, text = "add", bg = '#432', fg='green', font=('verdana', 15), command=self.add_member_student)
		self.invalid_students = Label(master, text="Both firstname and lastname are required", bg ="#238", fg="red", font =('verdana', 15,))



		#___________________placing the Admin login menu__________________________

		self.warning_label.place(x=80, y=50)
		self.admin_name_label.place(x=200, y=100)
		self.admin_name_entry.place(x=200, y=150)
		self.admin_password_label.place(x=200, y=200)
		self.admin_password_entry.place(x=200, y=250)
		self.login_button.place(x=200, y=300)



		#=======================main menu======================================
		self.welcome_label =  Label(master, text="welcome", bg ="#238", fg="white", font =('Arial', 20, 'bold'))
		#=======================Borrow-book====================================
		self.borrow_menu = Button(master, text="Borrow a Book", bg="#432", fg="white", font=('verdana',15),  command=lambda:self.screen_menu_display('borrow'))
		#=======================Return-book====================================
		self.return_menu = Button(master, text="Return a Book", bg="#432", fg="white", font=('verdana',15),command=lambda:self.screen_menu_display('return_menu'))
		
		self.add_student_menu = Button(master, text = "Add new student", bg = '#432', fg='white', font=('verdana', 15),command=lambda:self.screen_menu_display('register'))
		

		#======================Return menu======================================
		self.return_book =  Label(master, text="Returning a book", bg ="#258", fg="#147", font =('Arial', 12))
		self.search_entry = Entry(master, fg = "white", bg="#121", font=("Arial", 12), relief='flat')
		self.search_button = Button(master, text="Search a book", bg="#432", fg="#589", font=('verdana',10),  command=self.search_book_name)
		self.membermenu_label =  Label(master, bg ="#238", fg="white", font =('Arial', 12))
		self.idnomenu_label =  Label(master, bg ="#238", fg="white", font =('Arial', 12))
		self.firstname_menu_label =  Label(master, bg ="#238", fg="white", font =('Arial', 12))
		self.surname_menu_label = Label(master, bg ="#238", fg="white", font =('Arial', 12))
		self.bookid_menu_label =  Label(master, bg ="#238", fg="white", font =('Arial', 12))
		self.booktitle_menu_label =  Label(master, bg ="#238", fg="white", font =('Arial', 12))
		self.author_menu_label =  Label(master, bg ="#238", fg="white", font =('Arial', 12))
		self.date_menu_label =  Label(master, bg ="#238", fg="white", font =('Arial', 12))
		self.returned_menu_button=Button(master, text="Return", bg="#432", fg="#589", font=('verdana',10), command=lambda:self.book_status(status=2))
		self.next_menu_button=Button(master, text="Next", bg="#432", fg="#589", font=('verdana',10), command=self.next_book)
		self.back_menu_button=Button(master, text="back", bg="#432", fg="#589", font=('verdana',10), command=lambda:self.next_book(True))
		#==================Student information ====================
		self.student_info = Label(master, text="STUDENT INFORMATION", bg ="#238", fg="#187", font =('Arial', 15))
		#=============membership type====================
		self.member_type_label = Label(master, text="Member Type", bg="#238", fg="#492", font=('verdana', 12))
		self.member_type_entry = Entry(master, fg = "white", bg="#121", font=("Arial", 12), relief='flat')
		#=============membership-verifier=================
		self.member_verifier = Label(master, text ="membership type required", bg='#238', font=('verdana', 12), fg="red")
		#=============Ref no/ ID no =====================
		self.id_no_label = Label(master, text="ID Number", bg="#238", fg="#492", font=('verdana', 12))
		self.id_no_entry = Entry(master, fg = "white", bg="#121", font=("Arial", 12))
		#=============ID no-verifier=================
		self.id_no_verifier = Label(master, text ="id no required", bg='#238', font=('verdana', 12), fg="red")
		#=============First_name==========================
		self.firstname_label = Label(master, text="First Name", bg="#238", fg="#492", font=('verdana', 12))
		self.firstname_entry = Entry(master, fg = "white", bg="#121", font=("Arial", 12))
		#=============Firstname-verifier=================
		self.firstname_verifier = Label(master, text ="firstname required", bg='#238', font=('verdana', 12), fg="red")
		#=============Surname=============================
		self.surname_label=Label(master, text="Surname", bg="#238", fg="#492", font=('verdana', 12))
		self.surname_entry = Entry(master, fg = "white", bg="#222", font=("Arial", 12))
		#=============surname-verifier=================
		self.surname_verifier = Label(master, text ="surname required", bg='#238', font=('verdana', 12), fg="red")
		#==================book information ====================
		self.book_info = Label(master, text="BOOK INFORMATION", bg ="#238", fg="#187", font =('Arial', 15))
		#=============book ID ===========================	
		self.bookid_label = Label(master, text="Book ID", bg="#238", fg="#492", font=('verdana', 12))
		self.bookid_entry =  Entry(master, fg = "white", bg="#222", font=("Arial", 12))
                #=============book id-verifier=================
		self.bookid_verifier = Label(master, text ="book id required", bg='#238', font=('verdana', 12), fg="red")
		#=============book_title=========================
		self.booktitle_label = Label(master, text="Book Title", bg="#238", fg="#492", font=('verdana', 12))
		self.booktitle_entry =  Entry(master, fg = "white", bg="#222", font=("Arial", 12))
                #=============book title -verifier=================
		self.booktitle_verifier = Label(master, text ="book title required", bg='#238', font=('verdana', 12), fg="red")
		#=============book-Author========================
		self.author_label = Label(master, text="Book Author", bg="#238", fg="#492", font=('verdana', 12))
		self.author_entry =  Entry(master, fg = "white", bg="#222", font=("Arial", 12))
                #=============book author-verifier=================
		self.bookauthor_verifier = Label(master, text ="book author required", bg='#238', font=('verdana', 12), fg="red")
		#============Date borrowed========================
		self.date_borrowed_label = Label(master, text="Date borrowed", bg="#238", fg="#492", font=('verdana', 12))
		self.date_borrowed_entry =  Entry(master, fg = "white", bg="#222", font=("Arial", 12))
                #=============date-verifier=================
		self.date_verifier = Label(master, text ="Date required", bg='#238', font=('verdana', 12), fg="red")
		#===========borrow=================================
		self.borrow_button = Button(master, text="Borrow", bg="#438", font=('verdana', 15), fg="#763", relief='flat', command=lambda:self.borrow_verification(0))
	        #self.borrow_button.place(x=250, y=400)
		#===========back-to-menu=================================
		self.backmenu_button=Button(master, text="<---", bg="#312", font=('verdana', 15), fg="#763", relief='flat', command=self.screen_menu_display)
	        #self.borrow_button.place(x=250, y=400)

		self.student_absent = Label(master, text="The student is not registered", bg ="#238", fg="red", font =('Arial', 15))

		#======================initializing database================================
		self.db = create_engine('sqlite:///database.db')
		
		#_____________checking the borrowing table state__________________

		if 'borrow' in self.db.table_names():
			self.database = self.db.connect()
			pass
		#________________creating a borrowing table__________________
		else:	
			query='create table if not exists borrow(membership blob, id_no blob, firstname blob, surname blob,book_id blob, booktitle blob, author 					blob, date blob)'
			self.database = self.db.connect()
			self.database.execute(query)

		#_______________checking the student table__________________________
		if 'students' in self.db.table_names():
			self.students_db = self.db.connect()
			pass
		#________________creating the student table________________
		else:
			query = 'create table if not exists students(firstname blob, lastname blob)'
			self.student_db = self.db.connect()
			self.student_db.execute(query)

		#_______________checking the admin table___________________
		if 'admin' in self.db.table_names():
			self.admin_db = self.db.connect()
			pass
		#________________creating admin table_________________________
		else:
			query = 'create table if not exists admin(username blob, password blob)'
			self.admin_db = self.db.connect()
			self.admin_db.execute(query)

	#_________________admin verification_____________________
	def admin_verify(self):
		self.admin_name = self.admin_name_entry.get()
		self.admin_password = self.admin_password_entry.get()
		query = "select * from admin where username = '{}' and password='{}'".format(self.admin_name, self.admin_password)
		admin_authentification = self.admin_db.execute(query).fetchall()
		if admin_authentification:
			print(admin_authentification)
			self.start_window()
		else:
			self.invalid_label.place(x=200, y=350 )

	#_________________adding new student______________________
	def add_member_student(self, test = None):
		if test:
			firstname = self.firstname_entry.get()
			lastname = self.surname_entry.get()
			firstname = firstname.lower()
			lastname = lastname.lower()
			query = "select * from students where firstname = '{}' and lastname='{}'".format(firstname, lastname)
			student_authentification = self.students_db.execute(query).fetchall()
			if student_authentification:
				return True
			return False
		else:
			firstname = self.student_firstname_entry.get()
			lastname = self.student_lastname_entry.get()
			firstname = firstname.lower()
			lastname = lastname.lower()
			if not firstname or  not lastname:
				self.invalid_students.place(x = 100, y = 380)
			else:
				self.invalid_students.place_forget()
				query = 'insert into students(firstname, lastname) values("{}", "{}")'.format(firstname, lastname)
				self.students_db.execute(query)
				self.delete_registration()
				print('student added')


	def start_window(self):
	#________________Forgeting login menu____________________
		self.admin_name_label.place_forget()
		self.admin_name_entry.place_forget()
		self.admin_password_label.place_forget()
		self.admin_password_entry.place_forget()
		self.login_button.place_forget()
		self.warning_label.place_forget()
		self.invalid_label.place_forget()

	#_____________starting main menu________________________
		self.place_main_menu(place = True)

	
	def place_main_menu(self, place=None):
		if place:
			self.welcome_label.place(x=250, y=100)
			self.borrow_menu.place(x=150, y=255)
			self.return_menu.place(x=350, y=255)
			self.add_student_menu.place(x=250, y=350)
			self.back_menu_button.place_forget()
			print('added')	
		else:
			self.welcome_label.place_forget()
			self.borrow_menu.place_forget()
			self.return_menu.place_forget()
			self.add_student_menu.place_forget()
			
		#_________________student registration menu________________
	def student_registration_menu(self, place=None):
		if place:
			self.backmenu_button.place(x=0, y=0)
			self.student_welcome_label.place(x=80, y= 50)
			self.student_firstname_label.place(x = 200,y=100 )
			self.student_firstname_entry.place(x = 200, y = 150)
			self.student_lastname_label.place(x = 200, y = 200)
			self.student_lastname_entry.place(x =200, y=250)
			self.add_button.place(x = 200, y = 300)
		else:
			self.student_firstname_label.place_forget()
			self.student_firstname_entry.place_forget()
			self.student_lastname_label.place_forget()
			self.student_lastname_entry.place_forget()
			self.add_button.place_forget()
			self.back_menu_button.place_forget()
			self.student_welcome_label.place_forget()
			self.invalid_students.place_forget()

	def place_return_menu(self, place=None):
		if place:
			self.backmenu_button.place(x=0, y=0)
			self.search_entry.place(x=150,y=40)
			self.search_button.place(x=350, y=40)
			self.return_book.place(x=200 , y=30)
			self.membermenu_label.place(x=200, y=90)
			self.idnomenu_label.place(x=200 , y=120)
			self.firstname_menu_label.place(x=200, y=150)
			self.surname_menu_label.place(x=200, y=180)
			self.bookid_menu_label.place(x=200, y=210)
			self.booktitle_menu_label.place(x=200, y=240)
			self.author_menu_label.place(x=200,y=270)
			self.date_menu_label.place(x=200, y=300)
		else:
			self.return_book.place_forget()
			self.membermenu_label.place_forget()
			self.idnomenu_label.place_forget()
			self.firstname_menu_label.place_forget()
			self.surname_menu_label.place_forget()
			self.bookid_menu_label.place_forget()
			self.booktitle_menu_label.place_forget()
			self.author_menu_label.place_forget()
			self.date_menu_label.place_forget()
			self.returned_menu_button.place_forget()
			self.search_entry.place_forget()
			self.search_button.place_forget()
			self.next_menu_button.place_forget()
			self.back_menu_button.place_forget()
	

	def place_borrow_menu(self, place = None):
		if place:
			self.backmenu_button.place(x=0, y=0)
			self.student_info.place(x=180, y=60)	
			self.member_type_label.place(x=80, y=100)
			self.member_type_entry.place(x=210, y=100)
			self.id_no_label.place(x=80, y=130)
			self.id_no_entry.place(x=210, y=130)
			self.firstname_label.place(x=80, y=160)
			self.firstname_entry.place(x=210, y=160)
			self.surname_label.place(x=80, y=190)
			self.surname_entry.place(x=210, y=190)
			self.book_info.place(x=200, y=225)	
			self.bookid_label.place(x=80, y=260)
			self.bookid_entry.place(x=210, y=260)
			self.booktitle_label.place(x=80, y=290)
			self.booktitle_entry.place(x=210, y=290)
			self.author_label.place(x=80, y=320)
			self.author_entry.place(x=210, y=320)
			self.date_borrowed_label.place(x=80,y=350)
			self.date_borrowed_entry.place(x=210, y=350)
			self.borrow_button.place(x=250, y=400)
		else:
			self.student_info.place_forget()
			self.member_type_label.place_forget()
			self.member_type_entry.place_forget()
			self.id_no_label.place_forget()
			self.id_no_entry.place_forget()
			self.firstname_label.place_forget()
			self.firstname_entry.place_forget()
			self.surname_label.place_forget()
			self.surname_entry.place_forget()
			self.book_info.place_forget()
			self.bookid_label.place_forget()
			self.bookid_entry.place_forget()
			self.booktitle_label.place_forget()
			self.booktitle_entry.place_forget()
			self.author_label.place_forget()
			self.author_entry.place_forget()
			self.date_borrowed_label.place_forget()
			self.date_borrowed_entry.place_forget()
			self.borrow_button.place_forget()
			self.student_absent.place_forget()

	def borrow_menu_delete(self):
		self.member_type_entry.delete(0, 'end')
		self.id_no_entry.delete(0, 'end')
		self.firstname_entry.delete(0, 'end')
		self.surname_entry.delete(0, 'end')
		self.bookid_entry.delete(0, 'end')
		self.booktitle_entry.delete(0, 'end')
		self.author_entry.delete(0, 'end')
		self.date_borrowed_entry.delete(0, 'end') 

	def delete_registration(self):
		self.student_firstname_entry.delete(0, 'end')
		self.student_lastname_entry.delete(0, 'end')
	
	def verifier_delete(self):
		self.member_verifier.place_forget()
		self.id_no_verifier.place_forget()
		self.firstname_verifier.place_forget()
		self.surname_verifier.place_forget()
		self.bookid_verifier.place_forget()
		self.booktitle_verifier.place_forget()
		self.bookauthor_verifier.place_forget()
		self.date_verifier.place_forget()

	def return_delete(self):
		self.membermenu_label.config(text ='')
		self.idnomenu_label.config(text = '')
		self.firstname_menu_label.config(text ='')
		self.surname_menu_label.config(text ='')
		self.bookid_menu_label.config(text ='')
		self.booktitle_menu_label.config(text ='')
		self.author_menu_label.config(text ='')
		self.date_menu_label.config(text ='')
		

	def screen_menu_display(self,menu='main_menu'):
		if menu=='main_menu':
			self.place_main_menu(place=True)
			self.place_return_menu()
			self.place_borrow_menu()
			self.verifier_delete()
			self.return_delete()
			self.student_registration_menu()
			self.delete_registration()
		elif menu=='return_menu':
			self.place_main_menu()
			self.place_return_menu(place=True)
			self.place_borrow_menu()
			self.verifier_delete()
			self.return_delete()
			self.student_registration_menu()
			self.delete_registration()
		elif menu == 'register':
			self.place_main_menu()
			self.place_return_menu()
			self.place_borrow_menu()
			self.student_registration_menu(place=True)
		else:
			self.place_main_menu()
			self.place_return_menu()
			self.place_borrow_menu(place=True)
			self.return_delete()
			self.student_registration_menu()
			self.delete_registration()


	def book_status(self, status=None, name=None,n=0 ):
		if status==0:
			print(self.db.table_names())
			#===================adding the student information==================
			query = 'insert into borrow(membership, id_no, firstname,surname, book_id, booktitle, author, date) values("{}","{}","{}","{}","{}","{}","{}","{}")'.format(self.membership, self.id_no, self.firstname, self.surname, self.book_id, self.booktitle, self.author, self.date)
			self.database.execute(query)
			self.borrow_menu_delete()
			print("Information recorded")

		if status==1 and name:
			print(self.db.table_names())
			query = "select * from borrow where firstname='{}'".format(name)
			self.credentials = self.database.execute(query).fetchall()
			if self.credentials:
				self.n=n
				self.limit = len(self.credentials)
				member_text = "Membership type of student :::{}".format(self.credentials[self.n][0])
				id_text ="Student ID ::: {}".format(self.credentials[self.n][1])
				firstname_text="Firstname ::: {}".format(self.credentials[self.n][2])
				surname_text = "Surname ::: {}".format(self.credentials[self.n][3])
				bookid_text = "Book id ::: {}".format(self.credentials[self.n][4])
				booktitle_text = "Book title ::: {}".format(self.credentials[self.n][5])
				author_text ="Book Author ::: {}".format(self.credentials[self.n][6])
				date_text ="Date borrowed ::: {}".format(self.credentials[self.n][7])
				self.membermenu_label.config(text =member_text)
				self.idnomenu_label.config(text = id_text)
				self.firstname_menu_label.config(text =firstname_text)
				self.surname_menu_label.config(text =surname_text)
				self.bookid_menu_label.config(text =bookid_text)
				self.booktitle_menu_label.config(text =booktitle_text)
				self.author_menu_label.config(text =author_text)
				self.date_menu_label.config(text =date_text)
				self.next_menu_button.place(x=400, y=360)
				self.back_menu_button.place(x=350, y=360)
				self.returned_menu_button.place(x=200, y=360)
			else:
				self.firstname_menu_label.config(text="!!Student with above name is not found in our database")
			print("Searched completed")
		if status==2:
			query = "delete from borrow where membership = '{}'and id_no='{}' and firstname='{}'and surname='{}'and book_id='{}'and booktitle='{}'and author='{}' and date='{}'".format(self.credentials[self.n][0],self.credentials[self.n][1],self.credentials[self.n][2],self.credentials[self.n][3],self.credentials[self.n][4],self.credentials[self.n][5],self.credentials[self.n][6],self.credentials[self.n][7])
			self.database.execute(query)
			self.return_delete()
			self.firstname_menu_label.config(text="A book returned")
			print("Book returned")

	def search_book_name(self):
		self.return_delete()
		self.student_name = self.search_entry.get()
		if self.student_name:
			self.book_status(status=1,name=self.student_name) 	

	def next_book(self, status=None):	
		if status:
			if self.n>0:
				self.n-=1
				sname =self.student_name
				no = self.n
				self.book_status(status=1, name=sname, n =no )
		else:
			if self.n<self.limit-1:
				self.n+=1
				sname =self.student_name
				no = self.n
				self.book_status(status=1, name=sname, n =no )		


	def borrow_verification(self, session):
		count = 0
		if session==0:
			self.membership = self.member_type_entry.get()
			if not self.membership:
				count+=1
				self.member_verifier.place(x=400, y=100)
			else:
				self.member_verifier.place_forget()
			self.id_no = self.id_no_entry.get()
			if not self.id_no:
				count+=1
				self.id_no_verifier.place(x=400, y=130)
			else:
				self.id_no_verifier.place_forget()
			self.firstname = self.firstname_entry.get()
			if not self.firstname:
				count+=1
				self.firstname_verifier.place(x=400, y=160)
			else:
				self.firstname_verifier.place_forget()	
			self.surname  = self.surname_entry.get()
			if not self.surname:
				count+=1	
				self.surname_verifier.place(x=400, y=190)
			else:
				self.surname_verifier.place_forget()
			self.book_id = self.bookid_entry.get()
			if not self.book_id:
				count+=1
				self.bookid_verifier.place(x=400, y=260)
			else:
				self.bookid_verifier.place_forget()
			self.booktitle = self.booktitle_entry.get()
			if not self.booktitle:
				count+=1
				self.booktitle_verifier.place(x=400, y=290)
			else:
				self.booktitle_verifier.place_forget()
			self.author=self.author_entry.get()
			if not self.author:
				count+=1
				self.bookauthor_verifier.place(x=400, y=320)
			else:
				self.bookauthor_verifier.place_forget()
			self.date = self.date_borrowed_entry.get()
			if not self.date:
				count+=1
				self.date_verifier.place(x=400, y=350)		
			else:
				self.date_verifier.place_forget()
			if count==0:
				print("All information filled")
				if self.add_member_student(test = True):
					self.student_absent.place_forget()
					self.book_status(status=0)
				else:
					self.student_absent.place(x = 200, y = 450)


app = Library(root)
root.mainloop()
