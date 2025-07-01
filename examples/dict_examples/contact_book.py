import re
from collections import defaultdict


# ─── custom exceptions ──────────────────────────────────────────────────────
class DuplicateContactError(Exception):
    """Raised when exactly the same contact already exists."""


class ConflictingContactError(Exception):
    """Raised when name exists but with different details."""


class PhoneBook:
    def __init__(self):
        # now each key maps to a list of contact‐info dicts
        self.contacts = defaultdict(list)

        # for display grouping (unchanged)
        self.sections = {
            "0_9": list("0123456789"),
            "a_c": list("abc"),
            "d_h": list("defgh"),
            "i_m": list("ijklm"),
            "n_r": list("nopqr"),
            "s_z": list("stuvwxyz"),
        }

    def add_contact(self, name: str, address: str, phone_number: str):
        """Add a new entry; raise on duplicate or conflict."""
        if not self._validate_phone(phone_number):
            raise ValueError("Phone must be in format (XXX) XXX-XXXX")

        info = {"address": address, "phone_number": phone_number}
        key = name.lower()

        # have we seen this name before?
        if self.contacts[key]:
            # exact duplicate?
            if info in self.contacts[key]:
                raise DuplicateContactError(f"'{name}' ⟶ this entry already exists.")
            # same name but different details
            raise ConflictingContactError(f"'{name}' ⟶ conflict with existing entry.")

        # brand new name
        self.contacts[key].append(info)
        return info

    def find_contact(self, name: str):
        """Return list of entries for that name, or KeyError."""
        key = name.lower()
        entries = self.contacts.get(key)
        if not entries:
            raise KeyError(f"Contact '{name}' not found")
        return entries  # a list

    def get_section_contacts(self, section: str):
        """Filter names by their first letter."""
        if section not in self.sections:
            raise ValueError(f"Invalid section: {section}")
        letters = self.sections[section]
        return {
            name: infos for name, infos in self.contacts.items() if name[0] in letters
        }

    def list_all_contacts(self):
        """Shallow copy of the entire structure."""
        return dict(self.contacts)

    def remove_contact(self, name: str):
        """Delete all entries under that name."""
        key = name.lower()
        if key not in self.contacts:
            raise KeyError(f"Contact '{name}' not found")
        return self.contacts.pop(key)

    def update_contact(self, name: str, index: int = 0, **kwargs):
        """
        Update one of the entries for name.
        index=0 means the first entry; update only that dict.
        """
        key = name.lower()
        if key not in self.contacts:
            raise KeyError(f"Contact '{name}' not found")

        entries = self.contacts[key]
        if not (0 <= index < len(entries)):
            raise IndexError(f"Entry index {index} out of range for '{name}'")

        entries[index].update(kwargs)
        return entries[index]

    def _validate_phone(self, phone: str) -> bool:
        return bool(re.match(r"^\(\d{3}\) \d{3}-\d{4}$", phone))

    def display_contacts(self):
        """Pretty-print grouped by section."""
        for sec, letters in self.sections.items():
            bucket = self.get_section_contacts(sec)
            if not bucket:
                continue
            print(f"\n=== {sec.upper().replace('_', '-')} ===")
            for name, infos in sorted(bucket.items()):
                for i, info in enumerate(infos, 1):
                    print(f"{name}  ({i})")
                    print(f"  {info['address']}")
                    print(f"  {info['phone_number']}")
                print()


if __name__ == "__main__":
    pb = PhoneBook()

    # simple loop to demo merge/edit/skip on conflict
    while True:
        name = input("Name (or 'exit'): ")
        if name.lower() == "exit":
            break
        addr = input("Address: ")
        phone = input("Phone [(XXX) XXX-XXXX]: ")

        try:
            pb.add_contact(name, addr, phone)
            print(f"✅ Added '{name}'")
        except DuplicateContactError as e:
            print(f"❌ {e}  (skipping)")
        except ConflictingContactError as e:
            print(f"⚠️ {e}")
            choice = input("Merge (m), rename (r), or skip (s)? ").lower()
            if choice in ["m", "merge"]:
                pb.contacts[name.lower()].append(
                    {"name": name, "address": addr, "phone_number": phone}
                )
                print(f"🔀 Merged under '{name}'")
            elif choice in ["r", "rename"]:
                new_name = input("New name: ")
                # direct append under new key
                pb.contacts[new_name.lower()].append(
                    {"name": new_name, "address": addr, "phone_number": phone}
                )
                print(f"✏️ Saved as '{new_name}'")
            else:
                print("⏭ skipped")

    print("\n📒 Your phone book:")
    pb.display_contacts()
