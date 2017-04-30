'''
 File Name: Assign4.py
 Author Name: Zhe Huang
 Date: 2017-03-24
 Description: This file defines a class IInterface to general define core functions this project needs,
              and class Application to implements tip calculator's functions.
              Also, attached Unit_Assign3.py file to implement new features functionalities.
'''

# import embedded database sqlit3
import sqlite3

# a class in an interface role to specify core functions the project needs.
class IInterface(object):
    def __init__(self):
        pass

    def add_record (self):
        raise Exception("NotImplementedException")

    def delete_record(self):
        raise Exception("NotImplementedException")

    def lookup_record(self):
        raise Exception("NotImplementedException")

    def update_record(self):
        raise Exception("NotImplementedException")

    def print_all(self):
        raise Exception("NotImplementedException")

    def personal_sum_expense(self):
        raise Exception("NotImplementedException")

# class to include functions about add, delete, lookup, update, print records and summerize personal sum expenses.
class Application(IInterface):
    # open file to print menu
    def print_menu(self):
        #print('1. Add an Record')
        #print('2. Delete an Record')
        #print('3. Lookup an Record')
        #print('4. Update an Record')
        #print('5. Print All Records')
        #print('6. Calculate specific customer sum expenses')
        #print('7. Quit')
        with open('./menu_print.txt', 'r') as f:
            print(f.read())
        print()

    # calculate total expense based on tip
    def calculate_total(self, expenses):
        tip = 0.15
        expenses = int(expenses)
        total = expenses + expenses * tip
        return total

    # add an expense record
    def add_record(self):
        print('Add Name and Expenses:')
        id = input('ID: ')
        name = input('Name: ')
        expenses = input('Expenses: ')
        total = self.calculate_total(expenses)
        print('The total expenses is: ' + str(total))
        cursor.execute('insert into tip_record (id, name, expenses, total) values (?, ?, ?, ?)', (id, name, expenses, total))
        print('Record added!\n')

    # delete an expense record
    def delete_record(self):
        print('Remove Name and Expenses')
        id = input('ID: ')
        cursor.execute("delete from tip_record where id = '" + id + "'")
        print('Record deleted!\n')

    # look up an expense record
    def lookup_record(self):
        print('Lookup an Expense Record')
        id = input('ID: ')
        cursor.execute("select * from tip_record where ID = '" + id + "'")
        value = cursor.fetchall()
        print(value)
        print()

    # update an expense record
    def update_record(self):
        print('Edit an Expense Record')
        id = input('The ID of record to be edited is: ')
        expenses = input('The new value of expenses to be updated is: ')
        total = self.calculate_total(expenses)
        cursor.execute('update tip_record set expenses = ? where id = ? ', (expenses, id))
        cursor.execute('update tip_record set total = ? where id = ? ', (total, id))
        print('Record updated!\n')

    # print all records
    def print_all(self):
        print('All Records are:')
        rows = cursor.execute('select * from tip_record order by id')
        for row in rows:
            #print(row[0], row[1])
            print(row)
        print()

    # calculate sum expenses of a specific customer
    def personal_sum_expense(self):
        person_sum = 0
        L=[]
        print('Lookup an Expense Record')
        name = input('Name: ')
        rows = cursor.execute("select * from tip_record where name = '" + name + "'")
        for row in rows:
            print(row)
            L.append(row[3])
        print('The sum expense for ' + name + ' is: ' + str(self.sum_person(L)))
        print()

    # calculation of sum expense of a person
    def sum_person(self, L=[]):
        sum = 0
        for i in L:
            sum = sum + i
        return sum

    # judge the menu options
    def menu_option(self, menu_choice):
        while menu_choice != 7:
            try:
                menu_choice = int(input('Type in a number (1-7): '))
                if menu_choice == 1:
                    self.add_record()
                elif menu_choice == 2:
                    self.delete_record()
                elif menu_choice == 3:
                    self.lookup_record()
                elif menu_choice == 4:
                    self.update_record()
                elif menu_choice == 5:
                    self.print_all()
                elif menu_choice == 6:
                    self.personal_sum_expense()
                elif menu_choice == 7:
                    print('Exiting...')
                    quit()
                else:
                    print("Invalid characters.\n")
            except ValueError as e:
                print("Invalid characters.\n")

# main entry
if __name__ == '__main__':
    # global variable
    menu_choice = 0
    # initial class
    app = Application()
    # invoke function to print menu
    app.print_menu()
    # connect to SQLite Database
    conn = sqlite3.connect('tip_tracker.db')
    # create a Cursor:
    cursor = conn.cursor()
    # execute a sql command to create table
    cursor.execute('create table if not exists tip_record (id INTEGER PRIMARY KEY, name varchar(20), expenses number(20), total number(20))')
    # invoke function to judge menu options
    app.menu_option(menu_choice)
    # close cursor
    cursor.close()
    # close connection
    conn.close()
