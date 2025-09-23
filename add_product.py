from supabase import create_client
url = "https://gpbydptskbkujczuudte.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdwYnlkcHRza2JrdWpjenV1ZHRlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODI2MDAsImV4cCI6MjA3MzY1ODYwMH0.AXMK6IR7VTUGZFC5SvrFgIMkhiBAKPBlJREjlW1qK-w"
sb = create_client(url, key)

def add_product(prod_id, name, price, stock):
    payload = {
        "prod_id": prod_id,
        "name": name,
        "price": price,
        "stock": stock
    }
    resp = sb.table("products").upsert(payload).execute()
    return resp
prod_id = int(input("Enter prod_id: "))
name = input("Enter product name: ")
price = float(input("Enter price: "))
stock = int(input("Enter stock: "))

created = add_product(prod_id, name, price, stock)
print(" Product added/updated:", created)
