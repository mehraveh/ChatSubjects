

def filtering(str, words):
    if str.endswith("ها") :
        str = str.replace("ها" , "")
    elif str.endswith("هاش"):
        str = str.replace("هاش" ,"")
    elif str.endswith("های"):
        str = str.replace("هاش" , "")
    str_tmp = str
    if len(str_tmp) > 0:
        str_tmp = str.replace(str[len(str)-1] ,"")
        if str_tmp in words and str not in words:
            print("yes")
            str = str_tmp
    return str

