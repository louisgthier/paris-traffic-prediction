

import pandas as pd
import glob

def load_data(street):
    # Define the street
    street = "washington"

    # Path to the directory containing the CSV files
    directory = f"data/{street}/*.csv"

    # Define column mappings
    column_mapping = {
        "iu_ac": "Identifiant arc",
        "q": "Débit horaire",
        "k": "Taux d'occupation",
        "t_1h": "Date et heure de comptage",
        "iu_nd_amont": "Identifiant noeud amont",
        "libelle_nd_amont": "Libelle noeud amont",
        "iu_nd_aval": "Identifiant noeud aval",
        "libelle_nd_aval": "Libelle noeud aval",
        "etat_trafic": "Etat trafic",
        "etat_barre": "Etat arc",
        "libelle": "Libelle",
    }

    # Define the Arc id for filtering based on street
    arc_id_mapping = {
        "washington": 4264,
        "st_antoine": 376,
        "convention": 5672,
    }

    arc_id = arc_id_mapping.get(street.lower())

    # Read the main DataFrame
    filepath = f"data/comptages-routiers-permanents-{street}.csv"
    df = pd.read_csv(filepath, delimiter=";")

    # Filter based on Arc id
    df = df[df["Identifiant arc"] == arc_id]
        
    # Ensure proper column conversion
    df.rename(columns=column_mapping, inplace=True)

    # Filter based on Arc id
    df = df[df["Identifiant arc"] == arc_id]

    # Drop unnecessary columns
    df.drop(columns=["geo_point_2d", "geo_shape"], inplace=True)

    # Convert "Date et heure de comptage" to datetime
    df["Date et heure de comptage"] = pd.to_datetime(df["Date et heure de comptage"], errors="coerce", utc=True)

    # Initialize a list to hold DataFrames for concatenation
    dfs = [df]

    # Process all additional CSV files in the directory
    files = glob.glob(directory)

    for file in files:
        temp_df = pd.read_csv(file)
        
        # Rename columns to match the main DataFrame
        temp_df.rename(columns=column_mapping, inplace=True)
        
        # Filter based on Arc id
        temp_df = temp_df[temp_df["Identifiant arc"] == arc_id]
        
        # Convert "Date et heure de comptage" to datetime
        temp_df["Date et heure de comptage"] = pd.to_datetime(temp_df["Date et heure de comptage"], errors="coerce", utc=True)
        
        # Append to the list
        dfs.append(temp_df)

    # Concatenate all DataFrames
    final_df = pd.concat(dfs, ignore_index=True)

    # Sort by "Date et heure de comptage" and drop duplicates
    final_df.sort_values(by="Date et heure de comptage", inplace=True)
    final_df.drop_duplicates(subset="Date et heure de comptage", keep="first", inplace=True)

    # Reset index
    final_df.reset_index(drop=True, inplace=True)

    # Print summary
    print(f"Number of rows: {final_df.shape[0]}")
    print(f"First date: {final_df['Date et heure de comptage'].min()}, Last date: {final_df['Date et heure de comptage'].max()}")

    print("Columns:", final_df.columns)
    

    # Save to a filtered CSV
    # output_filepath = filepath.replace(".csv", "-filtered.csv")
    # final_df.to_csv(output_filepath, sep=";", index=False)

    # print(f"Filtered data saved to: {output_filepath}")
    
    return final_df