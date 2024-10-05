"""
This module has a class to define the differente types of an
arcade machine that an user could find in SIGNPUZT ARCADE.

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

from abc import ABC
from typing import List
from videogame import VideogamesFactory, Videogames


class Machine(ABC):
    """
    This class represents a general arcade videogames machine.
    """

    def __init__(self, name: str,material: str, color: str, dimensions: str, weight: int,
                 power_consumption: int, memory: str, processor: str, base_price: float, 
                 videogames: List[Videogames]):
        self.name = name
        self.material = material
        self.color = color
        self.dimensions = dimensions
        self.weight = weight
        self.power_consumption = power_consumption
        self.memory = memory
        self.processor = processor
        self.base_price = base_price
        self.videogames = videogames

    def define_values(self, base_price: float, weight: int, power_consumption: int, material: str):
        """
        This method defines the values of the machine according to the specs added.
        """
        if material == "wood":
            self.weight = weight * (1 + 0.1)
            self.base_price = base_price * (1 - 0.05)
            self.power_consumption = power_consumption * (1 + 0.15)
        elif material == "aluminium":
            self.weight = weight * (1 - 0.05)
            self.base_price = base_price * (1 + 0.1)
        elif material == "carbon_fiber":
            self.weight = weight * (1 - 0.15)
            self.base_price = base_price * (1 + 0.2)
            self.power_consumption = power_consumption * (1 - 0.1)

    def __str__(self) -> str:
        videogames_str = "\n".join(str(game) for game in self.videogames)
        return (
            f"\nMachine Details:\n"
            f"Type: {type(self).__name__}\n"
            f"Name: {self.name}\n"
            f"Material: {self.material}\n"
            f"Color: {self.color}\n"
            f"Dimensions: {self.dimensions}\n"
            f"Weight: {self.weight} kg\n"
            f"Power Consumption: {self.power_consumption} W\n"
            f"Memory: {self.memory}\n"
            f"Processor: {self.processor}\n"
            f"Base Price: ${self.base_price}\n"
            f"Videogames:\n{videogames_str}"
        )


class DanceRevolution(Machine):
    """This class defines a Dance Revolution arcade videogames machine."""

    def __init__(self, name: str, material: str, color: str):
        super().__init__(
            name=name,
            material=material,
            color=color,
            dimensions="10*4*10",
            weight="f{620}kg",
            power_consumption="f{500}ws",
            memory="1tb",
            processor="Intel Core",
            base_price=.0,
            videogames=[
                VideogamesFactory.create_videogames(
                    "Dance",
                    "Just dance",
                    "Hasbro",
                    "mOvEmEnT",
                    "Dance/Music",
                    25.9,
                    2000,
                ),
                VideogamesFactory.create_videogames(
                    "Dance",
                    "LMFAO, the game",
                    "Redfoo",
                    "Sony 3D",
                    "Dance/Music",
                    100.9,
                    2012,
                ),
            ],
        )
        self.difficulties = ["easy", "medium", "hard"]
        self.arrow_cardinalities = ["up", "down", "left", "right"]
        self.controls_price = 150

    def __str__(self) -> str:
        return (
            super().__str__() + f"\nDifficulties: {self.difficulties}\n"
            f"Arrow Cardinalities: {self.arrow_cardinalities}\n"
            f"Controls Price: ${self.controls_price}"
        )


class ClassicalArcade(Machine):
    """This class defines a Classical Arcade arcade videogames machine."""

    def __init__(self, name: str, material: str, color: str):
        super().__init__(
            name=name,
            material=material,
            color=color,
            dimensions="1*2*2",
            weight="f{120}kg",
            power_consumption="f{80}ws",
            memory="32gb",
            processor="Apple(?)",
            base_price=100.0,
            videogames=[
                VideogamesFactory.create_videogames(
                    "Classical",
                    "Pac-man",
                    "Toru Iwatani",
                    "Namco",
                    "Arcade",
                    5.0,
                    1980,
                ),
                VideogamesFactory.create_videogames(
                    "Classical",
                    "Prince of Persa",
                    "Shigeru Miyamoto",
                    "Nintendo",
                    "Adventure",
                    40.0,
                    1988,
                ),
            ],
        )
        self.make_vibration = False
        self.sound_record_alert = False

    def enable_vibration(self):
        """This method enables the vibration of the machine."""
        self.make_vibration = True

    def disable_vibration(self):
        """This method disables the vibration of the machine."""
        self.make_vibration = False

    def enable_sound_record_alert(self):
        """This method enables the sound record alert of the machine."""
        self.sound_record_alert = True

    def disable_sound_record_alert(self):
        """This method disables the sound record alert of the machine."""
        self.sound_record_alert = False

    def __str__(self) -> str:
        return (
            super().__str__() + f"\nMake Vibration: {self.make_vibration}\n"
            f"Sound Record Alert: {self.sound_record_alert}"
        )


class ShootingMachine(Machine):
    """This class defines a Shooting Machine arcade videogames machine."""

    def __init__(self, name: str, material: str, color: str):
        super().__init__(
            name=name,
            material=material,
            color=color,
            dimensions="2*4*2",
            weight="f{700}kg",
            power_consumption="f{300}ws",
            memory="500gb",
            processor="Intel Pentium",
            base_price=700,
            videogames=[
                VideogamesFactory.create_videogames(
                    "Shooting",
                    "Luigi's Mansion",
                    "Next level games",
                    "Nintendo",
                    "Action",
                    200.0,
                    2019,
                ),
                VideogamesFactory.create_videogames(
                    "Shooting",
                    "Kill the zombies",
                    "Little chicken",
                    "Noone",
                    "Shooter",
                    15.0,
                    2015,
                ),
            ],
        )
        self.gun_type = "Gun"
        self.gun_price = 25

    def __str__(self) -> str:
        return (
            super().__str__() + f"\nGun Type: {self.gun_type}\n"
            f"Gun Price: ${self.gun_price}"
        )


class RacingMachine(Machine):
    """This class defines a Racing Machine arcade videogames machine."""

    def __init__(self, name: str, material: str, color: str):
        super().__init__(
            name=name,
            material=material,
            color=color,
            dimensions="4*4*4",
            weight="f{400}kg",
            power_consumption="f{850}ws",
            memory="20gb",
            processor="F1",
            base_price=950.0,
            videogames=[
                VideogamesFactory.create_videogames(
                    "Racing",
                    "f1",
                    "Formula 1",
                    "EA Sports",
                    "Racing",
                    380.0,
                    2024,
                ),
                VideogamesFactory.create_videogames(
                    "Racing",
                    "Need for Speed",
                    "Electronic Arts",
                    "Turbo Graphics",
                    "Racing",
                    130.0,
                    2022,
                ),
            ],
        )
        self.type_vehicle = "Car"
        self.seats = 1

    def __str__(self) -> str:
        return (
            super().__str__() + f"\nType Vehicle: {self.type_vehicle}\n"
            f"Seats: {self.seats}"
        )


class VirtualReality(Machine):
    """This class defines a Virtual Reality arcade videogames machine."""

    def __init__(self, name: str, material: str, color: str):
        super().__init__(
            name=name,
            material=material,
            color=color,
            dimensions="1*2*2",
            weight="f{2}kg",
            power_consumption="f{17}ws",
            memory="128gb",
            processor="Apple 17",
            base_price=1200.0,
            videogames=[
                VideogamesFactory.create_videogames(
                    "Simulator",
                    "Persona",
                    "Bluesky",
                    "VRrecords",
                    "VR",
                    105.0,
                    2023,
                ),
                VideogamesFactory.create_videogames(
                    "Simulator",
                    "Market simulator",
                    "Unknown",
                    "usaVR",
                    "VR",
                    150.0,
                    2024,
                ),
            ],
        )
        self.type_glasses = "VR"
        self.resolution_glasses = "2040p"
        self.price_glasses = 1800

    def __str__(self) -> str:
        return (
            super().__str__() + f"\nType Glasses: {self.type_glasses}\n"
            f"Resolution Glasses: {self.resolution_glasses}\n"
            f"Price Glasses: ${self.price_glasses}"
        )


class MachineFactory:
    """This class is a factory to create machines of different types."""

    @staticmethod
    def create_machine(machine_type: str, name: str, material: str, color: str):
        """This method creates a machine of the specified type."""
        if machine_type == "DanceRevolution":
            return DanceRevolution(name, material, color)
        elif machine_type == "ClassicalArcade":
            return ClassicalArcade(name, material, color)
        elif machine_type == "ShootingMachine":
            return ShootingMachine(name, material, color)
        elif machine_type == "RacingMachine":
            return RacingMachine(name, material, color)
        elif machine_type == "VirtualReality":
            return VirtualReality(name, material, color)
