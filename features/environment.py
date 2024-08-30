# coding=utf-8
import uiautomator2 as u2
import behave2cucumber
import json
import time


def before_all(context):
    context.app_package_name = "free.video.downloader.converter.music"


def before_feature(context, feature):
    context.driver = u2.connect()
    context.driver.app_start(context.app_package_name)
    context.driver.implicitly_wait(30)
    context.driver.watcher.when(f'//*[@resource-id="{context.app_package_name}:id/rating_bar"]').press('back')
    context.driver.watcher.start()


def after_scenario(context, scenario):
    context.driver(resourceId=f"{context.app_package_name}:id/ivDownload").click()
    context.driver(resourceId=f"{context.app_package_name}:id/ivEnableBatchDelete").click()
    context.driver(resourceId=f"{context.app_package_name}:id/ivSelectAll").click()
    context.driver(resourceId=f"{context.app_package_name}:id/ivDeleteAll").click()
    context.driver(resourceId=f"{context.app_package_name}:id/right_actv").click()
    context.driver(resourceId=f"{context.app_package_name}:id/ivBack").click()
    context.driver(resourceId=f"{context.app_package_name}:id/tvTabsNum2").wait()
    num_text = context.driver(resourceId=f"{context.app_package_name}:id/tvTabsNum2").get_text()
    windows_num = int(num_text)
    if windows_num > 1:
        context.driver(resourceId=f"{context.app_package_name}:id/ivTabs2").click()
        context.driver(resourceId=f"{context.app_package_name}:id/ivClose").wait()
        i = context.driver(resourceId=f"{context.app_package_name}:id/ivClose").count
        while i > 0:
            context.driver(resourceId=f"{context.app_package_name}:id/ivClose").click()
            time.sleep(1)
            i -= 1


def after_step(context, step):
    if step.status == 'failed':
        step_name = step.name.replace(" ", "_")
        timestamp = time.strftime('%Y%m%d%H%M%S')
        screenshot_path = f'screenshots/{step_name}_{timestamp}.png'
        context.driver.screenshot(screenshot_path)


def after_feature(context, feature):
    context.driver.watcher.stop()
    context.driver.app_stop(context.app_package_name)


def after_all(context):
    with open(r'/Users/wan/PycharmProjects/Downloader/test_report.json', encoding='utf-8') as behave_json:
        cucumberJson = behave2cucumber.convert(json.load(behave_json))
    jsonStr = json.dumps(cucumberJson)
    jsonReport = open(r'/Users/wan/PycharmProjects/Downloader/report/json_report.json', 'w', encoding='utf-8')
    jsonReport.write(jsonStr)
    jsonReport.close()


if __name__ == '__main__':
    after_all(None)
