#先把每个页面的元素抓出来封装，方便调用，这个是我的页面的元素
from ..common.fengzhuangdingwei import Base
class MyPage(Base):
    loc1 = {'by': 'text', 'value': '我的'}
    loc2 = {'by': 'text', 'value': '我的足迹'}
    loc3 = {'by': 'text', 'value': 'sharenew'}
    loc4 = {"by": "class", "value": "android.view.View"}
    exceptresult = ["微信好友", "朋友圈"]