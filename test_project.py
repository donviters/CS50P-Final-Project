import pytest
from project import validate, register, generate_certificates

def test_validate():
    assert validate("Roger", "Federer", "rfederer@@atptour.com", "2024/05/24") == False
    assert validate("Rafael", "Nadal", "rnadal@atptour.com", "May 24, 2024") == False
    assert validate("Nov@k", "Djokovic", "ndjokovic@atptour.com", "2025/06/25") == False
    assert validate("Pete", "$ampras", "psampras@atptour.com", "2026/07/26") == False
    assert validate("Carlos", "Alcaraz", "calcaraz@atptour.com", "2027/13/32") == False


def test_register():
    assert register("Roger", "Federer", "rfederer@atptour.com", "2024/05/24") == True
    assert validate("Rafael", "Nadal", "rnadal@atptour.com", "2025/11/03") == True
    assert validate("Novak", "Djokovic", "ndjokovic@atptour.com", "2026/07/18") == True


def test_generate_certificates():
    with pytest.raises(SystemExit):
        generate_certificates("inexistent_file.csv")
