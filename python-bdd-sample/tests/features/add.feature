Feature: Add function
  As a user,
  I want to have an add function
  So it will add 1 to the input value

  # The "@" annotations are tags
  # One feature can have multiple scenarios
  # The lines immediately after the feature title are just comments

  Scenario: Basic add one function
    When the user input 5
    Then results is 6