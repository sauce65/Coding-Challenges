import re
str = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\t\tfile2.ext\n\t\tsubsubdir2"
# ^^ This is the file path string we are using, note the syntax
clean1 = re.sub("\\n\\t+", "/", str)
# ^^ In it's final state, we will be counting characters in this format
t_parse = re.findall("\\t+", str)
# ^^ Isolates all t-sequences for length analysis.
def string_length(a):
    length_check = []
    for i in range(len(a)):
        length_check.append(len(a[i]))
    return length_check
# ^^ This looks through a given list and returns the length of each element
b = max_length = max(string_length(t_parse))
# ^^ Variable containing the maximum length value of the t_parse list
t_string = ''
for i in range(b):
    t_string += '\\t'
deepest_terminus = f'{re.findall(t_string + ".+", str)}'
#print(deepest_terminus)
# ^^ Generates a string of t's matching the largest t series in the path, passes it into
# REGEX to locate in the main string
print(deepest_terminus)
dirty = 'dir'
sub = re.findall("\\n\\t+sub.+2", str)
file = re.findall("\\n\\t+file2.ext", str)
print(sub)
print(file)
for i in sub:
    dirty += i
for i in file:
    dirty += i
clean2 = re.sub("\\n\\t+", "/", dirty)
print(clean2)

#flaws: many.  Mainly, this doesn't auto-detect the main file branch number to reference in the lookback, and
#it doesn't have a contingency for when the terminating file in the path is just a subdir.  This is primitive but
#it works if you configure it for each string you parse
