"""
This module will iterate through the Input.txt and render an output in the format of the Output.dot
"""


class Tables:
    def __init__(self, name: str=None, f_name: str=None):
        self.name = name
        self.data = {}
        self.f_name = f_name
        self.head = 'digraph G {\n' \
                    'graph [rankdir=LR, ranksep=2, pad="0.5", nodesep="0.5"];\n' \
                    'node [shape=rectangle];'
        self.html = None
        self.conns = {}

    def input_data(self):
        # reads input file to parse tables and fields into data structure
        f = open(self.f_name, 'r')
        l = []
        t = None
        for i in f.readlines():
            k = i.split(':')[0]
            v = i.split(':')[1]
            if k == 'Table':
                # when table is found, add the list of fields to the dict, reset list of fields and table name
                if l and t:
                    self.data[t] = l
                    l = []
                t = v.strip('\n').strip(' ')
            elif k == 'Field':
                # when field is found, add field name to list of fields
                l.append(v.strip('\n').strip(' '))

    def generate_html(self):
        # format the data into html structure
        self.html = self.head + '\n'
        for table in self.data:
            i = 1
            self.html += '{0} [label=<<table border="0" cellborder="0" cellspacing="0"> \n' \
                         '<tr><td><i><b>{0}</b></i></td></tr><hr/> \n'.format(table)
            for field in self.data[table]:
                self.html += '<tr><td port="{0}">{1}</td></tr> \n'.format(i, field)
                i += 1
            self.html += '</table>>]; \n'

    def generate_connections(self):
        # iterate through the data to find matching fields
        if not self.data:
            self.input_data()
        for table in self.data:
            f = 1
            for field in self.data[table]:
                for table2 in self.data:
                    if table == table2:
                        pass
                    else:
                        if field in self.data[table2]:
                            self.conns['{0}:{1}'.format(table, f)] = \
                                '{0}:{1}'.format(table2, self.data[table2].index(field) + 1)
                f += 1

    def conns_to_html(self):
        # add the connections to the bottom of the html
        if not self.conns:
            self.generate_connections()
        if not self.html:
            self.generate_html()
        for k in self.conns:
            self.html += '\n' + '{0} -> {1};'.format(k, self.conns[k])
        self.html += '\n}'

    def save_output(self):
        # save the file to a .dot output
        if not self.html:
            self.generate_html()
        if not self.conns:
            self.generate_connections()
            self.conns_to_html()
        file = open('Dustin_Output.dot', 'w', newline='')
        file.write(self.html)
        file.close()


if __name__ == '__main__':
    nam = 'Input'
    inp = 'Input.txt'
    Tab = Tables(nam, inp)
    Tab.input_data()
    Tab.generate_html()
    Tab.generate_connections()
    Tab.conns_to_html()
    Tab.save_output()
