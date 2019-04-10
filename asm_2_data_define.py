import sys

def asm_data_define(asm_code):
    # 1. Bien dem db
    dbCounter = 0
    # 2. Bien dem dd
    ddCounter = 0
    # 3. Bien dem dw
    dwCounter = 0
    # 4. Bien dem db so luong db, dc, dw
    dcCounter = 0
    # 5. Bien dem db voi parameter == 0
    db0Counter = 0
    # 6. Bien dem db voi parameter != 0
    dbN0Counter = 0

    all = 0
    text = 0
    rdata = 0
    data = 0


    # Bien dem dd trong text section
    dd_text = 0
    # Bien dem db trong text section
    db_text = 0
    # Bien dem dd trong rdata section
    dd_rdata = 0
    # Bien dem db voi mot tham so != 0 trong phan rdata
    db3_rdata = 0
    # Bien dem db voi mot tham so != 0 trong phan data
    db3_data = 0
    # Bien dem db voi mot tham so != 0 trong ca file
    db3_all = 0
    # Bien dem dd voi 4 param
    dd4 = 0
    # Bien dem dd voi 5 param
    dd5 = 0
    # Bien dem dd voi 6 param
    dd6 = 0

    text = 0
    rdata = 0
    data = 0
    idata = 0
    # NotdataNottext
    NdNt = 0

    # Bien dem db voi param != 0 trong section idata
    db3_idata = 0
    db3_text = 0
    db3_rsrc = 0
    db3_NdNt = 0

    db3_zero = 0

    # Bien dem dd voi 4 param trong section chua xac dinh
    dd4_NdNt = 0
    # Bien dem dd voi 5 param trong section chua xac dinh
    dd5_NdNt = 0
    # Bien dem dd voi 6 param trong section chua xac dinh
    dd6_NdNt = 0

    i = 0
    for row in asm_code:
        # Doc ra cac thanh phan co trong mot dong code asm
        RowItems = row.split()
        # Doc ra section cua dong code
        Section = row.split(':')[0]
        
        # i += 1
        # if (i == 100):
        #     sys.exit()
        # Doc ra row loai bo dau ","
        RowComma = row.split(',')
        
        all += 1
        dbCounter += RowItems.count('db')
        ddCounter += RowItems.count('dd')
        dwCounter += RowItems.count('dw')
        if len(RowItems)>3:
            if RowItems[1]=='00' and RowItems[2]=='db':
                db0Counter += 1

        if Section=='.text':
            text +=1
            dd_text += RowItems.count('dd')
            db_text += RowItems.count('db')
        elif Section=='.rdata':
            rdata +=1
            dd_rdata += RowItems.count('dd')
            if len(RowItems) == 4 or len(RowItems) == 6:
                if RowItems[2] == 'db':
                    db3_rdata += RowItems.count('db')
        elif Section=='.data':
            data +=1
            if len(RowItems) == 4 or len(RowItems) == 6:
                if RowItems[2] == 'db':
                    db3_data += RowItems.count('db')
        elif Section=='.idata':
            idata +=1
            if len(RowItems) == 4 or len(RowItems) == 6:
                if RowItems[2] == 'db':
                    db3_idata += 1
        else:
            NdNt += 1
            if len(RowItems) == 4 or len(RowItems) == 6:
                if RowItems[2] == 'db':
                    db3_NdNt += 1

            if len(RowComma)==4:
                dd4_NdNt += RowItems.count('dd')

            if len(RowComma)==5:
                dd5_NdNt += RowItems.count('dd')

            if len(RowComma)==6:
                dd6_NdNt += RowItems.count('dd')

        if len(RowComma)==4:
            dd4 += RowItems.count('dd') # 13.

        if len(RowComma)==5:
            dd5 += RowItems.count('dd') # 14.

        if len(RowComma)==6:
            dd6 += RowItems.count('dd') # 15.

        if len(RowItems) == 4 or len(RowItems) == 6:
            if RowItems[2] == 'db':
                db3_all += 1
                if RowItems[1] == '00':
                    db3_zero += 1


    dcCounter = dbCounter + ddCounter + dwCounter
    # 1.
    db_por = float(dbCounter)/all
    # 2.
    dd_por = float(ddCounter)/all
    # 3.
    dw_por = float(dwCounter)/all
    # 4.
    dc_por = float(dcCounter)/all
    
    db0_por = dbN0_por = 0
    if dbCounter!=0:
        db0_por = float(db0Counter)/dbCounter # 5.
        dbN0_por = float(dbCounter - db0Counter)/dbCounter # 6.

    ############################

    Res_dd_text = 0
    Res_db_text = 0
    Res_dd_rdata = 0
    Res_db3_rdata = 0
    Res_db3_data = 0

    if text!=0:
        Res_dd_text = float(dd_text)/text   # 7.
        Res_db_text = float(db_text)/text   # 8.

    if rdata!=0:
        Res_dd_rdata = float(dd_rdata)/rdata    # 9.
        Res_db3_rdata = float(db3_rdata)/rdata  # 10.

    if data!=0:
        Res_db3_data = float(db3_data)/data # 11.

    Res_db3_all = float(db3_all)/all    # 12.

    Res_dd4_all = float(dd4)/all    # 16.
    Res_dd5_all = float(dd5)/all    # 17.
    Res_dd6_all = float(dd6)/all    # 18.

    Output = [Res_dd_text,Res_db_text,Res_dd_rdata,Res_db3_rdata \
              , Res_db3_data, Res_db3_all, dd4, dd5, dd6 \
              , Res_dd4_all, Res_dd5_all, Res_dd6_all]


    Res_db3_idata = 0
    Res_db3_NdNt = 0
    Res_dd4_NdNt = 0
    Res_dd5_NdNt = 0
    Res_dd6_NdNt = 0
    Res_db3_all_zero = 0

    if idata!=0:
        Res_db3_idata = float(db3_idata)/idata # 19.

    if NdNt!=0:
        Res_db3_NdNt = float(db3_NdNt)/NdNt # 20.
        Res_dd4_NdNt = float(dd4_NdNt)/NdNt # 21.
        Res_dd5_NdNt = float(dd5_NdNt)/NdNt # 22.
        Res_dd6_NdNt = float(dd6_NdNt)/NdNt # 23.

    if db3_all!=0:
        Res_db3_all_zero = float(db3_zero)/db3_all # 24.

    Output2 = [Res_db3_idata, Res_db3_NdNt, Res_dd4_NdNt \
              , Res_dd5_NdNt, Res_dd6_NdNt, Res_db3_all_zero ]
    return [db_por, dd_por, dw_por, dc_por, db0_por, dbN0_por] + Output + Output2

file_path = "samples/01IsoiSMh5gxyDYTl4CB.asm"
with open(file_path) as f:
    byte_code = f.readlines()

print asm_data_define(byte_code)
