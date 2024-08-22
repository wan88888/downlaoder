# coding=utf-8
import uiautomator2 as u2
import behave2cucumber
import json
import time


def before_all(context):
    context.app_package_name = "free.video.downloader.converter.music"


def before_feature(context, feature):
    # context.feature_name = feature.name
    # if "all1" in context.feature_name:
    #     context.app_package_name = "free.video.downloader.converter.music"
    # elif "all3" in context.feature_name:
    #     context.app_package_name = "video.downloader.videodownloader.tube"
    # else:
    #     print("package not exists!")
    context.driver = u2.connect()
    context.driver.app_start(context.app_package_name)
    context.driver.implicitly_wait(30)
    context.driver.watcher.when(
        f'//*[@resource-id="{context.app_package_name}:id/close_dialog_view"]').click()
    context.driver.watcher.start()


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
