import os
import subprocess as sp

def main():
    flag = True

    while (flag):
        getWelcome()
        getProcess()
        flag = ask()


def getProcess():
    processes_bin = sp.check_output("ps -e -o pid,ppid,comm,user",shell=True)
    processes = processes_bin.decode('UTF-8')
    processes_list = processes.split('\n')

    for proc in processes_list:
        print(proc)

    print('---------------------------------------')

    
def createProcess():
    name_proc = str(input("Insert application's name to open: "))
    try:
        sp.Popen([name_proc])
        print('\n----------------------------------')
        print('Process spawned successfully')
        print('----------------------------------\n')

    except:
        print('\n----------------------------------')
        print('Application not found')
        print('----------------------------------\n')


def getWelcome():
    print('Welcome to TaskManager')
    print('--------------------------------------\n')


def killProcess():
    refreshConsole()
    PID = input('Write the PID of process to kill: ')
    if PID in ["cancel","CANCEL","Cancel"]:
        pass
    else:
        try:
            kill = sp.check_output(f"sudo kill {PID}",shell=True)
            print('\n----------------------------------')
            print(f'Process {PID} deleted succesfully')
            print('----------------------------------\n')
        except:
            print('\n----------------------------------')
            print('Application not found')
            print('----------------------------------\n')


def refreshConsole():
    clear = sp.run("clear",shell=True)
    getProcess()

def users():
    users = sp.check_output("ps -A -o user | sort | uniq",shell=True)
    users1 = users.decode('UTF-8')
    users_list = users1.split('\n')
    users_list.pop()
    
    if "USER" in users_list:
        users_list.remove("USER")

    print('---------------------------------------\n')

    for i in range(0,len(users_list)):
        user2 = users_list[i]
        print(f"- {user2}")
                
    print('---------------------------------------\n')

def processUser():
    users()
    selUser = input('Select the user: ')

    print('------------------------\n')
    showProcess = sp.run(f"ps -U {selUser} -u {selUser} -o pid,ppid,comm,user",shell=True)
    print('------------------------\n')

def countProcesses():
    n = sp.check_output("ps aux | wc -l",shell=True)
    n = n.decode('UTF-8')
    print('------------------------\n')
    print(f'Number of processes: {n}')
    print('------------------------\n')


def child_sleep():
    x=sp.Popen("sleep 1000 &",shell=True)
    y=x.pid
    print('\n----------------------------------------')
    print(f"the PID of the new child process is {y+1}")
    print('----------------------------------------\n')


def createProcessUser():
    users()
    username=str(input("chosee the name of the user\n>>"))
    procname=str(input("choose the name of the process to open\n>>"))
    proc = sp.Popen(f"sudo -u {username} {procname}",shell=True)

    
def ask():
    res = ''

    while res != 'Q':
        print('Press 1 to spawn process')
        print('Press 2 to kill process')
        print('Press 3 to see the number of processes')
        print('Press 4 to update the list of processes')
        print('Press 5 to see the users')
        print('Press 6 to see the processes for each user')
        print('Press 7 to create a child process')
        print('Press 8 to create process with any other user')

        res = input('To exit press "Q" \n>> ')

        if (res == '1'):
            createProcess()

        elif (res == '2'):
            killProcess()

        elif (res == '3'):
            countProcesses()

        elif (res == '4'):
            refreshConsole()

        elif (res == '5'):
            users()

        elif (res == '6'):
            processUser()

        elif (res == '7'):
            child_sleep()

        elif (res == '8'):
            createProcessUser()

        elif (res == 'Q'):
            print('Good Bye!!')
            return False

        else:
            print('command not recognized')

    
main()