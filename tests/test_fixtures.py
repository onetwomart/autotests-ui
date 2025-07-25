import pytest

@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[Autouse] отправляем в сервис аналитики")

@pytest.fixture(scope="session")
def settings():
    print("[Session] Инициализируем настройки атвотестов")

pytest.fixture()
def user():
    print("[Function] Открываем браузер на каждый атвотест")



class TestUserFlow:
    def test_user_can_login(self,settings):
        ...