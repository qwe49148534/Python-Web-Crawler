'''
輸入對應的點餐編號會自動總結金額
'''

food={'1':'官保雞丁'
      ,'2':'青椒雞米粒'
      ,'3':'豆腐包肉'
      ,'4':'涼拌藕'
      ,'5':'红燒南瓜' 
      ,'6':'大白菜'
      , '7':'荷包蛋'
      ,'8':'蛋炒飯'}

price = {'官保雞丁':150,
         '青椒雞米粒':130,
         '豆腐包肉':100,'涼拌藕':100,
         '红燒南瓜':80,'大白菜':80, 
         '荷包蛋':15,'蛋炒飯':80}

num= input("請輸人你要的餐點編號").split()
total = 0
for i in num:
    print(food[i])
total = total + price[food[i]]
print(total)