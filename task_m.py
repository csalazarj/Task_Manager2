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

    print('------------------------')
    processes_list = []
    
def createProcess(name_proc):    
    try:
        sp.Popen([name_proc])
    except:
        print('Application not found')

def getWelcome():
    print('Welcome to TaskManager')
    print('------------------------\n')

def spawnProcess():
    app_name = str(input("Insert application's name to open\n>>"))
    createProcess(app_name)

def killProcess():
    PID = input('Write the PID of process to kill: ')
    kill = sp.check_output(f"kill {PID}",shell=True)
    print(f'Process {PID} deleted succesfully\n')

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

    print('------------------------\n')

    for i in range(0,len(users_list)):
        user2 = users_list[i]
        print(f"- {user2}")
                
    print('------------------------\n')

def processUser():
    users()
    selUser = input('Select the user \n')

    print('------------------------\n')
    showProcess = sp.run(f"ps -U {selUser} -u {selUser} -o pid,ppid,comm,user",shell=True)
    print('------------------------\n')

def countProcesses():
    n = sp.check_output("ps aux | wc -l",shell=True)
    n = n.decode('UTF-8')
    print(f'Number of processes: {n}')

def child_sleep():
    x=sp.Popen("sleep 1000 &",shell=True)
    y=x.pid
    print(f"the PID of the new child process is {y+1} \n")

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
        res = input('To exit press "Q" \n>> ')

        if (res == '1'):
            spawnProcess()

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

        elif (res == 'Q'):
            print('Good Bye!!')
            return False

        else:
            print('command not recognized')

    
main()