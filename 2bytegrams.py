# ham doc 2 bytes trong file .bytes
# params: tung dong cua file
# returns: mang chua tan suat xuat hien 2 bytes trong file
def byte_2gram(byte_code):
    # khai bao 1 mang gom 16^4 phan tu de luu so lan xuat hien cua 0x00 0x00->0xFF 0xFF
    # khoi tao gia tri bang 0
    twoByte = [0]*16**4
    for row in byte_code:
        codes = row.split()[1:]
        codes_2g = codes[:-1]
        for i in range(len(codes_2g)):
            codes_2g[i]+= codes[i+1]
        # doc hai bytes mot va chuyen ve decimal
        twoByteCode = []
        for i in codes_2g:
            if '??' not in i:
                twoByteCode += [int(i,16)]
        # dem so lan xuat hien
        for i in twoByteCode:
            twoByte[i] += 1
        print (twoByte)
    return twoByte
# --------------------------------------------------------------------------------------------


#
# params: asm_code
# returns: 
def asm_data_define(asm_code):
    dbCounter = 0
    ddCounter = 0
    dwCounter = 0
    dcCounter = 0
    db0Counter = 0
    dbN0Counter = 0

    all = 0
    text = 0
    rdata = 0
    data = 0
    dd_text = 0
    db_text = 0
    dd_rdata = 0
    db3_rdata = 0
    db3_data = 0
    db3_all = 0
    dd4 = 0
    dd5 = 0
    dd6 = 0

    all = 0

    text = 0
    rdata = 0
    data = 0
    idata = 0
    # NotdataNottext
    NdNt = 0

    db3_idata = 0
    db3_text = 0
    db3_rsrc = 0
    db3_NdNt = 0
    db3_all = 0
    db3_zero = 0

    dd_text = 0
    db_text = 0
    dd_rdata = 0
    db3_data = 0
    db3_all = 0
    dd4_NdNt = 0
    dd5_NdNt = 0
    dd6_NdNt = 0

    for row in asm_code:
        RowItems = row.split()
        Section = row.split(':')[0]
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

        if len(RowItems) == 4 or len(RowItems) == 6:
                if RowItems[2] == 'db':
                    db3_all += RowItems.count('db')
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
            dd4 += RowItems.count('dd')

        if len(RowComma)==5:
            dd5 += RowItems.count('dd')

        if len(RowComma)==6:
            dd6 += RowItems.count('dd')

        if len(RowItems) == 4 or len(RowItems) == 6:
            if RowItems[2] == 'db':
                db3_all += 1
                if RowItems[1] == '00':
                    db3_zero += 1


    dcCounter = dbCounter + ddCounter + dwCounter
    db_por = float(dbCounter)/all
    dd_por = float(ddCounter)/all
    dw_por = float(dwCounter)/all
    dc_por = float(dcCounter)/all
    db0_por = dbN0_por = 0
    if dbCounter!=0:
        db0_por = float(db0Counter)/dbCounter
        dbN0_por = float(dbCounter - db0Counter)/dbCounter

    ############################

    Res_dd_text = 0
    Res_db_text = 0
    Res_dd_rdata = 0
    Res_db3_rdata = 0
    Res_db3_data = 0

    if text!=0:
        Res_dd_text = float(dd_text)/text
        Res_db_text = float(db_text)/text

    if rdata!=0:
        Res_dd_rdata = float(dd_rdata)/rdata
        Res_db3_rdata = float(db3_rdata)/rdata

    if data!=0:
        Res_db3_data = float(db3_data)/data

    Res_db3_all = float(db3_all)/all

    Res_dd4_all = float(dd4)/all
    Res_dd5_all = float(dd5)/all
    Res_dd6_all = float(dd6)/all

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
        Res_db3_idata = float(db3_idata)/idata

    if NdNt!=0:
        Res_db3_NdNt = float(db3_NdNt)/NdNt
        Res_dd4_NdNt = float(dd4_NdNt)/NdNt
        Res_dd5_NdNt = float(dd5_NdNt)/NdNt
        Res_dd6_NdNt = float(dd6_NdNt)/NdNt

    if db3_all!=0:
        Res_db3_all_zero = float(db3_zero)/db3_all

    Output2 = [Res_db3_idata, Res_db3_NdNt, Res_dd4_NdNt \
              , Res_dd5_NdNt, Res_dd6_NdNt, Res_db3_all_zero ]


    #print [db_por, dd_por, dw_por, dc_por, db0_por, dbN0_por] + Output + Output2
    return [db_por, dd_por, dw_por, dc_por, db0_por, dbN0_por] + Output + Output2

