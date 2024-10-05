"""
This module has the worker classes into SIGNPUZT ARCADE.

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

from typing import List
from prefedined import Machine
from videogame import Videogames

class Admin:
    """
    This class represents the admins of the arcade videogames machines.
    """

    def __init__(self, id_: int, name: str, email: str):
        self.id_ = id_
        self.name = name
        self.email = email


class Customer:
    """
    This class represnts the customers of SIGNPUZT.
    """

    def __init__(self, id_: int, name: str, email: str, phone: str, adress: str):
        self.id_ = id_
        self.name = name
        self.email = email
        self.phone = phone
        self.adress = adress

    def add_videogame_to_catalog(self, machine: Machine, videogame: Videogames, videogame_resolution: str):
        """
        This function adds a videogame to the catalog

        Args:
            arcade_machine (Machine): The arcade machine
            videogame (Videogame): The videogame to add
            videogame_resolution (str): The resolution of the videogame that will be added
        """
        machine.videogames.append(videogame)
        if videogame_resolution == "HD":
            machine.price = machine.base_price + videogame.price * (1 + 0.1)
        elif videogame_resolution == "SD":
            machine.price = machine.base_price + videogame.price

    def remove_videogame_from_catalog(self, machine: Machine, videogame: Videogames, videogame_resolution: str):
        """
        This function removes a videogame from the catalog

        Args:
            arcade_machine (Machine): The arcade machine
            videogame (Videogame): The videogame to remove
            videogame_resolution (str): The resolution of the videogame that will be removed
        """
        machine.videogames.remove(videogame)
        if videogame_resolution == "HD":
            machine.price = machine.base_price - videogame.price * (1 + 0.1)
        elif videogame_resolution == "SD":
            machine.price = machine.base_price - videogame.price


class Catalog:
    """
    This class represents the catalog of machines.
    """

    def __init__(self):
        self.machines: List[Machine] = []

    def add_machine(self, machine: Machine):
        """
        Adds a machine to the catalog.
        """
        self.machines.append(machine)

    def search_by_videogame_count(self, count: int) -> List[Machine]:
        """
        Searches for machines with a specific number of videogames.
        """
        return [
            machine for machine in self.machines if len(machine.videogames) == count
        ]

    def search_by_material(self, material: str) -> List[Machine]:
        """
        Searches for machines with a specific type of material.
        """
        return [machine for machine in self.machines if machine.material == material]

    def search_by_videogame_name(self, videogame_name: str) -> List[Machine]:
        """
        Searches for machines that have a specific videogame by name.
        """
        return [
            machine
            for machine in self.machines
            if any(videogame.name == videogame_name for videogame in machine.videogames)
        ]
    def search_by_price_range(
        self, min_price: float, max_price: float
    ) -> List[Machine]:
        """
        Searches for machines within a specific price range.
        """
        return [
            machine
            for machine in self.machines
            if min_price <= machine.base_price <= max_price
        ]

    def search_by_weight_range(self, min_weight: int, max_weight: int) -> List[Machine]:
        """
        Searches for machines within a specific weight range.
        """
        return [
            machine
            for machine in self.machines
            if min_weight <= machine.weight <= max_weight
        ]

    def search_by_power_consumption_range(
        self, min_power: int, max_power: int
    ) -> List[Machine]:
        """
        Searches for machines within a specific power consumption range.
        """
        return [
            machine
            for machine in self.machines
            if min_power <= machine.power_consumption <= max_power
        ]
