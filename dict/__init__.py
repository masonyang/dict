#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    /Library/Python/2.7/site-packages/dict

    dict
    ~~~~

    Chinese/English Translation

    :date:      09/12/2013
    :author:    Feei <feei@feei.cn>
    :homepage:  https://github.com/wufeifei/dict
    :license:   MIT, see LICENSE for more details.
    :copyright: Copyright (c) 2017 Feei. All rights reserved
"""
from __future__ import unicode_literals
import sys
import json
import re
import translate

__name__ = 'dict-cli'
__version__ = '1.3.4'
__description__ = '命令行下中日英文翻译工具（Chinese and English translation tools in the command line）'
__keywords__ = 'Translation English2Chinese Chinese2Japanese Japanese2Chinese Command-line'
__author__ = 'Feei'
__contact__ = 'feei@feei.cn'
__url__ = 'https://github.com/wufeifei/dict'
__license__ = 'MIT'

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
    from urllib.parse import quote
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
    from urllib import quote


class Dict:
    key = '716426270'
    keyFrom = 'wufeifei'
    api = 'http://fanyi.youdao.com/openapi.do' \
          '?keyfrom=wufeifei&key=716426270&type=data&doctype=json&version=1.1&q='
    content = None

    def __init__(self, argv):
        message = ''
        if len(argv) > 0:
            for s in argv:
                message = message + s + ' '
            self.api = self.api + quote(message.encode('utf-8'))
            self.translate()
        else:
            print('Usage: dict test')

    def translate(self):
        try:
            content = urlopen(self.api).read()
            self.content = json.loads(content.decode('utf-8'))
            self.parse()
        except Exception as e:
            print('ERROR: Network or remote service error!')
            print(e)

    def parse(self):
        code = self.content['errorCode']
        if code == 0:  # Success
            c = None
            try:
                u = self.content['basic']['us-phonetic']  # English
                e = self.content['basic']['uk-phonetic']
            except KeyError:
                try:
                    c = self.content['basic']['phonetic']  # Chinese
                except KeyError:
                    c = 'None'
                u = 'None'
                e = 'None'

            try:
                explains = self.content['basic']['explains']
            except KeyError:
                explains = 'None'

            try:
                phrase = self.content['web']
            except KeyError:
                phrase = 'None'

            print('\033[1;31m################################### \033[0m')
            print('\033[1;31m# \033[0m {0} {1}'.format(
                self.content['query'], self.content['translation'][0]))
            if u != 'None':
                print('\033[1;31m# \033[0m (U: {0} E: {1})'.format(u, e))
            elif c != 'None':
                print('\033[1;31m# \033[0m (Pinyin: {0})'.format(c))
            else:
                print('\033[1;31m# \033[0m')

            print('\033[1;31m# \033[0m')

            if explains != 'None':
                for i in range(0, len(explains)):
                    print('\033[1;31m# \033[0m {0}'.format(explains[i]))
            else:
                print('\033[1;31m# \033[0m Explains None')

            print('\033[1;31m# \033[0m')

            if phrase != 'None':
                for p in phrase:
                    print('\033[1;31m# \033[0m {0} : {1}'.format(
                        p['key'], p['value'][0]))
                    if len(p['value']) > 0:
                        if re.match('[ \u4e00 -\u9fa5]+', p['key']) is None:
                            blank = len(p['key'].encode('gbk'))
                        else:
                            blank = len(p['key'])
                        for i in p['value'][1:]:
                            print('\033[1;31m# \033[0m {0} {1}'.format(
                                ' ' * (blank + 3), i))

            print('\033[1;31m################################### \033[0m')
            # Phrase
            # for i in range(0, len(self.content['web'])):
            #     print self.content['web'][i]['key'], ':'
            #     for j in range(0, len(self.content['web'][i]['value'])):
            #         print self.content['web'][i]['value'][j]
        elif code == 20:  # Text to long
            print('WORD TO LONG')
        elif code == 30:  # Trans error
            print('TRANSLATE ERROR')
        elif code == 40:  # Don't support this language
            print('CAN\'T SUPPORT THIS LANGUAGE')
        elif code == 50:  # Key failed
            print('KEY FAILED')
        elif code == 60:  # Don't have this word
            print('DO\'T HAVE THIS WORD')

class BdDict(object):
    

    content = None

    origin = None

    """docstring for BdDict"""
    def __init__(self, argv):
        message = ''
        if len(argv) > 0:
            for s in argv:
                message = message + s + ' '
            self.translate(message.encode('utf-8'))
        else:
            print('Usage: dict test')
    
    def translate(self,message):
        trans = translate.Translate()

        sentence = message.strip()

        self.origin = sentence

        if(sentence == ''):
            self.content = 'None'
        else:
            f = trans.langdetect(sentence)

            self.content = trans.trans(sentence,f)

        self.parse()

    def parse(self):
        print('\033[1;31m################################### \033[0m')

        trg_str = ''
        src_str = ''
        try:
            for item in self.content['phonetic']:
                for i in item:
                    if(i=='trg_str'):
                        trg_str = trg_str + item['trg_str']+' '
                    if(i=='src_str'):
                        src_str = src_str + item['src_str']+' '
        except KeyError:
            trg_str = '-'
            src_str = '-'

        print('\033[1;31m# \033[0m {0} (phonetic: {1})'.format(
            self.content['data'][0]['src'],src_str))
        print('\033[1;31m# \033[0m')
        print('\033[1;31m# \033[0m')
        print('\033[1;31m# \033[0m {0} (phonetic: {1})'.format(self.content['data'][0]['dst'],trg_str))
        print('\033[1;31m################################### \033[0m')

def main():
    BdDict(sys.argv[1:])


if __name__ == '__main__':
    main()
