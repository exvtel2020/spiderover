import sys
def supermarket() :
   goods=['超土豪咖啡_8','宇宙无敌大榴莲_12','自动翻译笔记本_15','科比签名篮球_500','路飞草帽_1000']
   print("欢迎光临翡翠限量版超市")
   print("以下是我们的价目表：")
   i=0
   for good in goods:
       print(good.replace("_",":")+"元")
   ps=""
   chooselist=""
   total=0
   while ps !="x" :
       choosegoods=input("请选择您需要的商品序号以及购买量【例:1 3】(直到按住x结束):")
       if  choosegoods.lower()=="x" :
           ps="x"
           continue
       else :
           seq,volumns=choosegoods.split(' ')
           if  int(seq)>=1 and int(seq)<=len(goods)+1:
               pickgoods=goods[int(seq)-1]
               getpickgoods=pickgoods.split("_")
               chooselist+=getpickgoods[0]+"："+volumns+"件,共"+str(int(volumns)*int(getpickgoods[1]))+"元\r\n"
               #chooselist.append(getpickgoods[0]+"："+volumns+"件,共"+str(int(volumns)*int(getpickgoods[1]))+"元")
               total=total+int(volumns)*int(getpickgoods[1])
           else:
               print('Woops! 我们只售卖以上五种商品哦！新货品敬请期待！')
   ismember=input("请问您是否是会员(Y或者N)：")
   print("您的账单为:")
   print(chooselist[:-2])
   if ismember.lower()=="y":
       #print(1)
       #print(chooselist)
       # for citem in chooselist :
       #     print(citem)
       print("您的总价为:%s元" % str(total))
       print("您的会员总价为:%s元" % str(total*0.9))
   else :
       print("您的总价为:%s元" % str(total))
if __name__ == '__main__':
    supermarket()