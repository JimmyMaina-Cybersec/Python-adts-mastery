if __name__ == "__main__":
    N = int(input())
    command_list = []
    for _ in range(N):
        command_list.append(input().strip())
    arr = []

    for cmd in command_list:
        cmd_parts = cmd.split()
        if not cmd_parts:
            print("Invalid command!")
            continue

        command = cmd_parts[0].lower()

        if command == "insert":
            if len(cmd_parts) < 3:  # Ensure required arguments exist
                print(f"Invalid input: '{cmd}' should be 'insert index value'")
                continue
            index, value = int(cmd_parts[1]), int(cmd_parts[2])
            arr.insert(index, value)

        elif command == "print":
            print(arr)

        elif command == "remove":
            if len(cmd_parts) < 2:
                print(f"Invalid input: '{cmd}' should be 'remove value'")
                continue
            value = int(cmd_parts[1])
            if value in arr:
                arr.remove(value)
            else:
                print(f"Value: {value} not found in list")

        elif command == "append":
            if len(cmd_parts) < 2:
                print(f"Invalid input: '{cmd}' should be 'append value'")
                continue
            value = int(cmd_parts[1])
            arr.append(value)

        elif command == "sort":
            arr.sort()

        elif command == "pop":
            if arr:  # Check if list is non-empty
                arr.pop()
            else:
                print("Cannot pop from an empty list!")

        elif command == "reverse":
            arr.reverse()

        else:
            print(f"Unrecognized command: {cmd_parts[0]}")
