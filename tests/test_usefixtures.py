import pytest

@pytest.fixture()
def clear_database():
    print("Фикстура удаляем из бд")

@pytest.fixture()
def fill_database():
    print("создаём новые данные в бд")

@pytest.mark.usefixtures('fill_database')
def test_read_all():
    print("Reading all books")


@pytest.mark.usefixtures(
    'clear_database',
    'fill_database'
)
class TestLibrary:
    def test_read_from_library(self):
        ...

    def test_delete_from_library(self):
        ...
