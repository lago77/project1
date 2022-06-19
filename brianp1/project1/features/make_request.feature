Feature: after logging in as employee I should be able to make or check current requests

    Scenario: employee is on dashboard and makes requests
        Given employee is on dashboard
        When employee makes a requests
        Then employee should see new request pending