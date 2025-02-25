"""import re
x = r'a(b*)'
test_strings = ['a', 'ab', 'abb', 'ac', 'b', 'aabb']
for string in test_strings:
    match = re.match(x, string)
    if match:
        print(f"'{string}' matches: {match.group()}")
    else:
        print(f"'{string}' does not match")



import re

x= r'a(b{2,3})'
test_strings = ['ab', 'abb', 'abbb', 'a', 'aabb', 'abbbb']
matches = [s for s in test_strings if re.fullmatch(x, s)]
print(matches)


import re

def sequences(string):
    return re.findall(r'\b[a-z]+_[a-z]+\b', string)
print(sequences("hello_world  Hello_world ")) 



import re

def uplow_sequences(string):
    return re.findall(r'[A-Z][a-z]+', string)
print(uplow_sequences("Hello World  hello")) 


import re

def match_a_b(string):
    return bool(re.fullmatch(r'a.*b', string))
print(match_a_anything_b("ax1243ddjcfutujb"))


import re

def replace(string):
    return re.sub(r'[ ,.]', ':', string)
print(replace("Hello, world.hello"))  


import re

def snake_camel(string):
    words = string.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])
print(snake_to_camel("hello_world_camel")) 


import re

def split_upper(string):
    return re.split(r'(?=[A-Z])', string)
print(split_upper("HelloWorldCase")) 


import re

def insert_space(string):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', string)
print(insert_space("helloWorldSpace")) """


import re

def camel_snake(string):
     return re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()
print(camel_snake("helloWorldSnake")) 













