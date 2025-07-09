import os
from pathlib import Path


def calculate_directory_size(path):
    """
    Calculate the total size in bytes of a directory and all its contents.
    Returns the total size in bytes.
    """
    # Your implementation here
    total_size = 0
    paths = []
    visited = []
    restricted_dir = []
    symlinks = []

    if not os.path.exists(path):
        print("File does not exist")
        exit()
    elif os.path.isfile(path):
        print("Path should be for a directory not a file")
        exit()

    paths.append(path)
    while paths:
        current_path = Path(paths.pop())

        try:
            for item in current_path.iterdir():
                item_stat = item.stat()
                item_dev = item_stat.st_dev
                item_ino = item_stat.st_ino
                visited.append((item_dev, item_ino))

                if os.path.islink(item):
                    if (item_dev, item_ino) not in visited:
                        try:
                            total_size += os.path.getsize(item)
                            symlinks.append(item)
                        except PermissionError as e:
                            restricted_dir.append(item)
                            print(f"Permission denied: {e}")
                    else:
                        print("Found a cyclic symlink")
                        break
                elif os.path.isfile(item):
                    try:
                        total_size += os.path.getsize(item)
                    except PermissionError as e:
                        restricted_dir.append(item)
                        print(f"Permission denied: {e}")
                elif os.path.isdir(item):
                    paths.append(item)
                else:
                    print(f"{current_path} is empty")
        except FileNotFoundError as e:
            print(f"File not found: {e}")

    return total_size, restricted_dir, symlinks


if __name__ == "__main__":
    total_size, restricted_dir, symlinks = calculate_directory_size(
        "../../../Python-adts-mastery"
    )
    print("\nSize of directory (in bytes):")
    print(f"{total_size}")
    print("\nRestricted files:")
    print(", ".join(str(p) for p in restricted_dir))
    print("\nSymlinks:")
    print(", ".join(str(p) for p in symlinks))
