import sys
import image_recognition
import objects

img_path = str(sys.argv[1])
object_name = str(sys.argv[2])

vessel_params = objects.get_details(object_name)
px_coordinates = image_recognition.get_objects_coordinate(
    img_path,
    vessel_params[objects.BGR_FILTER],
    vessel_params[objects.AREA_RANGE],
)
sys.stdout.write("Coordinate of the object '%s' in pixels:\n %s" % (object_name, px_coordinates))