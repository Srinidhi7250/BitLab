# borrow_book.py
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise ValueError("Supabase URL or Key not found in environment variables.")

sb: Client = create_client(url, key)

def borrow_book(member_id, book_id):
    # Check stock of the book
    book = sb.table("books").select("stock").eq("book_id", book_id).execute()
    if not book.data or book.data[0]["stock"] <= 0:
        print("Book is out of stock!")
        return None

    # Insert borrow record
    payload = {"member_id": member_id, "book_id": book_id}
    try:
        resp = sb.table("borrow_records").insert(payload).execute()
        # Decrease book stock
        sb.table("books").update({"stock": book.data[0]["stock"] - 1}).eq("book_id", book_id).execute()
        return resp.data
    except Exception as e:
        print("Error borrowing book:", e)
        return None

if __name__ == "__main__":
    member_id = int(input("Member ID: ").strip())
    book_id = int(input("Book ID: ").strip())
    result = borrow_book(member_id, book_id)
    print("Borrow record:", result)
