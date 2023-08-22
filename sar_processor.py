import subprocess
import time
ascii_code = '''
 -----------------------------------------@utsr_---------------------------------------
/  _|      _|  _|      _|  _|      _|  _|_|_|_|_|   _|_|_|_|_|  _|_|_|_|_|  _|_|_|     /
/  _|      _|  _|_|  _|_|  _|      _|      _|       _|          _|      _|  _|    _|   /
/  _|      _|  _|  _|  _|  _|      _|      _|       _|_|_|_|_|  _|_|_|_|_|  _|_|_|_|   /
/  _|      _|  _|      _|  _|      _|      _|               _|  _|      _|  _|  _|     /
/  _|_|_|_|_|  _|      _|  _|_|_|_|_|      _|       _|_|_|_|_|  _|      _|  _|    _|   /
/                                                       _|                             /
 -----------------------------------CREATED BY UMUT SAR-------------------------------

              *************************sar_scanner*************************
'''
def show_ascii_art(art):
    for line in art.splitlines():
        print(line)
        time.sleep(0.05)

show_ascii_art(ascii_code)

print("THIS PROGRAM INCLUDES 4 DIFFERENT WAYS.")
ways = '''
Way 1: Close one cpu core that you choosed.
Way 2: Close cpu cores that you choosed. (choosing a range)
Way 3: Open one cpu core that you choosed.
Way 4: Open cpu cores that you choosed. (choosing a range)
'''
print(ways)

def count_opened():
    for cpu_range in cpu_ranges:
        if '-' in cpu_range:
            start, end = map(int, cpu_range.split('-'))
            for i in range(start, end + 1):
                print(f"Open processor {i}")
        else:
            print(f"Open processor {int(cpu_range)}")
def count_operation():
    existing_cores = "cat /sys/devices/system/cpu/online"
    output_two = subprocess.check_output(existing_cores, shell=True)
    cpu_count_two = output_two.strip().decode()
    print("Total number of cpu cores:",cpu_count_two)
    cpu_ranges = cpu_count_two.split(',')
    count_opened()
count_operation()

print('\n######################################')

count_operation()
print('######################################')
way = input("Which way do you want to choose: ")

def way1():
    closing = input("Enter number of core for opening: ")
    subprocess.run(f'echo 0 | sudo tee /sys/devices/system/cpu/cpu{closing}/online', shell=True)
    count_operation()
    
def way2(w):
    subprocess.run(f'echo 0 | sudo tee /sys/devices/system/cpu/cpu{w}/online', shell=True)
def way3():
    opening = input("Enter number of core for opening: ")
    subprocess.run(f'echo 1 | sudo tee /sys/devices/system/cpu/cpu{opening}/online', shell=True)
    count_operation()
def way4(z):
    subprocess.run(f'echo 1 | sudo tee /sys/devices/system/cpu/cpu{z}/online', shell=True)
while True:
    if(way == '1'):
        print("way3")
        way1()
        way = input("Which way do you want to choose: ")
    elif(way == '2'):
        print("way2")
        print("Enter first and last number.")
        first_number = int(input("Enter first number: "))
        last_number = int(input("Enter last number: "))
        for i in range(first_number, last_number + 1, 1):
            way2(i)
        count_operation()
        way = input("Which way do you want to choose: ")
    elif(way == '3'):
        print("way3")
        way3()
        way = input("Which way do you want to choose: ")
    elif(way == '4'):
        print("way4")
        print("Enter first and last number.")
        first_number_2 = int(input("Enter first number: "))
        last_number_2 = int(input("Enter last number: "))
        for i in range(first_number_2, last_number_2 + 1, 1):
            way4(i)
        count_operation()
    elif(way == 'exit'):
        break
    else:
        print("way not found")
        count_operation()
        way = input("Which way do you want to choose: ")
