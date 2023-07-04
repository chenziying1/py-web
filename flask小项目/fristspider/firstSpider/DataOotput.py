import codecs

class DataOutput(object):
    def __init__(self):
        self.datas = []

    def store_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = codecs.open('baike.html','w',encoding='utf-8')
        fout.write("<html>")
        fout.write("<head><meta charset='utf-8' /></head>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            print("1")
            fout.write("<tr>")
            print("1")
            fout.write("<td>%s</td>"%data['url'])
            print("1")
            fout.write("<td>%s</td>"%data['title'])
            print("1")
            fout.write("<td>%s</td>"%data['summary'])
            print("1")
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()