import pandas as pd

def get_lga_results(lga_id):
    # Load CSV files
    results_df = pd.read_csv("announced_pu_results.csv")
    polling_df = pd.read_csv("polling_unit.csv")

    # Find polling units for the given LGA
    lga_polling_units = polling_df[polling_df["lga_id"] == int(lga_id)]["uniqueid"]

    # Filter results for those polling units
    lga_results = results_df[results_df["polling_unit_uniqueid"].isin(lga_polling_units)]
    
    # Aggregate scores per party
    summary = lga_results.groupby("party_abbreviation")["party_score"].sum().reset_index()

    return summary

lga_id = input("Enter LGA ID: ")
lga_results = get_lga_results(lga_id)

if lga_results.empty:
    print("❌ No results found for this LGA ID.")
else:
    for _, row in lga_results.iterrows():
        print(f"Party: {row['party_abbreviation']}, Total Score: {row['party_score']}")
