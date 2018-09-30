import urllib.request
import re

def getStuContent():
    for i in range(1845, 5039, 2):
        idNum = i
        html = urllib.request.urlopen('http://www.xygz.com.cn/teacher/index.php?m=content&c=index&a=show&catid=210&id='
                                  + str(idNum)).read()
        html = html.decode('gbk')
        # print(html)
        # 正则表达式  匹配数据  想要的数据加括号
        # req = '<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
        name = '<h1>(.*?)</h1>'
        school = 'button type="button" class="btn btn-danger btn-lg">(.*?)</button>'
        names = re.findall(name, html)
        schools = re.findall(school, html)
        f = open('./test.txt', 'a')
        f.write(str(names)+str(schools)+'\n')
        # print(names, schools)
        f.close()

if __name__ == '__main__':
    getStuContent()
