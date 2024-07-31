"""
# read the parts of a phone number and print the full number using the format below
  COUNTRY_CODE (AREA_CODE) PREFIX-LINE_NUMBER
  Ex: +1 (640) 850-1189
"""
country_code = input("Country code: ")
area_code = input("Area Code: ")
prefix = input("Prefix: ")
line_number = input("Line number: ")
print(country_code, "(", area_code, ")", prefix, "-", line_number)
print(country_code +  " (" + area_code + ") " + prefix + "-" + line_number)

formated_phone = country_code +  " (" + area_code + ") " + prefix + "-" + line_number
print(formated_phone)

formated_phone = f"{country_code} ({area_code}) {prefix}-{line_number}"
print(formated_phone)