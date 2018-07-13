#!/usr/bin/env python
#coding=utf-8

import sys
import json
from aliyunsdkcore import client
from aliyunsdkslb.request.v20140515 import AddAccessControlListEntryRequest
from aliyunsdkslb.request.v20140515 import DescribeAccessControlListAttributeRequest

clt = client.AcsClient('AccessKeyId','secret','cn-beijing')


AclEntryIP = [{u'entry': u'', u'comment': u''}]

AclEntryIP[0]["entry"] = sys.argv[1]+'/32'

AclEntryIP = json.dumps(AclEntryIP)

request = AddAccessControlListEntryRequest.AddAccessControlListEntryRequest()
request.set_accept_format('json')

request.add_query_param('RegionId', 'cn-beijing')
request.add_query_param('AclEntrys', AclEntryIP)
request.add_query_param('AclId', 'acl-fdsafdsafdsafdsaf')


## 发起请求
response = clt.do_action_with_exception(request)


# 查询
## 设置参数
request = DescribeAccessControlListAttributeRequest.DescribeAccessControlListAttributeRequest()
request.set_accept_format('json')

request.add_query_param('RegionId', 'cn-beijing')
request.add_query_param('AclId', 'acl-fdsafdsafdsafdsaf')

## 发起请求
response = clt.do_action_with_exception(request)

## 输出结果
print "黑名单列表：", response, '\n'
