# Function to read class names from a file
def read_class_names(file_path):
    with open(file_path, 'r') as file:
        class_names = [line.strip() for line in file.readlines()]
    return class_names