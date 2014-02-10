# Write a program, lettercount.py that opens a file named on
# the command line and counts how many times each letter occurs
# in that file. Your program should then print those counts to
# the screen in alphabetical order

print "Welcome to the letter counter. Please enter a file name."

def file_str(filename):
    """Given a file name, file_str returns a string rep of the file"""
    f = open(filename)
    f_str = f.read()
    return f_str

def count_letters(f_str):
    """Counts the occurences of letters a - z and prints out
    the count in order. Returns nothing."""
    for letter in range(97, 123):
        char_count = 0
        for character in f_str:
            if character == chr(letter):
                char_count += 1
        print char_count
            
filename = raw_input(">")
f_str = file_str(filename).lower()
count_letters(f_str)
