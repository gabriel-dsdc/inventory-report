from typing import Literal
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(self, path: str, type: Literal["simples", "completo"]):
        file_extension = path.split(".")[-1]
        file_types = {
            "csv": CsvImporter,
            "json": JsonImporter,
            "xml": XmlImporter}
        products = file_types[file_extension].read_file(path)

        if type == "simples":
            return SimpleReport.generate(products)
        elif type == "completo":
            return CompleteReport.generate(products)
        else:
            raise ValueError
