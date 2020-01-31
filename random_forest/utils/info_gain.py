from utils.gini import gini


def info_gain(left, right, current_uncertainty, column_number):
    """ Information Gain.
    The uncertainty of the starting node minus the weighted impurity of two child nodes.
    """
    p = float(len(left) / (len(left) + len(right)))
    return current_uncertainty - p * gini(left, column_number) - (1 - p) * gini(right, column_number)
