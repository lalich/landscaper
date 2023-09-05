#Starting a landscaping business

#Using teeth cut grass once per day for $1 can do as many times

user_input = input("Hello would you like to build a landscaping business, yes or no?")
if user_input.lower() == 'yes':
    print(f"Congratulaions on starting your business, you are starting from the bottom with $0 and can only cut grass with your teeth!")

if user_input.lower() == 'no':
    print('Thank you for the support have a nice life not winning')

landscaper_stats = {
    '$$$': 0,
    'tool': 'teeth',
    'dr': '1',
    'quit': False
    }
### starting with the teeth!
while landscaper_stats['tool'] == 'teeth' and not landscaper_stats['quit']:
    user_input = input(f"Hey Landscaper press 1 to cut the grass and earn that ${landscaper_stats['dr']}! or 2 to claim chapter 11")
    if (user_input == '1'):
        landscaper_stats['$$$'] +=1
        print(f"hey homie you now earned ${landscaper_stats['$$$']} using your {landscaper_stats['tool']}")
    if (user_input == '2'):
        landscaper_stats['quit'] = True
    if (landscaper_stats['quit'] == True):
        print(f"Okay you quit and will have to live off of ${landscaper_stats['$$$']}, have a nice life")
        break
  ## $5 scissor time  
    if (landscaper_stats['$$$'] == 5):
        print("You have enough money for a dental clean up and to buy some rusty scissors for $5, this will allow you to make $5 per day doing lawns. Would you like to upgrade?")
    if (user_input == 'yes'):
        landscaper_stats['tool'] = 'Rusties'
        landscaper_stats['dr'] = 5
        landscaper_stats['$$$'] = landscaper_stats['$$$']-5
while landscaper_stats['tool'] == 'Rusties' and not landscaper_stats['quit']:
    user_input = input(f"Hey Landscaper press 1 to cut the grass with {landscaper_stats['tool']} and earn that ${landscaper_stats['dr']}! or 2 to claim chapter 11")
    if (user_input == '1'):
        landscaper_stats['$$$'] +=5
        print(f"hey homie you now earned a total of ${landscaper_stats['$$$']} using your {landscaper_stats['tool']}")
    if (user_input == '2'):
        landscaper_stats['quit'] = True
    if (landscaper_stats['quit'] == True):
        print(f"Okay you quit and will have to live off of ${landscaper_stats['$$$']}, have a nice life")
        break
    
    if landscaper_stats['$$$'] == 1000:
        landscaper_stats['$$$'] = 0
        print("Congratulations you can now get a professional education in your field of choice")



