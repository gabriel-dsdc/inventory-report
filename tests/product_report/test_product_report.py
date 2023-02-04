from inventory_report.inventory.product import Product


def test_relatorio_produto():
    arguments = {"id": 1, "nome_do_produto": "Produto",
                 "nome_da_empresa": "Empresa",
                 "data_de_fabricacao": "01/31/2023",
                 "data_de_validade": "01/31/2024",
                 "numero_de_serie": "123",
                 "instrucoes_de_armazenamento": "Instruções"}
    product = Product(**arguments)
    assert repr(product) == (
        f"O produto {arguments['nome_do_produto']}"
        f" fabricado em {arguments['data_de_fabricacao']}"
        f" por {arguments['nome_da_empresa']} com validade"
        f" até {arguments['data_de_validade']}"
        f" precisa ser armazenado {arguments['instrucoes_de_armazenamento']}."
    )
