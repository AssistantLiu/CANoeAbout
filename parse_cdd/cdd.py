
import os

from lxml.html import etree


class mainClass(object):
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def get_abspath(self,file_suffix):
        ''' this function will get all filter files of  folder'''
        root_path = os.path.dirname(os.path.abspath(__file__))  # log文件的目录
        fileList = os.listdir(root_path)
        for file in fileList:
            if file.split(".")[-1] == file_suffix:
                self.get_files= os.path.join(root_path, file)
                print(self.get_files)
                return self.get_files


    def parseCdd(self,filename):
        cddXML = etree.parse(filename)
        if cddXML:
            ecu = cddXML.xpath("//VAR//DIAGINST//SERVICE//SHORTCUTNAME/TUV/text()")
            if ecu:
                self.diagCan = ''
                for i in ecu:
                    temp = i.replace("/","_").replace("#","_").replace(": ","_").replace(":","_").replace("  ","_").replace(" - ","_").replace("-","_").replace(" ","_")
                    self.diagCan = self.diagCan + "\n" + "diagRequest    " + temp +"    req_" + temp + ";"
                self.diagCan = "variables\n{\n%s\n}"%self.diagCan
                print(self.diagCan.encode("utf-8"))
                newFile = os.path.splitext(filename)[0] + '_DiagRequest_Variables.cin'
                with open(newFile,'w') as f:
                    f.write(self.diagCan)
            else:
                print("parse cdd file failed!")
        else:
            print("parse file failed!")


if __name__ == '__main__':
    c = mainClass()
    c.parseCdd("BYD_SC2E.cdd")

