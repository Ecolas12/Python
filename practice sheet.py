#Emmanuel Colas - COP2500
#courselist2.py - Add up to 5 courses in a schedule

  



def building_schedule():
    draft_display = str(input("what class to add?", ))
    draft_display = draft_display.title()
    draft_display = draft_display.split(",")
    print("This is your schedule")
    for count, draft_display in enumerate(draft_display, start=1):
        print(count,draft_display.strip())
    return draft_display
       
def adding_classes(new_list):
    schedule_addition = str(input("Must have 5 class, enter courses to add:", ))
    schedule_edit_add = new_list +" ," + schedule_addition
    schedule_edit_add = schedule_edit_add.title()
    schedule_edit_add_display = schedule_edit_add.split(",")
    print("This is your schedule")
    for count, schedule_edit_add_display in enumerate(schedule_edit_add_display, start=1):
        print(count,schedule_edit_add_display.strip())
    return schedule_edit_add


def dropping_classes(new_list):
    remove=input("Remove:",)
    new_list.replace(remove, " ")

    
    print("This is your schedule")
    for count, new_list in enumerate(new_list, start=1):
        print(count,new_list.strip())
    return new_list





    
def main():
    the_list = building_schedule()
    new_list = the_list
    add_to_schedule = adding_classes(new_list)
    drop_from_schedule = dropping_classes(new_list)
    
    
main()

