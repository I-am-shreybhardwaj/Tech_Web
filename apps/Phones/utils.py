import json


def html_tables_to_json(tables):
    try:
        result = []

        for table in tables:
            table_data = {}

            rows = table.find_all('tr')
            previous_key = ''
            main_key = ''
            for row in rows:
                cells = row.find_all(['th', 'td'])
                if cells:
                    key = cells[0].get_text(strip=True)
                    value = [cell.get_text(strip=True) for cell in cells[1:]]
                    if key:
                        previous_key = key
                        if key in ["Network","Launch","Body","Display","Platform","Memory","Main Camera","Selfie camera","Sound","Comms","Features","Battery","Misc","Tests"] and main_key not in ["Main Camera","Selfie camera","Tests"]:
                            main_key = key
                            table_data[value[0]] = value[1:]
                        else:
                            table_data[key] = value
                    if key == '':
                        if previous_key == main_key:
                            value = [table_data[list(table_data.keys())[0]][0] +" "+ value[0]]
                        else:
                            value = [table_data[previous_key][0] +" "+ value[0]]
                        table_data[previous_key] = value
                
            if main_key:
                result.append({main_key:table_data})

        return result
    except Exception as e:
        print(e)