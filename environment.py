import os
import allure
from allure_commons.types import AttachmentType


def before_scenario(context, scenario):
    # Create a new Allure test case
    testcase = allure.dynamic.title(scenario.name)

    # Add Allure labels for test case
    allure.dynamic.feature(scenario.feature.name)
    allure.dynamic.story(scenario.feature.description)
    allure.dynamic.label("severity", "normal")


def after_step(context, step):
    # Attach screenshot to Allure report on test failure
    if step.status == "failed":
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name="Screenshot",
            attachment_type=AttachmentType.PNG
        )


def after_scenario(context, scenario):
    # Add Allure description for test case
    allure.dynamic.description(scenario.description)

    # Add Allure links for test case
    if hasattr(scenario, "testcase_links"):
        for link in scenario.testcase_links:
            allure.dynamic.link(link.url, link.title)

    # Add Allure environment information
    allure.dynamic.environment(
        name="Browser",
        value=context.browser_name
    )


def after_all(context):
    # Generate Allure report
    os.system("allure generate allure-results --clean -o allure-report")
