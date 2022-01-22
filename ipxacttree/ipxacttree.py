import os
import xml.etree.ElementTree as ET
import json
import re


class Node():
    def __init__(self,data):
       self.data = data

       self.tag = re.sub(r'{.*}', '', data.tag) # clean-up namespace
       self.text = None if data.text  == "\n" else data.text # use node instead of strange \n

       self.children = []
       self.parent = None
       self.level = 0

    def add(self,node):
        node.parent = self
        self.children.append(node)
        node.level = self.level + 1

    def __iter__(self):
        for child in self.children:
            yield child

    def __str__(self):
        return f"[{self.level}]{self.tag}[{len(self.children)}]: {self.text}"

class IPXACTTree():
    def __init__(self,ipxactfile):
        def iterate_tree(xmlnode,node):
            for child in xmlnode:
                cn = Node(child)
                node.add(cn)
                iterate_tree(child, cn)

        tree = ET.parse(ipxactfile)
        xmlroot = tree.getroot()

        self.root = Node(xmlroot)
        iterate_tree(xmlroot,self.root)

    def __iter__(self):
        def dfs_internal(node):
            yield node
            for child in node.children:
                yield from dfs_internal(child)
        yield from dfs_internal(self.root)

    def __str__(self):
        return "".join([("\t" * node.level)+ f"{node.tag}: {node.text}\n"  for node in self])

    def findall(self,tag):
        all = [node  for node in self if tag == node.tag]
        return all

