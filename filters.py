from utils import get_db_query, get_formatted_response, add_attribute
from db import get_db_response

def filter_pgdb(playlist_item, connection_string, query_config):
    query = get_db_query(query_config)
    response = get_db_response(query, connection_string)
    json_response = get_formatted_response(query_config["columns"], response, query_config["is_array"])
    print(json_response)
    playlist_item = add_attribute(playlist_item, query_config["target_key"], json_response)
    return playlist_item

