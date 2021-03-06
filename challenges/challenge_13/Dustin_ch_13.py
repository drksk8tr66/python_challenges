#!/usr/bin/env python3
"""
This module will iterate through the Input.txt and render an output in the format of the Output.dot
"""
from typing import List, Set, Dict, Tuple, Optional
from copy import deepcopy


class Tables:
    def __init__(self, name: str=None, f_name: str=None):
        self.name = name
        self.data: Dict[str, str] = {}
        self.f_name = f_name
        self.head = 'digraph G {\n' \
                    'graph [rankdir=LR, ranksep=2, pad="0.5", nodesep="0.5"];'\
                    '\nnode [shape=rectangle];'
        self.html = None
        self.conns: Dict[str, str] = {}

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
                    # last table not being added - BUG
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
        # solve for multiple connections - BUG
        # iterate through the data to find matching fields
        if not self.data:
            self.input_data()
        table_dat = self.data.items()
        working = deepcopy(self.data)
        table = working.popitem()
        match_gen = (field for field in table  if field in working.values())
        breakpoint()
        for table in self.data:
            # gen = (field for field in self.data['Accounts'] if field in self.data['Assigned_Rackers'])
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
