import idc
print  idc.gen_file(idc.OFILE_LST , '2.lst', 0, idc.BADADDR, 0)
import ida_pro 
ida_pro.qexit()
