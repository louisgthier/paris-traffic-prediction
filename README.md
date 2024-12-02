# Paris Traffic Prediction - BCG X Datathon 2024

This repository contains the project developed for the BCG X Datathon, held in collaboration with CentraleSupélec. The challenge focuses on predicting traffic metrics for key routes in Paris to optimize delivery operations.

## Project Overview

### Objective
Develop a predictive model to forecast:
- **Hourly flow**: Number of vehicles per hour
- **Occupancy rate**: Percentage of time vehicles are present in a specific interval

These metrics are critical for optimizing delivery schedules, enhancing operational efficiency, and reducing costs.

### Scope
The project focuses on three specific routes (arcs) in Paris:
1. **Champs-Elysées**
2. **Rue de la Convention**
3. **Rue Saint-Antoine**

**Prediction Dates**: December 6–10, 2024  
**Evaluation Metric**: Root Mean Squared Error (RMSE)

### Deliverables
1. **Traffic Prediction**:
   - Predictions for hourly flow and occupancy rates for each route.
   - Submission format:
     - **CSV file** with predictions.
     - Accompanying **code** in a Jupyter notebook or repository.
2. **Presentation**:
   - Summary of the approach, results, and recommendations for next steps.

## Data Sources

The primary data is available on the Paris Open Data platform and includes traffic sensor readings. The dataset can be accessed and downloaded using the following link:

[Permanent Traffic Counts Dataset](https://opendata.paris.fr/explore/dataset/comptages-routiers-permanents/export/?disjunctive.libelle&disjunctive.etat_trafic&disjunctive.libelle_nd_amont&disjunctive.libelle_nd_aval&sort=t_1h)


https://opendata.paris.fr/explore/dataset/comptages-routiers-permanents-historique/information/

### Instructions to Download Data
1. **Access the Dataset**:
   - Use the link above to navigate to the dataset on the Paris Open Data platform.

2. **Filter Data by Arc Name**:
   - Use the **"Filters"** section on the left-hand side of the page to filter the data by arc name.
   - Enter the following keywords to filter and download data for each route:
     - **"washington"** for Champs-Elysées
     - **"convention"** for Rue de la Convention
     - **"st_antoine"** for Rue Saint-Antoine
   - Download each route's data separately to avoid missing records.

3. **Merge Data**:
   - Combine the individual datasets into one consolidated CSV file for further processing.

4. **Filter by Nodes in Code**:
   - After merging the data, filter the arcs programmatically using the following upstream and downstream nodes:
     - **Champs-Elysées**:
       - **Upstream Node**: "Av_Champs_Elysees-Washington"
       - **Downstream Node**: "Av_Champs_Elysees-Berri"
     - **Rue de la Convention**:
       - **Upstream Node**: "Convention-Blomet"
       - **Downstream Node**: "Lecourbe-Convention"
     - **Rue Saint-Antoine**:
       - **Upstream Node**: "Bastille-St_Antoine"
       - **Downstream Node**: "St_Antoine-Jacques_Coeur"

5. **Repeat the Download**:
   - Download the data twice:
     - Once for training the predictive models.
     - Again closer to the submission deadline to ensure the latest available data is used for final predictions.

6. **Additional Data**:
   - Supplementary external data can also be included:
     - Weather conditions
     - Road characteristics
     - Public holidays and school vacations

## Project Workflow

1. **Data Preparation**:
   - Clean, preprocess, and merge traffic and supplementary data.
   - Apply node-based filtering in the code to focus on the relevant sections of each route.

2. **Model Development**:
   - Use machine learning techniques to predict traffic metrics.
   - Validate model performance using historical data.

3. **Roadmap and Recommendations**:
   - Propose additional models and strategies for optimizing delivery operations.

## Output Format

The output must comply with the following structure:
- **Filename**: `output_<group_name>.csv`
- **Columns**:
  - `arc`: Route name (e.g., "Champs-Elysées", "Convention", "Saint-Antoine")
  - `datetime`: Timestamp in format `YYYY-MM-DD HH:MM`
  - `debit_horaire`: Hourly flow as a float
  - `taux_occupation`: Occupancy rate as a float

Ensure the output includes exactly **360 rows** (3 routes × 120 timestamps).

## Evaluation Criteria

1. **Data Science**:
   - Prediction quality measured using RMSE.
2. **Presentation**:
   - Clarity, structure, and relevance of insights and proposed roadmap.

## Key Dates

- **Submission Deadline**: December 6, 2024
- **Final Presentation**: December 11, 2024

## Acknowledgments

We extend our gratitude to BCG X and CentraleSupélec for organizing this datathon and providing mentorship and resources to tackle this real-world challenge.

---
_Disclaimer: This repository is developed solely for the BCG X Datathon._