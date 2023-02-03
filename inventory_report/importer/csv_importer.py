import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(self, path: str):
        file_extension = path.split(".")[-1]
        if file_extension != "csv":
            raise ValueError("Arquivo inválido")
        with open(path, mode="r") as csvfile:
            csv_reader = csv.DictReader(csvfile)
            return [row for row in csv_reader]
