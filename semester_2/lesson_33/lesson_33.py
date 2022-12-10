def do_stuff(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return "enter a valid number"
    except ValueError as err:
        return err
        
        # raise # программа полностью остановится

# print(isinstance([1,2,3], list))
# err = ValueError()
# print(isinstance(err, ValueError)) #True
# print(isinstance(err, TypeError)) # False


# import unittest

# def add_fish_aquarium(fish_list):
#     if len(fish_list) > 10:
#         # return "A maximum of 10 fish can be added to the aquarium"
#         raise ValueError("A maximum of 10 fish can be added to the aquarium")
#     return {"tank_a": fish_list}

# class TestAddFishToAquarium(unittest.TestCase):
#     def test_add_fish_to_aquarium_success(self):
#         # calling function to test
#         actual = add_fish_aquarium(fish_list=["shark", "tuna"])
#         expected = {"tank_a": ["shark", "tuna"]}
#         self.assertEqual(actual, expected)
    
#     def test_do_fish_to_aquarium_expection(self):
#         too_many_fish = ["shark"] * 9
#         with self.assertRaises(ValueError) as exception_context:
#             add_fish_aquarium(fish_list=too_many_fish)
#         self.assertEqual(
#             str(exception_context.exception),
#             "A maximum of 10 fish can be added to the aquarium"
#         )
# print(TestAddFishToAquarium())