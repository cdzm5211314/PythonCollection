import itertools

source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 写入数据条数
write_count = 0
print("写入中，请等待……")
# 组合,不重复
# 把1 - 33 的数字任意取6个写入到文件中
f = open("所有组合数据.txt","w+",encoding="utf-8")
for temp in list(itertools.combinations(source,6)):
    # 写入到文件的时候去掉元组括号
    write_count += 1
    print("正在写入第%s条数据!!!"%write_count)
    for num in temp:
        f.write(str(num)+" ")
    f.write('\n')
print("写入完成,共写入%d条数据..." %write_count)
f.close()


































