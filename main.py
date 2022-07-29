#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright
import re

with sync_playwright() as p:
    # browser = p.chromium.launch(headless=False)
    # page = browser.new_page()
    # page.goto('https://www.facebook.com/login')
    # page.wait_for_load_state('networkidle')
    # html = page.content()
    # html = re.sub('<script[^>]*>(?:.*?)<\/script>', '', html)

    # path = 'login.html'
    # f = open(path, 'w')
    # f.write(html)
    # f.close()
    # browser.close()

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://m.facebook.com/login?refsrc=deprecated&_rdr')
    page.wait_for_load_state('networkidle')
    html = page.content()
    html = re.sub('<script[^>]*>(?:.*?)<\/script>', '', html)

    path = 'login.html'
    f = open(path, 'w')
    f.write(html)
    f.close()
    browser.close()
