#Emmanuel Colas - COP 2500
#Courselist2 - A better was to add/ drop classes than the original


#This is the add_class function that when activated will add the
#classes added in the add_course input to the schedule list. 
def add_class(draftx):
    add_course = input()
    add_course = add_course.title()
    add_course = add_course.split(",")
    draftx = draftx + add_course
    for i in range(len(draftx)):
        draftx[i] = draftx[i].strip()
    for a, b in enumerate(draftx, 1):
        print( '{} {}'.format(a, b))
    return draftx

#The remove_class function with ask the user for what classes to remove and
#take them out of the orginal schedule list. 
def remove_class(draftd):
    drop_course = input()
    drop_course = drop_course.title()
    drop_course = drop_course.split(",")

    for i in drop_course:
        if i in draftd:
            index = draftd.index(i)
            draftd.pop(index)
        else:
            print("Course not in list")
        
    for a, b in enumerate(draftd, 1):
            print( '{} {}'.format(a, b))
    
    return draftd
    
    
    
#Down here is where the user will add the initial schedlue. Down here
#it will adjust the number of classes in the schedule with the while loop.

schedule = input("What classes do you want to take?",)
schedule = schedule.title()
schedule = schedule.split(",")
for i in range(len(schedule)):
    schedule[i] = schedule[i].strip()
print("This is your schedule so far")
for a, b in enumerate(schedule, 1):
    print( '{} {}'.format(a, b))

while len(schedule) != 5:
    
    if len(schedule) < 5:
        print("What classes do you want to take?")
        schedule = add_class(schedule)
        
    if len(schedule) > 5:
        print("What classes do you want to drop?")
        schedule = remove_class(schedule)
        
        
if len(schedule) == 5:
    print("Done!")
