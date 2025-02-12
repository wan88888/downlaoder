# Downloader 自动化测试项目

## 项目概述
这是一个基于Behave框架的自动化测试项目，用于测试Downloader应用的各项功能。项目使用Python编写，采用BDD（行为驱动开发）方法论，通过特性文件（feature files）描述测试场景，并使用步骤定义文件实现具体的测试步骤。

## 项目结构
```
- features/                # 测试特性文件目录
  - config.py             # 配置文件
  - environment.py        # 环境设置文件
  - steps/                # 步骤定义目录
    - test_downloader.py  # 测试步骤实现
  - *.feature            # 测试场景描述文件
- report/                 # 测试报告目录
- screenshots/            # 测试截图目录
```

## 环境要求
- Python 3.x
- Behave - BDD测试框架
- Selenium - Web自动化测试工具
- Appium - 移动应用自动化测试框架
- Android设备或模拟器
- behave2cucumber - Behave测试报告转换工具
- uiautomator2 - Android UI自动化测试库

### 依赖安装
```bash
pip install behave behave2cucumber uiautomator2
```

各依赖包说明：
- behave：Python的BDD测试框架，用于编写和运行行为驱动测试
- behave2cucumber：将Behave测试报告转换为Cucumber格式，便于结果展示和分析
- uiautomator2：提供Android设备UI自动化操作的Python封装库
```

## 测试场景
项目包含多个测试场景，涵盖了以下功能：
1. 搜索功能测试
2. 下载功能测试
3. 广告关闭功能测试
4. 导航功能测试
5. 页面滚动测试

## 主要功能模块

### 1. 重试机制
项目实现了自动重试机制，通过装饰器`@retry_on_exception`处理可能的临时失败：
- 最大重试次数可配置
- 重试间隔时间可调整
- 包含详细的日志记录

### 2. 元素等待
使用显式等待机制确保元素可用：
- 实现了`wait_for_element`函数
- 支持自定义超时时间
- 提供详细的等待过程日志

### 3. 页面操作
提供了丰富的页面操作函数：
- 搜索功能
- 点击操作
- 滑动操作
- 返回操作

## 配置说明
主要配置项位于`features/config.py`文件中：
- 超时设置
- 重试次数设置
- 按钮定位器配置
- 应用ID配置

## 运行测试
1. 确保环境配置正确
2. 连接Android设备或启动模拟器
3. 在项目根目录执行：
   ```bash
   behave features/[feature_file_name].feature
   ```

## 测试报告
- 测试结果将保存在`report`目录下
- 失败用例的截图将保存在`screenshots`目录下

## 注意事项
1. 运行测试前请确保：
   - Android设备已启用开发者选项
   - USB调试已开启
   - 设备已正确连接
2. 确保测试环境网络稳定
3. 定期清理测试报告和截图目录

## 维护建议
1. 定期更新依赖包
2. 保持测试用例的独立性
3. 及时更新测试数据
4. 保持良好的代码组织和注释

## 故障排除
常见问题及解决方案：
1. 元素定位失败
   - 检查元素定位器是否正确
   - 确认页面是否完全加载
   - 检查网络连接

2. 测试执行超时
   - 调整等待时间配置
   - 检查设备性能
   - 优化测试步骤

3. 设备连接问题
   - 检查USB连接
   - 确认ADB服务状态
   - 重启设备和开发环境