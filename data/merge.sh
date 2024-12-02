#!/bin/bash

# Input CSV files
csv1="comptages-routiers-permanents-convention.csv"
csv2="comptages-routiers-permanents-st_antoine.csv"
csv3="comptages-routiers-permanents-washington.csv"

# Output CSV file
output_csv="comptages-routiers-permanents.csv"

# Clear the output file if it exists
> "$output_csv"

# Add the header from the first CSV file
head -n 1 "$csv1" > "$output_csv"

# Append the contents of all CSVs except their first line (headers)
tail -n +2 "$csv1" >> "$output_csv"
tail -n +2 "$csv2" >> "$output_csv"
tail -n +2 "$csv3" >> "$output_csv"

echo "Files merged successfully into $output_csv"