import sqlalchemy as db
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String
from contextlib import contextmanager

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'contact'
    cust_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone = Column(String)
    address1 = Column(String)
    address2 = Column(String)
    address3 = Column(String)
    towncity = Column(String)
    postcode = Column(String)
    company = Column(String)
    detail = Column(String)

class CRUD:
    def __init__(self, database):
        self.engine = db.create_engine(f'sqlite:///{database}')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
    @contextmanager
    def session_scope(self):
            session = self.Session()
            try:
                yield session
                session.commit()
            except Exception:
                session.rollback()
                raise
            finally:
                session.close()
    def create_customer(self, cust_id, first_name, last_name, email, phone, address1, address2, address3, towncity, postcode, company, detail):
        with self.session_scope() as session:
            customer = Customer(
                cust_id=cust_id,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                address1=address1,
                address2=address2,
                address3=address3,
                towncity=towncity,
                postcode=postcode,
                company=company,
                detail=detail
            )
            session.add(customer)
    def read_all_customers(self):
        with self.session_scope() as session:
            customers = session.query(Customer).all()
            for customer in customers:
                print(customer.first_name, customer.last_name, customer.email)

    def update_customer(self, cust_id, column_name, update_data):
        with self.session_scope() as session:
            customer = session.query(Customer).filter_by(cust_id=cust_id).first()
            if customer:
                setattr(customer, column_name, update_data)
            else:
                print(f"No customer found with cust_id {cust_id}")

    def delete_table(self, cust_id):
        with self.session_scope() as session:
            try:
                target = session.query(Customer).filter(Customer.cust_id == cust_id).one()
                session.delete(target)
            except Exception as e:
                print('ERROR:', e)
                raise
            
    def delete_tableee(self):
        with self.session_scope() as session:
            try:
                session.query(Customer).delete()

                session.commit()
            except Exception as e:

                print('ERROR:', e)
                


if __name__ == "__main__":
    app = CRUD('crud.db')
    # app.delete_tableee()


