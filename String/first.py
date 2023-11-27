name : str = 'Abdullah "Khalid"'
name = "Abdullah 'Khalid'"
last : int = 20
name = f'''This is a multi-line
               string using triple single quotes.{last}
               "How are you"
               It can contain 'single quotes' without escaping.'''
print(name)

first  = f""" This is a multi line 
Comment can't "How are you" {name}
'How are you'
"""

print(first)

