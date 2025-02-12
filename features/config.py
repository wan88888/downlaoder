# coding=utf-8

# 元素等待超时时间（秒）
DEFAULT_TIMEOUT = 30
SHORT_TIMEOUT = 5

# 重试次数
MAX_RETRY_COUNT = 3
RETRY_INTERVAL = 1  # 重试间隔（秒）

# 元素定位器
BUTTON_LOCATORS = {
    'agree': {
        1: {"resourceId": "btn_agree"},
        2: {"textContains": "I'm"},
        3: {"resourceId": "age_check_yes"},
    },
    'play': {
        1: {"text": ""},
        2: {"text": "Play"},
        3: {"resourceId": 'player'},
        4: {"text": "재생"},
        5: {"resourceId": "kt_player"},
    },
    'close_ad': {
        1: {"text": "Close Ad"},
        2: {"text": "Close Ad ✖"}
    }
}

# 资源ID列表
RESOURCE_IDS = {
    'search': "tvSearch",
    'complete_load': "completeLoadView",
    'normal_load': "normalLoadView",
    'download': "downloadView",
    'title': "tvTitle",
    'top_title': "tvTopTitle",
    'go_home': "ivGoHome",
    'tabs_num': "tvTabsNum2",
    'tabs': "ivTabs2",
    'close': "ivClose",
    'result_1': "result_1"
}