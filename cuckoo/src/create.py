f = open('command.sh', 'w')
for i in range(178, 315):
    #f.writelines("cp /media/huydung/Storage/data-huydung/REPORTS/Zeus/"+str(i)+"/reports/report.json /media/huydung/Storage/data-huydung/REPORTS/src/json_zeus/"+str(i)+"report.json\n")
    #f.writelines("cp ~/.cuckoo/storage/analyses/"+str(i)+"/reports/report.json /media/huydung/Storage/data-huydung/REPORTS/src/json_kelihos2/"+str(i+135)+"report.json\n")        
    f.writelines("cp /media/huydung/Storage/data-huydung/REPORTS/Locky/"+str(i)+"/reports/report.json /media/huydung/Storage/data-huydung/REPORTS/src/json_locky/"+str(i-177)+"report.json\n")
        
f.close()