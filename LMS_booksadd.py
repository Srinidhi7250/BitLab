# add_book.py
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise ValueError("Supabase URL or Key not found in environment variables.")

sb: Client = create_client(url, key)

def add_book(title, author, category=None, stock=1):
    payload = {"title": title, "author": author, "category": category, "stock": stock}
    try:
        resp = sb.table("books").insert(payload).execute()
        return resp.data
    except Exception as e:
        print("Error adding book:", e)
        return None

if __name__ == "__main__":
    title = input("Book title: ").strip()
    author = input("Author: ").strip()
    category = input("Category (optional): ").strip() or None
    stock = input("Stock (default 1): ").strip()
    stock = int(stock) if stock else 1

    result = add_book(title, author, category, stock)
    print("Added:", result)
