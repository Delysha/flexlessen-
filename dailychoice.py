rungame = 0 
print ("you wake up and think by ur self will u SHOWER or NOT")
choice = input ()
if choice == 'SHOWER':
    print ("you stand up and go take a shower after the shower u go to ur room will u wear a DRESS or a JUMPSUIT")
elif choice == "not":
    print ("u didnt shower and to school all smelly and got bullied by ur friendgroup")
else :
    print (choice, "wasn't a valid choice")

choice = input ()
if choice == 'DRESS' :
    print (" you wear a dress and it accendently riped while biking")
elif choice == 'JUMPSUIT':
    print ("u put a jumpsuit on and went down stairs do u MAKE food for school or will u SIT on the sofa and dont bring food with u?")
else :
    print (choice, "wasn't a valid choice" )

choice = input ()
if choice == 'MAKE' :
    print (" u made food for school and got ur bag now will u BIKE to school or take the BUS ?")
elif choice == 'SIT' :
    print ("u didnt make food and ur mom got mad at u and said u had to eat something otherwise u can't come with her to the amuse park after school so u made foof but got sick and died.")
else :
    print (choice, "wasn't a valid choice")

choice = input ()
if choice == 'BIKE' :
    print ("u went on the bike and start to ride to school but u felt and went to the hospital cause u broke ur legg AKA GAME OVER")
elif choice == 'BUS' :
    print ("u went to school with the bus and saw ur friends but ur almost late in class so will u say HI or WALK to class")
else : 
    print (choice, "wasn't a valid choice")

choice = input ()
if choice == 'WALK' :
    print ("u walked past them and in class they got mad at u so they didnt talk u all day and u were alone the howl time and went home while u would actually meet up with them.")
elif choice == 'HI' : 
    print ('u said hi to ur friends and had a great time with ur friends. u went home happy and had a great day. now do u wanna RESTART or NO ? ')

restart = input ()
if restart == 'RESTART' :
         rungame = 0
else :
    if restart =='NOT' :
        print()
    exit ()