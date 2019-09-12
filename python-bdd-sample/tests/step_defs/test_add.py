import pytest
from AddModule.add import func
from pytest_bdd import scenarios, given, when, then, parsers

# Constants
# Scenarios

scenarios('../features/add.feature')

# Fixtures
# Given Steps

results = 0

@when(parsers.parse('the user input {input:d}'))
def user_input(input):
    global results
    results = func(5)

# Then Steps

@then(parsers.parse('results is {expected_results:d}'))
def search_results(expected_results):
    assert expected_results == results
