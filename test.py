from utils import get_query_config, get_formatted_response
from filters import filter_pgdb
from response import playlist

database_url = "dbname=dsp host=192.168.1.140 port=7000 user=postgres password=postgres"

query_config = get_query_config(["media_id", "is_premium"], {
        "item_selection_key": "xx123xx",
        "table_selection_column": "media_id"
    }, False, "medias", "premium_assets")
response = filter_pgdb(playlist["playlist"][0], database_url, query_config)
print(response)