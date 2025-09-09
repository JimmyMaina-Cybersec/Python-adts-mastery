class SelectionSort:
    def __init__(self, items: list[str | int]):
        self.items = items

    def selection_sort(self, items):
        current_items = items.copy()
        sorted_items = []

        print(f"Starting selection sort.\nItems to be sorted: {current_items}")
        iteration = 1

        while len(current_items) > 1:
            for i, item in enumerate(current_items[1:], 1):
                # Finding the minimum element
                print(
                    f"\nChecking if {item} in position {i} is smaller than {current_items[0]}"
                )
                if current_items[0] > item:
                    print(
                        f"Apparently it is. So I'm swapping {item} with {current_items[0]}"
                    )
                    # Swapping
                    temp = current_items[0]
                    current_items[0] = item
                    current_items[i] = temp
                    print(f"Here is the current items after swapping: {current_items}")
                else:
                    print(
                        f"{item} at position {i} is not smaller than {current_items[0]}"
                    )
                    print("Proceeding to the next item on the list...")
            # Removing the smallest item and storing it in a sorted list
            print(
                f"Here is the current list of items after iteration {iteration}: {current_items}"
            )
            print(
                f"I'm now popping out the smallest element which should be at index 0: {current_items[0]}"
            )
            smallest = current_items.pop(0)
            print(f"After popping the smallest element: {current_items}")
            sorted_items.append(smallest)
            print(
                f"Here is the sorted items after iteration {iteration}: {sorted_items}"
            )
            print(f"I've completed iteration {iteration}.\n")
            iteration += 1

        print("Finished scanning the entire list")
        print(f"Here is the current items: {current_items}")
        print("I'll now add the remaining element to the sorted list...")
        sorted_items.append(*current_items)
        print(f"About to return the sorted list: {sorted_items}")

        return sorted_items

    def check_element_type(self):
        has_str = any([item for item in self.items if isinstance(item, str)])
        has_int = any([item for item in self.items if isinstance(item, int)])
        has_both = has_int and has_str

        return has_both, has_int, has_str

    def start_selection_sort(self):
        multi_typed, _, has_str = self.check_element_type()

        if multi_typed:
            str_items = [item.lower() for item in self.items if isinstance(item, str)]
            int_items = [item for item in self.items if isinstance(item, int)]

            sorted_str = self.selection_sort(str_items)
            sorted_int = self.selection_sort(int_items)

            print(f"Sorted items: {sorted_int} + {sorted_str}")
        elif has_str:
            str_items = [item.lower() for item in self.items if isinstance(item, str)]
            sorted_str = self.selection_sort(str_items)
        else:
            sorted_items = self.selection_sort(self.items)

            print(f"Sorted items: {sorted_items}")


items = ["banana", "Avocado", "apple"]
sorter = SelectionSort(items)
sorter.start_selection_sort()
