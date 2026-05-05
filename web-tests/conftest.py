import pytest
from utils.driver_factory import create_driver


@pytest.fixture(scope="function")
def driver():
    driver = create_driver(headless=True)
    yield driver
    driver.quit()
