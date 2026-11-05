secret = 27
lives = 5
count = 0
guess = 0

print("="*20)
print("🎮 NUMBER GUESSING GAME")
print("="*20)
print("You've got a secret number to find between 1 and 50.")
print("You've got FIVE LIVES.")
print("After each wrong guess, I'll give you a hint.")
print()
while count < lives and guess != secret:
    guess = int(input("Enter number: "))
    count = count + 1
    if guess == secret:
        print("CONGRATS! You've won.")
    else:
        diff = (guess - secret) - 1
        
        if diff >= 20:
            print("ICE COLD.")
        elif diff >= 10:
            print("COLD.")
        elif diff >= 5:
            print("WARM.")
        else:
            print("HOT.")
            
    remaining = lives - count
    if remaining > 0:
        print("You have ", remaining, "lives left.")
    elif remaining == 0:
        print("Sorry, out of lives. Better luck next time!")
        print("The number is", secret, ".")