# Created by Leon Hunter at 3:57 PM 10/23/2020
class StringManipulator(object):
    def get_hello_world(self):
        return "Hello World"

    def concatenate(self, value_to_be_added_to, value_to_add):
        return str(value_to_be_added_to) + str(value_to_add)

    def substring_inclusive(self, string_to_fetch_from, starting_index, ending_index):
        return string_to_fetch_from[starting_index:ending_index+1]

    def substring_exclusive(self, string_to_fetch_from, starting_index, ending_index):
        return string_to_fetch_from[starting_index + 1: ending_index]

    def compare(self, first_value, second_value):
        str1= str(first_value)
        str2 = str(second_value)
        int1 = int(first_value)
        int2 = int(second_value)
        bool1 = bool(first_value)
        bool2 = bool(second_value)
        ev1 = int1 == int2
        ev2 = str1 == str2
        ev3 = bool1 == bool2
        if first_value == second_value or ev1 or ev2 or ev3:
            return True
        else:
            return False

    def get_middle_character(self, string_to_fetch_from):
        midchar = len(string_to_fetch_from)/2
        return string_to_fetch_from[midchar]

    def get_first_word(self, string_to_fetch_from):
        first_word = string_to_fetch_from.split()[0]
        return first_word
    def get_second_word(self, string_to_fetch_from):
        second_word = string_to_fetch_from.split()[1]
        return second_word

    def reverse(self, string_to_be_reversed):
        str_rev = string_to_be_reversed[::1]
        return str_rev