from inventory_report.inventory.product import Product


def test_cria_produto():
    arguments = {"id": 1, "nome_do_produto": "Produto",
                 "nome_da_empresa": "Empresa",
                 "data_de_fabricacao": "01/31/2023",
                 "data_de_validade": "01/31/2024",
                 "numero_de_serie": "123",
                 "instrucoes_de_armazenamento": "Instruções"}
    product = Product(**arguments)
    for key in arguments:
        assert getattr(product, key) == arguments[key]
