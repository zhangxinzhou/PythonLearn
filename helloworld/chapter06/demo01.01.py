def filterchar(string):
    '''
    功能: 过滤危险字符(如黑客),并将过来后的结果输出
    about: 要过来的字符串
    没有返回值
    '''
    import re
    pattern = r'(黑客)|(抓包)|(监听)|(Trojan)'
    sub = re.sub(pattern, '@_@', string)
    print(sub)


about = '窝是一名程序员,喜欢看黑客方面的书,想研究一下Trojan'
filterchar(about)
