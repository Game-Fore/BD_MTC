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