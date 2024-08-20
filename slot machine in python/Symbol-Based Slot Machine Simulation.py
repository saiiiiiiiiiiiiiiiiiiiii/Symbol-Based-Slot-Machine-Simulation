# Randomized Slot Machine Simulation
# Dynamic Slot Machine Simulator
# Configurable Slot Machine Engine
# Python Slot Machine RNG System
# Real-Time Slot Machine Game
# Symbol-Based Slot Machine Simulation

# Technical Description:
# Developed a Python-driven slot machine simulation with a 3x3 grid structure. The game dynamically generates random symbol combinations based on predefined symbol frequencies. It allows users to configure bets across multiple paylines, calculates winnings based on symbol alignment, and updates the player's balance in real-time. The system utilizes key Python concepts like list manipulation, loops, and conditional logic to simulate an authentic slot machine experience.



import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol_to_check != symbol:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols.copy()
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("Enter the amount to deposit Rs: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Invalid amount. Please enter a positive number.")
        else:
            print("Invalid amount. Please enter a valid amount.")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Invalid input. Please enter a valid number.")
    return lines

def get_bet_on_each_line():
    while True:
        bet = input(f"Enter the amount to bet on each line (Rs {MIN_BET}-{MAX_BET}): ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} and {MAX_BET}.")
        else:
            print("Invalid amount. Please enter a valid amount.")
    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet_on_each_line()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is Rs {balance}.")
        else:
            break

    print(f"You are betting Rs {bet} on {lines} lines. Total bet is equal to: Rs {total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, values)
    print(f"You won Rs {winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is Rs {balance}")
        answer = input("Press Enter to play (q to quit): ")
        if answer == 'q':
            break
        balance += spin(balance)
        if balance <= 0:
            print("You've run out of money! Game over.")
            break

    print(f"You left with Rs {balance}.")

main()
