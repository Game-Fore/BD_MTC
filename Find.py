# import sqlite3

# def connect_to_db(db_name):
#     try:
#         connection = sqlite3.connect(db_name)
#         print(f"Успешно подключено к базе данных: {db_name}")
#         return connection
#     except sqlite3.Error as e:
#         print(f"Ошибка подключения к базе данных: {e}")
#         return None

# def get_employee_info_by_job(connection, job_title):
#     cursor = connection.cursor()
#     try:
#         select_query = """
#         SELECT Фамилия, Имя, Роль, Занятость, Телефон 
#         FROM Base_date 
#         WHERE Должность = ?;
#         """
#         cursor.execute(select_query, (job_title,))
#         rows = cursor.fetchall()
#         return rows
#     except sqlite3.Error as e:
#         print(f"Ошибка при выполнении SELECT запроса: {e}")
#         return None

# def get_tables(connection):
#     cursor = connection.cursor()
#     try:
#         cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#         tables = cursor.fetchall()
#         return tables
#     except sqlite3.Error as e:
#         print(f"Ошибка при получении списка таблиц: {e}")
#         return None

# if __name__ == "__main__":
#     db_connection = connect_to_db('my_database.db')
#     if db_connection:
#         job_title = input("Введите должность: ")
#         rows = get_employee_info_by_job(db_connection, job_title)
#         if rows:
#             for row in rows:
#                 фамилия, имя, роль, занятость, телефон = row
#                 print(f"{фамилия},  {имя},  {роль}, "
#                       f" {занятость},  {телефон}")
#         else:
#             print(f"Не найдены сотрудники для должности '{job_title}'.")

#         db_connection.close()
#         print("Соединение с базой данных закрыто")







from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Employee(Base):
    __tablename__ = 'Base_date'
    
    id = Column(Integer, primary_key=True)
    Фамилия = Column(String)
    Имя = Column(String)
    Роль = Column(String)
    Занятость = Column(String)
    Телефон = Column(String)
    Должность = Column(String)


def connect_to_db(db_name):
    try:
        engine = create_engine(f"sqlite:///{db_name}")
        Base.metadata.create_all(engine)  
        Session = sessionmaker(bind=engine)
        session = Session()
        print(f"Успешно подключено к базе данных: {db_name}")
        return session
    except Exception as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None


def get_employee_info_by_job(session, job_title):
    try:
        employees = session.query(Employee).filter(Employee.Должность == job_title).all()
        return employees
    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return None

def get_tables(session):
    try:
        tables = session.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
        return tables
    except Exception as e:
        print(f"Ошибка при получении списка таблиц: {e}")
        return None

if __name__ == "__main__":
    db_name = 'my_database.db'
    session = connect_to_db(db_name)
    if session:
        job_title = input("Введите должность: ")
        employees = get_employee_info_by_job(session, job_title)
        if employees:
            for employee in employees:
                print(f"{employee.Фамилия}, {employee.Имя}, {employee.Роль}, "
                      f"{employee.Занятость}, {employee.Телефон}")
        else:
            print(f"Не найдены сотрудники для должности '{job_title}'.")
        session.close()
        print("Соединение с базой данных закрыто.")





