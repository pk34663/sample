import unittest
import sphereutils

class TestSphereUtils(unittest.TestCase):
    volume = 5.0
    def test_calcradius(self):
        r = sphereutils.calcradius(self.volume)
        self.assertEqual(r, 14)

    def test_calcarea(self):
        r = sphereutils.calcradius(self.volume)
        a = sphereutils.calcarea(self.volume, r)
        self.assertEqual(r, 14)

if __name__ == '__main__':
    unittest.main()