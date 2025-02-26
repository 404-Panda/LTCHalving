import pandas as pd
from datetime import datetime, timedelta
import time
import sys
from tabulate import tabulate
from colorama import Fore, Style, init

def generate_litecoin_halving_schedule():
    # Constants for Litecoin
    initial_subsidy = 50.0
    halving_interval = 840_000
    satoshis_per_ltc = 100_000_000
    block_time_minutes = 2.5
    start_date = datetime(2011, 10, 7)

    # Data collection
    data = {
        "Block Height": [],
        "Halving": [],
        "Binary (sats)": [],
        "Decimal (sats)": [],
        "Decimal (LTC)": [],
        "Date": []
    }

    # Calculating the schedule
    subsidy = initial_subsidy
    for i in range(34):  # Calculating up to 33 halvings
        block_height = i * halving_interval
        subsidy_sats = int(subsidy * satoshis_per_ltc)
        data["Block Height"].append(block_height)
        data["Halving"].append(i)
        data["Binary (sats)"].append(bin(subsidy_sats)[2:])
        data["Decimal (sats)"].append(subsidy_sats)
        data["Decimal (LTC)"].append(f"{subsidy:.8f}")
        data["Date"].append((start_date + timedelta(minutes=block_time_minutes * block_height)).strftime("%Y-%m-%d"))
        subsidy /= 2

    # Create DataFrame
    df = pd.DataFrame(data)
    return df

def typewriter_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != '\n':
            time.sleep(0.01)  # Reduced delay between characters
        else:
            time.sleep(0.1)  # Reduced delay between lines

if __name__ == "__main__":
    init()  # Initialize colorama to strip ANSI codes on Windows or use them on Unix
    ltc_schedule = generate_litecoin_halving_schedule()
    table_string = tabulate(ltc_schedule, headers="keys", tablefmt="fancy_grid")
    
    # Printing table with typewriter effect
    print(Fore.GREEN + Style.BRIGHT, end="")
    typewriter_effect(table_string)

    # ASCII Art
    ascii_art = '''
                #****************                
            *************************            
         #******************************         
       **********************************#       
     ******************:     :*************#     
    ******************=     .-***************    
   *******************..    .*****************   
  *******************-    . +******************  
 ********************   . .:******************** 
#*******************:  .. .+*********************
*******************=.     =**********************
*******************:.    .++=+*******************
******************+         .+*******************
***************+=..   . .+***********************
**************. .. .   .+************************
****************+.     :*************************
#***************:.   ..+*************************
 **************=.  . .-************************* 
  *************:         .      .   :**********  
   ***********+    .  .     . . .  .+*********   
    **********.....................:*********    
     ***************************************     
       #**********************************       
         *******************************         
            *************************            
                #***************#                
    '''
    time.sleep(1)  # Short pause before ASCII art
    typewriter_effect(Fore.YELLOW + ascii_art + Style.RESET_ALL)
