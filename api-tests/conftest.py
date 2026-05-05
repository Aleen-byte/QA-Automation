import pytest
from utils.client import PetstoreClient


@pytest.fixture(scope="session")
def client():
    return PetstoreClient()
