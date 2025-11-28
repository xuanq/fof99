# -*- coding: utf-8 -*-

import importlib.metadata

__version__ = importlib.metadata.version('fof99')

from .requests.factorrequest import (
    FactorFutures,
    FactorStyleCne5,
    FactorStyleCne6,
)
from .requests.indexrequest import (
    IndexPrice,
    IndexBatchPrice,
    IndexStockAmt,
    IndexStockTurn,
    IndexStockPE,
)
from .requests.fundrequest import (
    FundAdvancedList,
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
    FofSubFundTrackList,
)
from .requests.gmfundrequest import (
    GmFundInfo,
    GmFundPrice,
    GmFundBatchPrice,
)
from .requests.combirequest import (
    FoCombiPrice,
    CombiPrice,
)
from .requests.companyrequest import (
    CompanyInfo,
    CompanyScale,
    CompanyShareholder,
    CompanyFundList,
)
from .requests.traderequest import (
    FundBuyInfo,
    FofInvestCustomerPrice,
)