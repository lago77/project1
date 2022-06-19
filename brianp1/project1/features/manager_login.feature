Feature: managers who go to the login page should log in to the managers dashboard

    Scenario: manager clicks on login link 
       Given I am on the login page
       When I click on the login link
       Then I should log into the managers dashboard