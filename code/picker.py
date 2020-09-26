import os
import pathlib
import random

def get_file_element(file):
    lines = [i.rstrip() for i in open(file) if i.rstrip()]
    return random.choice(lines)

def pick_elements(folder):
    result = []
    for file in os.listdir(folder):
        file = os.path.join(folder, file)
        if file.endswith(".txt"):
            result.append(get_file_element(file))
    return result

def return_picked_elements(elements):
    print(elements)

def main():
    base_path = pathlib.Path(__file__).resolve().parent.parent
    data_path = os.path.join(base_path, "data")
    picked_elements = pick_elements(data_path)
    return_picked_elements(picked_elements)

if __name__ == "__main__":
    main()