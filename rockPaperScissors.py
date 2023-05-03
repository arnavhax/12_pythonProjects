import random

def play():
    user=input('Enter \'r\' for rock \'p\' for paper and \'s\' for scissors\n')
    computer=random.choice(['r', 'p', 's'])
    print(f'Computer\'s choice is {computer}')
    if(user==computer):
        return('Its is Tie\n')
    elif(is_win(user,computer)):
        return('User won!! Congrats!!\n')
    return('Computer won....sad....\n')

def is_win(user,computer):
    if(user=='r' and computer=='s'):
        return True
    if(user=='p' and computer=='r'):
        return True
    if(user=='s' and computer=='p'):
        return True
    return False
print(play())