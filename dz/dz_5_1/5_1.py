import keyword

variable_name = input("Enter variable name: ")

if (variable_name.isidentifier() and not
any(letter.isupper() for letter in
    variable_name) and not
(variable_name.strip("_") == "" and
 "__" in variable_name) and not
keyword.iskeyword(variable_name) and
        variable_name not in ("True", "False", "None")):
    print(True)
else:
    print(False)