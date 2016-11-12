#encoding=utf-8
Volume = float(raw_input("油箱体积（升）："))
Current_Volume = float(raw_input("当前油箱剩余油量（百分比）："))
DistancePer = float(raw_input("每升油可以走多远（km）："))
print Volume, Current_Volume, DistancePer
# 当前剩余油量还能行驶的路程
Current_distance = (Volume * Current_Volume - 5) * DistancePer
times = int(Current_distance / 200)
print times
if times == 0:
    print u"剩余油量：%s升，还能行驶：%skm，需要在当前的加油站加油。" %(Volume * Current_Volume, Current_distance)
else:
    print u"剩余油量：%s升，还能行驶：%skm，在接下来第%d个加油站加油即可。" % (Volume * Current_Volume, Current_distance, times)
