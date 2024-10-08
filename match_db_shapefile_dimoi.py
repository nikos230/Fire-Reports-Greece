import sqlite3
import geopandas as gpd
import pandas as pd
from unidecode import unidecode
import unicodedata


def normalize_and_transliterate(text):
    upper_text = text.upper()
    # Normalize the text (NFKD form)
    normalized_text = unicodedata.normalize('NFKD', upper_text)
    # Remove accents using unidecode and convert to lowercase
    transliterated_text = unidecode(normalized_text).lower()
    return transliterated_text

# Step 1: Load the .db file
db_path = "Deltia_Database.db"
conn = sqlite3.connect(db_path)

# Query to extract the required column from the Deltia_Pyrovestikis table
query = """
    SELECT [DHMOS-KOINOTITA Latin], [ΚΑΜΕΝΗ ΕΚΤΑΣΗ]
    FROM Deltia_Pyrosvestikis
    WHERE [ΚΑΜΕΝΗ ΕΚΤΑΣΗ] >= 250
"""
#WHERE [ΚΑΜΕΝΗ ΕΚΤΑΣΗ] >= 250
df_db = pd.read_sql_query(query, conn)


# Step 2: Load the shapefile
shapefile_path = "C:/Users/nikos/Desktop/greece_dimoi/dimoi.shp"
gdf = gpd.read_file(shapefile_path)

# Convert the NAME column to Latin characters and lowercase
gdf['NAME'] = gdf['NAME'].apply(normalize_and_transliterate)

# Step 3: Perform the match and count occurrences
# Group by NAME from the shapefile and count occurrences in the .db file
counts = df_db['DHMOS-KOINOTITA Latin'].value_counts().reset_index()
counts.columns = ['NAME', 'count']

# Convert NAME in counts to lowercase and Latin characters to ensure matching
#counts['NAME'] = counts['NAME'].apply(normalize_and_transliterate)

# Merge the counts with the original GeoDataFrame
gdf = gdf.merge(counts, on='NAME', how='left')


missing_matches = gdf[gdf['NAME'].isna()]

# Fill NaN values in the 'count' column with 0
gdf['count'] = gdf['count'].fillna(0)

print('Matched fires', gdf['count'].sum())    

# Step 4: Save the result as a new shapefile
output_shapefile_path = "C:/Users/nikos/Desktop/greece_dimoi/dimoi_with_counts_bigeher_than_250.shp"
gdf.to_file(output_shapefile_path)

print(f"Shapefile saved to {output_shapefile_path}")




# Get unique names from the shapefile and database
gdf_names = set(gdf['NAME'])
counts_names = set(counts['NAME'])

# Find names in the shapefile that don't have a match in the database
unmatched_in_gdf = gdf_names - counts_names
# Find names in the database that don't have a match in the shapefile
unmatched_in_counts = counts_names - gdf_names

# Print the unmatched names
#if unmatched_in_gdf:
    #print("Names in shapefile not found in the database:")
    #print(unmatched_in_gdf)

if unmatched_in_counts:
    print("Names in database not found in the shapefile:")
    print(unmatched_in_counts)
