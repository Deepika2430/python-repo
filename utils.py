import json

def get_query_config(columns, selection_criteria, is_array, target_key, table):
    # Construct the dictionary representing the JSON structure
    config_dict = {
        "columns": columns,
        "selection_criteria": {
            "item_selection_key": selection_criteria["item_selection_key"],
            "table_selection_column": selection_criteria["table_selection_column"]
        },
        "is_array": is_array,
        "target_key": target_key,
        "table": table
    }
    
    # Convert the dictionary to a JSON string
    # json_string = json.dumps(config_dict, indent=4)  # Optional: indent for pretty printing
    
    return config_dict


def get_db_query(query_config):
    columns = ",".join(query_config["columns"])
    table_name = query_config["table"]
    table_selection_column = query_config["selection_criteria"]["table_selection_column"]
    item_selection_key = query_config["selection_criteria"]["item_selection_key"]
    query = f"SELECT {columns} FROM {table_name} WHERE {table_selection_column} = '{item_selection_key}';"
    return query


def get_json_response(columns, values):
    result = {column: [] for column in columns}
   
    for record in values:
        for column, value in zip(columns, record):
            result[column] = (value)
   
    json_response = json.dumps(result, indent=4)
    return json_response

# def get_formatted_response(columns, is_array, values):
#     if is_array:
#         response = zip(columns, values)
#         return response

def get_formatted_response(columns, values, is_array):

    if not columns:
        raise ValueError("The columns list must not be empty.")
    if not values:
        raise ValueError("The values list must not be empty.")

    if not all(
        isinstance(record, tuple) and len(record) == len(columns) for record in values
    ):
        raise ValueError("Each record must be a tuple with the same length as columns.")

    if len(columns) == 1:
        if not is_array:
            return  values[0][0]
        elif is_array:
            newlist = []
            for item in values:
                newlist.append(item[0])
            return newlist
    elif len(columns) > 1:
        if not is_array:
            return dict(zip(columns, values[0])) 
        elif is_array:
            return [dict(zip(columns, record)) for record in values]

def add_attribute(playlist_item, target_key, target_value):
    playlist_item[target_key] = target_value
    return playlist_item
    