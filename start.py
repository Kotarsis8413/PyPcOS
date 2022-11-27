import os

import pypcos
type = 'cmd'
def start(name, version):
    name = pypcos.name
    version = pypcos.version

    print(name + ' ' + 'is loading...')
    print(name + ' version: ' + version)
    import time
    time.sleep(2)
    print(name + ' loaded')
    while True:
        q = input(pypcos.default_user_name + '@' + name + '$~')
        time.sleep(0.3)
        if q == 'power off':
            import sys
            sys.exit()

        if q == 'power reload':
            print(name + ' is reloading...')
            time.sleep(1.5)
            reload()

        if q == 'open url':
            print('which link do you want to open?')
            import webbrowser
            webbrowser.open(input('url$~'), new="2")
        if q == 'clear':
            print('\n' * 100)






        else:
            print('Ошибка...')
            time.sleep(1)
            print('deleting system...')
            time.sleep(0.5)
            print('OS name: ' + name)
            time.sleep(0.5)
            print('OS version: ' + version)
            time.sleep(0.5)
            print('USER name: ' + pypcos.default_user_name)
            time.sleep(0.5)
            pypcos.name = 'DELETED SYSTEM'
            pypcos.version = 'DELETED SYSTEM'
            pypcos.default_user_name = ''
            close()



def reload():
    start('name', 'version')
def close():
    from tkinter import messagebox
    while True:
        messagebox.showerror('ERROR', 'ERROR')

if __name__ == '__main__':
    start('name', 'version')