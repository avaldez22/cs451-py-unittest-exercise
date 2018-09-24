# test_geolocwrapper.py
import unittest

from geolocwrapper import GeoLocWrapper
from geopy.exc import GeopyError
from geopy.distance import geodesic


class TestGeoLocWrapper(unittest.TestCase):
    """A collection of unit tests for the BabySet class. 
    Used to demonstrate and introduce unit testing in Python.
    Related docs: https://docs.python.org/3/library/unittest.html
    """
    def test_init(self):
        """Unit test for GeoLocWrapper constructor."""
        loc = GeoLocWrapper('1701 bryant st, denver, co')
        self.assertEqual(loc.location.latitude, 39.743952)

    def test_init_fail(self):
        """Unit test for GeoLocWrapper constructor."""
        with self.assertRaises(GeopyError):
            dist = GeoLocWrapper()



    # Begin adding your unit tests for the GeoLocWrapper module.
        def test_init_fail(self):
        with self.assertRaises(GeopyError):
            test = GeoLocWrapper("2415 Calle Alegre, las vegas, nm")
            
    def test_get_distance_miles(self):
        loc = GeoLocWrapper('1701 bryant st, denver, co')
        dist = loc.get_distance_miles('1314 chavez st, las vegas, nm')
        self.assertEqual(dist, 286.80227495947776)
            
    def test_get_distance_kilometers(self):
        loc = GeoLocWrapper('1701 bryant st, denver, co')
        dist = loc.get_distance_kilometers('1314 chavez st, las vegas, nm')
        self.assertEqual(dist, 461.5635203923858)

if __name__ == '__main__':
    unittest.main()
