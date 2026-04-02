import json
import os

notebook_path = 'notebooks/Personalized_Ad_Composer.ipynb'

if not os.path.exists(notebook_path):
    print(f"Error: Notebook not found at {notebook_path}")
else:
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Target cell ID: 877ade58
    target_found = False
    for cell in nb['cells']:
        if cell.get('id') == '877ade58':
            # Found the brand cleaning cell
            cell['source'] = [
                "def smart_brand_extractor(row):\n",
                "    brand = str(row['brand']).strip()\n",
                "    # If brand is 'Unknown' or missing, extract from product title\n",
                "    if not brand or brand.lower() in ['unknown', 'nan', 'na', '']:\n",
                "        p_name = str(row['product_name']).strip()\n",
                "        words = p_name.split()\n",
                "        if not words: return 'Aura'  # Default fallback\n",
                "        \n",
                "        # Handle cases like \"The North Face\" (take first 2 words)\n",
                "        if words[0].lower() in ['the', 'a', 'an'] and len(words) > 1:\n",
                "            detected = f\"{words[0]} {words[1]}\"\n",
                "        else:\n",
                "            detected = words[0]\n",
                "            \n",
                "        return detected.strip(\",.:'\\\" \")\n",
                "    return brand\n",
                "\n",
                "df_clean['brand'] = df_clean.apply(smart_brand_extractor, axis=1)\n",
                "\n",
                "print('Top 10 brands after smart cleaning:')\n",
                "print(df_clean['brand'].value_counts().head(10))"
            ]
            target_found = True
            break
            
    if target_found:
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1)
        print("Success: Updated the brand cleaning cell in the notebook!")
    else:
        print("Error: Could not find the target cell in the notebook.")
