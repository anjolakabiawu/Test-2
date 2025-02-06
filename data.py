import pymysql
import pandas as pd

# Database connection parameters
host = "localhost"
user = "root"
password = "password123@"
database = "election_db"

# Connect to MySQL
try:
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    print("✅ Connected to MySQL successfully!")

    # Tables to export
    tables = ["announced_pu_results", "polling_unit"]
    
    for table in tables:
        query = f"SELECT * FROM {table}"
        df = pd.read_sql(query, connection)
        csv_filename = f"{table}.csv"
        df.to_csv(csv_filename, index=False)
        print(f"✅ Data from {table} exported to {csv_filename}")

except pymysql.MySQLError as e:
    print(f"❌ MySQL Error: {e}")

finally:
    if 'connection' in locals() and connection.open:
        connection.close()
        print("✅ MySQL connection closed.")
