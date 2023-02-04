from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.complete_report import CompleteReport


def test_decorar_relatorio():
    argument = [{"id": 1, "nome_do_produto": "Produto",
                 "nome_da_empresa": "Empresa",
                 "data_de_fabricacao": "2023-01-31",
                 "data_de_validade": "2024-01-31",
                 "numero_de_serie": "123",
                 "instrucoes_de_armazenamento": "Instruções"},
                {"id": 2, "nome_do_produto": "Cafe",
                 "nome_da_empresa": "Cafes Nature",
                 "data_de_fabricacao": "2020-07-04",
                 "data_de_validade": "2023-02-09",
                 "numero_de_serie": "FR48",
                 "instrucoes_de_armazenamento": "instrucao"}]
    colored_report = ColoredReport(CompleteReport).generate(argument)
    for colored_string in [
        "\033[32mData de fabricação mais antiga:\033[0m",
        f"\033[36m{argument[1]['data_de_fabricacao']}\033[0m\n",
        "\033[32mData de validade mais próxima:\033[0m",
        f"\033[36m{argument[1]['data_de_validade']}\033[0m\n",
        "\033[32mEmpresa com mais produtos:\033[0m",
        f"\033[31m{argument[0]['nome_da_empresa']}\033[0m"
    ]:
        assert colored_string in colored_report
