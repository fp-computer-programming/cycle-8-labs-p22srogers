# Author: SMR (AMDG) 12/1/21
def party_invites(lst):
    for name in lst:
        print("Hi {0}, You're invited to my birthday party on Friday!".format(name))
    
    print(party_invites(["Sean", 'Jack', 'Will']))
    