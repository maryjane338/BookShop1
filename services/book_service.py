from sqlalchemy.orm import Session
from models.book import Book, Client, Order, Payment, Administrator


class BookService:
    def __init__(self, db: Session):
        self.db = db

    def add_book(self, author: str,
                 book_name: str, book_picture: str, price: int):
        new_book = Book(
            author=author,
            book_name=book_name,
            book_picture=book_picture,
            price=price
        )
        self.db.add(new_book)
        self.db.commit()
        self.db.refresh(new_book)
        print(f"Added book:{new_book.book_name}")
        return new_book

    def update_book(self, id_book, author, book_name, book_picture, price):
        book = self.db.query(Book).filter_by(id_book=id_book).first()
        if book:
            book.author = author
            book.book_name = book_name
            book.book_picture = book_picture
            book.price = price
            self.db.commit()
            self.db.refresh(book)

    def delete_book(self, id_book):
        book = self.db.query(Book).filter_by(id_book=id_book).first()
        self.db.delete(book)
        self.db.commit()

    def select_book_query(self, book_name):
        query_book = self.db.query(Book.id_book).filter_by(book_name=book_name).scalar()
        return query_book

    def select_book_name(self, book_name):
        query_book = self.db.query(Book.id_book).filter_by(book_name=book_name).scalar()
        return query_book

    def load_book(self, id_book):
        query_name = self.db.query(Book.book_name).filter_by(id_book=id_book).scalar()
        query_author = self.db.query(Book.author).filter_by(id_book=id_book).scalar()
        query_price = self.db.query(Book.price).filter_by(id_book=id_book).scalar()
        query_picture = self.db.query(Book.book_picture).filter_by(id_book=id_book).scalar()
        query = [query_name, query_author, query_price, query_picture]
        return query

    def selected_book(self, id_book):
        query_book = self.db.query(Book.book_name, Book.author, Book.book_picture, Book.price).\
            filter_by(id_book=id_book).scalar()
        query = [query_book]
        return query

    def get_all_books(self):
        query = self.db.query(Book).all()

        books = []
        for b in query:
            book = []
            book.append(str(b.id_book))
            book.append(b.author)
            book.append(b.book_name)
            book.append(b.book_picture)
            book.append(str(b.price))
            books.append(book)
        return books


class ClientService:
    def __init__(self, db: Session):
        self.db = db

    def add_client(self, client_name: str,
                 phone_number: int, password: str):
        new_client = Client(
            client_name=client_name,
            phone_number=phone_number,
            password=password,
        )
        self.db.add(new_client)
        self.db.commit()
        self.db.refresh(new_client)
        print(f"Added client:{new_client.client_name}")
        return new_client

    def delete_client(self, id_client):
        client = self.db.query(Client).filter_by(id_client=id_client).first()
        self.db.delete(client)
        self.db.commit()

    def select_user_for_enter(self, user_name):
        user_password = self.db.query(Client.password).filter_by(client_name=user_name).scalar()
        return user_password

    def select_user(self, user_name):
        user_id = self.db.query(Client.id_client).filter_by(client_name=user_name).scalar()
        return user_id

    def get_all_clients(self):
        query = self.db.query(Client).all()

        clients = []
        for c in query:
            client = []
            client.append(str(c.id_client))
            client.append(c.client_name)
            client.append(str(c.phone_number))
            client.append(c.password)
            clients.append(client)
        return clients


class OrderService:
    def __init__(self, db: Session):
        self.db = db

    def add_order(self, client_name: int, book_name: int, address: str,
                 payment: int, delivery_date: str):
        new_order = Order(
            client_name=client_name,
            book_name=book_name,
            address=address,
            payment=payment,
            delivery_date=delivery_date,
        )
        self.db.add(new_order)
        self.db.commit()
        self.db.refresh(new_order)
        print(f"Added order:{new_order.address}")
        return new_order

    def delete_order(self, id_order):
        order = self.db.query(Order).filter_by(id_order=id_order).first()
        self.db.delete(order)
        self.db.commit()

    def update_order(self, id_order, book_name, address, payment, delivery_date):
        order = self.db.query(Order).filter_by(id_order=id_order).first()
        if order:
            order.book_name = book_name
            order.address = address
            order.payment = payment
            order.delivery_date = delivery_date
            self.db.commit()
            self.db.refresh(order)

    def load_orders_for_user(self, id_user):
        query_id = self.db.query(Order.id_order).filter_by(client_name=id_user).all()
        ids = list(map(str, [id_order[0] for id_order in query_id]))

        query_book_id = self.db.query(Order.book_name).filter_by(client_name=id_user).all()
        books_ids = [book_id[0] for book_id in query_book_id]
        final_book_name = [
            self.db.query(Book.book_name).filter_by(id_book=book_id).scalar()
            for book_id in books_ids
        ]

        query_address = self.db.query(Order.address).filter_by(client_name=id_user).all()
        addresses = [address[0] for address in query_address]

        query_payment_id = self.db.query(Order.payment).filter_by(client_name=id_user).all()
        payment_ids = [payment_id[0] for payment_id in query_payment_id]
        final_payment_status = [
            self.db.query(Payment.payment_status).filter_by(id_payment=payment_id).scalar()
            for payment_id in payment_ids
        ]

        query_date = self.db.query(Order.delivery_date).filter_by(client_name=id_user).all()
        dates = [date[0] for date in query_date]

        loaded_orders = []

        for i in range(len(ids)):
            loaded_order = []
            loaded_order.append(ids[i - 1])
            loaded_order.append(final_book_name[i - 1])
            loaded_order.append(addresses[i - 1])
            loaded_order.append(final_payment_status[i - 1])
            loaded_order.append(dates[i - 1])
            loaded_orders.append(loaded_order)

        return loaded_orders

    def get_all_orders(self):
        query = self.db.query(Order).all()

        orders = []
        for o in query:
            order = []
            order.append(str(o.id_order))
            order.append(str(o.client_name))
            order.append(str(o.book_name))
            order.append(o.address)
            order.append(str(o.payment))
            order.append(str(o.delivery_date))
            orders.append(order)
        return orders

class PaymentService:
    def __init__(self, db: Session):
        self.db = db

    def add_payment(self, payment_status: str):
        new_payment = Payment(
            payment_status=payment_status
        )
        self.db.add(new_payment)
        self.db.commit()
        self.db.refresh(new_payment)
        print(f"Added payment:{new_payment.payment_status}")
        return new_payment

    def get_all_payments(self):
        books = self.db.query(Book).all()
        return books


class AdminService:
    def __init__(self, db: Session):
        self.db = db

    def add_admin(self, login: str, password: str):
        new_admin = Administrator(
            login=login,
            password=password
        )
        self.db.add(new_admin)
        self.db.commit()
        self.db.refresh(new_admin)
        print(f"Added payment:{new_admin.login}")
        return new_admin

    def select_admin_for_enter(self, admin_name):
        admin_password = self.db.query(Administrator.password).filter_by(login=admin_name).scalar()
        return admin_password
