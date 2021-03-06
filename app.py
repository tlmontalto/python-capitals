state_capitals = [
  {
    "name": "Alabama",
    "capital": "Montgomery"
  },
  {
    "name": "Alaska",
    "capital": "Juneau"
  },
  {
    "name": "Arizona",
    "capital": "Phoenix"
  },
  {
    "name": "Arkansas",
    "capital": "Little Rock"
  },
  {
    "name": "California",
    "capital": "Sacramento"
  },
  {
    "name": "Colorado",
    "capital": "Denver"
  },
  {
    "name": "Connecticut",
    "capital": "Hartford"
  },
  {
    "name": "Delaware",
    "capital": "Dover"
  },
  {
    "name": "Florida",
    "capital": "Tallahassee"
  },
  {
    "name": "Georgia",
    "capital": "Atlanta"
  },
  {
    "name": "Hawaii",
    "capital": "Honolulu"
  },
  {
    "name": "Idaho",
    "capital": "Boise"
  },
  {
    "name": "Illinois",
    "capital": "Springfield"
  },
  {
    "name": "Indiana",
    "capital": "Indianapolis"
  },
  {
    "name": "Iowa",
    "capital": "Des Moines"
  },
  {
    "name": "Kansas",
    "capital": "Topeka"
  },
  {
    "name": "Kentucky",
    "capital": "Frankfort"
  },
  {
    "name": "Louisiana",
    "capital": "Baton Rouge"
  },
  {
    "name": "Maine",
    "capital": "Augusta"
  },
  {
    "name": "Maryland",
    "capital": "Annapolis"
  },
  {
    "name": "Massachusetts",
    "capital": "Boston"
  },
  {
    "name": "Michigan",
    "capital": "Lansing"
  },
  {
    "name": "Minnesota",
    "capital": "St. Paul"
  },
  {
    "name": "Mississippi",
    "capital": "Jackson"
  },
  {
    "name": "Missouri",
    "capital": "Jefferson City"
  },
  {
    "name": "Montana",
    "capital": "Helena"
  },
  {
    "name": "Nebraska",
    "capital": "Lincoln"
  },
  {
    "name": "Nevada",
    "capital": "Carson City"
  },
  {
    "name": "New Hampshire",
    "capital": "Concord"
  },
  {
    "name": "New Jersey",
    "capital": "Trenton"
  },
  {
    "name": "New Mexico",
    "capital": "Santa Fe"
  },
  {
    "name": "New York",
    "capital": "Albany"
  },
  {
    "name": "North Carolina",
    "capital": "Raleigh"
  },
  {
    "name": "North Dakota",
    "capital": "Bismarck"
  },
  {
    "name": "Ohio",
    "capital": "Columbus"
  },
  {
    "name": "Oklahoma",
    "capital": "Oklahoma City"
  },
  {
    "name": "Oregon",
    "capital": "Salem"
  },
  {
    "name": "Pennsylvania",
    "capital": "Harrisburg"
  },
  {
    "name": "Rhode Island",
    "capital": "Providence"
  },
  {
    "name": "South Carolina",
    "capital": "Columbia"
  },
  {
    "name": "South Dakota",
    "capital": "Pierre"
  },
  {
    "name": "Tennessee",
    "capital": "Nashville"
  },
  {
    "name": "Texas",
    "capital": "Austin"
  },
  {
    "name": "Utah",
    "capital": "Salt Lake City"
  },
  {
    "name": "Vermont",
    "capital": "Montpelier"
  },
  {
    "name": "Virginia",
    "capital": "Richmond"
  },
  {
    "name": "Washington",
    "capital": "Olympia"
  },
  {
    "name": "West Virginia",
    "capital": "Charleston"
  },
  {
    "name": "Wisconsin",
    "capital": "Madison"
  },
  {
    "name": "Wyoming",
    "capital": "Cheyenne"
  }
]

import random

correct = 0
incorrect = 0
total = 0

print('Welcome to the State Capitals game!')

while total < 51:

    if total == 50:
        print(f'You have gone through all the states, the game is now over. Your final score was {correct} correct, and {incorrect} incorrect!')

        correct = 0
        incorrect = 0
        total = 0

    start = input('Do you want to start the game? [yes/no] ').lower()

    if start == 'yes':
        random.shuffle(state_capitals)
        
        for state in state_capitals:
            question = input(f'What is the state capital of {state["name"]}? ').title()
            print(f'You answered {question}')

            if question == state["capital"]:
                correct += 1
                total += 1
                print(f'Correct! You have gotten {correct} correct and {incorrect} incorrect so far.')

            elif question != state["capital"]:
                incorrect += 1
                total += 1
                print(f'Sorry, that is incorrect. You have gotten {correct} correct and {incorrect} incorrect so far.')

    else:
        print('Maybe another time.')