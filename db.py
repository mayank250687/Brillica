import sqlite3

def create_table():
	con = sqlite3.connect('lite.db')
	cursor = con.cursor()
	cursor.execute("CREATE TABLE employee(id INTEGER PRIMARY KEY, name TEXT, dept TEXT, rating INT)")
	con.commit()
	con.close()
	print("table created \n")

def view():
    con = sqlite3.connect('lite.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM employee")
    data = cur.fetchall()
    con.close()
    for i in  data:
    	print(i)
    print("\n")

def insert(eid, name,dept,rating):
	con = sqlite3.connect('lite.db')
	cursor = con.cursor()
	cursor.execute("INSERT INTO employee VALUES(?,?,?,?)",(eid, name,dept,rating))
	con.commit()
	con.close()
	print("data inserted \n")
	view()


def delete(eid):
    con = sqlite3.connect('lite.db')
    cur = con.cursor()
    cur.execute("DELETE FROM employee WHERE id=?",(eid,))
    con.commit()
    con.close()
    print("data deleted \n")
    view()

def update(eid, name,dept,rating):
    con = sqlite3.connect('lite.db')
    cur = con.cursor()
    cur.execute("UPDATE employee SET name = ?, dept = ?, rating = ? WHERE id=?",(name,dept,rating,eid))
    con.commit()
    con.close()
    print("data updated \n")
    view()



while True:
	print("\n")
	print('''	Enter 1 to create table
	Enter 2 to Insert data
	Enter 3 to Delete data
	Enter 4 to Update data
	Enter 5 to view table
    	Enter 6 to exit''')
	try:
		choice = int(input())
		if choice == 1:
			try:
				create_table()
			except:
				print("Error: Please check if the table already exists")

		elif choice == 2:
			try:
				eid = int(input("enter emp id "))
				name = input('enter name ')
				dept = input("enter department ")
				rating = int(input("enter rating "))
				try:
					insert(eid, name,dept,rating)
				except:
					print('Error: check if employee id already exists')
			except:
				print("invalid value")

		elif choice == 3:
			try:
				eid = int(input("enter emp id "))
				try:
					delete(eid)
				except:
					print("record doesn't exist")
			except:
				print("invalid value")

		elif choice == 4:
			try:
				eid = int(input("enter emp id "))
				name = input('enter name ')
				dept = input("enter department ")
				rating = int(input("enter rating "))
				try:
					update(eid, name,dept,rating)
				except:
					print('Error: check if employee id exists')
			except:
				print("invalid value")

		elif choice ==5:
			view()
		elif choice == 6:
			break
		else:
			print("Invalid choice ")


	except:
		print('Invalid ')
	



