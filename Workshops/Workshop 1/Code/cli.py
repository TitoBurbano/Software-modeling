"""
This module has simple CLI for the Sigpuzt arcade videogame system.

This file is part of Signpuzt rcagames.

Signpuzt arcade games is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

Signpuzt arcade games is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with Signpuzt arcade games. If not, see <https://www.gnu.org/licenses/>. 
"""
from main_classes import User, ArcadeMachine, Purchase, Videogame, Manager

def admin_mode(manager):
    """This function represents the admin mode of the arcade videogame system."""
    while True:
        print("\nAdmin Mode")
        print("1. Show All Purchases")
        print("2. Return to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            manager.show_all_purchases()
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")


def user_mode(manager):
    """This function represents the user mode of the arcade videogame system."""
    while True:
        print("\nChoose the material of the arcade machine:")
        print("1. Wood")
        print("2. Aluminum")
        print("3. Carbon Fiber")
        material_choice = input("Enter your choice: ")

        if material_choice == "1":
            material = "Wood"
        elif material_choice == "2":
            material = "Aluminum"
        elif material_choice == "3":
            material = "Carbon fiber"
        else:
            print("Invalid choice, the material will be wood.")
            material = "wood"

        color = input("Enter the color of the arcade machine: ")
        arcade_machine = ArcadeMachine(1, material, color)

        while True:
            print("\nAlready?")
            print("1. Show Catalog")
            print("2. Search Videogame by Name")
            print("3. Add Videogame to my Catalog")
            print("4. Purchase!")
            print("5. Return to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                if not arcade_machine.catalog:
                    print("The catalog is empty.")
                else:
                    for videogame in arcade_machine.catalog:
                        videogame.show_videogame()
            elif choice == "2":
                name = input("Enter the name of the videogame: ")
                try:
                    videogame = next(
                        vg for vg in arcade_machine.catalog if vg.name == name
                    )
                    videogame.show_videogame()
                except StopIteration:
                    print("Videogame not found.")
            elif choice == "3":
                name = input("Enter the name of the videogame: ")
                while True:
                    try:
                        code = int(input("Enter the code of the videogame: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a numeric code.")
                new_videogame = Videogame(name, code)
                arcade_machine.catalog.append(new_videogame)
                print("Videogame added to catalog.")
            elif choice == "4":
                name = input("Enter your name: ")
                address = input("Enter your address: ")
                phone = input("Enter your phone number: ")
                email = input("Enter your email: ")
                user = User(name, address, phone, email)
                purchase = Purchase(user, arcade_machine)
                manager.add_purchase(purchase)
                purchase.show_purchase()
                return  
            elif choice == "5":
                break  
            else:
                print("Invalid choice.")


def main_menu():
    """This function represents the main menu of the arcade videogame system."""
    manager = Manager()

    while True:
        print("\nSIGNPUZT ARCADE!")
        print("1. Admin Mode")
        print("2. User Mode")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            admin_mode(manager)
        elif choice == "2":
            user_mode(manager)
        elif choice == "3":
            print("Bye Bye")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()