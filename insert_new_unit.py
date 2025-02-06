from database import connect_db

def insert_polling_unit_result(polling_unit_id, party, score, entered_by):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        query = """
            INSERT INTO announced_pu_results (polling_unit_uniqueid, party_abbreviation, party_score, entered_by_user, date_entered, user_ip_address)
            VALUES (%s, %s, %s, %s, NOW(), '127.0.0.1')
        """
        cursor.execute(query, (polling_unit_id, party, score, entered_by))
        conn.commit()
        conn.close()
        print("New result inserted successfully!")

polling_unit_id = input("Enter Polling Unit ID: ")
party = input("Enter Party Abbreviation: ")
score = input("Enter Party Score: ")
entered_by = input("Enter Your Name: ")

insert_polling_unit_result(polling_unit_id, party, score, entered_by)
