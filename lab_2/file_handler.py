def read_file(path: str) -> str:
    """The function of reading text from a file
    Args:
      path: the path to the file
    Returns:
      text from the file
    """
    with open(path, "r", encoding='UTF-8') as file:
        text = file.read()
    return text


def write_file(path: str, info: str) -> None:
    """The function of writing information to a file
    Args:
      path: the path to the file
    """
    with open(path, "w", encoding='UTF-8') as file:
        file.write(info)