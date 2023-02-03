from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, products: list[dict]) -> str:
        companies = {}
        for product in products:
            company_name = product["nome_da_empresa"]
            companies[company_name] = companies.get(company_name, 0) + 1

        output = "Produtos estocados por empresa:\n"
        for company_name in companies:
            output += f"- {company_name}: {companies[company_name]}\n"
        return (
            f"{super().generate(products)}\n"
            f"{output}"
        )
