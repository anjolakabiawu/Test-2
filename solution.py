from database import connect_db

def get_polling_unit_results(pollong_unit_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM announced_pu_results WHERE polling_unit_uniqueid = %s"
        cursor.execute(query, (pollong_unit_id,))
        results = cursor.fetchall()
        conn.close()
        return results
    
polling_unit_id = input("Enter Polling Unit ID: ")
results = get_polling_unit_results(polling_unit_id)

for result in results:
    print(f"Party: {result['party_abbreviation']}, Score: {result['party_score']}")