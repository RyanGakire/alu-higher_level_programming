#!/usr/bin/python3
def weight_average(my_list=[]):
    """Compute the weighted average of a list of (score, weight) tuples.

    Args:
        my_list (list): a list of (score, weight) tuples.

    Returns:
        float: the weighted average, or 0 if the list is empty.
    """
    if not my_list:
        return 0

    total_score = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for score, weight in my_list)

    if total_weight == 0:
        return 0

    return total_score / total_weight
