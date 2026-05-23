from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///ecommerce.db")


Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    city = Column(String)
    signup_date = Column(Date)

    orders = relationship("Order", back_populates="customer")



class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable=False)
    category = Column(String)
    price = Column(Float)
    stock = Column(Integer)

    order_items = relationship("OrderItem", back_populates="product")


class Employee(Base):
    __tablename__ = "employees"

    employee_id = Column(Integer, primary_key=True)
    employee_name = Column(String, nullable=False)
    department = Column(String)

    orders = relationship("Order", back_populates="employee")



class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)

    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    employee_id = Column(Integer, ForeignKey("employees.employee_id"))

    order_date = Column(Date)
    total_amount = Column(Float)

    customer = relationship("Customer", back_populates="orders")
    employee = relationship("Employee", back_populates="orders")

    order_items = relationship("OrderItem", back_populates="order")



class OrderItem(Base):
    __tablename__ = "order_items"

    order_item_id = Column(Integer, primary_key=True)

    order_id = Column(Integer, ForeignKey("orders.order_id"))
    product_id = Column(Integer, ForeignKey("products.product_id"))

    quantity = Column(Integer)

    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")



Base.metadata.create_all(engine)

print(" Database and tables created successfully!")