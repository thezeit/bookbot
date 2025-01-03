with open("books/frankenstein.txt") as f:
    file_contents = f.read()

count = 0
for word in file_contents.split():
    count +=1


alph_dict = {
    'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,
    'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
    's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
    }

lower_case = file_contents.lower()

for character in lower_case:
    if character in alph_dict:
        alph_dict[character] += 1
    
print("--- Begin report of books/frankenstein.txt ---")
print(f"{count} words were found in the document\n")

for key in alph_dict:
    print(f"The '{key}' character was found {alph_dict[key]} times")

print(" --- End report ---")