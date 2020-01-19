def current_game():
    starting_honor = int(input('What is the starting honor? '))
    game_length = int(input('How long was the game? '))
    ending_honor = int(input('What is the ending honor? '))
    total_honor_gain = ending_honor - starting_honor
    HpH_Calculator = ((60/game_length) * total_honor_gain)
    print('')
    print('Total honor gain is: ', total_honor_gain)
    print('')
    print('Based on game length, the HpH is: ', HpH_Calculator)
    print('')
current_game()
    
