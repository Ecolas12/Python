#Emmanuel Colas - COP 2500
#Courselist2 - A better was to add/ drop classes than the original



def add_class(draftx):
    add_course = input()
    add_course = add_course.title()
    add_course = add_course.split(",")
    draftx = draftx + add_course
    for a, b in enumerate(draftx, 1):
        print( '{} {}'.format(a, b))
    return draftx



def remove_class(draftd):
    drop_course = input()
    drop_course = drop_course.title()
    drop_course = drop_course.split(",")

    for i in drop_course:
        index = draftd.index(i)
        draftd.pop(index)
        
    for a, b in enumerate(draftd, 1):
            print( '{} {}'.format(a, b))
    
    #else:
     #   print("Invalid Entry")
      #  for a, b in enumerate(draftd, 1):
       #     print( '{} {}'.format(a, b))

        
    return draftd
    
    
    


schedule = input("What classes do you want to take?",)
schedule = schedule.title()
schedule = schedule.split(",")
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

