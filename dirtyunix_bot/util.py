import random


def random_line(file_path):
    """Get random line from a file."""
    # Fancy alg from http://stackoverflow.com/a/35579149 to avoid loading full file.
    line_num = 0
    selected_line = ""
    with open(file_path) as f:
        while 1:
            line = f.readline()
            if not line:
                break
            line_num += 1
            if random.uniform(0, line_num) < 1:
                selected_line = line

    return selected_line.strip()
