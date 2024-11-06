# coding=utf-8
import uiautomator2 as u2
import behave2cucumber
import json
import time
from time import sleep


def before_all(context):
    context.app_package_name = "free.video.downloader.converter.music"


def app_id(context, element_id):
    return f"{context.app_package_name}:id/{element_id}"


def before_feature(context, feature):
    context.driver = u2.connect()
    context.driver.app_start(context.app_package_name)
    context.driver.implicitly_wait(30)


def after_scenario(context, scenario):
    handle_downloads(context)
    close_extra_tabs(context)


def handle_downloads(context):
    context.driver(resourceId=app_id(context, "ivDownload")).click()
    sleep(2)
    dNum = context.driver(resourceId=app_id(context, "downloading_item_root_view")).count
    if dNum > 5:
        delete_all_downloads(context)
    context.driver.press('back')


def delete_all_downloads(context):
    resource_id_list = ["ivEnableBatchDelete", "ivSelectAll", "ivDeleteAll"]
    [context.driver(resourceId=app_id(context, resource_id)).click() for resource_id in resource_id_list]
    right_actv_button = context.driver(resourceId=app_id(context, "right_actv"))
    right_actv_button.wait()
    right_actv_button.click()


def close_extra_tabs(context):
    num_text = context.driver(resourceId=app_id(context, "tvTabsNum2")).get_text()
    windows_num = int(num_text)
    if windows_num > 1:
        context.driver(resourceId=app_id(context, "ivTabs2")).click()
        close_all_tabs(context, app_id(context, "ivClose"))


def close_all_tabs(context, resource_id):
    while context.driver(resourceId=resource_id).exists:
        context.driver(resourceId=resource_id).click()


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
