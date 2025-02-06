import pandas as pd

def insert_polling_unit_result(polling_unit_id, party, score, entered_by):
    df = pd.read_csv("announced_pu_results.csv")

    new_entry = pd.DataFrame([{
        "polling_unit_uniqueid": int(polling_unit_id),
        "party_abbreviation": party,
        "party_score": int(score),
        "entered_by_user": entered_by,
        "date_entered": pd.Timestamp.now(),
        "user_ip_address": "127.0.0.1"
    }])

    # Append using pd.concat()
    df = pd.concat([df, new_entry], ignore_index=True)

    # Save back to CSV
    df.to_csv("announced_pu_results.csv", index=False)
    print("✅ New result inserted successfully!")

# User input
polling_unit_id = input("Enter Polling Unit ID: ")
party = input("Enter Party Abbreviation: ")
score = input("Enter Party Score: ")
entered_by = input("Enter Your Name: ")

# Insert new result
insert_polling_unit_result(polling_unit_id, party, score, entered_by)
