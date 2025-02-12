# coding=utf-8
from behave import *
from features.environment import *
from features.config import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from functools import wraps
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def retry_on_exception(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for attempt in range(MAX_RETRY_COUNT):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if attempt < MAX_RETRY_COUNT - 1:
                    logger.warning(f"{func.__name__} 执行失败，正在重试 {attempt + 1}/{MAX_RETRY_COUNT}")
                    time.sleep(RETRY_INTERVAL)
                else:
                    logger.error(f"{func.__name__} 执行失败: {str(e)}")
                    raise
    return wrapper


@retry_on_exception
def wait_for_element(context, timeout=DEFAULT_TIMEOUT, **locator_args):
    logger.info(f"等待元素出现: {locator_args}")
    element = context.driver(**locator_args)
    WebDriverWait(context.driver, timeout).until(
        lambda x: element.exists
    )
    return element


def search_test(context, word, **locator_args):
    element = wait_for_element(context, **locator_args)
    element.click()
    context.driver.send_keys(word, clear=True)
    context.driver.press('enter')
    wait_for_element(context, resourceId=app_id(context, "completeLoadView"))


@step('用户在首页搜索框输入"{word}"')
def step_impl(context, word):
    search_test(context, resourceId=app_id(context, "tvSearch"), word=word)


@step("用户应该看到悬浮按钮")
def step_impl(context):
    check_element_exists(context, "normalLoadView")


@step("用户应该看到悬浮按钮亮起")
def step_impl(context):
    wait_for_element(context, resourceId=app_id(context, "completeLoadView"))


@step("用户点击悬浮下载按钮")
def step_impl(context):
    wait_for_element(context, resourceId=app_id(context, "completeLoadView")).click()
    wait_for_element(context, resourceId=app_id(context, "downloadView")).click()


@step("用户应该看到下载进度页")
def step_impl(context):
    check_element_exists(context, "tvTitle")


@step("用户点击底部工具栏主页按钮")
def step_impl(context):
    wait_and_click1(context, "ivGoHome")


@step("用户应该看到主页")
def step_impl(context):
    check_element_exists(context, "tvTopTitle")


@step("用户在当前页面点击坐标({x},{y})")
def step_impl(context, x, y):
    context.driver.click(float(x), float(y))
    wait_for_element(context, resourceId=app_id(context, "completeLoadView"))


@step("用户点击同意按钮{option}")
def step_impl(context, option):
    button_locator = BUTTON_LOCATORS['agree'].get(int(option))
    click_exists1(context, **button_locator)


@step("用户在当前页面点击播放按钮{item}")
def step_impl(context, item):
    button_locator = BUTTON_LOCATORS['play'].get(int(item))
    wait_and_click(context, **button_locator)


@step("用户在当前页面点击关闭广告2")
def step_impl(context):
    click_exists1(context, **BUTTON_LOCATORS['close_ad'][2])


@step("用户在当前页面点击关闭广告1")
def step_impl(context):
    click_exists1(context, **BUTTON_LOCATORS['close_ad'][1])


@step('用户在搜索框输入"{txt}"')
def step_impl(context, txt):
    search_test(context, txt, text="Search")


@step("用户在当前点击结果1")
def step_impl(context):
    wait_and_click(context, resourceId="result_1")
    wait_for_element(context, resourceId=app_id(context, "completeLoadView"))


@step("用户在当前页面点击关闭广告2")
def step_impl(context):
    click_exists1(context, text="Close Ad ✖")


@step("用户在当前页面点击关闭广告1")
def step_impl(context):
    click_exists1(context, text="Close Ad")


@step("用户检查工具栏窗口")
def step_impl(context):
    try:
        windows_num = get_ele_text(context, "tvTabsNum2")
        if windows_num > 1:
            app_action(context, "ivTabs2")
            wait_for_element(context, resourceId=app_id(context, "ivClose"))
            iv_close = get_element(context, "ivClose")
            iv_close[0].click()
            context.driver.press('back')
            wait_for_element(context, resourceId=app_id(context, "completeLoadView"))
    except Exception as e:
        print(f"检查工具栏窗口时发生错误: {e}")


@step("用户点击返回键")
def step_impl(context):
    context.driver.press('back')
    try:
        wait_for_element(context, timeout=5, resourceId=app_id(context, "completeLoadView"))
    except Exception:
        pass


@step("用户向上滑动页面{x}次")
def step_impl(context, x):
    [context.driver.swipe_ext("up") for _ in range(int(x))]


@step("用户在当前页面点击播放按钮")
def step_impl(context):
    wait_and_click(context, text="")
    sleep(2)
    click_exists2(context, locator1={"resourceId": app_id(context, "normalLoadView")},
                  locator2={"text": ""})
