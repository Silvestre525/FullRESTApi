from apps.userss.models import User
import pytest


@pytest.mark.django_db
def test_userss_creation():

    user = User.objects.create(
    email = "testusers@gmail.com",
    name = "testuser",
    password = "testpassword"
    )

    assert user.email == "testusers@gmail.com"
