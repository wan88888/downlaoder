# coding=utf-8
from time import sleep
from behave import *


@step('用户在首页搜索框输入"{word}"')
def step_impl(context, word):
    context.driver(resourceId=f"{context.app_package_name}:id/tvSearch").click()
    context.driver.send_keys(word, clear=True)
    context.driver.press('enter')
    sleep(10)


@step("用户应该看到悬浮按钮")
def step_impl(context):
    context.driver(resourceId=f"{context.app_package_name}:id/normalLoadView").wait()
    assert context.driver.exists(resourceId=f"{context.app_package_name}:id/normalLoadView")


@step("用户应该看到悬浮按钮亮起")
def step_impl(context):
    context.driver(resourceId=f"{context.app_package_name}:id/completeLoadView").wait()
    assert context.driver.exists(resourceId=f"{context.app_package_name}:id/completeLoadView")
    sleep(2)


@step("用户在当前页面点击悬浮下载按钮")
def step_impl(context):
    context.driver(resourceId=f"{context.app_package_name}:id/completeLoadView").click()
    sleep(2)


@step("用户应该看到下载进度页")
def step_impl(context):
    context.driver(resourceId=f"{context.app_package_name}:id/tvTitle").wait()
    assert context.driver.exists(resourceId=f"{context.app_package_name}:id/tvTitle")


@step("用户在下载进度页点击关闭按钮")
def step_impl(context):
    context.driver(resourceId=f"{context.app_package_name}:id/ivClose").click()
    sleep(2)


@step("用户点击底部工具栏主页按钮")
def step_impl(context):
    context.driver(resourceId=f"{context.app_package_name}:id/ivGoHome").wait()
    context.driver(resourceId=f"{context.app_package_name}:id/ivGoHome").click()


@step("用户应该看到主页")
def step_impl(context):
    context.driver(resourceId=f"{context.app_package_name}:id/tvTopTitle").wait()
    assert context.driver.exists(resourceId=f"{context.app_package_name}:id/tvTopTitle")
    sleep(2)


@step("用户用户应该看到下载列表")
def step_impl(context):
    context.driver(resourceId=f"{context.app_package_name}:id/downloadView").wait()
    assert context.driver.exists(resourceId=f"{context.app_package_name}:id/downloadView")


@step("用户在下载列表点击Download按钮")
def step_impl(context):
    context.driver(resourceId=f"{context.app_package_name}:id/downloadView").click()
    sleep(2)


@step("用户在当前页面点击坐标({x},{y})")
def step_impl(context, x, y):
    context.driver.click(float(x), float(y))
    sleep(5)


@step("用户点击同意按钮{option}")
def step_impl(context, option):
    match int(option):
        case 1:
            if context.driver(textContains="En").exists():
                context.driver.click(0.5, 0.69)
        case 2:
            if context.driver(textContains="I'm").exists():
                context.driver.click(0.5, 0.78)
        case 3:
            if context.driver(resourceId="age_check_yes").exists():
                context.driver(resourceId="age_check_yes").click()
        case 4:
            if context.driver(resourceId="btn_agree").exists():
                context.driver(resourceId="btn_agree").click()


@step("用户向上滑动")
def step_impl(context):
    context.driver.swipe_ext('up')
    sleep(2)


@step("用户在首页点击dailymotion图标")
def step_impl(context):
    context.driver(text="Dailymotion").wait()
    context.driver(text="Dailymotion").click()
    sleep(8)


@step("用户点击底部工具栏窗口按钮")
def step_impl(context):
    context.driver(resourceId=f"{context.app_package_name}:id/ivTabs2").click()
    sleep(2)


@step("用户点击第1个窗口的关闭按钮")
def step_impl(context):
    context.driver(resourceId=f"{context.app_package_name}:id/ivClose").wait()
    context.driver(resourceId=f"{context.app_package_name}:id/ivClose")[0].click()


@step("用户点击空白位置")
def step_impl(context):
    context.driver(resourceId=f"{context.app_package_name}:id/coordinator").click()
    sleep(2)


@step("用户在下载列表点击第1个下载按钮")
def step_impl(context):
    context.driver(resourceId=f"{context.app_package_name}:id/downloadView").wait()
    context.driver(resourceId=f"{context.app_package_name}:id/downloadView")[0].click()
    sleep(2)


@step("用户在当前页面点击播放按钮{item}")
def step_impl(context, item):
    match int(item):
        case 1:
            context.driver(text="").wait()
            context.driver(text="").click()
        case 2:
            context.driver(text="Play").wait()
            context.driver(text="Play").click()
        case 3:
            context.driver.xpath(
                '//*[@resource-id="videoPopup"]/android.view.View[1]/android.widget.ToggleButton[1]').wait()
            context.driver.xpath(
                '//*[@resource-id="videoPopup"]/android.view.View[1]/android.widget.ToggleButton[1]').click()


@step('用户在搜索框输入"{txt}"')
def step_impl(context, txt):
    context.driver(text="Search").wait()
    context.driver(text="Search").click()
    context.driver.send_keys(txt, clear=True)
    context.driver.press('enter')
    sleep(5)


@step("用户在当前点击第1条结果")
def step_impl(context):
    context.driver(resourceId="result_1").wait()
    context.driver(resourceId="result_1").click()


@step("用户在当前页面点击关闭广告按钮")
def step_impl(context):
    if context.driver(resourceId="Close Ad ✖").exists():
        context.driver(text="Close Ad ✖").click()
    sleep(2)