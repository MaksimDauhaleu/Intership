# Created by maksimdauhaleu at 12/22/23
Feature: The user can click on “Connect the company” on the left side of the main page

Scenario: Click on “Connect the company”
    Given Open main page
    Then Log in to the page
    Then Click on “Connect the company”
    Given Store original window
    Then Switch the new tab
    Then Verify the right tab opens