import unittest
import lesson_33

class TestLesson33(unittest.TestCase):
    def setUp(self): # запускается в начале каждой функции 
        print("начинается работа теста")

    def test_do_stuff(self):
        num = 10
        result = lesson_33.do_stuff(num)
        self.assertEqual(result, 15)
    
    def test_do_stuff_2(self):
        num = "10"
        result = lesson_33.do_stuff(num)
        self.assertEqual(result, 15)

    def test_do_stuff_3(self):
        num = "dads"
        result = lesson_33.do_stuff(num)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff_4(self):
        test_param = None
        result = lesson_33.do_stuff(test_param)
        self.assertEqual(result, "enter a valid number")

    def test_do_stuff_5(self):
        test_param = ''
        result = lesson_33.do_stuff(test_param)
        self.assertEqual(result, "enter a valid number")

    # def tearDown(self):
    #     print("заканчиваю работу функции")

if __name__ == '__main__':
    unittest.main()



# isinstance([1,2,3], list)
# unittest.main()
# py -m unittest