#先把每个页面的元素抓出来封装，方便调用，这个是我的页面的元素
from ..common.fengzhuangdingwei import Base
class MyPage():
    """页面元素抓取"""
    loc1 = {'by': 'text', 'value': '我的'}
    loc2 = {'by': 'text', 'value': '优惠券'}
    loc3 = {'by': 'text', 'value': '加速包/抢票券'}
    loc4 = {"by": "text", "value": "借现金"}
    loc5 = {"by": "text", "value": "拿去花"}
    loc6 = {"by": "text", "value": "常用信息"}
    loc7 = {"by": "text", "value": "客服中心"}
    loc8 = {"by": "text", "value": "产品意见"}
    loc9 = {"by": "text", "value": "出行服务"}
    loc10 = {"by": "text", "value": "学生认证"}
    loc11 = {"by": "text", "value": "我的足迹"}
    loc12 = {"by": "text", "value": "关注微信公众号"}
    loc13 = {"by": "text", "value": "实名认证"}
