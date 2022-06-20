from behave import given, when, then
import time
@given(u'I am on the main page')
def step_impl(context):
    print("in the driver")
    context.driver.get("http://127.0.0.1:5000")

@when(u'I click on the register button')
def step_impl(context):
    print("title is,",context.driver.title)
    # print("the username ",username)
    # context.registration.Register(username,password)
    # print(username)
    # print(password)
    context.registration.go_register()
    # print("my new context var ",context.element)
    print("in the when")
@then(u'I input my new "{username}" and "{password}" and select my "{Role}"')
def step_impl(context, username,password,Role):
    print("title is,",context.driver.title)
    print("the username ",username)
    context.registration.Register(username,password)
    print(username)
    print(password)
    assert context.driver.title =
    # print("my new context var ",context.element)


@then(u'I should be on a page with the title "{title}"')
def step_impl(context, title):
    time.sleep(2)
    # context.element=context.element+1
    # print("my last context var ",context.element)
    # num=context.login.element_count()
    # num=num/2
    # print("number of elements is ", num)
    print("my title",title)
    print("driver title ",context.driver.title)
    assert context.driver.title == title
