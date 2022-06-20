Feature: I can log in to the dashboard

    Scenario Outline:
        Given I am on the main page
        When I click on the register button
        then I input my new "<username>" and "<password>" and select my "<Role>"
        then I should be on a page with the title "<title>"
        then I login with "<username>" and "<password>"
        Then I should be on a new page with the title "<newtitle>"
        Then I approve a request
        Then I should remain on the dashboard page with "<newtitle>" and the new status is  "<status>"
        Examples:
            | username    | password    | description | amount |Role    | title | newtitle | status |
            | Omarfsdf       | password1   | d1          | 8      | Manager | Login | Dashboard | approve |
            | Marko  | password2     | d2          | 9      | Manager | Login | Dashboard | approve |
            | omar    | password3     | d3          | 10     | Manager| Login | Dashboard | approve |

