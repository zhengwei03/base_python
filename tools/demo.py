#!/usr/bin/env python
from PyPDF2 import PdfFileReader
from pptx import Presentation


import zipfile
import xml.etree.ElementTree as ET

import olefile
from oletools.common.io_encoding import ensure_stdout_handles_unicode
import comtypes.client


def init_powerpoint():
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1
    return powerpoint


def ppt_to_pdf(powerpoint, inputFileName, outputFileName, formatType = 32):
    if outputFileName[-3:] != 'pdf':
        outputFileName = outputFileName + ".pdf"
    deck = powerpoint.Presentations.Open(inputFileName)
    deck.SaveAs(outputFileName, formatType) # formatType = 32 for ppt to pdf
    deck.Close()

def process_ole(filename):
    ole = olefile.OleFileIO(filename)
    meta = ole.get_metadata()
    ensure_stdout_handles_unicode()
    data = {}
    for prop in meta.SUMMARY_ATTRIBS:
        value = getattr(meta, prop)
        if value is not None:
            if prop == "num_pages":
                data[prop] = value
            if prop == "author":
                data[prop] = value.replace("\x00", "")

    return data





def get_num_pages(file_path):
    """
    获取文件总页码
    :param file_path: 文件路径
    :return:
    """
    reader = PdfFileReader(file_path)
    # 不解密可能会报错：PyPDF2.utils.PdfReadError: File has not been decrypted
    if reader.isEncrypted:
        reader.decrypt('')
    page_num = reader.getNumPages()
    return page_num




def get_pptx_page(pptx_path):
    try:
        p = Presentation(pptx_path)

        page = len(p.slides)
    except KeyError as e:
        print(e)
        page = 0
    return page

def getPages(filename):
    with zipfile.ZipFile(filename) as docx:
        tree = ET.XML(docx.read('docProps/app.xml'))
        switch = 1
        for child in tree:
            # print(child.tag.find('Pages'))

            if child.tag.find('Pages') != -1:
                # if child.tag.find('Pages') == 75 and switch:
                #     switch = 0
                #     continue
                return child.text
                # return child.tag.find('Pages')
        # return "child.tag.find('Pages')"

if __name__ == '__main__':
    print("doc信息", process_ole(r"E:\python_test\geshi\document\DOC\C6914A609923FE57DC891549F230B4D3"))
    print("docx信息", getPages(r"E:\python_test\geshi\document\DOCX\3F26695913AE98CB6FFA2E373C002521.docx"))


    print("pdf页码", get_num_pages(r"E:\python_test\geshi\document\PDF\2C1F563C4ACBB5C58923E6FC81A4916D"))

    print("PPTX页码", get_pptx_page(r"E:\python_test\geshi\document\PPTX\6E69A3EEF743FC60845A60119AA9C8F2"))
    powerpoint = init_powerpoint()
    ppt_to_pdf(powerpoint, "E:\python_test\geshi\document\PPT\pp.ppt", "E:\python_test\geshi\document\DOCX\pp.pdf")
    powerpoint.Quit()
    print("ppt页码", get_num_pages(r"E:\python_test\geshi\document\DOCX\pp.pdf"))




    # document = zipfile.ZipFile(r'E:\python_test\geshi\document\DOCX\3F26695913AE98CB6FFA2E373C002521.docx')
    #
    # xml = document.read("word/document.xml")
    #
    # wordObj = BeautifulSoup(xml.decode("utf-8"))
    #
    # texts = wordObj.findAll("w:t")
    #
    # for text in texts:
    #     print(text.text)




