class BinarySearch:
    def __init__(self, items: list[int | str], correct_guess):
        self.items = sorted(items)  # Binary search needs sorted list!
        self.correct_guess = correct_guess

    def check_mixed_types(self):
        """Check if list contains both int and str"""
        has_int = any(isinstance(item, int) for item in self.items)
        has_str = any(isinstance(item, str) for item in self.items)
        return has_int and has_str

    def binary_search(self, items):
        """Binary search implementation"""
        current_items = items.copy()

        if self.correct_guess not in current_items:
            return f"'{self.correct_guess}' not found in the list"

        while len(current_items) > 1:
            mid_index = len(current_items) // 2
            guess = current_items[mid_index]

            print(f"Progress: {current_items}")

            if self.correct_guess == guess:
                print("Correct!")
                return f"Found it! The answer is {guess}"
            elif self.correct_guess > guess:
                current_items = current_items[mid_index + 1 :]  # exclude mid
                print(f"Correct answer is higher up than {guess}")
            else:
                current_items = current_items[:mid_index]
                print(f"Correct answer is lower down than {guess}")

        return f"Found it! The answer is {current_items[0]}"

    def start_search(self):
        """Main method to start the search"""
        if self.check_mixed_types():
            print("Mixed types detected. You can't binary search mixed int/str lists.")
            print("Separating strings from integers into separate sorted lists...")
            # Separating into list and passing relevant list to search
            if isinstance(self.correct_guess, int):
                int_items = [item for item in self.items if isinstance(item, int)]
                return self.binary_search(sorted(int_items))
            else:
                str_items = [item for item in self.items if isinstance(item, str)]
                return self.binary_search(sorted(str_items))
        else:
            # All same type, search normally
            return self.binary_search(self.items)


# Usage example
items = [1, 30, 51, 37, 9, 11, 43, 10]
searcher = BinarySearch(items, 7)
searcher.start_search()
