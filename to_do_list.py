from prettytable import PrettyTable

t = PrettyTable(['Key', 'Description'],align = "l")

t.add_rows(
    [
        ["V","View Tasks" ],
        ["C", "Create a Task"],
        ["U", "Update a Task"],
        ["D", "Delete a Task"],
        ["E", "Exit"]
    ]
)

print(t)

task_list= []


def main():
    while True:

        s = input("What do you want to do? ").strip()
        s = s.upper()
        t_view = PrettyTable(['ID', 'Task'],align = "l")
        e_list= enumerate(task_list,start = 1)
        t_view.add_rows(list(e_list))
        
        if s == 'E':
            print('Thank you,bye')
            break
    
        if s == 'C':
            task = input('Write a Task: ')
            task_list.append(task)
        
        if s == 'U':

            print(t_view)
            task_update = input('Which one do you want update? ').strip()
            
            task_up_index = int(task_update)
            task_list[task_up_index-1] = input('What do you want to update it to?:')

        if s == 'D':
            print(t_view)

            task_delete = input('Which one do you want delete? ').strip()
            task_del_index = int(task_delete)
            task_list.remove(task_list[task_del_index-1])

        if s == 'V':
            print(t_view)


if __name__ =='__main__':
    main()