#1
import random
number = random.randint(1, 10)
for attempt in range(3):
    guess = int(input("Guess the number (1-10): "))
    if guess == number:
        print("You win!")
        break
    else:
        print("Wrong!")
else:
    print("You lose! Number was:", number)
#2
import time
minutes = int(input("Enter minutes: "))
seconds = minutes * 60
while seconds > 0:
    print(seconds, "seconds left")
    time.sleep(1)
    seconds -= 1
print("Time is up!")
#3
import time
input("Press Enter to start")
start = time.time()
laps = []
for i in range(3):
    input(f"Press Enter for lap {i+1}")
    lap = time.time() - start
    laps.append(lap)
print("Lap times:")
for lap in laps:
    print(round(lap, 2), "seconds")
#4
import random
symbols = "abcdefghijklmnopqrstuvwxyz0123456789"
password = ""
for i in range(8):
    password += random.choice(symbols)
print(password)
#5
import random
choice = input("Choose heads or tails: ")
coin = random.choice(["heads", "tails"])
print("Coin:", coin)
if choice == coin:
    print("You win!")
else:
    print("You lose!")
#6
import time
start = time.time()
for i in range(1000000):
    pass
end = time.time()
print(end - start)
#7
import random
import time
print("Wait for GO...")
time.sleep(random.randint(2, 5))
print("GO!")
start = time.time()
input()
end = time.time()
print("Your reaction time:", round(end - start, 3), "seconds")
