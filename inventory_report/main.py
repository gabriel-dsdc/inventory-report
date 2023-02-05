import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos")
        # return print("Verifique os argumentos", file=sys.stderr)
    path = sys.argv[1]
    report_type = sys.argv[2]
    file_extension = path.split(".")[-1]
    file_types = {
        "csv": CsvImporter,
        "json": JsonImporter,
        "xml": XmlImporter}
    inventory = InventoryRefactor(file_types[file_extension])
    sys.stdout.write(inventory.import_data(path, report_type))
    # print(inventory.import_data(path, report_type), file=sys.stdout, end="")


if __name__ == "__main__":
    main()
