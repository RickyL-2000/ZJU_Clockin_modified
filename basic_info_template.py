EMAIL_SERVER = {
    "FROM_EMAIL": "to-be-determined@qq.com",
    "AUTHCODE": "to-be-determined",
    "HOST": "smtp.qq.com"   # 默认qq邮箱
}

USERS = {
    "user-1": {
        "ZJU_NUMBER": "to-be-determined",
        "ZJU_PASSWD": "to-be-determined",
        "TO_EMAIL": "to-be-determined@zju.edu.cn",  # 默认学校邮箱
        "SPECIFIED_INFO": {
            "name": "to-be-determined",
            "address": "浙江省杭州市西湖区",
            "area": "浙江省 杭州市 西湖区",
        }
    },
}

# OLDINFO
# 当fetch缓存数据失败(即oldinfo={})的时候使用。即用静态oldinfo数据来覆盖缓存数据。尽量使用真实的oldinfo数据包。
# 不能使用 oldInfo_template 这个名字，原因不详
OLDINFO = {}
