#!/usr/bin/env python
# -*- coding: utf-8 -*-

import praw
import re
import hashlib
import csv
import smtplib
import sys


def csvcheck(l):
    md5list = []
    with open('list.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            md5list.append(row[0])
        if l[0] in md5list:
            return 0
        else:
            csvwrite(l)


def csvwrite(l):
    with open('list.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(l)
        urltitle = [l[1], l[2]]
        links2email.append(urltitle)


def md5encode(submissionurl):
    concat = submissionurl
    m = hashlib.md5()
    m.update(concat)
    m = m.hexdigest()
    return m


def subtophot():
    for submission in subreddit.get_hot(limit=20):
        match = re.search("(reddit.com)", submission.url)
        if match:
            pass
        else:
            md5url = md5encode(submission.url)
            l = (md5url, submission.url.encode('utf-8'), submission.title.encode('utf-8'))
            csvcheck(l)


def sendusinggmail():
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.login(GMAILUSER, GMAILPASS)
    headers = "\r\n".join(["from: " + GMAILUSER,
                           "subject: " + "Hot Netsec Topics",
                           "to: " + SENDTOEMAIL,
                           "mime-version: 1.0",
                           "content-type: text/html"])
    linksend = '<html><body>'

    for a in links2email:
        linksend += '<br>'
        linksend += unicode(str(a)).strip('"\'')
        linksend += '<br>'
    print linksend
    content = headers + "\r\n\r\n" + linksend
    session.sendmail(GMAILUSER, SENDTOEMAIL, content)

#Email Vars
GMAILUSER = ""
GMAILPASS = ""
SENDTOEMAIL = ""

links2email = []
r = praw.Reddit(user_agent='HOT Netsec Topics Emailler v1')
sub = 'netsec'
subreddit = r.get_subreddit(sub)
subtophot()

if len(links2email) == 0:
    sys.exit()
else:
    sendusinggmail()
