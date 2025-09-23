# add_member.py
import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
if not url or not key:
    raise ValueError("Supabase URL or Key not found in environment variables.")
sb: Client = create_client(url, key)
def add_member(name, email):
    return sb.table("members").insert({"name": name, "email": email}).execute()
if __name__ == "__main__":
    name = input("Enter member name: ").strip()
    email = input("Enter member email: ").strip()
    result = add_member(name, email)
    print("Inserted:", result.data)
