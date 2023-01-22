import pytest
from rest_framework.test import APIClient

BASE_URL = '/api/v1'


@pytest.fixture
def cli():
    return APIClient()


def test_create_invalid_type(cli, mocker):
    res = cli.post(
        f'{BASE_URL}/trello_cards/',
        {
            'type': 'invalid_type',
        },
        format='json'
    )

    assert res.status_code == 400


def test_create_issue(cli, mocker):
    mocker.patch(
        'api_v1.views.issue_create',
        return_value='63cb1aa68620a700aa8ab870'
    )

    res = cli.post(
        f'{BASE_URL}/trello_cards/',
        {
            'type': 'issue',
            'title': 'Crear issue',
            'description': 'La tarjeta debe tener descripción'
        },
        format='json'
    )

    assert res.status_code == 201


def test_create_bug(cli, mocker):
    mocker.patch(
        'api_v1.views.bug_create',
        return_value='63cb1aa68620a700aa8ab870'
    )

    res = cli.post(
        f'{BASE_URL}/trello_cards/',
        {
            'type': 'bug',
            'description': 'No funciona la API'
        },
        format='json'
    )

    assert res.status_code == 201


@pytest.mark.parametrize('category', ['Test', 'Research', 'Maintenance'])
def test_create_task(cli, mocker, category):
    mocker.patch(
        'api_v1.views.task_create',
        return_value='63cb1aa68620a700aa8ab870'
    )

    res = cli.post(
        f'{BASE_URL}/trello_cards/',
        {
            'type': 'task',
            'title': 'Probar la API',
            'category': category
        },
        format='json'
    )

    assert res.status_code == 201


def test_create_task_invalid_category(cli, mocker):
    mocker.patch(
        'api_v1.views.task_create',
        return_value='63cb1aa68620a700aa8ab870'
    )

    res = cli.post(
        f'{BASE_URL}/trello_cards/',
        {
            'type': 'task',
            'title': 'Probar la API',
            'category': 'Invalid'
        },
        format='json'
    )

    assert res.status_code == 400
