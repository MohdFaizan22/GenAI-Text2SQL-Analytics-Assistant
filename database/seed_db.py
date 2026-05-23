import random
from faker import Faker
from datetime import datetime, timedelta

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from create_db import (
    Base,
    Customer,
    Product,
    Employee,
    Order,
    OrderItem
)



fake = Faker()

engine = create_engine("sqlite:///ecommerce.db")
Session = sessionmaker(bind=engine)

session = Session()



customers = []

for _ in range(100):
    customer = Customer(
        name=fake.name(),
        email=fake.unique.email(),
        city=fake.city(),
        signup_date=fake.date_between(start_date="-2y", end_date="today")
    )

    customers.append(customer)

session.add_all(customers)
session.commit()

print(" Customers inserted")



categories = [
    "Electronics",
    "Clothing",
    "Books",
    "Home",
    "Sports"
]

products = []

for _ in range(50):
    product = Product(
        product_name=fake.word().capitalize() + " Product",
        category=random.choice(categories),
        price=round(random.uniform(10, 1000), 2),
        stock=random.randint(10, 500)
    )

    products.append(product)

session.add_all(products)
session.commit()

print(" Products inserted")


departments = [
    "Sales",
    "Support",
    "Operations",
    "HR"
]

employees = []

for _ in range(10):
    employee = Employee(
        employee_name=fake.name(),
        department=random.choice(departments)
    )

    employees.append(employee)

session.add_all(employees)
session.commit()

print(" Employees inserted")



orders = []

for _ in range(500):

    customer = random.choice(customers)
    employee = random.choice(employees)

    order = Order(
        customer_id=customer.customer_id,
        employee_id=employee.employee_id,
        order_date=fake.date_between(start_date="-1y", end_date="today"),
        total_amount=0
    )

    session.add(order)
    session.flush()

    total_amount = 0

    # Each order gets 1-5 products
    for _ in range(random.randint(1, 5)):

        product = random.choice(products)

        quantity = random.randint(1, 5)

        order_item = OrderItem(
            order_id=order.order_id,
            product_id=product.product_id,
            quantity=quantity
        )

        session.add(order_item)

        total_amount += product.price * quantity

    order.total_amount = round(total_amount, 2)

    orders.append(order)

session.commit()

print(" Orders and order items inserted")

print("\n🎉 Database successfully populated with synthetic data!")