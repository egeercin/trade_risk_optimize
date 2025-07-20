import random
import numpy as np
import matplotlib.pyplot as plt
BWHITE = "\033[97m"

print(f"{BWHITE}Trade W/L Simulator")
print(f"{BWHITE}Please enter your parameters:")
win_rate = input(f"{BWHITE}Win rate (0-1): ")
p_l_ratio = input(f"{BWHITE}Profit/Loss ratio (win amount : loss amount, e.g., 1:1): ")
steps = input(f"{BWHITE}Timeframe (in steps): ")
risk_percent = input(f"{BWHITE}Risk per trade (as percentage of balance, e.g., 1 for 1%): ")

# Configurable parameters
starting_balance = 1000
win_rate = float(win_rate)
try:
    win_amt, loss_amt = map(float, p_l_ratio.split(":"))
    pl_ratio = win_amt / loss_amt
except Exception:
    print("Invalid P/L ratio format. Please use the format '1:2'.")
    exit(1)
steps = int(steps)
risk_percent = float(risk_percent)

R = 1
plt.figure()
for path in range(R):
    balance = [starting_balance]
    for _ in range(steps):
        if random.random() < win_rate:
            new_balance = balance[-1] + balance[-1] * risk_percent / 100 * pl_ratio
        else:
            new_balance = balance[-1] - balance[-1] * risk_percent / 100
        balance.append(new_balance)
    plt.plot(balance, linewidth=1, label=f'Path {path+1}')
plt.hlines(starting_balance, 0, steps, label='Breakeven', color='orange', linestyle='--')
final_balance = balance[-1]
color = 'green' if final_balance > starting_balance else 'red'
plt.vlines(steps, starting_balance, final_balance, color=color, linewidth=1, label='P/L')
plt.ylabel('Balance')
plt.legend()
plt.gca().set_facecolor('black')
plt.gcf().patch.set_facecolor('black')
plt.gca().spines['bottom'].set_color('gray')
plt.gca().spines['top'].set_color('gray')
plt.gca().spines['right'].set_color('gray')
plt.gca().spines['left'].set_color('gray')
plt.gca().tick_params(axis='x', colors='gray')
plt.gca().tick_params(axis='y', colors='gray')
plt.ylabel('Balance', color='gray')
plt.title(f'Randomized Trading Simulation ({R} Path)', color='gray')
for line in plt.gca().get_lines():
    if line.get_label() == 'Breakeven' or line.get_label() == 'P/L':
        line.set_color('gray')
    else:
        line.set_color('white')
plt.legend(facecolor='black', edgecolor='gray', labelcolor='gray')
plt.show()

# Risk percent optimization graph (unchanged)
risk_range = np.linspace(0.1, 100, 200)
final_balances = []

for rp in risk_range:
    balance = starting_balance
    for _ in range(steps):
        if random.random() < win_rate:
            balance += balance * rp / 100 * pl_ratio
        else:
            balance -= balance * rp / 100
    final_balances.append(balance)

plt.figure()
plt.plot(risk_range, final_balances, color='blue')
plt.xlabel('Risk per Trade (%)')
plt.ylabel('Final Balance')
plt.title('Risk Percent Optimization')
plt.gca().set_facecolor('black')
plt.gcf().patch.set_facecolor('black')
plt.gca().spines['bottom'].set_color('gray')
plt.gca().spines['top'].set_color('gray')
plt.gca().spines['right'].set_color('gray')
plt.gca().spines['left'].set_color('gray')
plt.gca().tick_params(axis='x', colors='gray')
plt.gca().tick_params(axis='y', colors='gray')
plt.grid(True)
plt.show()
