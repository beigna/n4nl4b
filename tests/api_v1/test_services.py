import pytest
from api_v1.services import board_get, list_get, label_get, member_list


def test_board_get_ok(mocker):
    mocker.patch(
        'api_v1.services._trello_get',
        return_value=[
            {'id': '5591a0f126ca78a0f4954920', 'name': 'Assets - Roadmap'},
            {'id': '54efcb810944d954bbe89294', 'name': 'Casita BB'},
            {'id': '63ca9e1b4a6dd800a47f2cc4', 'name': 'NaNLab'},
            {'id': '552bcf6223131d6268054074', 'name': 'Podcast Igualdad'},
            {'id': '5310711084b78dc61155d6d6', 'name': 'UTN'},
            {'id': '52efe6cebe079dcf5215971d', 'name': 'Welcome Board'}
        ]
    )

    board = board_get('NaNLab')

    assert board['id'] == '63ca9e1b4a6dd800a47f2cc4'


def test_board_get_fail(mocker):
    mocker.patch(
        'api_v1.services._trello_get',
        return_value=[
            {'id': '52efe6cebe079dcf5215971d', 'name': 'Welcome Board'}
        ]
    )

    with pytest.raises(Exception) as e:
        board_get('NaNLab')

    assert str(e.value) == 'You must setup a board called "NaNLab" on Trello'


def test_list_get_ok(mocker):
    mocker.patch(
        'api_v1.services._trello_get',
        return_value=[
            {'id': '63ca9e57ea882503f1188670', 'name': 'To-Do'},
            {'id': '63ca9e54f223b403b1d3f32c', 'name': 'Assigned'},
            {'id': '63ca9e5eb1f33e0018c686fd', 'name': 'In Progress'}
        ]
    )

    list_ = list_get('123sef', 'To-Do')

    assert list_['id'] == '63ca9e57ea882503f1188670'


def test_list_get_fail(mocker):
    mocker.patch(
        'api_v1.services._trello_get',
        return_value=[
            {'id': '63ca9e54f223b403b1d3f32c', 'name': 'Assigned'},
        ]
    )

    with pytest.raises(Exception) as e:
        list_get('123sef', 'To-Do')

    assert str(e.value) == 'You must setup a list called "To-Do" on Trello'


def test_label_get_ok(mocker):
    mocker.patch(
        'api_v1.services._trello_get',
        return_value=[
            {'id': '63ca9e57ea882503f1188670', 'name': 'Bug'},
            {'id': '63ca9e54f223b403b1d3f32c', 'name': 'Test'},
            {'id': '63ca9e5eb1f33e0018c686fd', 'name': 'Research'}
        ]
    )

    list_ = label_get('123sef', 'Bug')

    assert list_['id'] == '63ca9e57ea882503f1188670'


def test_label_get_fail(mocker):
    mocker.patch(
        'api_v1.services._trello_get',
        return_value=[
            {'id': '63ca9e54f223b403b1d3f32c', 'name': 'Test'},
        ]
    )

    with pytest.raises(Exception) as e:
        label_get('123sef', 'Bug')

    assert str(e.value) == 'You must setup a label called "Bug" on Trello'


def test_member_list_ok(mocker):
    mocker.patch(
        'api_v1.services._trello_get',
        return_value=[
            {'id': '63ca9e57ea882503f1188670', 'name': 'Juan'},
            {'id': '63ca9e54f223b403b1d3f32c', 'name': 'Pedro'},
            {'id': '63ca9e5eb1f33e0018c686fd', 'name': 'Teresa'}
        ]
    )

    members = member_list('123sef')

    assert len(members) == 3
