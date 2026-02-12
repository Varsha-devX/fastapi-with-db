import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

sql = """
-- change column type
ALTER TABLE users 
    ALTER COLUMN password TYPE varchar;
-- change column name
ALTER TABLE users 
    RENAME COLUMN password TO password;
-- Change column comment
COMMENT ON COLUMN users.password IS 'comment';
"""

try:
    conn = psycopg2.connect(DATABASE_URL)
    conn.autocommit = True
    with conn.cursor() as cur:
        cur.execute(sql)
    print("Migration successful")
except Exception as e:
    print(f"Migration failed: {e}")
finally:
    if 'conn' in locals():
        conn.close()
