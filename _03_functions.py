units_formulae = 24 * 60  # global scope variable
unit_name = "minutes"


def days_to_units(no_of_days, message):
    print(f"{no_of_days} days are {no_of_days * units_formulae} {unit_name}")
    print(message)


days_to_units(2, "great")
days_to_units(5, "awesome")
days_to_units(7, "jhakaas")
