# -*- coding: utf-8 -*-
import urllib.request
import json
import datetime

import time


app_id = "642354359227192"
app_secret = "665001410366056|BkqVb5MtH8tu5KxlQE4osIlV94g"  # DO NOT SHARE WITH ANYONE!

access_token = app_id + "|" + app_secret
access_token = "EAACEdEose0cBAMb8TdqBqcrLPvPq2MbyEN426ZCdylc8VWzZBktI1njDhHuODnY0rh4dZCUAlBesEY6E9deoy8hYiMppkSMYGDyVDxWUGoMLqrxHA5XmxFgcSFBnyHNZCTqHrDIyKkEubmyZCWqfdJ8V6ZBlodA4KPlTZA8kcvWaosZAn4hkFazymgvDS6GAhZCgZD"
page_id = 'hufsbamboo'

def testFacebookPageData(page_id, access_token):
    # construct the URL string
    base = "https://graph.facebook.com/v2.4"
    node = "/" + page_id
    parameters = "/?access_token=%s" % access_token
    url = base + node + parameters

    # retrieve data
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req).read().decode('utf-8')
    data = json.loads(response)

    #print(json.dumps(data, indent=4, sort_keys=True))



def request_until_succeed(url):
    req = urllib.request.Request(url)
    success = False
    while success is False:
        try:
            response = urllib.request.urlopen(req)
            if response.getcode() == 200:
                success = True
        except Exception:
            time.sleep(5)

            print("Error for URL %s: %s" % (url, datetime.datetime.now()))
            return False

    return urllib.request.urlopen(req).read().decode('utf-8')




def testFacebookPageFeedData(page_id, access_token, _list):
    count = 400;
    # construct the URL string
    base = "https://graph.facebook.com/v2.9"
    node = "/" + page_id + "/feed"  # changed
    parameters = "/?access_token=%s" % access_token
    url = base + node + parameters
    next_url = url
    # print(url)
    # retrieve data
    while 1:
        if count == 0:
           break
        try:
            data = json.loads(request_until_succeed(next_url), encoding='utf-8')
            next_url = data['paging']['next']
            if data == False:
                break
            else:
                print(count)
                count = count - 1
                _list.append(data)
        except:
            break
            #return False

    return _list
    #print(json.dumps(data, indent=4, sort_keys=True))



testFacebookPageData(page_id, access_token)
ex_list = []
temp = testFacebookPageFeedData(page_id, access_token, ex_list)



output = "./"+page_id+"_output.txt"
with open(output, 'w', encoding='utf-8') as outfile :

    for outbox in temp :
        for inbox in outbox['data'] :
            try :

                message = inbox['message'].replace("\n", " ")
                result = message
                outfile.write(result + "\n")

            except KeyError :
                pass