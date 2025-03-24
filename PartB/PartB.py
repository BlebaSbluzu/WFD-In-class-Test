import PartA.PartA
import unittest

class UnitTests(unittest.TestCase):
    def test_part_of_object(self):

        self.assertTrue(isinstance(PartA.PartA.my_car, PartA.PartA.Vehicle))

    def test_not_part_of_object(self):
        self.assertFalse(isinstance(PartA.PartA.my_vehicle, PartA.PartA.Car))

    def test_are_objects_identical(self):
        self.assertNotEqual(PartA.PartA.my_car, PartA.PartA.my_vehicle)

    def test_update_vehicle_attributes(self):
        PartA.PartA.my_vehicle.set_colour("purple")
        self.assertEqual(PartA.PartA.my_vehicle.colour, "purple")
        PartA.PartA.my_vehicle.set_year(2022)
        self.assertEqual(PartA.PartA.my_vehicle.year, 2022)

    def test_update_car_attributes(self):
        PartA.PartA.my_car.set_make("Sedan")
        self.assertEqual(PartA.PartA.my_car.make, "Sedan")


if __name__ == "__main__":
    unittest.main()
