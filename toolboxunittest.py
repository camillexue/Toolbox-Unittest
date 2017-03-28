import unittest


def filter_list(original_list):
    new_list = []
    for item in sorted(original_list):
        if item < 0:
            continue
        else:
            new_list.append(item)
    return new_list


class TestFilterList(unittest.TestCase):
    def test_filter_list(self):
        test_list = [1, 5, -4, 10239, -30, 7]
        test_list2 = [1, 'cats', 'a', 5, 20]
        self.assertEqual(filter_list(test_list), [1, 5, 7, 10239])
        with self.assertRaises(TypeError):
            filter_list(test_list2)


if __name__ == '__main__':
    unittest.main()
