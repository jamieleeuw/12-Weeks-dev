import sys
import importlib
import requests
import pytest


@pytest.fixture
def client():
    fake_todos = [
        {"id": 1, "userId": 1, "title": "Buy milk", "completed": False},
        {"id": 2, "userId": 1, "title": "Walk dog", "completed": True},
    ]

    class FakeResponse:
        def json(self):
            return [dict(t) for t in fake_todos]

        def raise_for_status(self):
            pass

    def fake_get(*args, **kwargs):
        return FakeResponse()

    original_get = requests.get
    requests.get = fake_get

    if "src.api_client.client" in sys.modules:
        module = importlib.reload(sys.modules["src.api_client.client"])
    else:
        module = importlib.import_module("src.api_client.client")

    requests.get = original_get

    return module


def test_view_todo_prints_the_tasks(client, capsys):
    client.view_todo()

    printed = capsys.readouterr().out
    assert "Buy milk" in printed
    assert "Walk dog" in printed


def test_view_todo_by_id_prints_the_right_task(client, capsys, monkeypatch):
    class FakeResponse:
        def json(self):
            return {"id": 1, "userId": 1, "title": "Buy milk", "completed": False}

        def raise_for_status(self):
            pass

    monkeypatch.setattr(requests, "get", lambda *a, **k: FakeResponse())

    client.view_todo_by_id(1)

    printed = capsys.readouterr().out
    assert "Buy milk" in printed


def test_view_todo_by_id_handles_network_error(client, capsys, monkeypatch):
    def fake_get_that_fails(*args, **kwargs):
        raise requests.exceptions.RequestException("no internet")

    monkeypatch.setattr(requests, "get", fake_get_that_fails)

    client.view_todo_by_id(1)

    printed = capsys.readouterr().out
    assert "Could not get Todo #1" in printed


def test_add_todo_success(client, capsys, monkeypatch):
    answers = iter(["1", "New task"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))

    class FakeResponse:
        status_code = 201

        def json(self):
            return {"id": 3, "userId": 1, "title": "New task", "completed": False}

        def raise_for_status(self):
            pass

    monkeypatch.setattr(requests, "post", lambda *a, **k: FakeResponse())

    client.add_todo()

    printed = capsys.readouterr().out
    assert "Task Created!!!" in printed


def test_add_todo_rejects_non_number_userid(client, capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt: "not-a-number")

    client.add_todo()

    printed = capsys.readouterr().out
    assert "UserID must be a number." in printed


def test_update_todo_success(client, capsys, monkeypatch):
    answers = iter(["1", "updated title"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))

    class FakeResponse:
        status_code = 200

        def raise_for_status(self):
            pass

    monkeypatch.setattr(requests, "put", lambda *a, **k: FakeResponse())

    client.update_todo()

    printed = capsys.readouterr().out
    assert "Task Updated!!!" in printed
    assert client.response[0]["title"] == "updated title"


def test_update_todo_asks_again_for_bad_id(client, capsys, monkeypatch):
    answers = iter(["999", "1", "updated title"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))

    class FakeResponse:
        status_code = 200

        def raise_for_status(self):
            pass

    monkeypatch.setattr(requests, "put", lambda *a, **k: FakeResponse())

    client.update_todo()

    printed = capsys.readouterr().out
    assert "That ID does not exist try again" in printed
    assert "Task Updated!!!" in printed


def test_delete_todo_success(client, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt: "1")

    class FakeResponse:
        status_code = 200

        def raise_for_status(self):
            pass

    monkeypatch.setattr(requests, "delete", lambda *a, **k: FakeResponse())

    client.delete_todo()

    remaining_ids = [task["id"] for task in client.response]
    assert 1 not in remaining_ids


def test_delete_todo_handles_network_error(client, capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt: "1")

    def fake_delete_that_fails(*args, **kwargs):
        raise requests.exceptions.RequestException("no internet")

    monkeypatch.setattr(requests, "delete", fake_delete_that_fails)

    client.delete_todo()

    printed = capsys.readouterr().out
    assert "Could not delete task" in printed
    remaining_ids = [task["id"] for task in client.response]
    assert 1 in remaining_ids