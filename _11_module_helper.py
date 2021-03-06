def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        result = num_of_days * 24
    elif conversion_unit == "minutes":
        result = num_of_days * 24 * 60
    elif conversion_unit == "seconds":
        result = num_of_days * 24 * 60 * 60
    else:
        return "unsupported unit"

    return f"{num_of_days} days are {result} hours"


def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number")
        else:
            print("you entered a negative number, no conversion for you!")
    except ValueError:
        print("your input is not a valid number. Don't ruin my program!")


