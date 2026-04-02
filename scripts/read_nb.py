import json

with open('Personalized_Ad_Composer.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

cells = nb['cells']
print(f"Total cells: {len(cells)}")
print(f"Notebook format: {nb.get('nbformat', 'unknown')}.{nb.get('nbformat_minor', 'unknown')}")
print(f"Kernelspec: {nb.get('metadata', {}).get('kernelspec', {}).get('display_name', 'unknown')}")
print()

for i, c in enumerate(cells):
    cell_type = c['cell_type']
    source = ''.join(c.get('source', []))
    print(f"=== CELL {i} ({cell_type}) ===")
    print(source[:3000])
    print()
