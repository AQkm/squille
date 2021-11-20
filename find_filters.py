""" Support script for getting BGR filter and are size range from image """
import sys

import cv2
import numpy as np

img = cv2.imread(str(sys.argv[1]))
cv2.imshow("Your image", img)


def empty():
    """Empty"""


cv2.namedWindow("TrackColors")
cv2.resizeWindow("TrackColors", 1200, 500)
cv2.createTrackbar("Blue Min", "TrackColors", 0, 255, empty)
cv2.createTrackbar("Blue Max", "TrackColors", 255, 255, empty)
cv2.createTrackbar("Green Min", "TrackColors", 0, 255, empty)
cv2.createTrackbar("Green Max", "TrackColors", 255, 255, empty)
cv2.createTrackbar("Red Min", "TrackColors", 0, 255, empty)
cv2.createTrackbar("Red Max", "TrackColors", 255, 255, empty)
cv2.createTrackbar("Size Min", "TrackColors", 0, 100000, empty)
cv2.createTrackbar("Size Max", "TrackColors", 100000, 100000, empty)

while True:
    try:
        b_min = cv2.getTrackbarPos("Blue Min", "TrackColors")
        b_max = cv2.getTrackbarPos("Blue Max", "TrackColors")
        g_min = cv2.getTrackbarPos("Green Min", "TrackColors")
        g_max = cv2.getTrackbarPos("Green Max", "TrackColors")
        r_min = cv2.getTrackbarPos("Red Min", "TrackColors")
        r_max = cv2.getTrackbarPos("Red Max", "TrackColors")
        s_min = cv2.getTrackbarPos("Size Min", "TrackColors")
        s_max = cv2.getTrackbarPos("Size Max", "TrackColors")
    except:  # noqa pylint: disable=bare-except
        break
    lower = np.array([b_min, g_min, r_min])
    upper = np.array([b_max, g_max, r_max])
    mask = cv2.inRange(img, lower, upper)
    print("Current Lower and Upper:")
    print(lower)
    print(upper)
    print("Size:", s_min, s_max)

    contours, hierarchy = cv2.findContours(  # noqa pylint: disable=unused-variable
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
    )
    els = list()
    for contour in contours:
        area = cv2.contourArea(contour)
        if s_min < area < s_max:
            els.append(contour)
    img_with_el = img.copy()
    cv2.drawContours(img_with_el, els, -1, (b_min-20, g_min-20, r_min-20), 2)
    cv2.imshow("Filtered image", mask)
    cv2.imshow("Founded Elements", img_with_el)
    cv2.waitKey(100)
