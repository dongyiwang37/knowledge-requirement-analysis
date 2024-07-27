from lxml import etree
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import os
import time
import urllib
import random
from selenium.webdriver.common.keys import Keys
import json


profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.http', '127.0.0.1')
profile.set_preference('network.proxy.http_port', 17890)  # int
profile.update_preferences()

Browser = webdriver.Firefox(firefox_profile=profile)
Browser.set_page_load_timeout(30)
Browser.set_script_timeout(30)
'''
f = open('D:/hrefs.txt','w',encoding='utf-8')
for ir in range(1,10):
    url = 'https://www.researchgate.net/topic/Engineering/'+str(ir)
    old_scroll_height = 0
    js1 = 'return document.body.scrollHeight'
    js2 = 'window.scrollTo(0, document.body.scrollHeight)'
    try:
        Browser.get(url)
    except:
        Browser.execute_script('window.stop()')
    time.sleep(5)

    html = Browser.page_source
    tree = etree.HTML(html)
    hrefs = tree.xpath('//a[@class="nova-c-button nova-c-button--align-center nova-c-button--radius-m nova-c-button--size-s nova-c-button--color-blue nova-c-button--theme-bare nova-c-button--width-auto nova-v-message-contribution-item__action"]/@href')
    print(hrefs)
    f.write('\n'.join(hrefs))
'''

f = open('D:/file_2.txt', 'r', encoding='utf-8')
hrefs = f.read().split('\n')
count = 0

url = 'https://www.researchgate.net/login'
try:
    Browser.get(url)
except:
    Browser.execute_script('window.stop()')
time.sleep(10)
Browser.find_element_by_xpath('//*[@id="input-login"]').send_keys('wangziha21@mails.tsinghua.edu.cn')
Browser.find_element_by_xpath('//*[@id="input-password"]').send_keys('wzhlovelol0528')
#Browser.find_element_by_xpath('//*[@id="input-login"]').send_keys('wangdy37@mail2.sysu.edu.cn')
#Browser.find_element_by_xpath('//*[@id="input-password"]').send_keys('520520wdy')
try:
    Browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div/div/div/form/div/div[4]/button/span').click()
except:
    Browser.execute_script('window.stop()')
time.sleep(5)

tempJs = 'let childrens = document.querySelectorAll("div.nova-v-person-list-item__body");' \
             'childrens[childrens.length - 1].scrollIntoView();return childrens.length;'
Js = 'let childrens = document.querySelectorAll("div.nova-v-person-list-item__body");' \
     'return childrens.length;'


