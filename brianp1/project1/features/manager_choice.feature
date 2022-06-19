Feature: Managers should be able to check current requests and accept or deny them

     Scenario: when managers are on the dashboard all employee requests should be available to decide on
             Given manager is on manager dashboard
             When I click on requests
             When I click a request
             Then I should be able to accept or deny request