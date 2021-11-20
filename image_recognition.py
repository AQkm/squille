""" Functions for image recognition """
import base64

import cv2
import numpy as np

LOWER_KEY = "lower"
UPPER_KEY = "upper"


def filter_image(image_rgb, lower_array, upper_array):
    """Given image is filtered by given range of colors"""
    lower = np.array(lower_array)
    upper = np.array(upper_array)
    return cv2.inRange(image_rgb, lower, upper)


def find_area(image_to_search, area_range):
    """Finding objects with given area range on image"""
    contours, hierarchy = cv2.findContours(  # noqa pylint: disable=unused-variable
        image_to_search, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
    )
    objects = list()
    for contour in contours:
        area = cv2.contourArea(contour)
        if area_range[0] < area < area_range[1]:
            objects.append(contour)
    return objects


def get_center_coordinate(element):
    """Getting center point of area"""
    contour_perimeter = cv2.arcLength(element, True)
    approx = cv2.approxPolyDP(element, 0.02 * contour_perimeter, True)
    point_x, point_y, width, height = cv2.boundingRect(approx)
    center_x = point_x + (width - 1) / 2
    center_y = point_y + (height - 1) / 2
    return int(center_x), int(center_y)


def get_objects_coordinate(img_path, filters, area_range):
    """Getting coordinates of objects with given colors and area ranges"""
    img_input = cv2.imread(img_path)
    filtered_image = filter_image(img_input, filters[LOWER_KEY], filters[UPPER_KEY])
    found_objects = find_area(filtered_image, area_range)
    objects_coordinate = list()
    for found_object in found_objects:
        objects_coordinate.append(get_center_coordinate(found_object))
    return objects_coordinate
