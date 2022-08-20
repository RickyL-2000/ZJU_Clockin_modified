# Automatic Clockin for ZJU

Following [idlesilver/ZJU_auto_health_report: 浙江大学健康打卡](https://github.com/idlesilver/ZJU_auto_health_report)。

## 基础配置
1. 安装 yagmail 第三方库 用于邮件通知
    ```
    pip install yagmail
    # 2022-3-5 亲测最新版的yagmail有些问题，会出现没有邮件正文的情况，安装旧版本可以解决这个问题，建议以下命令。
    pip install yagmail==0.14.260
    ```
2. 打开或新建 `basic_info.py` 填写相应配置，模板参考`basic_info_template.py` 
3. windows运行 `打卡.bat`，linux服务器参考下文

> 注意：这里的 `EMAIL_PASSWD` 不是邮箱密码，而是授权码AUTHCODE。[什么是授权码，它又是如何设置？_QQ邮箱帮助中心](https://service.mail.qq.com/cgi-bin/help?subtype=1&&no=1001256&&id=28)

## 自动周期
### windows
参考[win10设置每天定时开机方法](http://www.win7zhijia.cn/win10jc/win10_36026.html#:~:text=%E8%BF%99%E9%87%8C%E5%B0%8F%E7%BC%96%E5%B0%B1%E6%9D%A5%E5%91%8A%E8%AF%89%E5%A4%A7%E5%AE%B6win10%E8%AE%BE%E7%BD%AE%E6%AF%8F%E5%A4%A9%E5%AE%9A%E6%97%B6%E5%BC%80%E6%9C%BA%E6%96%B9%E6%B3%95%E3%80%82%201%E3%80%81%E9%A6%96%E5%85%88%E5%91%A2%EF%BC%8C%E6%88%91%E4%BB%AC%E6%89%93%E5%BC%80%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91%EF%BC%8C%E6%88%91%E4%BB%AC%E5%9C%A8%E6%A1%8C%E9%9D%A2%E4%B8%8A%E6%89%BE%E5%88%B0%E2%80%9C%E6%AD%A4%E7%94%B5%E8%84%91%E2%80%9D%E5%BA%94%E7%94%A8%EF%BC%8C%E9%BC%A0%E6%A0%87%E7%82%B9%E5%87%BB%E5%8F%B3%E9%94%AE%EF%BC%8C%E9%80%89%E6%8B%A9%E2%80%9C%E7%AE%A1%E7%90%86%E2%80%9D%E9%80%89%E9%A1%B9%E8%BF%9B%E5%85%A5%E3%80%82,2%E3%80%81%E5%9C%A8%E5%BC%B9%E5%87%BA%E6%9D%A5%E7%9A%84%E5%AF%B9%E8%AF%9D%E6%A1%86%E4%B8%AD%E7%82%B9%E5%87%BB%E5%B7%A6%E6%A0%8F%E4%B8%AD%E7%9A%84%E2%80%9D%E4%BB%BB%E5%8A%A1%E8%AE%A1%E5%88%92%E7%A8%8B%E5%BA%8F%E2%80%9C%EF%BC%8C%E8%BF%9B%E5%85%A5%E9%A1%B5%E9%9D%A2%E5%90%8E%E7%82%B9%E5%87%BB%E5%8F%B3%E6%A0%8F%E4%B8%AD%E7%9A%84%E2%80%9C%E5%88%9B%E5%BB%BA%E5%9F%BA%E6%9C%AC%E4%BB%BB%E5%8A%A1%E2%80%9D%E6%8C%89%E9%92%AE%E3%80%82%203%E3%80%81%E5%9C%A8%E5%BC%B9%E5%87%BA%E6%9D%A5%E7%9A%84%E5%AF%B9%E8%AF%9D%E6%A1%86%E4%B8%AD%E5%9C%A8%E5%90%8D%E7%A7%B0%E5%A4%84%E8%BE%93%E5%85%A5%E2%80%9C%E5%AE%9A%E6%97%B6%E5%BC%80%E6%9C%BA%E2%80%9D%EF%BC%8C%E7%82%B9%E5%87%BB%E2%80%9C%E4%B8%8B%E4%B8%80%E6%AD%A5%E2%80%9D%E6%8C%89%E9%92%AE%EF%BC%8C%E7%84%B6%E5%90%8E%E6%88%91%E4%BB%AC%E5%9C%A8%E4%BB%BB%E5%8A%A1%E8%A7%A6%E5%8F%91%E5%99%A8%E9%A1%B5%E9%9D%A2%E4%B8%AD%E9%80%89%E9%A1%B9%E6%89%80%E8%A6%81%E6%B1%82%E7%9A%84%E9%A2%91%E7%8E%87%E3%80%82)。把最后一步的 `程序与脚本` 选择为目录中的 `打卡.bat`

注：Windows自动周期本人未实现过，不保证可行。

### linux
使用 [`crontab`](https://www.cnblogs.com/ftl1012/p/crontab.html)。注意在ubuntu环境下使用cron命令而不是crond命令。

```bash
crontab -e
```

新增一行，注意`path_to_python_interpreter`换成对应的conda或venv环境
```
0 8 * * * ${path_to_python_interpreter} ${path_to_project_dir}/ZJU_auto_health_report/clock-in.py >/dev/null 2>&1
```

## 其他资源

校友提供的自动打卡网站：https://tool.zjucjh.com:666/dk/
