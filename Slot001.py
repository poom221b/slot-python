import random

MAX_LINES = 3 #จำนวนสูงสุดที่จะเลือกแถวที่จะเล่น
MAX_BET = 100
MIN_BET = 1
#ทำให้เป็นตาราง 3x3 แบบสล๊อต
ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
#line = แถวแนวนอน  column = แถวแนวตั้ง
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

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
           current_symbols.remove(value)
           column.append(value)

       columns.append(column)

   return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns): #enumerate จะหาค่า index ให้ คือดึงมาทั้ง i ทั้ง column
            if i != len(columns) - 1 :
                print(column[row], end="|")
            else:
                print(column[row], end="")

        print()

def deposit():
    while True: #ใช้ลูปเพื่อให้ผู้ใช้ใส่ข้อมูลจนกว่าจะได้ข้อมูลที่ถูกต้อง
        amount = input("What would you like to deposit? $")
        if amount.isdigit(): #ถ้าใส่เป็นจำนวนเต็ม
            amount = int(amount)
            if amount > 0:
                break #เบรคเพื่อไปต่อที่ขั้นต่อไป
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" +str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

def get_bet(): #รับค่าคำสั่งลงตัง + เลือกของผู้ใช้
    while True:
        amount = input("What would you like to bet on each lines? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is {balance} $ ")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to : ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winnings_lines)
    return winnings - total_bet

def main(): #ฟังชั่นที่รวมฟังชั่นทุกอย่า่งไว้เพื่อเรียกใช้งาน ฟังชั่นหลัก
    balance = deposit() # อัพเดทตังที่มีให้เท่ากับตังที่ฝากเข้ามา
    while True:
        print((f"Current balance is ${balance}"))
        anwser = input(f"Press enter to spin (q to quit)")
        if anwser == "q":
            break
        balance += spin(balance) #อัพเดทยอดคงเหลือตามผลของแต่ละเกมที่เล่นไป

    print((f"You left with ${balance}"))
main()