import json

try:
    with open('Personalized_Ad_Composer.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)

    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = cell.get('source', [])
            for i, line in enumerate(source):
                if 'cleaned_flipkart_products.csv' in line:
                    source[i] = line.replace('cleaned_flipkart_products.csv', 'cleaned_product_data.csv')
            cell['source'] = source

    with open('Personalized_Ad_Composer.ipynb', 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    print("Notebook updated successfully.")
except Exception as e:
    print(f"Error: {e}")
