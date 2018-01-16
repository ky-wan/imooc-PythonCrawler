class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        # 在windows下新文件的默认编码是gbk，需手动改为utf-8
        fout = open('output.html', 'w', encoding='utf-8')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<a>")

        for data in self.datas:
            # 注释掉原来的，重新写一个更美观的输出效果
            # fout.write("<tr>")
            # fout.write("<td>%s</td>" % data['url'])
            # fout.write("<td>%s</td>" % data['title'])
            # fout.write("<td>%s</td>" % data['summary'])
            # fout.write("</tr>")
            fout.write('<a href="%s">%s</a>' % (data['url'], data['title']))
            fout.write('<p>%s</p>' % data['summary'])

        fout.write("</a>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()

