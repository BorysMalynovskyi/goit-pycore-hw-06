def get_cats_info(path):
    """
    Reads a text file with cat information and returns a list of dictionaries.

    Each line in the file should be in the format:
        id,name,age

    Parameters:
        path (str): Path to the text file containing cat data.

    Returns:
        list[dict]: A list of dictionaries, each with keys "id", "name", "age".
    """
    cats = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            line = file.readline()

            while line:
                line = line.strip()
                cat_id, name, age = line.split(",")
                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }
                cats.append(cat_info)

                line = file.readline()

        return cats

    except FileNotFoundError:
        print("File not found.")
        return []

cats_info = get_cats_info("homework_6\cats.txt")

for cat_info in cats_info:
    print(cat_info)
