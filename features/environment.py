# coding=utf-8
import uiautomator2 as u2
import behave2cucumber
import json
import random
import time


def before_all(context):
    context.app_package_name = "free.video.downloader.converter.music"


def app_id(context, element_id):
    return f"{context.app_package_name}:id/{element_id}"


def get_element(context, element_id):
    return context.driver(resourceId=app_id(context, element_id))


def check_element_exists(context, element_id):
    element = get_element(context, element_id)
    element.wait()
    assert element.exists


def app_action(context, element_id, action="click"):
    element = get_element(context, element_id)
    actions = {
        "click": element.click,
        "wait": element.wait,
        "get_text": element.get_text
    }
    return actions[action]()


def click_exists1(context, **locator_args):
    element = context.driver(**locator_args)
    if element.exists:
        element.click()


def click_exists2(context, locator1, locator2):
    element1 = context.driver(**locator1)
    element2 = context.driver(**locator2)
    if element1.exists:
        element2.click()


def wait_and_click(context, **locator_args):
    element = context.driver(**locator_args)
    element.wait()
    element.click()


def wait_and_click1(context, element_id):
    element = get_element(context, element_id)
    element.wait()
    element.click()


def before_feature(context, feature):
    context.driver = u2.connect()
    context.driver.app_start(context.app_package_name)
    context.driver.implicitly_wait(30)


def after_scenario(context, scenario):
    random_number = random.randint(1, 5)
    if random_number == 3:
        handle_downloads(context)
        close_extra_tabs(context)


def handle_downloads(context):
    app_action(context, "ivDownload")
    delete_all_downloads(context)
    context.driver.press('back')


def delete_all_downloads(context):
    resource_id_list = ["ivEnableBatchDelete", "ivSelectAll", "ivDeleteAll"]
    [app_action(context, resource_id) for resource_id in resource_id_list]
    wait_and_click1(context, "right_actv")


def close_extra_tabs(context):
    num_text = app_action(context, "tvTabsNum2", "get_text")
    windows_num = int(num_text)
    if windows_num > 1:
        app_action(context, "ivTabs2")
        iv_close = get_element(context, "ivClose")
        while iv_close.exists:
            iv_close.click()


def after_step(context, step):
    if step.status == 'failed':
        save_screenshot(context, step)


def save_screenshot(context, step):
    timestamp = time.strftime('%Y%m%d%H%M%S')
    step_name = step.name.replace(" ", "_")
    screenshot_path = f'screenshots/{step_name}_{timestamp}.png'
    context.driver.screenshot(screenshot_path)


def after_feature(context, feature):
    context.driver.app_stop(context.app_package_name)


def after_all(context):
    input_path = r'/Users/wan/PycharmProjects/Downloader/test_report.json'
    output_path = r'/Users/wan/PycharmProjects/Downloader/report/json_report.json'
    with open(input_path, encoding='utf-8') as behave_json:
        cucumberJson = behave2cucumber.convert(json.load(behave_json))
    jsonStr = json.dumps(cucumberJson)
    with open(output_path, 'w', encoding='utf-8') as jsonReport:
        jsonReport.write(jsonStr)


if __name__ == '__main__':
    after_all(None)
