from schema import Bookmark

def add_bookmark():
    bookmark_name = str(input('Insert name of bookmark: '))
    bookmark_link = str(input('Paste link of bookmark: '))
    Bookmark(name = bookmark_name, link = bookmark_link).save()

    if bookmark_name and bookmark_link:
        print('Successfully added bookmark')
        answer = str(input('Would you like to add another bookmark? (y/n): '))
        if answer.lower() == 'yes' or answer.lower() == 'y':
            add_bookmark()
        elif answer.lower() == 'no' or answer.lower() == 'n':
            exit()
        else:
            print('invalid input.')

add_bookmark()