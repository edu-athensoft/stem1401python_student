"""
stem1402_python_final_p2_ken
Ken

Commented out is an interactive result inputter.
"""


# results = []
# continues = True
#
# while continues:
#     results.append(input("Please write the team's number: "))
#     results.append(input("Please write the team's name: "))
#     results.append(input("Please write the team's 1st score: "))
#     results.append(input("Please write the team's 2nd score: "))
#     while continues:
#         choice = input("Add another team?:\n"
#                           "Enter 'yes' if so\n"
#                           "Enter 'no' if done\n")
#         if choice == "yes":
#             break
#         elif choice == "no":
#             continues = False
#         else:
#             print("Invalid input, try again")
#             continue

# Test the inputter above if desired. However, the data is already here.
results = ['1', 'Robert Master', '220', '340',
           '2', 'Montreal Sprite', '320', '270',
           '3', 'Smart Maker', '115', '405',
           '4', 'Nova Robert', '450', '380',
           '5', '10 Stars', '100', '330']


def lego_competition_sorter(result):
    number_of_teams = len(result)/4
    count = 0
    deleted = 0
    # Remove the lowest score for each team.
    for value in range(len(results)):
        index = count - deleted
        if (count)%4 == 2:
            if results[index] <= results[index+1]:
                del results[index]
                deleted += 1
            else:
                del results[index+1]
                deleted += 1
        count += 1

    # Create nested lists of teams
    list_of_list_teams = []
    list_of_teams = []
    for count in range(len(results)):
        list_of_teams.append(results[count])
        if count%3 == 2:
            list_of_list_teams.append(list_of_teams)
            list_of_teams = []

    # Sort nested lists of teams
    sorted_list_of_list_of_teams = sorted(list_of_list_teams, key=lambda x: x[2], reverse=True)

    return sorted_list_of_list_of_teams







print("Leaderboards of the International FIRST LEGO Robotic Competition")
placement = 1
for detail in lego_competition_sorter(results):
    print(f"Place number {placement} is team no. {detail[0]}, {detail[1]}, with a score of {detail[2]}.")
    placement += 1