for href in hrefs[16993:18000]:
    data = {}
    print(hrefs.index(href), href)
    try:
        Browser.get('https://www.researchgate.net/' + href)
    except:
        Browser.execute_script('window.stop()')
    time.sleep(5)
    try:
        cnt = 0
        while Browser.find_element_by_xpath(
                '//button[@class="nova-legacy-c-button nova-legacy-c-button--align-center nova-legacy-c-button--radius-m nova-legacy-c-button--size-m nova-legacy-c-button--color-grey nova-legacy-c-button--theme-bare nova-legacy-c-button--width-full"]'):
            document = Browser.execute_script('return document.body.scrollHeight;')
            Browser.find_element_by_xpath(
                '//button[@class="nova-legacy-c-button nova-legacy-c-button--align-center nova-legacy-c-button--radius-m nova-legacy-c-button--size-m nova-legacy-c-button--color-grey nova-legacy-c-button--theme-bare nova-legacy-c-button--width-full"]').click()
            time.sleep(3)
            document2 = Browser.execute_script('return document.body.scrollHeight;')
            if document == document2:
                dict20[20]

    except:
        html = Browser.page_source
        tree = etree.HTML(html)

        title = tree.xpath('/html/head/title/text()')
        title[0]


        # information
        read_times = tree.xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/div/div[1]/div/div[2]/div/div/div[2]/text()')

        followers = {}
        followers['name'] = []
        followers['score'] = []
        followers['univ'] = []

        f_b = Browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/div/div[2]/div/div[1]/div')
        if f_b.is_enabled():
            f_b.click()
            time.sleep(3)
            if len(Browser.find_elements_by_xpath('/html/body/div/div/div/div[2]/div/div[2]/div[1]/div/div/div')) > 7:
                time.sleep(2)
                while 1:
                    len1 = len(
                        Browser.find_elements_by_xpath('/html/body/div/div/div/div[2]/div/div[2]/div[1]/div/div/div'))
                    for ii in range(40):
                        ActionChains(Browser).send_keys(Keys.ARROW_DOWN).perform()
                    time.sleep(3)
                    len2 = len(
                        Browser.find_elements_by_xpath('/html/body/div/div/div/div[2]/div/div[2]/div[1]/div/div/div'))
                    #print(len1, len2)
                    if len1 == len2:
                        break
                    # Browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[2]/div[1]/div/div').send_keys(Keys.DOWN)
            html = Browser.page_source
            tree = etree.HTML(html)
            print(len(tree.xpath('/html/body/div/div/div/div[2]/div/div[2]/div[1]/div/div/div')))
            for ii in range(len(tree.xpath('/html/body/div/div/div/div[2]/div/div[2]/div[1]/div/div/div'))):
                fl_name = '\t'.join(tree.xpath(
                    '/html/body/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[{}]/div/div/div[2]/div/div/div/div/span/div/a/text()'.format(
                        ii + 1)))
                fl_sc = '\t'.join(tree.xpath(
                    '/html/body/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[{}]/div/div/div[2]/div/div/div/div/ul/li/span/text()'.format(
                        ii + 1)))
                fl_univ = '\t'.join(tree.xpath(
                    '/html/body/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[{}]/div/div/div[2]/div/div/div/div/ul/li[2]/span/span/text()'.format(
                        ii + 1)))
                followers['name'].append(fl_name)
                followers['score'].append(fl_sc)
                followers['univ'].append(fl_univ)
            time.sleep(2)
            ActionChains(Browser).send_keys(Keys.ESCAPE).perform()
            time.sleep(2)


        recommendations = {}
        recommendations['name'] = []
        recommendations['score'] = []
        recommendations['univ'] = []

        r_b = Browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/div/div[4]/div/div[1]/div')
        if r_b.is_enabled():
            r_b.click()
            time.sleep(3)
            if len(Browser.find_elements_by_xpath('/html/body/div/div/div/div[2]/div/div[2]/div[1]/div/div/div')) > 7:
                time.sleep(3)
                while 1:
                    len1 = len(
                        Browser.find_elements_by_xpath('/html/body/div/div/div/div[2]/div/div[2]/div[1]/div/div/div'))
                    for ii in range(40):
                        ActionChains(Browser).send_keys(Keys.ARROW_DOWN).perform()
                    time.sleep(3)
                    len2 = len(
                        Browser.find_elements_by_xpath('/html/body/div/div/div/div[2]/div/div[2]/div[1]/div/div/div'))
                    # print(len1, len2)
                    if len1 == len2:
                        break
            html = Browser.page_source
            tree = etree.HTML(html)
            print(len(tree.xpath('/html/body/div/div/div/div[2]/div/div[2]/div[1]/div/div/div')))
            for ii in range(len(tree.xpath('/html/body/div/div/div/div[2]/div/div[2]/div[1]/div/div/div'))):
                rec_name = '\t'.join(tree.xpath(
                    '/html/body/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[{}]/div/div/div[2]/div/div/div/div/span/div/a/text()'.format(
                        ii + 1)))
                rec_sc = '\t'.join(tree.xpath(
                    '/html/body/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[{}]/div/div/div[2]/div/div/div/div/ul/li/span/text()'.format(
                        ii + 1)))
                rec_univ = '\t'.join(tree.xpath(
                    '/html/body/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[{}]/div/div/div[2]/div/div/div/div/ul/li[2]/span/span/text()'.format(
                        ii + 1)))
                recommendations['name'].append(rec_name)
                recommendations['score'].append(rec_sc)
                recommendations['univ'].append(rec_univ)
            ActionChains(Browser).send_keys(Keys.ESCAPE).perform()
        time.sleep(3)
        data['followers'] = followers
        data['recommendations'] = recommendations
        data['read_times'] = read_times


        '''
        po_text_pic = tree.xpath('//img[@class="nova-legacy-c-image-tiles__image"]/@src')
        po_text_file = tree.xpath('//a[@class="nova-legacy-e-link nova-legacy-e-link--color-inherit nova-legacy-e-link--theme-decorated nova-legacy-v-file-inline-item__name-container"]/@href')
                                    '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div/div/div/button/div/img'
        '''

        for rm_btn in Browser.find_elements_by_xpath('//div[@class="nova-legacy-e-expandable-text__read-more"]/button'):
            rm_btn.click()
            time.sleep(1.5)
        time.sleep(1)

        html = Browser.page_source
        tree = etree.HTML(html)
        po_text = tree.xpath(
            'string(/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[3]/div)')
        po_score = tree.xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div/div/div/ul/li[1]/span/text()')
        po_univ = tree.xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div/div/div/ul/li[2]/span/a/text()')
        po_time = tree.xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/ul/li/span/time/text()')
        po_name = tree.xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div/div/div/span/span/div/a/span/text()')
        po_href = tree.xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div/div/div/span/span/div/a/@href')
        po_pic = tree.xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div/div/div[1]/div/div[1]/div/div/div[1]/span/span/a/img/@src')
        all_text = tree.xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div/div/div[4]/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div/div')
        # all_text = tree.xpath('//div[@class="nova-legacy-e-expandable-text__container"]')

        texts = []
        for t in range(len(all_text)):
            texts.append(tree.xpath(
                'string(/html/body/div[1]/div[3]/div[1]/div/div/div/div[4]/div/div/div[2]/div/div[{}]/div/div[2]/div/div/div/div/div/div/div)'.format(
                    t + 1)))

        an_time = tree.xpath(
            '//div[@class="nova-legacy-e-text nova-legacy-e-text--size-s nova-legacy-e-text--family-sans-serif nova-legacy-e-text--spacing-none nova-legacy-e-text--color-inherit nova-legacy-v-activity-list-item__time"]/time/text()')
        an_href = tree.xpath(
            '//a[@class="nova-legacy-e-link nova-legacy-e-link--color-inherit nova-legacy-e-link--theme-bare nova-legacy-v-activity-list-item__story-subject-link"]/@href')
        an_name = tree.xpath(
            '//a[@class="nova-legacy-e-link nova-legacy-e-link--color-inherit nova-legacy-e-link--theme-bare nova-legacy-v-activity-list-item__story-subject-link"]/span/text()')
        an_pic = tree.xpath(
            '//a[@class="nova-legacy-e-avatar nova-legacy-e-avatar--size-s nova-legacy-e-avatar--radius-full nova-legacy-e-avatar--framed nova-legacy-v-activity-list-item__story-image"]/img/@src')

        recom = []
        for ii in range(len(an_href)):
            recom.append('\t'.join(tree.xpath(
                '/html/body/div[1]/div[3]/div[1]/div/div/div/div[4]/div/div/div[2]/div/div[{}]/div/div[2]/div/div/div/div/div/div/footer/div[2]/ul/li/span/button/text()'.format(
                    ii + 1))))
        time.sleep(random.randint(3, 5))
        data['post_time'] = po_time
        data['post_name'] = po_name
        data['poster_href'] = po_href
        data['post_text'] = po_text
        data['post_picture'] = po_pic


        data['answer_text'] = texts
        data['answer_time'] = an_time
        data['answerer_href'] = an_href
        data['answer_name'] = an_name
        data['answer_picture'] = an_pic
        data['answer_rec'] = recom
        json.dump(data, open("D:/rg_answer/{}.json".format(href.replace(r'post/', '')), 'w', encoding='utf-8'))

        '''print(po_time)
        print(po_name)
        print(po_href)
        print(po_text)

        print(texts)
        print(an_time)
        print(an_href)
        print(an_name)'''