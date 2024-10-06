Feature: Check the navigation menu from the home page

  Scenario: User navigates to the homepage and checks navigation links

    Given the user is on the homepage

    When the user clicks on the 'Home' link
    Then the user should be on the homepage

    When the user clicks on the 'About' link
    Then the user should see the about section

    When the user clicks on the 'Skills' link
    Then the user should see the skills section

    When the user clicks on the 'Projects' link
    Then the user should see the projects section

    When the user clicks on the 'Contacts' link
    Then the user should see the contacts sections
