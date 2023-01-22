import requests
from django.conf import settings
from random import randint, choice


WORDS = [
    'yard', 'yeah', 'year', 'yes', 'yet', 'you', 'young', 'your', 'yourself'
]


def _trello_get(url, custom_params):
    params = {  # Trello Auth
        'key': settings.TRELLO_API_KEY,
        'token': settings.TRELLO_API_TOKEN,
    }

    if custom_params:
        params.update(custom_params)

    return requests.get(url, params=params).json()


def _trello_post(url, custom_params):
    params = {  # Trello Auth
        'key': settings.TRELLO_API_KEY,
        'token': settings.TRELLO_API_TOKEN,
    }

    if custom_params:
        params.update(custom_params)

    return requests.post(url, params=params).json()


def board_get(name):
    url = settings.TRELLO_API_URL + 'members/me/boards/'
    params = {
        'fields': 'id,name'
    }

    data = _trello_get(url, params)

    try:
        return next(item for item in data if item['name'] == name)

    except StopIteration:
        raise Exception(f'You must setup a board called "{name}" on Trello')


def list_get(board_id, name):
    url = settings.TRELLO_API_URL + f'boards/{board_id}/lists'
    params = {
        'fields': 'id,name'
    }

    data = _trello_get(url, params)

    try:
        return next(item for item in data if item['name'] == name)

    except StopIteration:
        raise Exception(f'You must setup a list called "{name}" on Trello')


def label_get(board_id, name):
    url = settings.TRELLO_API_URL + f'boards/{board_id}/labels'
    params = {
        'fields': 'id,name'
    }

    data = _trello_get(url, params)

    try:
        return next(item for item in data if item['name'] == name)

    except StopIteration:
        raise Exception(f'You must setup a label called "{name}" on Trello')


def member_list(board_id):
    url = settings.TRELLO_API_URL + f'boards/{board_id}/members'
    params = {
        'fields': 'id,username'
    }
    return _trello_get(url, params)


def issue_create(title: str, description: str):
    url = settings.TRELLO_API_URL + 'cards'

    board = board_get(name=settings.TRELLO_BOARD_NAME)
    list_ = list_get(board_id=board['id'], name=settings.TRELLO_LIST_TODO)

    data = _trello_post(
        url,
        {
            'idList': list_['id'],
            'name': title,
            'desc': description,
        }
    )

    return data.get('id')


def bug_create(description: str):
    url = settings.TRELLO_API_URL + 'cards'

    board = board_get(name=settings.TRELLO_BOARD_NAME)
    list_ = list_get(board_id=board['id'], name=settings.TRELLO_LIST_TODO)
    label = label_get(board_id=board['id'],
                      name=settings.TRELLO_LABEL_BUG_NAME)
    member = choice(member_list(board_id=board['id']))

    data = _trello_post(
        url,
        {
            'idList': list_['id'],
            'name': f'bug-{choice(WORDS)}-{randint(0, 99999)}',
            'desc': description,
            'idLabels': label['id'],
            'idMembers': member['id']
        }
    )

    return data.get('id')


def task_create(title: str, category: str):
    url = settings.TRELLO_API_URL + 'cards'

    board = board_get(name=settings.TRELLO_BOARD_NAME)
    list_ = list_get(board_id=board['id'], name=settings.TRELLO_LIST_TODO)
    label = label_get(board_id=board['id'], name=category)

    data = _trello_post(
        url,
        {
            'idList': list_['id'],
            'name': title,
            'idLabels': label['id'],
        }
    )

    return data.get('id')
