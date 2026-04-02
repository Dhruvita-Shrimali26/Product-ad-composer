import pandas as pd
import os

# Define file path
csv_path = 'notebooks/cleaned_product_data.csv'

if not os.path.exists(csv_path):
    print(f"ERROR: File not found: {csv_path}")
else:
    print(f"Reading {csv_path}...")
    df = pd.read_csv(csv_path)
    
    # Statistics before change
    initial_unknowns = len(df[df['brand'].str.lower() == 'unknown']) if 'brand' in df.columns else 0
    print(f"Found {initial_unknowns} 'unknown' brands.")

    # Function for smart extraction
    def extract_brand(row):
        brand = row.get('brand', '')
        # If brand is 'unknown' or empty, extract from product_name
        if pd.isna(brand) or str(brand).lower() in ['unknown', 'na', 'nan', '']:
            product_name = str(row.get('product_name', ''))
            words = product_name.split()
            if not words:
                return 'Aura' # Default fallback
            
            # Smart logic (same as app.py)
            if words[0].lower() in ["the", "a", "an"] and len(words) > 1:
                detected = f"{words[0]} {words[1]}"
            else:
                detected = words[0]
            
            return detected.strip(",.:'\" ")
        return brand

    # Apply changes
    df['brand'] = df.apply(extract_brand, axis=1)
    
    # Save back
    df.to_csv(csv_path, index=False)
    
    # Statistics after change
    remaining_unknowns = len(df[df['brand'].str.lower() == 'unknown'])
    print(f"Data updated! Remaining 'unknown' brands: {remaining_unknowns}")
    print(f"CSV saved successfully to {csv_path}")
