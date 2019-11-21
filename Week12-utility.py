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

# ScoreFinder 
def ScoreFinder(player_list, score_list, player):
    lower_player_list = []
    for item in player_list:
        lower_player_list.append(item.lower())
    lower_player = player.lower()
    player_name = lower_player.capitalize()
    index = lower_player_list.index(lower_player)
    if index > -1:
        player_score = score_list[index]
        output = "%s got a score of %d" % (player_name, player_score)
    else:
        output = "player not found"
    return output

# Union
def Union(list1, list2):
    new_list1 = []
    new_list2 = []
    for i in list1:
        if i not in new_list1:
            new_list1.append(i)
    for n in list2:
        if n not in new_list2:
            new_list1.append(2)
    combined_list = new_list1 + new_list2

# Intersection
def Intersection(list1, list2):
    intersect_list = []
    for n in list1:
        if n in list2:
            intersect_list.append(n)
    return intersect_list

# NotIn
def NotIn(list1, list2):
    notIn _list = []
    for n in list2:
        if n not in list1:
            notIn_list.append(n)
    return notIn_list

