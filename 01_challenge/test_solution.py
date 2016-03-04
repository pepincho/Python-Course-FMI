import unittest
from solution import body_mass_index, shape_of


class TestBodyMassIndex(unittest.TestCase):
    def test_body_mass_index(self):
        self.assertEqual(body_mass_index(90, 2), 22.5)
        self.assertEqual(body_mass_index(90, 1.88), 25.5)


class TestShapeOf(unittest.TestCase):
    def test_shape_of_severe_malnutrition(self):
        self.assertEqual(shape_of(13, 1), 'тежко недохранване')
        self.assertEqual(shape_of(17, 1.2), 'тежко недохранване')

    def test_shape_of_average_malnutrition(self):
        self.assertEqual(shape_of(15.1, 1), 'средно недохранване')
        self.assertEqual(shape_of(19, 1.1), 'средно недохранване')

    def test_shape_of_mild_malnutrition(self):
        self.assertEqual(shape_of(16.1, 1), 'леко недохранване')
        self.assertEqual(shape_of(18.5, 1), 'леко недохранване')

    def test_shape_of_normal_weight(self):
        self.assertEqual(shape_of(22.9, 1.1), 'нормално тегло')
        self.assertEqual(shape_of(60, 1.77), 'нормално тегло')

    def test_shape_of_overweight(self):
        self.assertEqual(shape_of(25.1, 1), 'наднормено тегло')
        self.assertEqual(shape_of(30, 1), 'наднормено тегло')

    def test_shape_of_first_obesity(self):
        self.assertEqual(shape_of(32, 1), 'затлъстяване I степен')
        self.assertEqual(shape_of(35, 1), 'затлъстяване I степен')

    def test_shape_of_second_obesity(self):
        self.assertEqual(shape_of(35.1, 1), 'затлъстяване II степен')
        self.assertEqual(shape_of(40, 1), 'затлъстяване II степен')

    def test_shape_of_third_obesity(self):
        self.assertEqual(shape_of(55, 1), 'затлъстяване III степен')
        self.assertEqual(shape_of(999, 2), 'затлъстяване III степен')


if __name__ == '__main__':
    unittest.main(verbosity=2)
