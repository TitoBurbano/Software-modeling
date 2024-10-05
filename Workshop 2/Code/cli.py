"""
This module has a interactive menu where the user could 
navegate into SIGNPUZT ARCADE.

Author: Tito Alejandro Burbano Plazas <titoalejandro3118@gmail.com>

SIGNPUZT ARCADE is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

SIGNPUZT ARCADE is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with SIGNPUZT ARCADE. If not, see <https://www.gnu.org/licenses/>.
"""

from users import Catalog, Customer
from videogame import VideogamesFactory
from prefedined import MachineFactory

def user_mode(catalog: Catalog):
    """
    This function represents the user mode of the system.
    """
    print("\nEnter your information:")
    user_id = int(input("Id: "))
    user_name = input("Name: ")
    user_email = input("Email: ")
    user_phone = input("Phone: ")
    user_address = input("Address: ")

    user = Customer(user_id, user_name, user_email, user_phone, user_address)
    print(
        f"\nUser Details -> ID: {user.id_}, Name: {user.name}, Email: {user.email}, Phone: {user.phone}, Address: {user.adress}"
    )

    while True:
        print("\nUser Mode")
        print("1. Select machine type")
        print("2. Show machines list.")
        print("3. Search by price.")
        print("4. Search by weight")
        print("5. Search by power consume.")
        print("6. Exit")
        choice = input("Please select an option: ")

        if choice == "6":
            print("BYE!")
            break

        if choice == "1":
            while True:
                print("1. Dance Revolution")
                print("2. Classical Arcade")
                print("3. Shooting Machine")
                print("4. Racing Machine")
                print("5. Virtual Reality")
                print("6. Exit")
                machine_choice = input("Select the type of your arcade machine: ")

                if machine_choice == "6":
                    print("BYE!")
                    break

                name = input("Enter the name of your machine: ")

                print("\nSelect the material of your machine:")
                print("1. Wood")
                print("2. Aluminium")
                print("3. Carbon Fiber")
                material_choice = input("Please select the material: ")

                if material_choice == "1":
                    material = "wood"
                elif material_choice == "2":
                    material = "aluminium"
                elif material_choice == "3":
                    material = "carbon fiber"
                else:
                    print("Invalid choice.")
                    continue

                color = input("Enter the color of your machine: ")

                if machine_choice == "1":
                    machine = MachineFactory.create_machine(
                        "DanceRevolution", name, material, color
                    )
                elif machine_choice == "2":
                    machine = MachineFactory.create_machine(
                        "ClassicalArcade", name, material, color
                    )
                elif machine_choice == "3":
                    machine = MachineFactory.create_machine(
                        "ShootingMachine", name, material, color
                    )
                elif machine_choice == "4":
                    machine = MachineFactory.create_machine(
                        "RacingMachine", name, material, color
                    )
                elif machine_choice == "5":
                    machine = MachineFactory.create_machine(
                        "VirtualReality", name, material, color
                    )
                else:
                    print("Invalid choice. Please select a valid option.")
                    continue

                machine.define_values(
                    machine.base_price,
                    machine.weight,
                    machine.power_consumption,
                    machine.material,
                )
                print(machine)

                while True:
                    print("\nManage Videogames")
                    print("1. Add a videogame")
                    print("2. Remove a videogame")
                    print("3. Finish")
                    manage_choice = input("Please select an option: ")

                    if manage_choice == "1":
                        videogame_name = input(
                            "Enter the name of the videogame: "
                        )
                        videogame_storytelling_creator = input(
                            "Enter the storytelling creator of the videogame: "
                        )
                        videogame_graphics_creator = input(
                            "Enter the graphics creator of the videogame: "
                        )
                        videogame_category = input(
                            "Enter the category of the videogame: "
                        )
                        videogame_price = float(
                            input("Enter the price of the videogame: ")
                        )
                        videogame_year = int(input("Enter the year of the videogame: ")
                                             )
                        print("\nSelect the resolution of the game:")
                        print("1. HD")
                        print("2. SH")
                        videogame_resolution_input = input(
                            "Please select an option: "
                        )

                        if videogame_resolution_input == "1":
                            videogame_resolution = "HD"
                        elif videogame_resolution_input == "2":
                            videogame_resolution = "SH"
                        else:
                            print("Invalid choice. Please select a valid option.")
                            continue

                        if type(machine).__name__ == "DanceRevolution":
                            videogame_machine_type = "dance"
                        elif type(machine).__name__ == "ClassicalArcade":
                            videogame_machine_type = "classical"
                        elif type(machine).__name__ == "RacingMachine":
                            videogame_machine_type = "racing"
                        elif type(machine).__name__ == "ShootingMachine":
                            videogame_machine_type = "shooting"
                        elif type(machine).__name__ == "VirtualReality":
                            videogame_machine_type = "virtualreality"

                        videogame_added = VideogamesFactory.create_videogames(
                            videogame_machine_type,
                            videogame_name,
                            videogame_storytelling_creator,
                            videogame_graphics_creator,
                            videogame_category,
                            videogame_price,
                            videogame_year,
                        )

                        print(videogame_added)

                        if videogame_added is not None:
                            user.add_videogame_to_catalog(
                                machine, videogame_added, videogame_resolution
                            )
                            print(f"Videogame '{videogame_name}' added.")
                        else:
                            print("Error: Failed to create videogame.")
                    elif manage_choice == "2":
                        videogame_name = input(
                            "Enter the name of the videogame: "
                        )
                        print("\nSelect the resolution of the game to remove:")
                        print("1. HD")
                        print("2. SH")
                        videogame_resolution_input = input(
                            "Please select an option: "
                        )

                        if videogame_resolution_input == "1":
                            videogame_resolution = "HD"
                        elif videogame_resolution_input == "2":
                            videogame_resolution = "SH"
                        else:
                            print("Invalid choice.")
                            continue

                        for vg in machine.videogames:
                            if vg.name == videogame_name:
                                user.remove_videogame_from_catalog(
                                    machine, vg, videogame_resolution
                                )
                                print(f"Videogame '{videogame_name}' removed.")
                                break
                        else:
                            print(f"Videogame '{videogame_name}' not found.")
                    elif manage_choice == "3":
                        break
                    else:
                        print("Invalid choice.")

                print("\nReturning to main menu.")
                break
        
        elif choice == "2":
            print("\nList of Predefined Machines:")
            for machine in catalog.machines:
                print(machine)
            print("\nEnd of list.")
        
        elif choice == "3":
            min_price = float(input("Enter the minimum price: "))
            max_price = float(input("Enter the maximum price: "))
            results = catalog.search_by_price_range(min_price, max_price)
            if results:
                print("\nSearch Results:")
                for machine in results:
                    print(machine)
            else:
                print("\nNo machines found matching the criteria.")

        elif choice == "4":
            min_weight = int(input("Enter the minimum weight: "))
            max_weight = int(input("Enter the maximum weight: "))
            results = catalog.search_by_weight_range(min_weight, max_weight)
            if results:
                print("\nSearch Results:")
                for machine in results:
                    print(machine)
            else:
                print("\nNo machines found matching the criteria.")

        elif choice == "5":
            min_power = int(input("Enter the minimum power consumption: "))
            max_power = int(input("Enter the maximum power consumption: "))
            results = catalog.search_by_power_consumption_range(min_power, max_power)
            if results:
                print("\nSearch Results:")
                for machine in results:
                    print(machine)
            else:
                print("\nNo machines found matching the criteria.")    
        else:
            print("Invalid choice. Please select a valid option.")


