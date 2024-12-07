from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Book(Base):
    __tablename__ = 'books'

    id_book = Column(Integer, primary_key=True, index=True, autoincrement=True)
    author = Column(String, nullable=False)
    book_name = Column(String, nullable=False)
    book_picture = Column(String, nullable=False)
    price = Column(Integer, default=False)

    book_ship_order = relationship('Order', back_populates='order_ship_book')


class Client(Base):
    __tablename__ = 'clients'

    id_client = Column(Integer, primary_key=True, index=True, autoincrement=True)
    client_name = Column(String, nullable=False)
    phone_number = Column(Integer, nullable=False)
    password = Column(String, nullable=False)

    client_ship = relationship('Order', back_populates='order_ship_client')


class Order(Base):
    __tablename__ = 'orders'

    id_order = Column(Integer, primary_key=True, index=True, autoincrement=True)
    client_name = Column(Integer, ForeignKey('clients.id_client'), nullable=False)
    book_name = Column(Integer, ForeignKey('books.id_book'), nullable=False)
    address = Column(String, nullable=False)
    payment = Column(Integer, ForeignKey('payments.id_payment'), nullable=False)
    delivery_date = Column(String, nullable=False)

    order_ship_book = relationship('Book', back_populates='book_ship_order')
    order_ship_client = relationship('Client', back_populates='client_ship')
    order_ship_payment = relationship('Payment', back_populates='payment_ship')


class Payment(Base):
    __tablename__ = 'payments'

    id_payment = Column(Integer, primary_key=True, index=True, autoincrement=True)
    payment_status = Column(String, nullable=False)

    payment_ship = relationship('Order', back_populates='order_ship_payment')


class Administrator(Base):
    __tablename__ = 'admins'

    id_admin = Column(Integer, primary_key=True, index=True, autoincrement=True)
    login = Column(Integer, nullable=False)
    password = Column(String, nullable=False)
