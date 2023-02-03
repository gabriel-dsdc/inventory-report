import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(self, path: str):
        file_extension = path.split(".")[-1]
        if file_extension != "xml":
            raise ValueError("Arquivo inválido")
        with open(path, mode="r") as xmlfile:
            xml_reader = xmltodict.parse(xmlfile.read())
            return [row for row in xml_reader["dataset"]["record"]]
