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


@then(u'I login with "{username}" and "{password}"')
def step_impl(context, username,password):
    print("title is,",context.driver.title)
    print("the username ",username)
    context.login.login(username,password)
    print(username)
    print(password)
    
    # print("my new context var ",context.element)


@then(u'I should be on a new page with the title "{newtitle}"')
def step_impl(context, newtitle):
    time.sleep(2)

    # print("my last context var ",context.element)
    num=context.login.element_count()
    num=num/2
    context.num=num
    print("number of elements is ", num)
    print("my title",newtitle)
    print("driver title ",context.driver.title)
    assert context.driver.title == newtitle


@then(u'I enter in a "{description}" and an "{amount}"')
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

@then(u'I should remain on the dashboard page with "{newtitle}" and the number of requests should increase')
def step_impl(context, newtitle):
    time.sleep(2)
    print("title is")
    print(context.driver.title)
    newnum=context.login.element_count()
    newnum=newnum/2

    print("contextnum ", context.num)
    print("new num ", newnum)
    print((context.num<newnum))
    assert (context.num<newnum) == True
@then(u'I cancel a request')
def step_impl(context):
    time.sleep(2)
    print("title is")
    print(context.driver.title)
    context.dashboard.cancel()
    num=context.login.element_count()
    num=num/2
    context.num=num
    print("contextnum ", context.num)
    print("new num ", num)

@then(u'I should remain on the dashboard page with "{newtitle}" and the number of requests should decrease')
def step_impl(context, newtitle):
    time.sleep(2)
    print("title is")
    print(context.driver.title)
    newnum=context.login.element_count()
    newnum=newnum/2

    print("contextnum ", context.num)
    print("new num ", newnum)
