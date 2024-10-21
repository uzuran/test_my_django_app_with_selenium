Feature: Check the navigation menu from the home page
  Background:
    Given the user is on the homepage

  @smoke
  Scenario: User navigates to the homepage
    When the user clicks on the 'Home' link
    Then the user should be on the homepage

  @smoke
  Scenario: User navigate to the about section
    When the user clicks on the 'About' link
    Then the user should see the about section

  Scenario: User navigate to the skill section
    When the user clicks on the 'Skills' link
    Then the user should see the skills section

  Scenario: User navigate to the projects section
    When the user clicks on the 'Projects' link
    Then the user should see the projects section

  Scenario: User navigate to the contacts section
    When the user clicks on the 'Contacts' link
    Then the user should see the contacts sections
