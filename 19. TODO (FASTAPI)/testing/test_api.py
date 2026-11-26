import pytest
from main import app
from fastapi.testclient import TestClient


@pytest.fixture(scope="class")
def client():
    with TestClient(app) as test_client:
        yield test_client


class TestAPI:
    id=None

    def test_home(self, client):
        response = client.get("/")
        assert response.status_code == 200

    def test_alltodos(self, client):
        response = client.get("/api/alltodos")

        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_activetodos(self, client):
        for query in ["active", "inactive", "completed"]:
            response = client.get(
                f"/api/activetodos?status={query}"
            )

            assert response.status_code == 200

            for todo in response.json():
                assert todo["status"] == query

    def test_addtodos(self,client):
        response=client.post("/api/addtodos",json={"name":"testing","status":"active"})
        assert response.status_code==201
        assert isinstance(response.json(),dict)
        self.__class__.id=response.json()['id']
        # print(id)

    def test_todobyid(self, client):
        assert self.__class__.id is not None
        response = client.get(f"/api/todos/{self.__class__.id}")
        assert response.status_code == 200
        assert isinstance(response.json(),dict)

    def test_updatetodo(self,client):
        assert self.__class__.id is not None
        response=client.put(f"/api/updatetodos/{self.__class__.id}",json={"name":"testing","status":"completed"})
        assert response.status_code==200

    def test_deltetodos(self,client):
        assert self.__class__.id is not None
        response=client.delete(f"/api/deletetodos/{self.__class__.id}")
        assert response.status_code==200



    
        
