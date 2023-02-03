class SimpleReport:
    @classmethod
    def generate(self, products: list[dict]) -> str:
        manufacturing_date_list = []
        expiration_date_list = []
        companies = {}
        for product in products:
            manufacturing_date_list.append(product["data_de_fabricacao"])
            expiration_date_list.append(product["data_de_validade"])
            company_name = product["nome_da_empresa"]
            companies[company_name] = companies.get(company_name, 0) + 1
        return (
            f"Data de fabricação mais antiga: {min(manufacturing_date_list)}\n"
            f"Data de validade mais próxima: {min(expiration_date_list)}\n"
            f"Empresa com mais produtos: {max(companies, key=companies.get)}"
        )
