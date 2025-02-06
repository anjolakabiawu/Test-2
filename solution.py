import pandas as pd

def get_polling_unit_results(polling_unit_id):
    df = pd.read_csv("announced_pu_results.csv")
    
    # Filter by polling unit ID
    results = df[df["polling_unit_uniqueid"] == int(polling_unit_id)][["party_abbreviation", "party_score"]]
    
    return results

polling_unit_id = input("Enter Polling Unit ID: ")
results = get_polling_unit_results(polling_unit_id)

if results.empty:
    print("❌ No results found for this Polling Unit ID.")
else:
    for _, row in results.iterrows():
        print(f"Party: {row['party_abbreviation']}, Score: {row['party_score']}")
