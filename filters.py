# Executed filters using exec()

from jw_player_response import response

filter_repo = {
    "filter_update_image_type" : {
        "code" : '''def filter_update_image_type(playlist):
        print("called")
        images = playlist["images"]
        type = images[0]["type"]
        images = [{key: value for key, value in image.items() if key != 'type'} for image in images]
        new_dictionary = {"type": type, "list": images}
        playlist["images"] = new_dictionary
        return playlist'''
    },
    "filter_watch_free": {
        "code" : '''def filter_watch_free(playlist):
        watch_free = False
        if not playlist["requiresSubscription"]:
            watch_free = True
        playlist["watchFree"] = watch_free
        return playlist'''
    }
}

media = response["playlist"][0]

for filter, filter_function in filter_repo.items():
    exec(filter_function["code"])

filter_functions = [filter_update_image_type, filter_watch_free]

for counter in range(0, len(filter_functions)):
    media = filter_functions[counter](media)

print(media)