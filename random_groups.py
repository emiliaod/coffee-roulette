import csv
import random

# Read data from the CSV file
people = []
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if row['Role'] != 'Partner':  # Exclude people with role 'D'
            people.append(row)

# Create dictionaries to keep track of people's roles and teams
roles_count = {}
teams_count = {}

# Separate people by role and team
for person in people:
    role = person['Role']
    team = person['Team']
    if role not in roles_count:
        roles_count[role] = []
    roles_count[role].append(person)
    if team not in teams_count:
        teams_count[team] = []
    teams_count[team].append(person)

# Randomly shuffle the list of people
random.shuffle(people)

# Initialize lists for groups and people not in a group
groups = []
not_in_group = []

# Create groups of three people
while len(people) >= 3:
    group = []
    # Ensure people in the group have different roles and teams
    while len(group) < 3:
        person = people.pop()
        role = person['Role']
        team = person['Team']
        if len(roles_count[role]) > 1 and len(teams_count[team]) > 1:
            group.append(person)
        else:
            not_in_group.append(person)
    groups.append(group)

# Any remaining people go in the "not_in_group" list
not_in_group.extend(people)

# Write the groups to a CSV file with the group name and names of the people in each group
with open('coffee_groups.csv', 'w', newline='') as csv_file:
    fieldnames = ['Group', 'Name1', 'Name2', 'Name3']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    for i, group in enumerate(groups, start=1):
        names = [person['Name'] for person in group]
        csv_writer.writerow({'Group': f'Group {i}', 'Name1': names[0], 'Name2': names[1], 'Name3': names[2]})

# Print the people not in a group
print("\nPeople not in a group:")
for person in not_in_group:
    print(f"Name: {person['Name']}, Role: {person['Role']}, Team: {person['Team']}")
