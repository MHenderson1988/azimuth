import os
from unittest import TestCase

from main.location import Location
from main.location_reference_converter import convert_decimal_lat_long, convert_easting_northing, \
    convert_british_national_grid, conversion_type

DECIMAL_DEGREES_FILE_NAME = "test_decimal_degrees.csv"
BNG_FILE_NAME = "test_bng.csv"
OSBG_FILE_NAME = "test_osbg36.csv"

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


class TestLocationReferenceConverter(TestCase):
    def test_conversion_type(self):
        decimal_lat_long_expected = [Location(55.053203, -1.6918945, 200, "House 1")]
        xy_expected = [Location(54.906163, -1.381980, 150, "Fawcett street")]
        bng_expected = [Location(51.503532, -0.12779641, 150, "10 Downing street")]

        actual_list_decimal = conversion_type(self.create_test_file_path(DECIMAL_DEGREES_FILE_NAME), "decimal")
        actual_list_xy = conversion_type(self.create_test_file_path(OSBG_FILE_NAME), "xy")
        actual_bng = conversion_type(self.create_test_file_path(BNG_FILE_NAME), "bng")
        self.assertEqual(decimal_lat_long_expected[0].latitude, actual_list_decimal[0].latitude)
        self.assertEqual(xy_expected[0].latitude, actual_list_xy[0].latitude)
        self.assertEqual(round(bng_expected[0].latitude, 4), round(actual_bng[0].latitude, 4))

    def test_convert_easting_northing(self):
        list_to_test = [Location(54.906163, -1.381980, 150, "Fawcett street")]
        returned_list = convert_easting_northing(self.create_test_file_path(OSBG_FILE_NAME))
        self.assertEqual(list_to_test[0].latitude, returned_list[0].latitude)

    def test_convert_decimal_lat_long(self):
        list_to_test = [Location(55.053203, -1.6918945, 200, "House 1")]
        returned_list = convert_decimal_lat_long(self.create_test_file_path(DECIMAL_DEGREES_FILE_NAME))
        self.assertEqual(list_to_test[0].latitude, returned_list[0].latitude)

    def test_convert_british_national_grid(self):
        list_to_test = [Location(51.503532, -0.12779641, 200, "10 Downing street")]
        returned_list = convert_british_national_grid(self.create_test_file_path(BNG_FILE_NAME))
        self.assertEqual(round(list_to_test[0].latitude, 4), round(returned_list[0].latitude, 4))

    @staticmethod
    def create_test_file_path(filename):
        return os.path.join(CURRENT_DIR, "data/" + filename)
