'''
# Variable
  # A computer is a special machine that operates by processing on data (information) and 
    variables are the basic structures to store data/information.
  # Each variable has: a name (identifier), a type and its content

# Type
  A computer stores any type of information in a binary mode, (like zeroes and ones), 
  that means it is necessary to associate the stored content to a type, so the computer
  can interpreter the data as expected.
  # Common types in Python:
    # Integer
    # Floating point
    # Boolean
    # String

# Identifier
  # An identifier is a name used to identify something in a program.
  # In Python an identifier is case sensitive, and starts with a letter, or
    an underscore (_) followed by zero or more letters, underscores or digits (0 to 9)
  # PS: An identifier can't start with a number (This is valid for all languages I know)
  # Reserved words:
    and       del       from      not       while
    as        elif      global    or        with
    assert    else      if        pass      yield
    break     except    import    print
    class     exec      in        raise
    continue  finally   is        return
    def       for       lambda    try
'''

# Integer
age = 52  # Declaring and assigning an integer value

# Prints to the default output:
# type of age, the string 'age =' and the content of age variable
# All separated by one white space
print(type(age), 'age =', age)

# Floating point
payment = 345.67
print(type(payment), 'payment =', payment)

# Boolean
approved = True
print(type(approved))
print('approved =', approved)
approved = False
print('approved =', approved)
approved = True
print('approved =', approved)

# String
first_name = 'José'
print(type(first_name), 'name =', first_name)

last_name = 'Santos'
print('Full name =', first_name, last_name)

# 'Crazy' thing about python. It is dynamically typed
# # Not a static typed language, like many other languages Java, C, C++, C#, Kotlin, Scala
age = 'Leila'
approved = 100.5
first_name = 52
print('age: ', age, 'approved:', approved, 'first_name', first_name)

# Explain these cases below witht the presentation
# and show it debugging

name = "Jose Santos"
age = 52
name = "Leila"


# Mutiple reference to the same variable
lang_1 = "Python"
lang_2 = lang_1
print("lang_1:", lang_1, "; lang_2:", lang_2)

lang_2 = "Java"
print("lang_1:", lang_1, "; lang_2:", lang_2)

# Attention: Remember to mention that in the future we will learn
# reference types