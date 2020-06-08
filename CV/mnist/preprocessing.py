#python3
import pandas as pd

def from_file(path):
    """

    :param path: "the path to file"
    :return:
    """
    file_content = pd.read_csv(path)
    y = file_content[file_content.columns[:-1]] / 255
    x = y.values.tolist()
    return x


