import pytest
from fof99 import FundInfo
import os
appid = os.getenv("HFN_APPID")
appkey = os.getenv("HFN_APPKEY")

def test_fund_info():
    req = FundInfo(appid, appkey)
    req.set_params(reg_code='SSM234')
    fund_info = req.do_request(use_df=True)
    assert fund_info['register_number'][0] == 'SSM234'