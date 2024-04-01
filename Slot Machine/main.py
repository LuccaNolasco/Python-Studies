import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = { #Dictionary
  "A": 2,
  "B": 4,
  "C": 6,
  "D":8
}

symbol_values = { #Dictionary
  "A": 5,
  "B": 4,
  "C": 3,
  "D":2
}

def check_winnings(columns, lines, bet, values):
  for line in range(lines):
    

def get_slot_machine_spin(rows, cols, symbols):
  all_symbols = []
  #symbol_count representa os numeros, e nao o dicionario. Apenas coincidiu o nome.
  #Exemplo: symbol= A, symbol_count= 2, symbols= O dicionario. O segundo for sera iterado 2 vezes
  #e dois "A"s serao adicionados a lista
  for symbol, symbol_count in symbols.items(): 
    for _ in range(symbol_count):
      all_symbols.append(symbol)
  
  columns = []
  for _ in range(cols):
    column = []
    current_symbols = all_symbols[:]
    for _ in range (rows):
      value = random.choice(current_symbols)
      current_symbols.remove(value)
      column.append(value)

    columns.append(column)

  return columns


def print_slot_machine(columns):
  for row in range(len(columns[0])):
    for i, column in enumerate(columns):
      if i != len(columns)-1:
        print(column[row],end= " | " )
      else:
        print(column[row], end="\n")


#Defines the user deposit of money
def deposit():
  while True:
    amount = input("How much you want to deposit? $")
    if amount.isdigit():
      amount=int(amount)
      if amount > 0:
        break
      else:
        print("You must deposit more than 0$")
    else:
      print("You must type a number")
  
  return amount

#Defines in how many lines the user wants to bet
def get_number_of_lines():
  while True:
    lines = input("In how many lines you want to bet? (1 -"+str(MAX_LINES)+") ")
    if lines.isdigit():
      lines=int(lines)
      if 1<= lines <= MAX_LINES:
        break
      else:
        print("Enter a valide number of lines")
    else:
      print("You must type a number")
  
  return lines 

#Defines how much the user wants to bet
def get_bet():
  while True:
    amount = input("How much you want to bet on each line ? $")
    if amount.isdigit():
      amount=int(amount)
      if MIN_BET<= amount <= MAX_BET:
        break
      else:
        print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
    else:
      print("You must type a number")
  
  return amount

def main():
  balance = deposit()
  lines = get_number_of_lines()

  while True:
    bet = get_bet()
    total_bet = bet * lines
    if total_bet> balance:
      print(f"You do not have enough to bet. Your balance is ${balance} ")
    else:
      break

  print(f"You are betting ${bet} on {lines}.\nTotal bet = ${total_bet}")

  slots=get_slot_machine_spin(ROWS, COLS,symbol_count)
  print_slot_machine(slots)



main()
      
