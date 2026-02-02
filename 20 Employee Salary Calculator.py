def calculate_salary(hours, rate):
    gross_salary = hours * rate
    tax = 0.33 * gross_salary if gross_salary > 2500 else 0.24 * gross_salary
    net_salary = gross_salary - tax
    return gross_salary, tax, net_salary


def create_original_file():
    with open("Original.txt", "w") as original_file:
        for i in range(20):
            print(f"\nEmployee #{i+1}")
            name = input("Enter Employee Name: ").strip()
            emp_id = input("Enter ID: ").strip()
            hours = float(input("Enter Weekly Hours: "))
            rate = float(input("Enter Pay per Hour: "))

            # Save as CSV: name,id,hours,rate
            original_file.write(f"{name},{emp_id},{hours},{rate}\n")


def process_employee_data():
    with open("Original.txt", "r") as original_file, open("Copy.txt", "w") as copy_file:
        copy_file.write("Name,ID,Hours,Rate,Gross,Tax,Net\n")

        for line in original_file:
            name, emp_id, hours, rate = line.strip().split(",")

            hours = float(hours)
            rate = float(rate)

            gross, tax, net = calculate_salary(hours, rate)

            copy_file.write(
                f"{name},{emp_id},{hours},{rate},{gross:.2f},{tax:.2f},{net:.2f}\n"
            )


def display_employee_data():
    with open("Copy.txt", "r") as copy_file:
        print("\n--- Copy.txt Content ---")
        for line in copy_file:
            print(line.strip())


def main():
    create_original_file()      # makes Original.txt
    process_employee_data()     # reads Original.txt, writes Copy.txt
    display_employee_data()     # reads Copy.txt, prints to screen


if __name__ == "__main__":
    main()
