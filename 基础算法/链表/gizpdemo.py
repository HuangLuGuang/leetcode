# -*- coding: utf-8 -*-
# @createTime    : 2019/6/12 9:31
# @author  : Huanglg
# @fileName: gizp.py
# @email: luguang.huang@mabotech.com
import gzip
import io

str1 = """H4sIAAAAAAAAALWTX2vCMBTF3/0U0mel98a/K6EgNo6CabrWITJkBBpB2HRrU1+G332xIrFTuoexvN3fuck5l97SXH2WqtDhbrP3W21zaLpKF4wvVjHzCVL3qjzrXPBlGIskYMmZVPSCIuEDIALB4bA3GlD3Srjtrp5FQNtmjX6aifjKrxINSdnTM4umrLKFPnXrrN7Pw6ngnEUL/+XL2SiVve4PueOZIpNabrV6dzzLO85BvpXKIAQwVaFlrgOpT4QAPnRh2EXShrGH4FUdapc16lmZS73d7xwPj2vzYPFhvO5EsML/Z9BSl8VNgDO17rFYmg8wmzVEgF8ijCodaxHIgAA5dpq9w2DO/jR6D73+qD56D8an6eNEPCYTPgvnLI0mnJmrznFNXbsodhPde6tYo36LurXf6RtW7jmjXQMAAA=="""
data = gzip.decompress()
print(data)
