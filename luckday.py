'''
*
* batch filter luck day
*
* @author : Ethan.Yu
* @version: 1.0.0
* @email  : yusiyuan1208@qq.com
*
'''

import os
import requests
import datetime
from lxml import etree
import lxml
count = 60
stime = datetime.datetime.strptime("2021-03-23", "%Y-%m-%d")
print("                                **********建满平收黑，除危定执黄。成开皆可用，闭破不相当。**********")
print("----------------------------------------------------------------------------------------------------")
for num in range(0, count):
  time = stime + datetime.timedelta(days = num)
  days = time.strftime("%Y") + "-" + time.strftime("%m").lstrip('0') + "-" + time.strftime("%d").lstrip('0')
  url = "https://nongli.911cha.com/" + days + ".html"
  header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
  html = requests.get(url, headers = header)
  html.encoding="utf-8"
  selecter = etree.HTML(html.text)
  gld = selecter.xpath("""//table[@class="mt f14"]/tr/td[contains(text(), '公元')]/text()""")
  nld = selecter.xpath("""//table[@class="mt f14"]/tr/th[contains(text(), '农历')]/../td/text()""")
  srs = selecter.xpath("""//table[@class="mt f14"]/tr/td[contains(text(), '执位')]/text()""")
  srb = selecter.xpath("""//table[@class="mt f14"]/tr/td/span[contains(text(), '值日星宿')]/../text()""")
  hdr = ""
  if srs[0][0] in ["除", "危", "定", "执", "黄"] and srb[0][8] == "吉":
    hdr = "吉"
  else:
    hdr = "  "
  print(time.strftime("%Y-%m-%d") + " " + gld[0][-3:] + " " + " ".join(nld) + "\t" + hdr + "\t" + srs[0] + "\t" + " ".join(srb))
print("----------------------------------------------------------------------------------------------------")
os.system('pause')