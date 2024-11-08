fr = open('C:\\Users\\29174\\Desktop\\Code\\python\\hello\\文件\\bill.txt','r',encoding='utf8')
fw = open('C:\\Users\\29174\\Desktop\\Code\\python\\hello\\文件\\bill.txt.bak','w',encoding='utf8')

for line in fr:
    line = line.strip()
    if line.split(',')[4] == '测试':
        continue        #continue进入下一次循环,这一次后面的内容就跳过了
    else:
        fw.write(line)
        fw.write('\n')
fr.close()
fw.close()

