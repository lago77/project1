Feature: employees who go to the login page should log in to the employee dashboard

    Scenario: employee clicks on login link
       Given I am on the login page
       When I click on the login link
       Then I should log into the employee dashboard