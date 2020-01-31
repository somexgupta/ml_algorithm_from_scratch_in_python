def unique_vals(rows, column_number):
    """Find the unique values from a column in a dataset based on column number"""
    return set([row[column_number] for row in rows])
