import unittest
import lesson_34

class TestFindNumber(unittest.TestCase):
    def setUp(self):
        print("Начинается работа функции")

    def test_find_number_success(self):
        self.assertTrue(lesson_34.find_number(3, 3))

    def test_find_number_wrong_answer(self):
        self.assertFalse(lesson_34.find_number(4, 2))

    def test_find_number_out_of_range(self):
        self.assertFalse(lesson_34.find_number(12, 4))

    def test_find_number_invalid_value(self):
        self.assertFalse(lesson_34.find_number('2', '4'))
    
    def test_find_number_invalid_type(self):
        self.assertFalse(lesson_34.find_number('11', 5))
    
    def tearDown(self):
        print("заканнчиваю работу функции")

unittest.main()

# -v более детально