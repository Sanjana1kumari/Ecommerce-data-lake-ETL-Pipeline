from faker import Faker
import pandas as pd
import random
import os
fake=Faker()
random.seed(42)
os.makedirs("data/bronze", exist_ok=True)
customers=[] 
for _ in range(1,501):
    customer.append({
        "customer_id":i,
        "name":fake.name(),
        "email":fake.city(),
        "region":random.choice(["North", "South", "East", "West"]),
                })
    customers_df=pd.dataframe(customers)
    customers_df.to_csv("data/bronze/customers.csv", index=False)
    print(f"customers saved: {len(customers_df)} rows")
    
    categories=["clothing","books","electronics","lights","games"]
    products=[]
    for i in range(1,101):
        products.append({
            "product_id":i,
            "name":fake.word(),
            "category":random.choice(categories),
            "price":round(random.uniform(10, 100), 2),
            "stock":random.randint(0,100)
        })
    products_df=pd.DataFrame(products)
    products_df.to_csv("data/bronze/products.csv", index=False)
    print(f"products saved: {len(products_df)} rows")
    orders=[]
    for i in range(1,1001):
        orders.append({
            "order_id":i,
            "customer id":random.randint(1,500),
            "product id":random.randint(1,100),
            "quantity":random.randint(1,5),
            "order date":fake.date_this_year(),
            "status":random.choice(["delivered","pending","cancelled"])
       }) orders_df = pd.DataFrame(orders)
        orders_df.to_csv("data/bronze/orders.csv",index=False)
        print(f"orders saved:{len(orders_df)} rows")
        print("/---sample customers---/")
        print(customers_df.head(3).to_string(index=False))
        print("/sample products---?")
        print(products_df.head(3).to_string(index=False))
        print("/---sample orders---/")
        print(orders_df.head(3).to_string(index=False))
        print("\nphase 1 completed!Check the data/bronze/folder.")

        