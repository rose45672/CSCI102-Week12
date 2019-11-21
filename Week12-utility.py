# PrintOutput
def PrintOutput(input_string):
    print("OUTPUT", input_string)
    
# LoadFile
def LoadFile(filename):
    with open(filename, 'r') as f:
        contents = f.read()
    contents = contents.split('\n')
    return contents

# UpdateString
def UpdateString(string_one, string_two, num):
    list_one = list(string_one)
    list_one[num] = string_two
    new_string = ''.join(list_one)
    return new_string 

# FindWordCount
def FindWordCount(user_list, user_string):
    count = 0
    for n in user_list:
        count += n.count(user_string)
    return count

