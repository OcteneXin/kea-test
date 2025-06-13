[![PyPI](https://img.shields.io/pypi/v/kea2-python.svg)](https://pypi.python.org/pypi/kea2-python)
[![PyPI Downloads](https://static.pepy.tech/badge/kea2-python)](https://pepy.tech/projects/kea2-python)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)

<div>
    <img src="https://github.com/user-attachments/assets/1a64635b-a8f2-40f1-8f16-55e47b1d74e7" style="border-radius: 14px; width: 20%; height: 20%;"/> 
</div>

## 关于

Kea2是一个易于使用的Python库，用于支持、定制和改进移动应用的自动化UI测试。Kea2的创新之处在于能够将人工编写的脚本与自动化UI测试工具融合，从而提供许多有趣且强大的功能。

Kea2目前基于[Fastbot](https://github.com/bytedance/Fastbot_Android)和[uiautomator2](https://github.com/openatx/uiautomator2)构建，目标平台为[Android](https://en.wikipedia.org/wiki/Android_(operating_system))应用。

## 重要特性
- **特性1**(查找稳定性问题): 继承[Fastbot](https://github.com/bytedance/Fastbot_Android)的全部能力，用于压力测试和发现*稳定性问题*（即*崩溃错误*）； 

- **特性2**(自定义测试场景\事件序列\黑白名单\黑白控件[^1]): 在运行Fastbot时自定义测试场景（例如测试特定应用功能、执行特定事件序列、进入特定UI页面、达到特定应用状态、屏蔽特定活动/UI控件/UI区域），充分利用*python*语言和[uiautomator2](https://github.com/openatx/uiautomator2)的完整能力和灵活性； 

- **特性3**(支持断言机制[^2]): 在运行Fastbot时支持自动断言，基于[Kea](https://github.com/ecnusse/Kea)继承的[基于性质的测试](https://en.wikipedia.org/wiki/Software_testing#Property_testing)理念，用于发现*逻辑错误*（即*非崩溃错误*）


**Kea2三大特性的能力对比**
|  | **特性1** | **特性2** | **特性3** |
| --- | --- | --- | ---- |
| **发现崩溃错误** | :+1: | :+1: | :+1: |
| **发现深层状态的崩溃错误** |  | :+1: | :+1: |
| **发现非崩溃的功能性（逻辑）错误** |  |  | :+1: |


<div align="center">
    <div style="max-width:80%; max-height:80%">
    <img src="docs/intro.png" style="border-radius: 14px; width: 80%; height: 80%;"/> 
    </div>
</div>