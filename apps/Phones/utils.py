import json


def html_tables_to_json(tables):
    result = []

    for table in tables:
        table_data = {}
        
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all(['th', 'td'])
            key = cells[0].get_text(strip=True)
            value = [cell.get_text(strip=True) for cell in cells[1:]]
            table_data[key] = value
        
        result.append(table_data)
    
    return result