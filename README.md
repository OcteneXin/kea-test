

[![PyPI](https://img.shields.io/pypi/v/kea2-python.svg)](https://pypi.python.org/pypi/kea2-python)
[![PyPI Downloads](https://static.pepy.tech/badge/kea2-python)](https://pepy.tech/projects/kea2-python)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)

<div>
    <img src="https://github.com/user-attachments/assets/1a64635b-a8f2-40f1-8f16-55e47b1d74e7" style="border-radius: 14px; width: 20%; height: 20%;"/> 
</div>

## About

Kea2 is an easy-to-use Python library for supporting, customizing and improving automated UI testing for mobile apps. Kea2's novelty is able to fuse the scripts (usually written by human) with automated UI testing tools, thus allowing many interesting and powerful features. 

Kea2 is currently built on top of [Fastbot](https://github.com/bytedance/Fastbot_Android) and [uiautomator2](https://github.com/openatx/uiautomator2) and targets [Android](https://en.wikipedia.org/wiki/Android_(operating_system)) apps.

## Important features
- **Feature 1**(查找稳定性问题): coming with the full capability of [Fastbot](https://github.com/bytedance/Fastbot_Android) for stress testing and finding *stability problems* (i.e., *crashing bugs*); 

- **Feature 2**(自定义测试场景\事件序列\黑白名单\黑白控件[^1]): customizing testing scenarios when running Fastbot (e.g., testing specific app functionalities, executing specific event traces, entering specifc UI pages, reaching specific app states, blacklisting specific activities/UI widgets/UI regions) with the full capability and flexibility powered by *python* language and [uiautomator2](https://github.com/openatx/uiautomator2);

- **Feature 3**(支持断言机制[^2]): supporting auto-assertions when running Fastbot, based on the idea of [property-based testing](https://en.wikipedia.org/wiki/Software_testing#Property_testing) inheritted from [Kea](https://github.com/ecnusse/Kea), for finding *logic bugs* (i.e., *non-crashing bugs*)


**The ability of the three features in Kea2**
|  | **Feature 1** | **Feature 2** | **Feature 3** |
| --- | --- | --- | ---- |
| **Finding crashes** | :+1: | :+1: | :+1: |
| **Finding crashes in deep states** |  | :+1: | :+1: |
| **Finding non-crashing functional (logic) bugs** |  |  | :+1: |


<div align="center">
    <div style="max-width:80%; max-height:80%">
    <img src="docs/intro.png" style="border-radius: 14px; width: 80%; height: 80%;"/> 
    </div>
</div>



## Design & Roadmap
Kea2, released as a Python library, currently works with:
- [unittest](https://docs.python.org/3/library/unittest.html) as the testing framework;
- [uiautomator2](https://github.com/openatx/uiautomator2) as the UI test driver; 
- [Fastbot](https://github.com/bytedance/Fastbot_Android) as the backend automated UI testing tool.

In the future, Kea2 will be extended to support
- [pytest](https://docs.pytest.org/en/stable/)
- [Appium](https://github.com/appium/appium), [Hypium](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-python-guidelines) (for HarmonyOS/Open Harmony)
- other automated UI testing tools (not limited to Fastbot)


## Installation

Running environment:
- support Windows, MacOS and Linux
- python 3.8+, Android 4.4+ (Android SDK installed)
- **VPN closed** (Features 2 and 3 required)

Install Kea2 by `pip`:
```bash
python3 -m pip install kea2-python
```

Find Kea2's options by running 
```bash
kea2 -h
```

## Quick Test

Kea2 connects to and runs on Android devices. We recommend you to do a quick test to ensure that Kea2 is compatible with your devices.

1. Connect to a real Android device or an Android emulator (only one device is enough) and make sure you can see the connected device by running `adb devices`. 

2. Run `quicktest.py` to test a sample app `omninotes` (released as `omninotes.apk` in Kea2's repository). The script `quicktest.py` will automatically install and test this sample app for a short time.

Initialize Kea2 under your preferred working directory:
```python
kea2 init
```

> This step is always needed if it is your first time to run Kea2.

Run the quick test:
```python
python3 quicktest.py
```

If you can see the app `omninotes` is successfully running and tested, Kea2 works!
Otherwise, please help [file a bug report](https://github.com/ecnusse/Kea2/issues) with the error message to us. Thank you!



## Feature 1(运行基础版Fastbot：查找稳定性错误)

Test your app with the full capability of Fastbot for stress testing and finding *stability problems* (i.e., *crashing bugs*); 


```bash
kea2 run -s "emulator-5554" -p it.feio.android.omninotes.alpha --agent native --running-minutes 10 --throttle 200
```

理解上述选项含义请查看[文档](docs/manual_en.md#launching-kea2)

> The usage is similar to the the original Fastbot's [shell commands](https://github.com/bytedance/Fastbot_Android?tab=readme-ov-file#run-fastbot-with-shell-command). 

See more options by 
```bash
kea2 run -h
```

## Feature 2(运行增强版Fastbot：自定义测试场景\事件序列\黑白控件)

When running any automated UI testing tools like Fastbot to test your apps, you may find that some specifc UI pages or functionalities are difficult to reach or cover. The reason is that Fastbot lacks knowledge of your apps. Fortunately, this is the strength of script testing. In Feature 2, Kea2 can support writing small scripts to guide Fastbot to explore wherever we want. You can also use such small scripts to block specific widgets during UI testing.

In Kea2, a script is composed of two elements:
-  **Precondition:** When to execute the script.
- **Interaction scenario:** The interaction logic (specified in the script's test method) to reach where we want.

### Simple Example

Assuming `Privacy` is a hard-to-reach UI page during automated UI testing. Kea2 can easily guide Fastbot to reach this page.

```python
    @prob(0.5)
    # precondition: when we are at the page `Home`
    @precondition(lambda self: 
        self.d(text="Home").exists
    )
    def test_goToPrivacy(self):
        """
        Guide Fastbot to the page `Privacy` by opening `Drawer`, 
        clicking the option `Setting` and clicking `Privacy`.
        """
        self.d(description="Drawer").click()
        self.d(text="Settings").click()
        self.d(text="Privacy").click()
```

- By the decorator `@precondition`, we specify the precondition --- when we are at the `Home` page. 
In this case, the `Home` page is the entry page of the `Privacy` page and the `Home` page can be easily reached by Fastbot. Thus, the script will be activated when we are at `Home` page by checking whether a unique widget `Home` exists. 
- In script's test method `test_goToPrivacy`, we specify the interaction logic (i.e., opening `Drawer`, clicking the option `Setting` and clicking `Privacy`) to guide Fastbot to reach the `Privacy` page.
- By the decorator `@prob`, we specify the probability (50% in this example) to do the guidance when we are at the `Home` page. As a result, Kea2 still allows Fastbot to explore other pages.

You can find the full example in script `quicktest.py`, and run this script with Fastbot by the command `kea2 run`:

```bash
# Launch Kea2 and load one single script quicktest.py.
kea2 run -s "emulator-5554" -p it.feio.android.omninotes.alpha --agent u2 --running-minutes 10 --throttle 200 --driver-name d unittest discover -p quicktest.py
```

## Feature 3(运行增强版Fastbot：加入自动断言)

Kea2 supports auto-assertions when running Fastbot for finding *logic bugs* (i.e., *non-crashing bugs*). To achieve this, you can add assertions in the scripts. When an assertion fails during automated UI testing, we find a likely functional bug. 

In Feature 3, a script is composed of three elements:

- **Precondition:** When to execute the script.
- **Interaction scenario:** The interaction logic (specified in the script's test method).
- **Assertion:** The expected app behaviour.

### Example

In a social media app, message sending is a common feature. On the message sending page, the `send` button should always appears when the input box is not empty (i.e., has some message).

<div align="center" >
    <div >
        <img src="docs/socialAppBug.png" style="border-radius: 14px; width:30%; height:40%;"/>
    </div>
    <p>The expected behavior (the upper figure) and the buggy behavior (the lower figure).
<p/>
</div>

For the preceding always-holding property, we can write the following script to validate the functional correctness: when there is an `input_box` widget on the message sending page, we can type any non-empty string text into the input box and assert `send_button` should always exists.


```python
    @precondition(
        lambda self: self.d(description="input_box").exists
    )
    def test_input_box(self):
        from hypothesis.strategies import text, ascii_letters
        random_str = text(alphabet=ascii_letters).example()
        self.d(description="input_box").set_text(random_str)
        assert self.d(description="send_button").exist

        # we can even do more assertions, e.g.,
        #       the input string should exist on the message sending page
        assert self.d(text=random_str).exist
```
>  We use [hypothesis](https://github.com/HypothesisWorks/hypothesis) to generate random texts.

You can run this example by using the similar command line in Feature 2. 

## Documentations（更多文档）

[更多文档](docs/manual_en.md)，包括了：
- Kea2的案例教程（基于微信介绍）、
- Kea2脚本的定义方法，支持的脚本装饰器(如`@precondition`、`@prob`、`@max_tries`)、
- Kea2的启动方式、命令行选项
- 查看/理解Kea2的运行结果（如界面截图、测试覆盖率、脚本执行成功与否）。
- [如何黑白控件/区域](docs/blacklisting.md)

## Open-source projects used by Kea2

- [Fastbot](https://github.com/bytedance/Fastbot_Android)
- [uiautomator2](https://github.com/openatx/uiautomator2)
- [hypothesis](https://github.com/HypothesisWorks/hypothesis)

## Relevant papers of Kea2

> General and Practical Property-based Testing for Android Apps. ASE 2024. [pdf](https://dl.acm.org/doi/10.1145/3691620.3694986)

> An Empirical Study of Functional Bugs in Android Apps. ISSTA 2023. [pdf](https://dl.acm.org/doi/10.1145/3597926.3598138)

> Fastbot2: Reusable Automated Model-based GUI Testing for Android Enhanced by Reinforcement Learning. ASE 2022. [pdf](https://dl.acm.org/doi/10.1145/3551349.3559505)

> Guided, Stochastic Model-Based GUI Testing of Android Apps. ESEC/FSE 2017.  [pdf](https://dl.acm.org/doi/10.1145/3106237.3106298)

### Maintainers/Contributors

Kea2 has been actively developed and maintained by the people in [ecnusse](https://github.com/ecnusse):

- [Xixian Liang](https://xixianliang.github.io/resume/) ([@XixianLiang][])
- Bo Ma ([@majuzi123][])
- Chen Peng ([@Drifterpc][])
- [Ting Su](https://tingsu.github.io/) ([@tingsu][])

[@XixianLiang]: https://github.com/XixianLiang
[@majuzi123]: https://github.com/majuzi123
[@Drifterpc]: https://github.com/Drifterpc
[@tingsu]: https://github.com/tingsu

[Zhendong Su](https://people.inf.ethz.ch/suz/), [Yiheng Xiong](https://xyiheng.github.io/), [Xiangchen Shen](https://xiangchenshen.github.io/), [Mengqian Xu](https://mengqianx.github.io/), [Haiying Sun](https://faculty.ecnu.edu.cn/_s43/shy/main.psp), [Jingling Sun](https://jinglingsun.github.io/), [Jue Wang](https://cv.juewang.info/) have also been actively participated in this project and contributed a lot!

Kea2 has also received many valuable insights, advices, feedbacks and lessons shared by several industrial people from Bytedance ([Zhao Zhang](https://github.com/zhangzhao4444), Yuhui Su from the Fastbot team), OPay (Tiesong Liu), WeChat (Haochuan Lu, Yuetang Deng), Huawei, Xiaomi and etc. Kudos!

[^1]: 不少UI自动化测试工具提供了“自定义事件序列”能力（如[Fastbot](https://github.com/bytedance/Fastbot_Android/blob/main/handbook-cn.md#%E8%87%AA%E5%AE%9A%E4%B9%89%E4%BA%8B%E4%BB%B6%E5%BA%8F%E5%88%97) 和[AppCrawler](https://github.com/seveniruby/AppCrawler)），但在实际使用中存在不少问题，如自定义能力有限、使用不灵活等。此前不少Fastbot用户抱怨过其“自定义事件序列”在使用中的问题，如[#209](https://github.com/bytedance/Fastbot_Android/issues/209), [#225](https://github.com/bytedance/Fastbot_Android/issues/225), [#286](https://github.com/bytedance/Fastbot_Android/issues/286)等。

[^2]: 在UI自动化测试过程中支持自动断言是一个很重要的能力，但几乎没有测试工具提供这样的能力。我们注意到[AppCrawler](https://ceshiren.com/t/topic/15801/5)的开发者曾经希望提供一种断言机制，得到了用户的热切响应，不少用户从21年就开始催更，但始终未能实现。