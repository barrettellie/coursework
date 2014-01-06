#create tables and enititys

import sqlite3

def create_table(db_name, table_name,sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name = ?",(table_name,))
        result = cursor.fetchall()
        if len(result) == 0:
            #turn on foriegn keys
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute(sql)
            db.commit()#theChoice
        else:
            pass

if __name__ == "__main__":
    db_name = "bed_and_breakfast.db"
    table_name = "Employee"
    sql = ("""create table Employee
             (EmployeeID integer,
             PositionID integer,
             Title text,
             FirstName text,
             LastName text,
             DateOfBirth text,
             Telephone integer,
             Email text,
             HouseName Number text,
             StreetName text,
             Town text,
             County text,
             PostCode text,
             NINumber text,
             DateStarted text,
             DateLeft text,
             TaxCode text,
             SortCode integer,
             AccountNumber integer,
             primary key(EmployeeID),
             foreign key(PositionID) references Position(PositionID))""")
    create_table(db_name, table_name, sql)
    
    table_name = "Position"
    sql = ("""create table Position
             (PositionID integer,
             TypeID integer,
             RateofPay integer,
             primary key(PositionID),
             foreign key(TypeID) references Type(TypeID))""")
    create_table(db_name, table_name, sql)
    
    table_name = "Type"
    sql = ("""create table Type
             (TypeID integer,
             Description text,
             primary key(TypeID))""")
    create_table(db_name, table_name, sql)
    
    table_name = "Payment"
    sql = ("""create table Payment
             (PaymentID integer,
             DeliveryMethodID integer,
             PayFrequency text,
             BankName text,
             primary key(PaymentID),
             foreign key(DeliveryMethodID) references DeliverMethod(DeliveryMethodID))""")
    create_table(db_name, table_name, sql)

    table_name = "DeliveryMethod"
    sql = ("""create table DeliveryMethod
             (DeliveryMethodID integer,
             PayMethod text,
             DeliveryMethod text,
             primary key(DeliveryMethodID))""")
    create_table(db_name, table_name, sql)

    table_name = "Manager"
    sql = ("""create table Manager
             (ManagerID integer,
             Title text,
             FirstName text,
             LastName text,
             DateOfBirth text,
             Telephone integer,
             Email text,
             HouseName Number text,
             StreetName text,
             Town text,
             County text,
             PostCode text,
             primary key(ManagerID))""")
    create_table(db_name, table_name, sql)
    
    table_name = "Timesheet"
    sql = ("""create table Timesheet
             (TimesheetID integer,
             EmployeeID integer,
             PaymentID integer,
             DateWorked text,
             TimeStarted text,
             TimeEnded text,
             NumberOfHours integer,
             OvertimeHours integer,
             OvertimePay integer,
             TotalPay integer,
             primary key(TimesheetID),
             foreign key(EmployeeID) references Employee(EmployeeID),
             foreign key(PaymentID) references Payment(PaymentID))""")
    create_table(db_name, table_name, sql)
             
             
    
