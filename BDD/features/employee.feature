Feature: I can log in to the dashboard

    Scenario Outline:
        Given I am on the main page
        When I click on the register button
        then I input my new "<username>" and "<password>" and select my "<Role>"
        then I should be on a page with the title "<title>"
        then I login with "<username>" and "<password>"
        Then I should be on a new page with the title "<newtitle>"
        then I enter in a "<description>" and an "<amount>"
        Then I should remain on the dashboard page with "<newtitle>" and the number of requests should increase
        Then I cancel a request
        Then I should remain on the dashboard page with "<newtitle>" and the number of requests should decrease
        Examples:
            | username    | password    | description | amount |Role    | title | newtitle |
            | Omar1       | password1   | d1          | 8      | Employee | Login | Dashboard |
            | Omar2     | password2     | d2          | 9      | Employee | Login | Dashboard |
            | Omar3     | password3     | d3          | 10     |Employee| Login | Dashboard |

