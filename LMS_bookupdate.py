# update_book.py
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise ValueError("Supabase URL or Key not found in environment variables.")

sb: Client = create_client(url, key)

def update_book(book_id, title=None, author=None, category=None, stock=None):
    payload = {}
    if title: payload["title"] = title
    if author: payload["author"] = author
    if category: payload["category"] = category
    if stock is not None: payload["stock"] = stock

    try:
        resp = sb.table("books").update(payload).eq("book_id", book_id).execute()
        return resp.data
    except Exception as e:
        print("Error updating book:", e)
        return None

if __name__ == "__main__":
    book_id = int(input("Book ID to update: ").strip())
    title = input("New title (leave blank to skip): ").strip() or None
    author = input("New author (leave blank to skip): ").strip() or None
    category = input("New category (leave blank to skip): ").strip() or None
    stock = input("New stock (leave blank to skip): ").strip()
    stock = int(stock) if stock else None

    result = update_book(book_id, title, author, category, stock)
    print("Updated:", result)