# return_book.py
import os
from supabase import create_client, Client
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise ValueError("Supabase URL or Key not found in environment variables.")

sb: Client = create_client(url, key)

def return_book(record_id):
    # Fetch borrow record
    record = sb.table("borrow_records").select("book_id", "return_date").eq("record_id", record_id).execute()
    if not record.data:
        print("Borrow record not found!")
        return None
    if record.data[0]["return_date"]:
        print("Book already returned!")
        return None

    book_id = record.data[0]["book_id"]

    try:
        # Update return date
        resp = sb.table("borrow_records").update({"return_date": datetime.now().isoformat()}).eq("record_id", record_id).execute()
        # Increase book stock
        book = sb.table("books").select("stock").eq("book_id", book_id).execute()
        sb.table("books").update({"stock": book.data[0]["stock"] + 1}).eq("book_id", book_id).execute()
        return resp.data
    except Exception as e:
        print("Error returning book:", e)
        return None

if __name__ == "__main__":
    record_id = int(input("Borrow Record ID to return: ").strip())
    result = return_book(record_id)
    print("Return record:", result)
