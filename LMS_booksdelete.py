# remove_book.py
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise ValueError("Supabase URL or Key not found in environment variables.")

sb: Client = create_client(url, key)

def remove_book(book_id):
    try:
        resp = sb.table("books").delete().eq("book_id", book_id).execute()
        return resp.data
    except Exception as e:
        print("Error removing book:", e)
        return None

if __name__ == "__main__":
    book_id = int(input("Book ID to remove: ").strip())
    result = remove_book(book_id)
    print("Removed:", result)
