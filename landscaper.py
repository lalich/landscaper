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
    if (landscaper_stats['$$$'] >= 5):
        print("You have enough money for a dental clean up and to buy some rusty scissors for $5, this will allow you to make $5 per day doing lawns. Would you like to upgrade?")
    if (user_input.lower() == 'yes'):
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

## ol timey-push mower
    if (landscaper_stats['$$$'] >= 25):
        print("Yo, landScraper you now have enough money to buy a nice Timey-Push mower for $25! This will allow you to earn $50 a day doing the lawn. Would you like to upgrade?")
        if (user_input.lower() == 'yes'):
            landscaper_stats['tool'] = 'Timey'
            landscaper_stats['$$$'] = landscaper_stats['$$$']-25
            landscaper_stats['dr'] = 50
while landscaper_stats['tool'] == 'Timey' and not landscaper_stats['quit']:
    user_input = input(f"Hey Landscaper press 1 to cut the grass with {landscaper_stats['tool']} and earn that ${landscaper_stats['dr']}! or 2 to claim chaper 11")
    if (user_input == '1'):
        landscaper_stats['$$$'] +=50
        print(f"Hey Homie, you now earned a total of ${landscaper_stats['$$$']} and are using the {landscaper_stats['tool']} to make a living")
    if (user_input == '2'):
        landscaper_stats['quit'] = True
    if (landscaper_stats['quit'] == True):
        print(f"Okay you quit and will have to live off of ${landscaper_stats['$$$']}, have a nice life")
        break

## Fancy push mower time
    if (landscaper_stats['$$$'] >= 250):
        user_input = input("Yo Timey pusher you now can upgrade to a Fancy A$$ E-Push mower, it'll cost you $250 and allow you to make $100 per day. Do you want to upgrade?")
        if (user_input.lower() == 'yes'):
            landscaper_stats['tool'] = 'EPM'
            landscaper_stats['dr'] = 100
            landscaper_stats['$$$'] = landscaper_stats['$$$']-250
while landscaper_stats['tool'] == 'EPM' and not landscaper_stats['quit']:
    user_input = input(f"Hey Landscapie press 1 to cut the grass with {landscaper_stats['tool']} and earn ${landscaper_stats['dr']}, or press 2 to file your chapter 7")
    if (user_input == '1'):
        landscaper_stats['$$$'] +=100
        print(f"Hey Homie, nice day at the office using dat {landscaper_stats['tool']}, you've now earned a current balance of ${landscaper_stats['$$$']}")
    if (user_input == '2'):
        landscaper_stats['quit'] = True
    if (landscaper_stats['quit'] == True):
        print(f"Okie Dokie duoiippy, you quit and have ${landscaper_stats['$$$']} to make yo life work.. may I reccomend the YoLo APp!")
        break

## hire dat team
    if (landscaper_stats['$$$'] >= 500):
        user_input = input("Hey EPM level scraper, you can now hire a team to work for you!!! If you invest $500, you will be able to earn $250 a day in your business! Would you like to scale?")
        if (user_input.lower() == 'yes'):
            landscaper_stats['tool'] = 'Dat Team'
            landscaper_stats['dr'] = 250
            landscaper_stats['$$$'] = landscaper_stats['$$$'] - 500
while landscaper_stats['tool'] == 'Dat Team' and not landscaper_stats['quit']:
    user_input = input(f"Hey Mogule, press 1 to send {landscaper_stats['tool']} out to earn ${landscaper_stats['dr']} for you, press 2 to deploy the exit parachute")
    if (user_input == '1'):
        landscaper_stats['$$$'] +=250
        print(f"Whoa, Mogul, using {landscaper_stats['tool']} you now have ca$h money of ${landscaper_stats['$$$']}, you are well on your way to a stack at the casino of life!")
    if (user_input == '2'):
        landscaper_stats[quit] = True
    if (landscaper_stats['quit'] == True):
        print("You almost made it to the promise land, better luck next time!")
        break


## Game winning $hot
    if landscaper_stats['$$$'] == 1000:
        print("Congratulations you can now get a professional education in your field of choice")
        break



