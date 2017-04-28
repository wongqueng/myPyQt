# -*-coding:UTF-8-*-
def parstr(num):
    if str(num).count("万"):
        int_num=num.replace("万","")
        return str(float(int_num)*10000)
    return num
print parstr("1.5")