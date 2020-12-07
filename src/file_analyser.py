import os

def analyse_from_filepath(filepath):
    with open(filepath, 'r')  as file:
        output = analyse_file(file)
        output.update(get_extension_from_filepath(filepath))
        return output

def analyse_file(file):
    lines = file.readlines()
    line_count = len(lines)
    line_lengths = []
    for line in lines:
        line_lengths.append(len(line))
    return {"line_count": line_count,
            "line_lengths": line_lengths}

def get_extension_from_filepath(filepath):
    _, extension = os.path.splitext(filepath)
    return {"extension": extension}
