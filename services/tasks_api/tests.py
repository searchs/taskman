# import pytest
# from fastapi import status
# from starlette.testclient import TestClient

# from main import app


# @pytest.fixture
# def client():
#     return TestClient(app)


# def test_health_check(client):
#     """
#     GIVEN
#     WHEN health check endpoint is called with GET method
#     THEN response with status 200 and body OK is returned
#     """
#     response = client.get("/api/health-check/")
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json() == {"message": "OK"}


from uuid import uuid4

import pytest
from fastapi.testclient import TestClient

from main import app
from models import Task, TaskStatus

client = TestClient(app)


def test_health_check():
    response = client.get("/api/health-check/")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Allo Ola"}


def test_task_create():
    # Arrange
    task_id = uuid4()
    title = "Sample Task"
    owner = "User 1"

    # Act
    task = Task.create(id=task_id, title=title, owner=owner)

    # Assert
    assert task.id == task_id
    assert task.title == title
    assert task.owner == owner
    assert task.status == TaskStatus.OPEN  # Default status should be OPEN


def test_task_status_enum():
    # Check if the enum has the expected values
    assert TaskStatus.OPEN == "OPEN"
    assert TaskStatus.CLOSED == "CLOSED"


def test_task_create_invalid_id():
    # Ensure that the ID is actually a UUID
    invalid_id = "invalid-id"
    with pytest.raises(ValueError):
        Task.create(id=invalid_id, title="Invalid Task", owner="User 1")


def test_task_create_empty_title():
    # Ensure that an empty title raises an error (or handles it as needed)
    task_id = uuid4()
    print(f"\n\tTASK ID: {task_id}")
    owner = "User 1"

    with pytest.raises(
        ValueError
    ):  # This might change depending on your validation logic
        Task.create(id=task_id, title="", owner=owner)
