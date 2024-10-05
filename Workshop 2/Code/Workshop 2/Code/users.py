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

from prefedined import Machine
from videogame import Videogames

class User:
    """
    This class represents the users of the arcade videogames machines.
    """

    def __init__(self, id_: int, name: str, email: str):
        self.id_ = id_
        self.name = name
        self.email = email


class Admin(User):
    """
    This class represents the admins of the arcade videogames machines.
    """

class Customer(User):
    """
    This class represents the customers of SIGNPUZT.
    """

    def __init__(self, id_: int, name: str, email: str, phone: str, address: str):
        super().__init__(id_, name, email)
        self.phone = phone
        self.address = address

    def add_videogame_to_catalog(self, machine: Machine, videogame: Videogames, videogame_resolution: str):
        """
        This function adds a videogame to the catalog.

        Args:
            machine (Machine): The arcade machine
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
        This function removes a videogame from the catalog.

        Args:
            machine (Machine): The arcade machine
            videogame (Videogame): The videogame to remove
            videogame_resolution (str): The resolution of the videogame that will be removed
        """
        machine.videogames.remove(videogame)
        if videogame_resolution == "HD":
            machine.price = machine.base_price - videogame.price * (1 + 0.1)
        elif videogame_resolution == "SD":
            machine.price = machine.base_price - videogame.price
