from datetime import datetime

def test_format_and_output_validity(output_df):
    # Expected output column specifications
    output_columns = {
        "arc": object,
        "datetime": object,
        "debit_horaire": float,
        "taux_occupation": float
    }

    try:
        # 1. Check relevant columns are in the output dataframe
        assert sorted(list(output_df.columns)) == list(output_columns.keys()), (
            f"Some columns are missing or unnecessary columns are in output: "
            f"expected {list(output_columns.keys())}, found {list(output_df.columns)}"
        )
        print("[VALIDATION] Column names are valid.")

        # 2. Check data types for each column
        for col, col_type in output_columns.items():
            assert output_df[col].dtype == col_type, (
                f"Column {col} does not have the correct type: "
                f"expected {col_type}, found {output_df[col].dtype}"
            )
        print("[VALIDATION] Column data types are valid.")

        # 3. Check datetime strings have the right format
        output_df["datetime"].apply(
            lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M")
        )
        print("[VALIDATION] Datetime format is valid.")

        # 4. Check the 'arc' column has the correct unique values
        expected_arcs = ["Champs-Elysées", "Convention", "Saint-Antoine"]
        assert sorted(list(output_df["arc"].unique())) == expected_arcs, (
            f"'arc' column does not have the expected unique values: "
            f"expected {expected_arcs}, found {list(output_df['arc'].unique())}"
        )
        print("[VALIDATION] 'arc' column values are valid.")

        # 5. Check the dataframe has the expected number of rows
        expected_rows = 360
        assert output_df.shape[0] == expected_rows, (
            f"Expected number of rows is {expected_rows}, "
            f"but output has {output_df.shape[0]}"
        )
        print("[VALIDATION] Row count is valid.")

        print("[SUCCESS] The file is valid.")
    except AssertionError as e:
        print(f"[ERROR] Validation failed: {e}")
    except ValueError as e:
        print(f"[ERROR] Datetime validation failed: {e}")

# Example usage
import pandas as pd

# Load the generated CSV file
output_file = "predictions.csv"  # Path to the generated CSV file
output_df = pd.read_csv(output_file, sep=";")

# Validate and print results
test_format_and_output_validity(output_df)