import os
import subprocess
import time

import cursor_lib as cslib

LOADBAR_NUMBER = 30

def clear():
    command = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(command, shell=True)

def hide_cursor():
    print('\033[? 25l', end="")

def print_ascii_text():

    f = open("ascii_text.txt", 'r')

    file_contents = f.read()

    print (file_contents)

    f.close()

    return

                                  
def draw_loading():
    
    # Draw    [ █ █ █ █ █ █ █ █ █ █ █ ] 100%

   
    for i in range(LOADBAR_NUMBER):
    
        print("\t[",end='')
        for j in range(LOADBAR_NUMBER):

            if i >= j:
                print('█',end='')    
            else:
                print(' ',end='')   
                 
        print("]  ",end='')      

        prc = i/j * 100
        print(f"{round(prc)} %")
                     
        time.sleep(0.5 / (1+prc))    

        if i != LOADBAR_NUMBER-1:
            clear()
            print_ascii_text()

    time.sleep(0.4)                
    return


def main():
    
    clear()
    cslib.hide_cursor()

    print_ascii_text()

    time.sleep(0.2)
    
    draw_loading()   

    time.sleep(0.2)

    time.sleep(0.2)
    clear()
    cslib.show_cursor()
    return

if __name__ == "__main__":
    main()
