import message

def act():
  message.help_message('new', '<DB>', 'Create new a DB')
  message.help_message('delete', '<DB>', 'Delete a DB')

def handle(command):
    if len(command) != 0:
        message.error_message(command[0], "cmw")
        return False

    act()