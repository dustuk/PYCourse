project_number = input("Enter a project number: ")

if project_number == "1":
    while True:
        word = input("")

        if word == "done":
            print("Done!")
            break

        if len(word) == 0 or word.startswith("#"):
            continue

        print(word)


if project_number == "2":
    import random
    random_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess the number: "))
        attempts += 1

        if guess < random_number:
            print("Too low, try again")
        elif guess > random_number:
            print("Too high, try again")
        else:
            print(f"You guessed the number in {attempts} attempts")
            break


if project_number == "3":
    numbers = [953, 776, 532, 665, 973, 683, 484, 499, 741, 980]
    multiple = 7

    while True:
        multiple += 7

        if multiple in numbers:
            break

    print(multiple)


if project_number == "4":
    scores = []

    while True:
        score = input("Enter a score (or type 'done' to exit): ")

        if score == "done" or len(score) == 0:
            break

        score = float(score)
        scores.append(score)
    
    average_score = sum(scores) / len(scores)
    print(f"The average of the scores is: {average_score:.2f}")