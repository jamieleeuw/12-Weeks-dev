def input_(choice):
    if choice.isdigit() == True:
        choice = int(choice)
        return choice
    else:
        return False

def user_id(userid):
    if userid.isdigit() == True:
        userid = int(userid)
        return userid
    else:
        return False

    