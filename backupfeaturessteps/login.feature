Feature: I can log in to the dashboard

    Scenario Outline:
        Given I am on the login page
        When I login with "<username>" and "<password>"
        Then I should be on a page with the title "<title>"

        Examples:
            | username    | password     | title     |
            | Omar        |passo      | Dashboard |
            | Marko       | fsdf      | Dashboard |
            | Anthony     | dsf       | Dashboard |



