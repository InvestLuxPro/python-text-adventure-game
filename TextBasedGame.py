# Anthony Bowser
# IT 140 Project Two: Text-Based Adventure Game
# Quest of the Silk Lair

def show_instructions():
    """Display game title, goal, and valid commands."""
    print("Quest of the Silk Lair")
    print("Choose your class and collect the required items before facing the Spider Queen.")
    print("Move commands: go North, go South, go East, go West")
    print("Add to Inventory: get [item name]")
    print("-" * 32)


def show_status(current_room, inventory, rooms, required_items, player_class):
    """Display the player's current location, inventory, and room item."""

    print(f"\nClass: {player_class}")
    print(f"You are in the {current_room}")

    if inventory:
        print(f"Inventory: {sorted(inventory)}")
    else:
        print("Inventory: None")

    items_remaining = len(required_items) - len(inventory)
    print(f"Items remaining to collect: {items_remaining}")

    room_item = rooms[current_room].get("item")
    if room_item and room_item not in inventory:
        print(f"You see a {room_item} in this room.")

    if current_room == "Guard Post" and items_remaining > 0:
        print("⚠ Warning: The Spider Queen's Lair is to the East!")
        print("Collect all required items before entering!")

    print("-" * 32)


def normalize_command(command):
    return " ".join(command.strip().split())


def choose_class():
    """Prompt user to choose Mage or Warrior."""
    while True:
        choice = input("Choose your class (Mage/Warrior): ").strip().title()
        if choice in ["Mage", "Warrior"]:
            return choice
        print("Invalid class. Please type Mage or Warrior.")


def main():

    rooms = {
        "Entrance Chamber": {
            "North": "Guard Post",
            "South": "Barracks",
            "East": "Arcane Forge",
            "West": "Armory"
        },

        "Guard Post": {
            "South": "Entrance Chamber",
            "East": "Spider Queen's Lair",
            "item": "Dungeon Key"
        },

        "Spider Queen's Lair": {
            "West": "Guard Post"
        },

        "Armory": {
            "East": "Entrance Chamber",
            "item": "Sword"
        },

        "Barracks": {
            "North": "Entrance Chamber",
            "East": "Rune Library",
            "item": "Shield"
        },

        "Rune Library": {
            "West": "Barracks",
            "item": "Spellbook"
        },

        "Arcane Forge": {
            "West": "Entrance Chamber",
            "North": "Apothecary",
            "item": "Mage Staff"
        },

        "Apothecary": {
            "South": "Arcane Forge",
            "item": "Healing Potion"
        }
    }

    villain_room = "Spider Queen's Lair"

    show_instructions()

    player_class = choose_class()

    # Class-specific intro line
    if player_class == "Mage":
        print("\nYou feel arcane energy humming at your fingertips...")
    else:
        print("\nYou tighten your grip on your weapon and steady your stance...")

    # Required items based on class
    universal_items = ["Dungeon Key", "Healing Potion"]

    if player_class == "Mage":
        class_items = ["Spellbook", "Mage Staff"]
    else:
        class_items = ["Sword", "Shield"]

    required_items = universal_items + class_items

    current_room = "Entrance Chamber"
    inventory = []

    while True:

        if current_room == villain_room:

            if all(item in inventory for item in required_items):

                print("\n✨ You step into the Spider Queen's Lair fully prepared!")

                if player_class == "Mage":
                    print("Arcane energy surges through your staff.")
                    print("With a blast of magical power, you bind the Spider Queen in radiant light!")
                    print("The Silk Lair trembles as your spell seals her fate.")
                else:
                    print("Steel clashes against chitin as you charge forward.")
                    print("With shield raised and sword blazing, you strike the final blow!")
                    print("The Spider Queen falls beneath your strength and resolve.")

                print("\n🏆 VICTORY!")
                print("Thanks for playing Quest of the Silk Lair.")

            else:
                print("\nNOM NOM...GAME OVER!")
                print("The Spider Queen defeats you before you were ready.")
                print("Thanks for playing Quest of the Silk Lair.")

            break

        show_status(current_room, inventory, rooms, required_items, player_class)

        command = normalize_command(input("Enter your move: "))

        if command.lower() in ("exit", "quit"):
            print("\nYou chose to leave the dungeon.")
            print("Thanks for playing.")
            break

        if command.lower().startswith("go "):
            direction = command[3:].strip().title()

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                print(f"\nYou moved {direction}.")
                print(f"Progress update: {len(inventory)}/{len(required_items)} items collected.")
            else:
                print("You can't go that way.")

        elif command.lower().startswith("get "):
            requested_item = command[4:].strip()
            room_item = rooms[current_room].get("item")

            if not room_item:
                print("There is nothing to get in this room.")
            elif room_item.lower() != requested_item.lower():
                print(f"You don't see '{requested_item}' here.")
            elif room_item in inventory:
                print("You already have that item.")
            else:
                inventory.append(room_item)
                print(f"{room_item} retrieved!")

        else:
            print("Invalid command.")
            print("Try: go North / go South / go East / go West / get [item name]")


if __name__ == "__main__":
    main()