""" Managing details of objects to search """
import json

BGR_FILTER = "bgr_filter"
BGR_FILTERS = "bgr_filters"
AREA_RANGE = "area_range"


def get_details(object_name):
    """Get details of obcjects given by name"""
    with open("./objectsParams.json") as file:
        return json.load(file)[object_name]
