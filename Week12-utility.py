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

