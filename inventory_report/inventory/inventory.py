import csv
from abc import ABC, abstractmethod
from typing import Literal
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class AbstractImport(ABC):
    @abstractmethod
    def import_data(self, path: str):
        pass


class CSVImport(AbstractImport):
    @classmethod
    def import_data(self, path: str):
        with open(path, mode="r") as csvfile:
            csv_reader = csv.DictReader(csvfile)
            return [row for row in csv_reader]


class Inventory:
    @classmethod
    def import_data(self, path: str, type: Literal["simples", "completo"]):
        file_types = {"csv": CSVImport}
        products = file_types[path[-3:]].import_data(path)

        if type == "simples":
            return SimpleReport.generate(products)
        elif type == "completo":
            return CompleteReport.generate(products)
        else:
            raise ValueError
