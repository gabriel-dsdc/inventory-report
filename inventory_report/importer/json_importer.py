import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(self, path: str):
        file_extension = path.split(".")[-1]
        if file_extension != "json":
            raise ValueError("Arquivo inválido")
        with open(path, mode="r") as jsonfile:
            json_reader = json.load(jsonfile)
            return [row for row in json_reader]
