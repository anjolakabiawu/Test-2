from database import connect_db

def get_lga_results(lga_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT party_abbreviation, SUM(party_score) AS total_score 
            FROM announced_pu_results
            WHERE polling_unit_uniqueid IN (
                SELECT uniqueid FROM polling_unit WHERE lga_id = %s
            )
            GROUP BY party_abbreviation
        """
        cursor.execute(query, (lga_id,))
        results = cursor.fetchall()
        conn.close()
        return results

lga_id = input("Enter LGA ID: ")
lga_results = get_lga_results(lga_id)

for result in lga_results:
    print(f"Party: {result['party_abbreviation']}, Total Score: {result['total_score']}")
