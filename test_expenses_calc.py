import pytest
import expenses_calculator


def almost_equal(x, y, threshold=0.01):
    return abs(x - y) < threshold


def dict_almost_equal(d1, d2):
    return all(almost_equal(d1[k], d2[k]) for k in d1)


def test_split_bills_one_item():
    contribution = {
        "Ciara": 80.61,
        'Gordon': 0.0,
        'Nina': 0.0,
        'Eunice': 0.0
    }
    involvement = {
        "Ciara": True,
        'Gordon': True,
        'Nina': True,
        'Eunice': True
    }
    balance = {
        "Ciara": 0.0,
        'Gordon': 0.0,
        'Nina': 0.0,
        'Eunice': 0.0
    }
    assert expenses_calculator.split_bills(contribution, involvement, balance) == {'Ciara': 20.1525 - 80.61,
                                                                                   'Gordon': 20.1525, 'Nina': 20.1525,
                                                                                   'Eunice': 20.1525}


def test_split_bills_two_items():
    contributions = [{
        "Ciara": 80.61,
        'Gordon': 0.0,
        'Nina': 0.0,
        'Eunice': 0.0
    }, {
        "Ciara": 0.0,
        'Gordon': 0.0,
        'Nina': 0.0,
        'Eunice': 46.86
    }]

    involvements = [{
        "Ciara": True,
        'Gordon': True,
        'Nina': True,
        'Eunice': True
    }, {
        "Ciara": True,
        'Gordon': True,
        'Nina': True,
        'Eunice': True
    }]
    balance = {
        "Ciara": 0.0,
        'Gordon': 0.0,
        'Nina': 0.0,
        'Eunice': 0.0
    }

    for contribution, involvement in zip(contributions, involvements):
        balance = expenses_calculator.split_bills(contribution, involvement, balance)

    assert dict_almost_equal(balance, {'Ciara': 31.8675 - 80.61,
                                       'Gordon': 31.8675,
                                       'Nina': 31.8675,
                                       'Eunice': 31.8675 - 46.86})


def test_split_bills_all():
    contributions = [{
        "Ciara": 80.61}, {
        'Eunice': 46.86
    }, {
        'Gordon': 71.75,
        'Nina': 71.75,

    }, {
        'Eunice': 17.64
    }, {
        'Eunice': 8.0
    }, {
        'Eunice': 18.45
    }, {
        'Gordon': 6.55,

    }]

    involvements = [{    }, {
         }, {
        }, {
        "Ciara": False,
    }, {
    }, {
    }, {
    }]
    balance = {
        "Ciara": 0.0,
        'Gordon': 0.0,
        'Nina': 0.0,
        'Eunice': 0.0
    }

    for contribution, involvement in zip(contributions, involvements):
        balance = expenses_calculator.split_bills(contribution, involvement, balance)

    assert dict_almost_equal(balance, {'Ciara': -4.62,
                                       'Gordon': 3.57,
                                       'Nina': 10.12,
                                       'Eunice': -9.08})
