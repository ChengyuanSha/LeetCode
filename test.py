def equal_num_occurrence(list_a, list_b, target):
    """
  This function uses iteration to see if to lists both have the same
  number of occurrences of a number.
  Returns False if one of the list is empty or if the lists dont have the same
  number of occurrences of a target number.
  """
    a_target_occure = 0
    b_target_occure = 0
    if (len(list_a) == 0) or (len(list_b) == 0):
        return False
    else:
        for num in list_a:
            if num == target:
                a_target_occure += 1
        for num in list_b:
            if num == target:
                b_target_occure += 1
        if a_target_occure == b_target_occure:
            return True
        else:
            return False


def test_one():
    """ Tests when both lists are empty """
    assert equal_num_occurrence([], [], 5) == False


def test_two():
    """Tests when one list is empty"""
    assert equal_num_occurrence([5], [], 5) == False


def test_three():
    """Tests when both lists have the same number of occurrences of the target
  number """
    assert equal_num_occurrence([1, 2, 4, 5, 4], [3, 4, 4], 4) == True