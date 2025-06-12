car = "Subaru"

if car.lower() == "subaru":
    print(f"Your car is a {car}.")

# Shorthand
print(
    f"Shorthand result: Your car is indeed still a {car}"
    if car.lower() == "subaru"
    else f"Your car isn't a {car}"
)

print("Is car = 'Subaru'? I predict True")
print(car.lower() == "subaru")

# More conditional tests
# Numerical test
pass_mark = 80

qualification = (
    "Passed! You are heading to Pizzaria!!"
    if int(input("\nEnter your score: ")) >= pass_mark
    else "Failed. You'll not be going to Pizzaria."
)
print(qualification)

if "Passed" in qualification:
    # Test multiple conditions
    """
    requested_toppings = [
    "mushroom",
    "extra cheese",
    "pepparoni",
    "olives",
    "pineapple"
    ]
    """

    print("\nWelcome to Pizzaria! \nFor you to make an order,")
    number_of_toppings = int(
        input("...please state the number of toppings you would like: ")
    )
    # Get actual topping names
    # "j+1 caters for the off by one error introduces by using range()"
    requested_toppings = [
        input(f"Enter topping {j + 1}: ").lower().strip()
        for j in range(number_of_toppings)
    ]
    available_toppings = ["pepperoni", "mushroom", "green pepper"]
    proceed = []
    i = 0

    """
    First Approach:
        - This demonstrates exactly why experienced programmers
        generally avoid forcing complex logic into ternary operators.
        The code is nearly unreadable and extremely difficult to debug or
        modify.
    """
    # Without input validation
    print("\n=== Example 1: Messy Ternary Logic ===")
    print("  • Fails to validate inputs beyond exact 'yes' or 'no';")
    print("    typing 'y' instead of 'yes' defaults to cancelling your order")
    print("  • Code is hard to read, debug, or extend\n")
    while i < len(requested_toppings):
        # This is the key: we make i equal to whatever the ternary expression
        # evaluates to
        i = (
            i + 1
            if requested_toppings[i] in available_toppings
            and print(
                f"{requested_toppings[i].title()} is available, " "adding topping..."
            )
            is None
            else (
                len(requested_toppings)
                if proceed.append(
                    input(
                        f"{requested_toppings[i].title()} is currently "
                        "unavailable, do you wish to proceed? [yes/no]: "
                    )
                )
                is None
                and proceed[-1].lower() != "yes"
                and print("\nCancelling your order...We are sorry.") is None
                else (
                    i + 1
                    if print("Proceeding with your order anyways...\n") is None
                    else i + 1
                )
            )
        )

    """
    Better Approach:
        - Traditional if-else statements provide much better clarity and
        maintainability.
        - Perfectly illustrates why readable code is so valuable - it's much
        easier to spot and fix these kinds of logical errors when the code is
        clear and well-structured.
    """
    # Without input validation
    print("\n=== Example 2: Structured but Unvalidated ===")
    print("  • Output unchanged, and still no input checks just as in example 1")
    print("  • But uses clearer if/else blocks\n")
    for i, topping in enumerate(requested_toppings):
        message = (
            f"{topping.title()} is available, adding topping..."
            if topping in available_toppings
            else f"{topping.title()} is unavailable."
        )
        print(message)

        if topping not in available_toppings:
            response = input("\tProceed? [yes/no]: ")
            action = (
                "Proceeding with your order anyways...\n"
                if response.lower() == "yes"
                else "\nCancelling your order...We are sorry."
            )
            print(action)
            should_continue = True if response.lower() == "yes" else False

            if not should_continue:
                break

    print("\n=== Example 3: Graceful Error Handling ===")
    print("  • Same behaviour, but now reprompts on bad answers")
    print("  • Uses a loop to validate yes/no responses\n")
    # With input validation
    for i, topping in enumerate(requested_toppings):
        message = (
            f"{topping.title()} is available, adding topping..."
            if topping in available_toppings
            else f"{topping.title()} is unavailable."
        )
        print(message)

        if topping not in available_toppings:
            while True:
                response = input("\tProceed? [yes/no]: ").lower().strip()
                if response in ["yes", "y", "yeah", "yep"]:
                    print("Proceeding with your order anyways...\n")
                    should_continue = True
                    break
                elif response in ["no", "n", "nope"]:
                    print("\nCancelling your order...We are sorry.")
                    should_continue = False
                    break
                else:
                    print("\n\tPlease enter yes or no.")

            # Now we can use the flag to decide what to do
            if not should_continue:
                break  # Break outer loop only if user said no

    print("\n=== Example 4: Clean & Reusable ===")
    print("  • Same results as example 3 but code is maintainable and robust")
    print("  • Extracts validation into get_yes_no_input()\n")

    # With input validation (cleaner implementation)
    def get_yes_no_input(prompt):
        while True:
            response = input(prompt).lower().strip()
            if response in ["yes", "y", "yeah", "yep"]:
                return True
            elif response in ["no", "n", "nope"]:
                return False
            else:
                print("\n\tPlease enter yes or no.")

    for i, topping in enumerate(requested_toppings):
        message = (
            f"{topping} is available, adding topping..."
            if topping in available_toppings
            else f"{topping} is unavailable."
        )
        print(message)

        if topping not in available_toppings:
            if not get_yes_no_input("\tProceed? [yes/no]: "):
                print("\nCancelling your order...We are sorry.")
                break
            else:
                print("Proceeding with your order anyways...\n.")
