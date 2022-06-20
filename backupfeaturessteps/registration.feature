Feature: I can log in to the dashboard

    Scenario Outline:
        Given I am on the main page
        When I click on the register button
        then I input my new "<username>" and "<password>" and select my "<Role>"
        Then I should be on a page with the title "<title>"

        Examples:
            | username    | password     | Role    | title |
            | Omar1       | password1   | Employee | Login |
            | Omar2     | password2   | Manager    | Login |
            | Omar3     | password3      | Employee| Login |

