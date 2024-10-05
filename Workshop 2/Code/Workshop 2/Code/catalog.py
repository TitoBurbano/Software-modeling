from typing import List
from prefedined import Machine
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
        return [machine for machine in self.machines if len(machine.videogames) == count]

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

    def search_by_price_range(self, min_price: float, max_price: float) -> List[Machine]:
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

    def search_by_power_consumption_range(self, min_power: int, max_power: int) -> List[Machine]:
        """
        Searches for machines within a specific power consumption range.
        """
        return [
            machine
            for machine in self.machines
            if min_power <= machine.power_consumption <= max_power
        ]