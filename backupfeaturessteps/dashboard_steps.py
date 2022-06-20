from behave import given, when, then
import time

@given(u'I am on the login page')
def step_impl(context):
    print("in the driver")
    context.driver.get("http://127.0.0.1:5000/loginpage")

@when(u'I login with "{username}" and "{password}"')
def step_impl(context, username,password):
    print("title is,",context.driver.title)
    print("the username ",username)
    context.login.login(username,password)
    print(username)
    print(password)
    
    # print("my new context var ",context.element)


@then(u'I should be on a page with the title "{title}"')
def step_impl(context, title):
    time.sleep(2)
    # context.element=context.element+1
    # print("my last context var ",context.element)
    num=context.login.element_count()
    num=num/2
    print("number of elements is ", num)
    print("my title",title)
    print("driver title ",context.driver.title)
    context.num=num
    assert context.driver.title == title


@when(u'I enter in a "{description}" and an "{amount}"')
def step_impl(context, description,amount):
    # print("title is,",context.driver.title)
    # print("the username ",username)
    context.dashboard.insert_request(description, amount)
    # print(username)
    # print(password)
    print("num: ",context.num)
    print("my description ",description)
    print("my amount", amount)
    print("2")

@then(u'I should remain on the dashboard page with "{title}" and the number of requests should increase')
def step_impl(context, title):
    time.sleep(2)
    print("title is")
    print(context.driver.title)
    newnum=context.login.element_count()
    newnum=newnum/2
    print("contextnum ", context.num)
    print("new num ", newnum)

    # print("number of elements is ", num)
    # print("my title",title)
    # print("driver title ",context.driver.title)
    # assert context.driver.title == title
    print((newnum>context.num))
    assert (newnum>context.num) == True
    print("3")

# Feature: I am making a request on the dashboard

#     Scenario Outline:
#         Given I am on the dashboard page
#         When I enter in a "<description>" and an "<amount>"
#         Then I should remain on the dashboard page with "<title>" and the number of requests should increase

#         Examples:
#             | description    | amount     | title     |
#             | Description1       | 100     | Dashboard |
#             | Description 2       | 6     | Dashboard |
#             | Description3    | 99      | Dashboard |

