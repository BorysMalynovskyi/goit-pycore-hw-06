def total_salary(path):
    """
    Calculates the total and average salary of employees from a text file.

    Parameters:
        path (str): path to the text file containing data in the format "Full Name,Salary"

    Returns:
        tuple: (total_salary, average_salary)
    """
    try:
        with open(path, 'r', encoding="utf-8") as file:
            total = 0
            count = 0

            for line in file:

                line = line.strip()

                if not line:
                    continue

                try:
                    _, salary = line.split(',')
                    total += int(salary)
                    count += 1

                except ValueError:
                    print(f"Error in the line: {line}")

            if count == 0:
                return (0, 0)

            average = total / count
            return (total, average)

    except FileNotFoundError:
        print("File not found.")
        return (0, 0)

total, average = total_salary("homework_6\salary.txt")

print(f"Total: {total}, Average: {average}")
