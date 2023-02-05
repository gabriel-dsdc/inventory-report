from typing import Literal
from collections.abc import Iterable
from inventory_report.importer.importer import Importer
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer: Importer) -> None:
        self.importer = importer
        self.data = []

    def __iter__(self) -> InventoryIterator:
        return InventoryIterator(self.data)

    def import_data(self, path: str, type: Literal["simples", "completo"]):
        self.data += self.importer.import_data(path)

        if type == "simples":
            return SimpleReport.generate(self.data)
        elif type == "completo":
            return CompleteReport.generate(self.data)
        else:
            raise ValueError