def admin_mode(catalog: Catalog):
    """
    This function represents the admin mode of the system.
    """
    while True:
        print("\nAdmin Mode")
        print("1. Search by videogame count")
        print("2. Search by material")
        print("3. Search by videogame name")
        print("4. Back to main menu")
        choice = input("Please select an option: ")

        if choice == "4":
            break

        if choice == "1":
            count = int(input("Enter the number of videogames: "))
            results = catalog.search_by_videogame_count(count)
        elif choice == "2":
            material = input("Enter the material: ")
            results = catalog.search_by_material(material)
        elif choice == "3":
            videogame_name = input("Enter the name of the videogame: ")
            results = catalog.search_by_videogame_name(videogame_name)
        else:
            print("Invalid choice. Select a valid option.")
            continue

        if results:
            print("\nSearch Results:")
            for machine in results:
                print(machine)
        else:
            print("\nNo machines found.")


def main():
    """
    This function represents the main menu of the system.
    """
    catalog = Catalog()

    catalog.add_machine(
        MachineFactory.create_machine(
            "DanceRevolution", "DDR Machine", "aluminium", "red"
        )
    )
    catalog.add_machine(
        MachineFactory.create_machine(
            "ClassicalArcade", "Classic Machine", "wood", "blue"
        )
    )
    catalog.add_machine(
        MachineFactory.create_machine(
            "ShootingMachine", "Shooter Machine", "carbon fiber", "green"
        )
    )
    catalog.add_machine(
        MachineFactory.create_machine(
            "RacingMachine", "Racer Machine", "carbon fiber", "yellow"
        )
    )
    catalog.add_machine(
        MachineFactory.create_machine("VirtualReality", "VR Machine", "wood", "black")
    )

    while True:
        print("\nWho are you?")
        print("1. An admin")
        print("2. An user")
        print("3. Nobody")
        choice = input("Please choose an option: ")

        if choice == "3":
            print("BYE!")
            break

        if choice == "1":
            admin_mode(catalog)
        elif choice == "2":
            user_mode(catalog)
        else:
            print("Invalid choice. Select a valid option.")

if __name__ == "__main__":
    main()