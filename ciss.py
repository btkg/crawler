import urllib.request
import re


def getCissContents():
    url_base = 'https://ciss.tsinghua.edu.cn'
    page_final = urllib.request.urlopen('https://ciss.tsinghua.edu.cn/column/qb/1').read()
    page_final = page_final.decode('utf-8')
    page_final_num = 'class="">...(.*?)</a>'
    page_final_nums = re.findall(page_final_num, page_final)

    f = open('./test.csv', 'a')
    f.write('page, web page, pdf' + '\n')

    for i in range(1, int(page_final_nums[0])+1, 1):
        page_num = i
        html = urllib.request.urlopen('https://ciss.tsinghua.edu.cn/column/qb/' + str(page_num)).read()
        html = html.decode('utf-8')

        page_url = '<a href="(.*?)">\s+<div class="articles-item-right">'
        page_urls = re.findall(page_url, html)

        for path in page_urls:
            f.write(str(page_num) + ', ')
            f.write(str(url_base+path) + ', ')

            content = urllib.request.urlopen(str(url_base+path)).read()
            content = content.decode('utf-8')

            pdf_url = '<div class="pdfdis"><a href="(.*?)">请点击下载后观看。</a></div>'
            pdf_urls = re.findall(pdf_url, content)

            if len(pdf_urls) == 0:
                f.write('null' + ', \n')
            else:
                f.write(str(url_base+str(pdf_urls[0])) + ', \n')

    f.close()


if __name__ == '__main__':
    getCissContents()
