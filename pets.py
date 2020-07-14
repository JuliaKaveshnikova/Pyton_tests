import requests

class PetstorTest:
    responseId: str

def test_addPet():
    response = requests.post("https://petstore.swagger.io/v2/pet", json = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "cats"
  },
  "name": "Tom",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
    assert response.status_code == 200
    assert response.json()["name"] == "Tom"
    PetstorTest.responseId = response.json()["id"]
    assert response.json()["id"]

def test_getPet():
      response = requests.get(str("https://petstore.swagger.io/v2/pet/") + str(PetstorTest.responseId))
      print("AAAAAAAAAA")
      print(response.status_code)
      assert response.status_code == 200

def test_deletePet():
    response = requests.delete(str("https://petstore.swagger.io/v2/pet/") + str(PetstorTest.responseId))
    assert response.status_code == 200
    print(response.status_code)


def test_getDeletedPet():
    response = requests.get(str("https://petstore.swagger.io/v2/pet/") + str(PetstorTest.responseId))
    assert response.status_code == 404




