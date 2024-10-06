Feature: User Navigation on Homepage

  Scenario: Navigate to the Homepage
    Given the user is on the homepage
    When the user clicks on the "Home" link
    Then the user should be on the homepage
