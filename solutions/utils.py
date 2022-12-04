def get_data(path:str)-> list[str]:
    """Read Data, return list of rows.

    Args:
        path (str): Path to data

    Returns:
        list[str]: List of rows
    """
    data_rows = open(path).read().split("\n")

    return data_rows