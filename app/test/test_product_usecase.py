# tests/test_product_usecase.py
import pytest
from unittest.mock import MagicMock
from use_cases.product_usecase import ProductUseCase

@pytest.fixture
def mock_product_usecase():
    usecase = ProductUseCase()
    usecase.service.get_all = MagicMock(return_value=[
        {"id":1, "nombre":"Producto1"}
    ])
    usecase.service.get_by_id = MagicMock(return_value={"id":1, "nombre":"Producto1"})
    usecase.service.create = MagicMock(return_value={"id":2, "nombre":"Producto2"})
    usecase.service.update = MagicMock(return_value={"id":1, "nombre":"Producto1Updated"})
    usecase.service.delete = MagicMock(return_value=True)
    return usecase

def test_list_products(mock_product_usecase):
    result = mock_product_usecase.list_products()
    assert len(result) == 1
    assert result[0]["nombre"] == "Producto1"

def test_create_product(mock_product_usecase):
    data = {"nombre":"Producto2","precio":100.0}
    product = mock_product_usecase.create_product(data)
    assert product["nombre"] == "Producto2"

def test_update_product(mock_product_usecase):
    data = {"nombre":"Producto1Updated"}
    product = mock_product_usecase.update_product(1, data)
    assert product["nombre"] == "Producto1Updated"

def test_delete_product(mock_product_usecase):
    result = mock_product_usecase.delete_product(1)
    assert result is True
