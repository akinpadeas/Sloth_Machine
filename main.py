import random

MAX_LINES = 3
MIN_LINES = 1
MIN_BET = 0
MAX_BET =100

ROWS = 3
COLS = 3


symbol_dict = {"A":2,"B":4,"C":6,"D":8}
value_dict = {"A":5,"B":4,"C":3,"D":2}


def check_winning(columns,lines,bet,values):
    winning = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winning += values[symbol] * bet
            winning_line.append(line + 1)
    return winning,winning_line

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            column.append(value)
            current_symbols.remove(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row],end="")
        print() # print on the next line

def deposit():
    tries = 0
    while True:
        if tries > 0:
            amount = input("Re-enter the amount you want to deposit: $")
        else:
            amount = input("Enter the amount you want to deposit: $")
            tries +=1
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print(f"Your deposit should be greater than ${amount}.")
        else:
            print("Please re-enter your deposit")
    
    return amount

def get_number_lines():
    tries = 0
    while True:
        if tries > 0:
            lines = input("Re-enter number of lines you want to bet on, should be between (1-" + str(MAX_LINES) + ") ")
        else:
            lines = input("How many lines you want to bet on (1-" + str(MAX_LINES) + ")? ")
            tries +=1
        if lines.isdigit():
            lines = int(lines)
            if MIN_LINES <= lines <= MAX_LINES:
                break
            else:
                print("Number of lines should be between (1-" + str(MAX_LINES) + ") ")
        else:
            print("Please re-enter the number of lines:")
            
    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Your bet should be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please re-enter your bet")
    
    return amount
def spin(balance):
    lines = get_number_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet <= balance:
            break
        else:
            print(f"Your balance is ${balance} which is lower that your bet. Please add money to your balance")
    print(f"You are placing ${bet} bet on each line, total bet is ${total_bet}")
    slot = get_slot_machine_spin(ROWS,COLS,symbol_dict)
    print_slot_machine(slot)
    winnings,winning_lines = check_winning(slot,lines,bet,value_dict)
    if winnings > 0:
        print(f" You won ${winnings} on line {winning_lines}")
        #print(f" You won on lines:",  *winning_lines)
    else:
        print(f"You earn nothing") 
    return winnings - total_bet, winnings 

def main():
    balance =  deposit()
    while True:
        #print(f"current balance is ${balance}")
        answer = input("press enter to play (q to quit)")
        if answer == "q":
            break
        bal,earn = spin(balance)
        balance += bal 
        if earn > 0:
            print(f"You earn ${earn} and your total balance is ${balance} ")
        else:
            print(f"You left with ${balance} with no winning")
main()