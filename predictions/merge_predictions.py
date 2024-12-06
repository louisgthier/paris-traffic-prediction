import os
import pandas as pd

# Mapping from filename arc to required arc names
arc_name_map = {
    "convention": "Convention",
    "st_antoine": "Saint-Antoine",
    "washington": "Champs-Elysées"
}

# Mapping from filename target to required column names
target_map = {
    "Débit horaire": "debit_horaire",
    "Taux d'occupation": "taux_occupation"
}

input_dir = "./"
arc_data = {}

# Iterate over each CSV file in the directory
for filename in os.listdir(input_dir):
    if filename.endswith(".csv") and filename.startswith("series-"):
        # Extract arc and target from filename, e.g. series_convention_Débit horaire.csv
        parts = filename.split("-")
        # Expected pattern: ['series', '<arc>', '<target>.csv']
        arc_key = parts[1]
        # Target might have spaces or apostrophes, join all parts except the first two and remove .csv
        raw_target = "-".join(parts[2:]).replace(".csv", "")

        # Load the CSV
        filepath = os.path.join(input_dir, filename)
        df = pd.read_csv(filepath)

        # Convert arc and target to proper names
        arc = arc_name_map.get(arc_key, arc_key)  # fallback if not in map
        target_col = target_map.get(raw_target, raw_target)  # fallback if not in map

        # Rename 'timestamp' column to 'datetime'
        if 'timestamp' in df.columns:
            df = df.rename(columns={'timestamp': 'datetime'})
        else:
            raise ValueError(f"Expected column 'timestamp' not found in {filename}")

        # Rename 'mean' column to the target_col if 'mean' exists
        if 'mean' in df.columns:
            df = df.rename(columns={'mean': target_col})
        else:
            # If the CSV doesn't have 'mean', adjust this logic as needed
            pass
        
        # Convert 'datetime' column to timezone-aware datetime
        df['datetime'] = pd.to_datetime(df['datetime']).dt.tz_localize("UTC").dt.tz_convert("Europe/Paris").dt.strftime("%Y-%m-%d %H:%M")

        # Prepare data for merging
        this_arc_df = df[['datetime', target_col]]

        # Merge dataframes for the same arc
        if arc not in arc_data:
            arc_data[arc] = this_arc_df
        else:
            arc_data[arc] = arc_data[arc].merge(this_arc_df, on='datetime', how='outer')

# Combine all arcs into one final dataframe
final_df_list = []
for arc, arc_df in arc_data.items():
    arc_df['arc'] = arc
    # Format datetime column
    arc_df['datetime'] = pd.to_datetime(arc_df['datetime']).dt.strftime("%Y-%m-%d %H:%M")
    # Ensure columns exist (if one target might not be present for some arc, fill with NaNs)
    if 'debit_horaire' not in arc_df.columns:
        arc_df['debit_horaire'] = float('nan')
    if 'taux_occupation' not in arc_df.columns:
        arc_df['taux_occupation'] = float('nan')

    final_df_list.append(arc_df[['arc', 'datetime', 'debit_horaire', 'taux_occupation']])

final_df = pd.concat(final_df_list, ignore_index=True).sort_values(by=['arc', 'datetime'])

# Save the final CSV
final_df.to_csv("predictions.csv", index=False, sep=";")