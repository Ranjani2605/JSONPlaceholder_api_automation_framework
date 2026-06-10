import pytest
from clients.posts_client import PostsClient



@pytest.fixture(scope="session")
def posts_client():
    return PostsClient()

@pytest.fixture
def valid_post_id():
    return 1

@pytest.fixture
def invalid_post_id():
    return 99999

