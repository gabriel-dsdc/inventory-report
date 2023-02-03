import csv
import json
from abc import ABC, abstractmethod
from typing import Literal
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class AbstractImport(ABC):
    @abstractmethod
    def read_file(self, path: str):
        pass


class CSVImport(AbstractImport):
    @classmethod
    def read_file(self, path: str):
        with open(path, mode="r") as csvfile:
            csv_reader = csv.DictReader(csvfile)
            return [row for row in csv_reader]


class JSONImport(AbstractImport):
    @classmethod
    def read_file(self, path: str):
        with open(path, mode="r") as jsonfile:
            json_reader = json.load(jsonfile)
            return [row for row in json_reader]


class Inventory:
    @classmethod
    def import_data(self, path: str, type: Literal["simples", "completo"]):
        file_extension = path.split(".")[-1]
        file_types = {"csv": CSVImport, "json": JSONImport}
        products = file_types[file_extension].read_file(path)

        if type == "simples":
            return SimpleReport.generate(products)
        elif type == "completo":
            return CompleteReport.generate(products)
        else:
            raise ValueError
