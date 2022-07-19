from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_error():
    response = client.get("/cause_a_404/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


def test_create_payment():
    response = client.post("/payments/?name=Testing&amount=123.45")
    assert response.status_code == 200
    assert response.json() == {"amount": 123.45, "id": 1, "name": "Testing"}


def test_get_payments():
    response = client.get("/payments/")
    assert response.status_code == 200
    assert response.json() == [{"amount": 123.45, "id": 1, "name": "Testing"}]


def test_update_payments():
    response = client.put("/payments/1?new_payment=543.21")
    assert response.status_code == 200
    assert response.json() == 1


def test_get_payments_by_name():
    response = client.get("/payments/Testing")
    assert response.status_code == 200
    assert response.json() == [{"amount": 543.21, "id": 1, "name": "Testing"}]


def test_drop_payment():
    response = client.delete("/payments/1")
    assert response.status_code == 200
    assert response.json() == {"amount": 543.21, "id": 1, "name": "Testing"}


def test_create_owner():
    response = client.post("/owners/?name=Test&paid=True")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Test", "paid": True}


def test_get_owner():
    response = client.get("/owners/")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "name": "Test", "paid": True}]


def test_delete_owner():
    response = client.delete("/owners/1")
    assert response.status_code == 200
    assert response.json() == {"dogs": [], "id": 1, "name": "Test", "paid": True}


def test_create_dog():
    response = client.post("/dogs/?name=Testing&breed=Testing&age=123&owner_id=1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Testing",
        "breed": "Testing",
        "age": 123,
        "owner_id": 1,
    }


def test_read_dog():
    response = client.get("/dogs/")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "name": "Testing",
            "breed": "Testing",
            "age": 123,
            "owner_id": 1,
        }
    ]


def test_delete_dog():
    response = client.delete("/dogs/?id=1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Testing",
        "breed": "Testing",
        "age": 123,
        "owner_id": 1,
    }


def test_add_owner():
    response = client.post("/owners/?name=Testing&paid=True")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Testing", "paid": True}


def test_add_dog():
    response = client.post("/dogs/?name=Testing&breed=Testing&age=123&owner_id=1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "age": 123,
        "name": "Testing",
        "breed": "Testing",
        "owner_id": 1,
    }


def test_read_owners_dogs():
    response = client.get("/owners_dogs/Testing")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "age": 123,
            "name": "Testing",
            "breed": "Testing",
            "owner_id": 1,
        }
    ]


def test_delete_dog_2():
    response = client.delete("/dogs/?id=1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Testing",
        "breed": "Testing",
        "age": 123,
        "owner_id": 1,
    }


def test_delete_owner2():
    response = client.delete("/owners/1")
    assert response.status_code == 200
    assert response.json() == {"dogs": [], "id": 1, "name": "Testing", "paid": True}


def test_get_remaining():
    response = client.get("/all/")
    assert response.status_code == 200
    assert response.json() == [[], [], []]
