# coding=utf-8
from time import sleep
from behave import *
from features.environment import *


def search_test(context, word, sec, **locator_args):
    wait_and_click(context, **locator_args)
    context.driver.send_keys(word, clear=True)
    context.driver.press('enter')
    sleep(sec)


@step('用户在首页搜索框输入"{word}"')
def step_impl(context, word):
    search_test(context, word, 10, resourceId=app_id(context, "tvSearch"))


@step("用户应该看到悬浮按钮")
def step_impl(context):
    check_element_exists(context, "normalLoadView")


@step("用户应该看到悬浮按钮亮起")
def step_impl(context):
    check_element_exists(context, "completeLoadView")
    sleep(1)


@step("用户点击悬浮下载按钮")
def step_impl(context):
    count_text = app_action(context, "remindCountView", "get_text")
    download_num = int(count_text)
    app_action(context, "completeLoadView")
    sleep(2)
    download_button = get_element(context, "downloadView")
    tv_list = get_element(context, "tvVideoList")
    if download_num > 1 or tv_list.exists:
        download_button.click()


@step("用户应该看到下载进度页")
def step_impl(context):
    check_element_exists(context, "tvTitle")


@step("用户检查下载页存在")
def step_impl(context):
    click_exists2(context, locator1={"resourceId": app_id(context, "completeLoadView")},
                  locator2={"resourceId": app_id(context, "ivDownload")})


@step("用户点击底部工具栏主页按钮")
def step_impl(context):
    wait_and_click1(context, "ivGoHome")


@step("用户应该看到主页")
def step_impl(context):
    check_element_exists(context, "tvTopTitle")
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
    click_exists1(context, **button_conditions.get(int(option), {}))


@step("用户在当前页面点击播放按钮{item}")
def step_impl(context, item):
    buttons = {
        1: {"text": ""},
        2: {"text": "Play"},
        3: {"resourceId": 'movie_player'},
        4: {"text": "재생"},
    }
    button_locator = buttons.get(int(item))
    wait_and_click(context, **button_locator)


@step('用户在搜索框输入"{txt}"')
def step_impl(context, txt):
    search_test(context, txt, 5, text="Search")


@step("用户在当前点击结果1")
def step_impl(context):
    wait_and_click(context, resourceId="result_1")


@step("用户在当前页面点击关闭广告按钮")
def step_impl(context):
    click_exists1(context, text="Close Ad ✖")
    sleep(2)


@step("用户检查工具栏窗口")
def step_impl(context):
    sleep(2)
    num_text = app_action(context, "tvTabsNum2", "get_text")
    windows_num = int(num_text)
    if windows_num > 1:
        app_action(context, "ivTabs2")
        sleep(2)
        iv_close = get_element(context, "ivClose")
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


@step("用户在当前页面点击播放按钮")
def step_impl(context):
    wait_and_click(context, text="")
    sleep(2)
    click_exists2(context, locator1={"resourceId": app_id(context, "normalLoadView")},
                  locator2={"text": ""})
