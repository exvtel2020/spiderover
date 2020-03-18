#contact id:heliang01
from datetime import datetime
import os
import random
def supermarket_upgrade(member="") :
   goods=['超土豪咖啡_8','宇宙无敌大榴莲_12','自动翻译笔记本_15','科比签名篮球_500','路飞草帽_1000']
   print("欢迎光临翡翠限量版超市")
   print("以下是我们的价目表：")
   i=1
   for good in goods:
       print(str(i)+"."+good.replace("_",":")+"元")
       i=i+1
   ps=""
   chooselist=""
   choosepick=[]
   total=0
   markgoods=[]
   bill=[]
   while ps !="x" :
       choosegoods=input("请选择您需要的商品序号以及购买量【例:1 3】(直到按住x结束):")
       if  choosegoods.lower()=="x" :
           ps="x"
           continue
       else :
           markgoods=choosegoods.strip().split()
           if len(markgoods)>=3 :
               print("输入方式有误，例1 3或者x")
               continue
           if len(markgoods)<2  :
               print("您输入项是1项，缺少产品序号或者数量.")
               continue
           seq,volumns=choosegoods.strip().split()
           if  int(seq)>=1 and int(seq)<=len(goods)+1:
               pickgoods=goods[int(seq)-1]
               getpickgoods=pickgoods.split("_")
               chooselist+=getpickgoods[0]+"："+volumns+"件,共"+str(int(volumns)*int(getpickgoods[1]))+"元\r\n"
               choosepick.append(getpickgoods[0]+"："+volumns+"件,共"+str(int(volumns)*int(getpickgoods[1]))+"元")
               #chooselist.append(getpickgoods[0]+"："+volumns+"件,共"+str(int(volumns)*int(getpickgoods[1]))+"元")
               total=total+int(volumns)*int(getpickgoods[1])

           else:
               print('Woops! 我们只售卖以上五种商品哦！新货品敬请期待！')
   if len(chooselist)<=0 :
       print("您没有购买任何东西!")
       return False
   #ismember=input("请问您是否是会员(Y或者N)：")
   ismember=""
   if member=="no" :
       ismember==False
   else :
       ismember=checkismember(member)
   print("您的账单为:")
   print(chooselist[:-2])
   if ismember==True:
       #print(1)
       #print(chooselist)
       # for citem in chooselist :
       #     print(citem)
       print("您的总价为:%s元" % str(total))
       print("您的会员总价为:%s元" % str(total*0.9))
       bill.append(choosepick)
       bill.append(total)
       bill.append(total*0.9)
       return bill
   else :
       print("您的总价为:%s元" % str(total))
       bill.append(choosepick)
       bill.append(total)
       return bill
def customer() :
    #everydaycustoms={}
    folder=os.getcwd()+r'\stageone\\'
    #print(folder)
    #exit()
    datefornow=datetime.now().strftime("%Y-%m-%d")

    #print(datetime.now().strftime("%Y-%m-%d"))
    if not os.path.exists(folder) :
        os.mkdir(folder)
        everydaycollections = folder + 'supermarket_' + datefornow + ".txt"
        for items in range(1,12) :
            print("欢迎光临，第%s号顾客" % items)
            tomember = ""
            membership = input("如果您有会员号,请输入(如果没有输入no):")
            if membership == "no":
                tomember = "none"
                memberadd = input("请问是否需要加入会员？(是的选Y或不需要则选N):")
                if memberadd.lower() == "y":
                    membershipadd = genmemno()
            elif checkismember(membership) == False:
                tomember = "none"
                memberadd = input("您的账号在系统中不存在!请问是否需要加入会员？(是的选Y或不需要则选N):")
                if memberadd.lower() == "y":
                    membershipadd = genmemno()
            else:
                tomember = membership
            getcustom = []
            getcustom.append(items)
            getcustom.append(tomember)
            getcustom.append(customer(membership))
            if items==11 :
                print("今日已闭店，欢迎您明天光临")
                file = open(everydaycollections, "w+")
                file.write("close your mouth")
                file.close()




    else :
        everydaycollections = folder + 'supermarket_' + datefornow + ".txt"
        if os.path.exists(everydaycollections) :
            return False
        else :
            for items in range(1,12) :
                if items==11 :
                    print("今日已闭店，欢迎您明天光临")
                else :
                    print("欢迎光临，第%s号顾客"%items)
                    file = open(everydaycollections,"w+")
                    file.write("close your mouth")
                    file.close()
def checkismember(code="") :
    membercontainer=os.getcwd()+r'\members.txt'
    if os.path.exists(membercontainer) :
        openthelid=open(membercontainer,"r")
        mytext=openthelid.readlines()
        openthelid.close()
        membercheck=False
        for line in mytext :
            linelist=line.split()
            #print(linelist)
            if code==linelist[0] and linelist[1]=="1" :
                membercheck=True
                break
            else :
                continue
        return membercheck
    else :
        return False
def genmemno() :
    return "S"+str(random.randrange(1000001,1999999))
if __name__ == '__main__':
    #startmemberlist = ["158", "253", "398"]
    #print(supermarket_upgrade())
    #customer()
    #print(checkismember("S1000356"))
    #print("")
    #(supermarket_upgrade("S1000356"))
    #customer()
    print(genmemno())