import xlrd
import requests

read_path = "待下载表格.xls"
bk = xlrd.open_workbook(read_path)
shxrange = range(bk.nsheets)
sh = bk.sheet_by_index(0)
# 获取总行数
nrows = sh.nrows
print("共有 "+str(nrows)+" 组数据；")
for i in range(nrows):
    print("正在下载第"+str(i+1)+"组图片")
    url1 = sh.cell_value(i, 6)  # 依次读取每行第5列的数据，也就是 URL
    url2 = sh.cell_value(i, 7)  # 依次读取每行第5列的数据，也就是 URL
    name1 = sh.cell_value(i, 2) + '-图片名称1'  # 读取图片名称
    name2 = sh.cell_value(i, 2) + '-图片名称2'  # 读取图片名称
    f1 = requests.get(url1)  # 下载图片
    f2 = requests.get(url2)  # 下载图片
    pic_name1 = "./Down_Pic/" + name1 + "." + "jpg"  # 构造完整文件路径+名称
    with open(pic_name1, "wb") as code1:
        code1.write(f1.content)  # 保存文件
    pic_name2 = "./Down_Pic/" + name2 + "." + "jpg"  # 构造完整文件路径+名称
    with open(pic_name2, "wb") as code2:
        code2.write(f2.content)  # 保存文件
print("-- 已下载完成！--")
