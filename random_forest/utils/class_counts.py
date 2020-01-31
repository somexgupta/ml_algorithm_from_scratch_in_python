def class_counts(rows, column_number):
    """ counts the occurance of object in dataset for a particular column number
    return dic of object:count"""
    counts = {}  # a dictionary of label -> count
    for row in rows:
        label = row[column_number]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts
