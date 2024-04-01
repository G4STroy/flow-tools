from behave import given, when, then, use_step_matcher
from app import app

use_step_matcher("re")

@given("the application is running")
def step_impl(context):
    context.client = app.test_client()
    context.response = None

@when("the user requests the template download")
def step_impl(context):
    context.response = context.client.get('/download-template')

@then("the Excel template should be downloaded successfully")
def step_impl(context):
    assert context.response.status_code == 200
    assert 'attachment' in context.response.headers.get('Content-Disposition', '')