import os
import pytest
from fof99 import (FundAdvancedList,
                   FundInfo,
                   FundPrice,
                   FundCompanyPrice,
                   FundMultiPrice,
                   FundMultiCompanyPrice,
                   PersonalFundPrice,
                   MonitorLogList,
                   FofSubFundVirtualPrice,
                   DirectFundVirtualPrice,
                   FundScore,
                   FofSubFund,
                   FofSubFundDeals,
                   CompanyPriceBatchAdd,
                   PrivatePriceBatchAdd,
                   InnerPriceBatchAdd,
                   FofSubFundTrackList)

appid = os.getenv("HFN_APPID")
appkey = os.getenv("HFN_APPKEY")


def test_fund_info():
    req = FundInfo(appid, appkey)
    req.set_params(reg_code='SSM234')
    fund_info = req.do_request(use_df=False)
    assert fund_info['register_number'] == 'SSM234'


def test_fund_company_price():
    req = FundCompanyPrice(appid, appkey)
    req.set_params(reg_code='SSM234', start_date='2024-01-01',
                   end_date='2024-12-31')
    fund_price = req.do_request(use_df=True)
    assert len(fund_price) > 0
    assert fund_price['nav'].iloc[-1] == 1.1256

def test_fund_multi_company_price():
    req = FundMultiCompanyPrice(appid, appkey)
    req.set_params(reg_code='SSM234,LW453A,SQN990', date_='2024-12-31')
    fund_price = req.do_request(use_df=True)
    assert len(fund_price) == 3
    assert fund_price.query("reg_code == 'SSM234'")['nav'].iloc[0] == 1.1256