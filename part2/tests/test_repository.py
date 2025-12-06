import pytest
from hbnb.persistence.in_memory.repository import InMemoryRepository

def test_crud_lifecycle():
    repo = InMemoryRepository()

    # create
    user = {"username": "alice", "email": "alice@example.com"}
    created = repo.create("User", user)
    assert "id" in created
    uid = created["id"]

    # get
    got = repo.get("User", uid)
    assert got["username"] == "alice"

    # list
    lst = repo.list("User")
    assert isinstance(lst, list) and len(lst) == 1

    # update
    updated = repo.update("User", uid, {"username": "alice2"})
    assert updated["username"] == "alice2"

    # delete
    assert repo.delete("User", uid) is True
    assert repo.get("User", uid) is None
