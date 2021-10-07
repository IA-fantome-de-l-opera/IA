from collections import Counter

# counting how many people in a room are still suspects
def suspects_in_room(data, room):
    suspects = 0
    for character in data:
        if (character["position"] == room) and (character["suspect"] == True):
            suspects += 1
    return suspects

def inspector_points(data, shadow):
    alone_suspects = 0
    grouped_suspects = 0
    # counting how many people are in each room
    positions = Counter(d["position"] for d in data)
    for position, count in positions.most_common():
        if (count > 1) and (shadow != position):
            grouped_suspects += suspects_in_room(data, position)
        else:
            alone_suspects += suspects_in_room(data, position)
    print("grouped suspects: ", grouped_suspects)
    print("alone suspects: ", alone_suspects)
    # calculate the minimum possible gain
    min_points = min(grouped_suspects, alone_suspects)
    # add a small bonus for red character's power
    red = next((character for character in data if character["color"] == "red"), None)
    if red["power"]:
        min_points += 0.5
    print("final points: ", min_points)
    return min_points

def phantom_points(data, shadow, phantom_color):
    phantom_suspects = 0
    safe_suspects = 0
    phantom_scream = True
    phantom = next((character for character in data if character["color"] == phantom_color), None)
    # counting how many people are in each room
    positions = Counter(d["position"] for d in data)
    # if the phantom is alone or in the dark it screams
    if (positions[phantom["position"]] > 1) and (shadow != phantom["position"]):
        phantom_scream = False
    for position, count in positions.most_common():
        if (count > 1) and (shadow != position):
            if phantom_scream:
                safe_suspects += suspects_in_room(data, position)
            else:
                phantom_suspects += suspects_in_room(data, position)
        else:
            if phantom_scream:
                phantom_suspects += suspects_in_room(data, position)
            else:
                safe_suspects += suspects_in_room(data, position)
    print("phantom suspects: ", phantom_suspects)
    print("safe suspects: ", safe_suspects)
    points = phantom_suspects
    # add a small bonus for red character's power
    red = next((character for character in data if character["color"] == "red"), None)
    if red["power"]:
        points += 0.5
    # calculate the points
    print("final points: ", points)
    return points



#testing

test_data =  [
    {'color': 'white', 'suspect': True, 'position': 3, 'power': False},
    {'color': 'red', 'suspect': True, 'position': 3, 'power': True},
    {'color': 'blue', 'suspect': True, 'position': 3, 'power': True},
    {'color': 'purple', 'suspect': True, 'position': 9, 'power': False},
    {'color': 'black', 'suspect': True, 'position': 9, 'power': False},
    {'color': 'pink', 'suspect': True, 'position': 8, 'power': False},
    {'color': 'grey', 'suspect': True, 'position': 1, 'power': False}
]

print ("inspector /o\\\n")
inspector_points(test_data, 0)
print ("\nphantom \\o/\n")
phantom_points(test_data, 0, "white")