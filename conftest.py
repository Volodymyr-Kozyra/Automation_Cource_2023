import pytest

class User:
    def __init__(self, age) -> None:
        self.age = age
        
    def remove(self):
        self.age = None

@pytest.fixture(scope="session")
def user():
    # before test
    print("User created")
    user = User(42)
    
    # pass user object to test
    yield user
    
    # after test
    print("User removed")
    user.remove()