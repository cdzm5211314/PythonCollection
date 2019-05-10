import pymysql

# 链接数据库
host = "localhost"
port = 3306
user = "root"
passwd = "root"
db = "ssqdb"

def get_write_file(file):
    # 链接数据库
    connect = pymysql.Connect(host=host, port=3306, user=user, passwd=passwd, db=db, charset='utf8')
    print("写入中，请等待……")
    # 光标
    cursor = connect.cursor()
    # 执行sql语句
    sql = "SELECT redOne,redTwo,redThree,redFour,redFive,redSix FROM excel ORDER BY redOne ASC,redTwo ASC,redThree ASC,redFour ASC,redFive ASC,redSix ASC"
    cursor.execute(sql)
    number = cursor.fetchall()
    # 打开文件
    f = open(file,"w+",encoding="utf-8")
    # 查询数据条数
    select_count = 0
    for tempNumber in number:
        # print(tempNumber,type(tempNumber))
        # 计算查询数据条数
        select_count += 1
        # 写入查询到的数据到文件中
        for temp in tempNumber:
            f.write(str(temp) + " ")
        f.write('\n')
        # f.write(str(tempNumber[0]))
    f.close()
    cursor.close()
    connect.close()
    print("写入完成,共写入%d条数据……" %select_count)

if __name__ == "__main__":
    file = "E:\workspace_PyCharm\ShuangSeQiu\往期中奖数据.txt"
    get_write_file(file)