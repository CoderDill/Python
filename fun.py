# num = 0

# while num <= 100:
#     print(num)
#     num += 10

# print("ALL DONE")


# target = 37
# guess = None

# while guess != target:
#     guess = input("Please enter a guess..")
#     if guess == "q" or guess == "quit":
#         break
#     guess = int(guess)

# print("alldone")

scores = [45, 99, 100, 49]

if 45 in scores:

    vegan_no_nos = ["eggs", "meat", "fish"]

    pie_ingredients = ["sugar", "eggs"]

    for food in pie_ingredients:
        if food in vegan_no_nos:
            print(f"You cannot eat {food}")
        else:
            print(f"You can eat {food}")
