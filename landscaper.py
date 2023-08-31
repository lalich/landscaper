#Starting a landscaping business

#Using teeth cut grass once per day for $1 can do as many times

user_input = input('Hello would you like to build a landscaping business, yes or no?')
if user_input.lower() == 'yes':
    print(f"Congratulaions on starting your business, you are starting from the bottom with $0 and can only cut grass with your teeth!")

if user_input.lower() == 'no':
    print('Thank you for the support have a nice life not winning')

landscaper_stats = {
    '$$$': 0,
    'quit': False
    }
while True:
    user_input = input('Hey Landscaper press 1 to cut the grass and earn that $1! or 2 to claim chapter 11')
    if (user_input == '1'):
        landscaper_stats['$$$'] +=1
        print(f"hey homie you now have ${landscaper_stats['$$$']}")
    
    if (user_input == '2'):
        landscaper_stats['quit'] = True

    if (landscaper_stats['quit'] == True):
        print(f"Okay you quit and will have to live off of ${landscaper_stats['$$$']}, have a nice life")
        break
    if landscaper_stats['$$$'] == 11:
        landscaper_stats['$$$'] = 0
        print('Congratulations you can now get a pizza and eat')



