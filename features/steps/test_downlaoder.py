# coding=utf-8
from time import sleep
from behave import *
from features.environment import app_id


@step('用户在首页搜索框输入"{word}"')
def step_impl(context, word):
    search_input = context.driver(resourceId=app_id(context, "tvSearch"))
    search_input.wait()
    search_input.click()
    context.driver.send_keys(word, clear=True)
    context.driver.press('enter')
    sleep(10)


@step("用户应该看到悬浮按钮")
def step_impl(context):
    normal_load = context.driver(resourceId=app_id(context, "normalLoadView"))
    normal_load.wait()
    assert normal_load.exists


@step("用户应该看到悬浮按钮亮起")
def step_impl(context):
    complete_load = context.driver(resourceId=app_id(context, "completeLoadView"))
    complete_load.wait()
    assert complete_load.exists
    sleep(1)


@step("用户点击悬浮下载按钮")
def step_impl(context):
    count_text = context.driver(resourceId=app_id(context, "remindCountView")).get_text()
    download_num = int(count_text)
    complete_load = context.driver(resourceId=app_id(context, "completeLoadView"))
    complete_load.click()
    sleep(2)
    download_button = context.driver(resourceId=app_id(context, "downloadView"))
    tv_list = context.driver(resourceId=app_id(context, "tvVideoList"))
    if download_num > 1 or tv_list.exists:
        download_button.click()


@step("用户应该看到下载进度页")
def step_impl(context):
    tv_title = context.driver(resourceId=app_id(context, "tvTitle"))
    tv_title.wait()
    assert tv_title.exists


@step("用户检查下载页存在")
def step_impl(context):
    complete_load = context.driver(resourceId=app_id(context, "completeLoadView"))
    iv_load = context.driver(resourceId=app_id(context, "ivDownload"))
    if complete_load.exists:
        iv_load.click()


@step("用户点击底部工具栏主页按钮")
def step_impl(context):
    iv_home = context.driver(resourceId=app_id(context, "ivGoHome"))
    iv_home.wait()
    iv_home.click()


@step("用户应该看到主页")
def step_impl(context):
    tv_top_title = context.driver(resourceId=app_id(context, "tvTopTitle"))
    tv_top_title.wait()
    assert tv_top_title.exists
    sleep(1)


@step("用户在当前页面点击坐标({x},{y})")
def step_impl(context, x, y):
    context.driver.click(float(x), float(y))
    sleep(4)


@step("用户点击同意按钮{option}")
def step_impl(context, option):
    button_conditions = {
        1: {"textContains": "Enter"},
        2: {"textContains": "I'm"},
        3: {"resourceId": "age_check_yes"},
    }
    wait_and_click(context, **button_conditions.get(int(option), {}))


def wait_and_click(context, **locator_args):
    element = context.driver(**locator_args)
    if element.wait():
        element.click()


@step("用户在当前页面点击播放按钮{item}")
def step_impl(context, item):
    buttons = {
        1: {"text": ""},
        2: {"text": "Play"},
        3: {"xpath": '//*[@resource-id="videoPopup"]/android.view.View[1]/android.widget.ToggleButton[1]'},
        4: {"text": "재생"},
    }
    button_locator = buttons.get(int(item))
    if button_locator:
        wait_and_click(context, **button_locator)


@step('用户在搜索框输入"{txt}"')
def step_impl(context, txt):
    search_icon = context.driver(text="Search")
    search_icon.wait()
    search_icon.click()
    context.driver.send_keys(txt, clear=True)
    context.driver.press('enter')
    sleep(5)


@step("用户在当前点击结果1")
def step_impl(context):
    result_1 = context.driver(resourceId="result_1")
    result_1.wait()
    result_1.click()


@step("用户在当前页面点击关闭广告按钮")
def step_impl(context):
    ad_close = context.driver(text="Close Ad ✖")
    if ad_close.exists:
        ad_close.click()
    sleep(2)


@step("用户检查工具栏窗口")
def step_impl(context):
    sleep(2)
    tv_tab = context.driver(resourceId=app_id(context, "tvTabsNum2"))
    num_text = tv_tab.get_text()
    windows_num = int(num_text)
    if windows_num > 1:
        iv_tab = context.driver(resourceId=app_id(context, "ivTabs2"))
        iv_tab.click()
        sleep(2)
        iv_close = context.driver(resourceId=app_id(context, "ivClose"))
        iv_close[0].click()
        context.driver.press('back')
        sleep(1)


@step("用户点击返回键")
def step_impl(context):
    context.driver.press('back')
    sleep(1)


@step("用户向上滑动页面{x}次")
def step_impl(context, x):
    [context.driver.swipe_ext("up") for _ in range(int(x))]
