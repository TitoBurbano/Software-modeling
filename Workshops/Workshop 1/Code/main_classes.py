"""
This module contains an internal platform SIGNPUZT ARCADE machines.

Author: <titoalejandro3118@gmail.com>

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

from typing import List
from datetime import datetime

class Videogame:
    """This class represents a videogame"""

    def __init__(self, name: str, code: int):
        self.name = name
        self.code = code

    def show_videogame(self):
        """This function shows the videogame"""
        print(f"(Name: {self.name}, ID: {self.code})")


class ArcadeMachine:
    """This class represents an arcade machine"""

    def __init__(self, code: int, material: str, color: str):
        self.code = code
        self.material = material
        self.color = color
        self.catalog = Catalog().videogames

    def show_machine(self):
        """This method shows the arcade machine"""
        print("Success purchase")
        print(self.material)

   
class User:
    """This class represents a user of the system"""

    def __init__(self, name: str, address: str, phone: str, email: str):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Address: {self.address}, Phone: {self.phone}, Email: {self.email}"


class Catalog:
    """This class represents a catalog of videogames"""

    def __init__(self):
        self.videogames = self.main_videogames()

    def show_catalog(self):
        """This function shows the catalog of videogames"""
        print("Catalog of videogames")
        for videogame in self.videogames:
            videogame.show_videogame()

    def search_videogame_by_name(self, name: str) -> Videogame:
        """This function searches a videogame by name

        Args:
            name (str): The name of the videogame

        Returns:
            Videogame: The videogame searched
        """
        for videogame in self.videogames:
            if videogame.name == name:
                return videogame
        raise ValueError("Videogame not found")

    @staticmethod
    def main_videogames() -> list:
        """This function instantiates the main videogames

        Returns:
            list: The list of videogames installed in the arcade machine
        """
        list_videogames = [
            Videogame("The Legend of Zelda", 1),
            Videogame("Metroid", 2),
            Videogame("Mega Man", 3),
            Videogame("Final Fantasy", 4),
            Videogame("Castlevania", 5),
            Videogame("Contra", 6),
            Videogame("Street Fighter II", 7),
        ]
        return list_videogames


class Purchase:
    """This class represents a purchase of a videogame"""

    def __init__(self, user: User, arcade_machine: ArcadeMachine):
        self.user = user
        self.arcade_machine = arcade_machine

    def show_purchase(self):
        """This function shows the purchase"""
        print("Success purchase")
        print(
            f"{datetime.now()} -> User: {self.user}, Arcade machine: {self.arcade_machine.material}, {self.arcade_machine.color}"
        )


class Manager:
    """This class manages all purchases"""

    def __init__(self):
        self.purchases: List[Purchase] = []

    def add_purchase(self, purchase: Purchase):
        """This method adds a purchase to the list of purchases

        Args:
            purchase (Purchase): The purchase to add
        """
        self.purchases.append(purchase)

    def show_all_purchases(self):
        """This method shows all purchases"""
        if not self.purchases:
            print("No purchases have been made.")
        else:
            for purchase in self.purchases:
                purchase.show_purchase()
        with open("purchases.txt", "w", encoding="utf-8") as file:
            for purchase in self.purchases:
                file.write(
                    f"{datetime.now()} -> User: {purchase.user}, Arcade machine: {purchase.arcade_machine.material}, {purchase.arcade_machine.color}\n"
                )

    def add_videogame_to_catalog(self, arcade_machine: ArcadeMachine, videogame: Videogame):
        """This method adds a videogame to the catalog of the arcade machine

        Args:
            arcade_machine (ArcadeMachine): The arcade machine
            videogame (Videogame): The videogame to add
        """
        arcade_machine.catalog.append(videogame)