#!/user/bin/env python
# -*- coding:utf-8 -*-
# time:2018/3/20
import requests
from bs4 import BeautifulSoup
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
soup=BeautifulSoup(html,'lxml')
#print(soup.select('ul li')[0].get_text())
print(soup.li)