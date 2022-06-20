Feature: I am making a request on the dashboard

    Scenario Outline:
        Given I am on the login page
        When I login with "<username>" and "<password>"
        Then I should be on a page with the title "<title>"
        When I enter in a "<description>" and an "<amount>"
        Then I should remain on the dashboard page with "<title>" and the number of requests should increase

        Examples:
            | username    | password  | title     | description  | amount | title |
            | Omar        |passo      | Dashboard | Description1 | 100    | Dashboard |
            | Marko       | fsdf      | Dashboard | Description2 |999     | Dashboard |
            | Anthony     | dsf       | Dashboard | Description3 |777     | Dashboard |
