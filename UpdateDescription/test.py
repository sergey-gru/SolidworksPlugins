# -*- coding: utf-8 -*-

from PathInfo import PathInfo


def Test(parr: list, sarr: list):
    """Unit test function"""
    
    s: str = ""
    n: int = len(parr)
    ok: int = 0
    p2 = PathInfo()
    
    for i in range(n):
        p2.SetPath(sarr[i])
        
        if parr[i] == p2:
            ok += 1
        else:
            s = s + "i=" + str(i) + ": err\n"
            s = s + "string: " + sarr[i] + "\n"
            s = s + "PathInfo:\n" + p2.__str__() + "\n"

    print("Completed " + str(ok) + " of " + str(n), "Reports:", s, sep="\n")


def InitTest1():
    
    parr = []
    sarr = []
    
    #Empty string
    sarr.append("")
    
    p = PathInfo()
    parr.append(p)
    

    #Test dir/name^at.ext
    #DIR
    
    sarr.append("/")
    p = PathInfo()
    p.dir = ""
    p.name = ""
    p.at = ""
    p.ext = ""
    p.id = ""
    p.id_base = ""
    p.rev = ""
    p.kind = ""
    p.desc = ""
    parr.append(p)
    
    
    p = PathInfo()
    sarr.append("/dir/")
    p.dir = "/dir"
    p.name = ""
    p.at = ""
    p.ext = ""
    p.id = ""
    p.id_base = ""
    p.rev = ""
    p.kind = ""
    p.desc = ""
    parr.append(p)
    
    
    p = PathInfo()
    sarr.append("\\di r\\")
    p.dir = "\\di r"
    p.name = ""
    p.at = ""
    p.ext = ""
    p.id = ""
    p.id_base = ""
    p.rev = ""
    p.kind = ""
    p.desc = ""
    parr.append(p)
    
    
    p = PathInfo()
    sarr.append("\\dir/dir1\\dir2\\")
    p.dir = "\\dir/dir1\\dir2"
    p.name = ""
    p.at = ""
    p.ext = ""
    p.id = ""
    p.id_base = ""
    p.rev = ""
    p.kind = ""
    p.desc = ""
    parr.append(p)
    
    
    #NAME
    
    p = PathInfo()
    sarr.append("/d i r/d i r2/ n ame")
    p.dir = "/d i r/d i r2"
    p.name = " n ame"
    p.at = ""
    p.ext = ""
    p.id = ""
    p.id_base = ""
    p.rev = ""
    p.kind = ""
    p.desc = "n ame"
    parr.append(p)
    
    
    p = PathInfo()
    sarr.append("/ name")
    p.dir = ""
    p.name = " name"
    p.at = ""
    p.ext = ""
    p.id = ""
    p.id_base = ""
    p.rev = ""
    p.kind = ""
    p.desc = "name"
    parr.append(p)
    
    
    p = PathInfo()
    sarr.append("/d i r/dir2/n a m e")
    p.dir = "/d i r/dir2"
    p.name = "n a m e"
    p.at = ""
    p.ext = ""
    p.id = "n"
    p.id_base = "n"
    p.rev = ""
    p.kind = ""
    p.desc = "a m e"
    parr.append(p)
    
    
    p = PathInfo()
    sarr.append("name_-+1.")
    p.dir = ""
    p.name = "name_-+1"
    p.at = ""
    p.ext = ""
    p.id = "name"
    p.id_base = "name"
    p.rev = ""
    p.kind = "-+1"
    p.desc = ""
    parr.append(p)
    
    
    #AT
    
    p = PathInfo()
    sarr.append("/d i r/di r2/name^^")
    p.dir = "/d i r/di r2"
    p.name = "name^"
    p.at = ""
    p.ext = ""
    p.id = ""
    p.id_base = ""
    p.rev = ""
    p.kind = ""
    p.desc = "name^"
    parr.append(p)
    
    
    p = PathInfo()
    sarr.append("/d i r/di r2/name^^at")
    p.dir = "/d i r/di r2"
    p.name = "name^"
    p.at = "at"
    p.ext = ""
    p.id = ""
    p.id_base = ""
    p.rev = ""
    p.kind = ""
    p.desc = "name^"
    parr.append(p)
    
    
    p = PathInfo()
    sarr.append("/d i r/di r2/name^at")
    p.dir = "/d i r/di r2"
    p.name = "name"
    p.at = "at"
    p.ext = ""
    p.id = ""
    p.id_base = ""
    p.rev = ""
    p.kind = ""
    p.desc = "name"
    parr.append(p)
    
    
    
    #EXT
    
    p = PathInfo()
    sarr.append("/d i r/di r2/name^.ext")
    p.dir = "/d i r/di r2"
    p.name = "name"
    p.at = ""
    p.ext = "ext"
    p.id = ""
    p.id_base = ""
    p.rev = ""
    p.kind = ""
    p.desc = "name"
    parr.append(p)
    
    
    p = PathInfo()
    sarr.append("/d i r/di r2/name^at.ext")
    p.dir = "/d i r/di r2"
    p.name = "name"
    p.at = "at"
    p.ext = "ext"
    p.id = ""
    p.id_base = ""
    p.rev = ""
    p.kind = ""
    p.desc = "name"
    parr.append(p)
    
    
    #DIR/NAME^AT.EXT
    
    p = PathInfo()
    sarr.append("/dir/di.r2/na.me^^at")
    p.dir = "/dir/di.r2"
    p.name = "na.me^"
    p.at = "at"
    p.ext = ""
    p.id = ""
    p.id_base = ""
    p.rev = ""
    p.kind = ""
    p.desc = "na.me^"
    parr.append(p)
    
    
    p = PathInfo()
    sarr.append("/dir/di^r2/na.me^at")
    p.dir = "/dir/di^r2"
    p.name = "na.me"
    p.at = "at"
    p.ext = ""
    p.id = ""
    p.id_base = ""
    p.rev = ""
    p.kind = ""
    p.desc = "na.me"
    parr.append(p)
    
    
    p = PathInfo()
    sarr.append("/dir/di^r2/name .ext")
    p.dir = "/dir/di^r2"
    p.name = "name "
    p.at = ""
    p.ext = "ext"
    p.id = "name"
    p.id_base = "name"
    p.rev = ""
    p.kind = ""
    p.desc = ""
    parr.append(p)
    
    
    Test(parr, sarr)
    


def InitTest2():
    
    parr = []
    sarr = []
    
    #Empty string
    sarr.append("")
    
    p = PathInfo()
    parr.append(p)
    
    

    #Test dir/name^at.ext
    #DIR
    
    p = PathInfo()
    sarr.append("/")
    p.dir = ""
    p.name = ""
    p.at = ""
    p.ext = ""
    p.id = ""
    p.id_base = ""
    p.rev = ""
    p.kind = ""
    p.desc = ""
    parr.append(p)
    
    
    
    #DIR/NAME^AT.EXT
    
    p = PathInfo()
    sarr.append("/dir/di.r2/na.me^^at")
    p.dir = "/dir/di.r2"
    p.name = "na.me^"
    p.at = "at"
    p.ext = ""
    p.id = ""
    p.id_base = ""
    p.rev = ""
    p.kind = ""
    p.desc = "na.me^"
    parr.append(p)
    
    
    p = PathInfo()
    sarr.append("/dir/di^r2/na.me^at")
    p.dir = "/dir/di^r2"
    p.name = "na.me"
    p.at = "at"
    p.ext = ""
    p.id = ""
    p.id_base = ""
    p.rev = ""
    p.kind = ""
    p.desc = "na.me"
    parr.append(p)
    
    
    p = PathInfo()
    sarr.append("/dir/di^r2/name .ext")
    p.dir = "/dir/di^r2"
    p.name = "name "
    p.at = ""
    p.ext = "ext"
    p.id = "name"
    p.id_base = "name"
    p.rev = ""
    p.kind = ""
    p.desc = ""
    parr.append(p)
    
    
    
    #id-rev_kind desc
    
    p = PathInfo()
    sarr.append("id-rev_kind desc.ext")
    p.dir = ""
    p.name = "id-rev_kind desc"
    p.at = ""
    p.ext = "ext"
    p.id = "id-rev"
    p.id_base = "id"
    p.rev = "rev"
    p.kind = "kind"
    p.desc = "desc"
    parr.append(p)
    
    
    
    #real
    
    #"E:\Archive\ЭлеваторМельмаш.Сушилка\СШ01-100 Сушилка для зерна\СШ01-100_ВО Сушилка зерновая шахтного типа.SLDASM"
    p = PathInfo()
    sarr.append(r"E:\Archive\ЭлеваторМельмаш.Сушилка\СШ01-100 Сушилка для зерна\СШ01-100_ВО Сушилка зерновая шахтного типа.SLDASM")
    p.dir = r"E:\Archive\ЭлеваторМельмаш.Сушилка\СШ01-100 Сушилка для зерна"
    p.name = "СШ01-100_ВО Сушилка зерновая шахтного типа"
    p.at = ""
    p.ext = "SLDASM"
    p.id = "СШ01-100"
    p.id_base = "СШ01"
    p.rev = "100"
    p.kind = "ВО"
    p.desc = "Сушилка зерновая шахтного типа"
    parr.append(p)
    
    
    #"C:\Users\User\AppData\Local\Temp\swx12748\VC~~\2952497740\Деталь1^СШ01-100_ВО Сушилка зерновая шахтного типа.sldprt"
    p = PathInfo()
    sarr.append(r"C:\Users\User\AppData\Local\Temp\swx12748\VC~~\2952497740\Деталь1^СШ01-100_ВО Сушилка зерновая шахтного типа.sldprt")
    p.dir = r"C:\Users\User\AppData\Local\Temp\swx12748\VC~~\2952497740"
    p.name = "Деталь1"
    p.at = "СШ01-100_ВО Сушилка зерновая шахтного типа"
    p.ext = "sldprt"
    p.id = ""
    p.id_base = ""
    p.rev = ""
    p.kind = ""
    p.desc = "Деталь1"
    parr.append(p)
    
    
    #"C:\Users\User\AppData\Local\Temp\swx12748\VC~~\2952497740\Сборка1^СШ01-100_ВО Сушилка зерновая шахтного типа.sldasm"
    p = PathInfo()
    sarr.append(r"C:\Users\User\AppData\Local\Temp\swx12748\VC~~\2952497740\Сборка1^СШ01-100_ВО Сушилка зерновая шахтного типа.sldasm")
    p.dir = r"C:\Users\User\AppData\Local\Temp\swx12748\VC~~\2952497740"
    p.name = "Сборка1"
    p.at = "СШ01-100_ВО Сушилка зерновая шахтного типа"
    p.ext = "sldasm"
    p.id = ""
    p.id_base = ""
    p.rev = ""
    p.kind = ""
    p.desc = "Сборка1"
    parr.append(p)
    
    
    #"C:\Users\User\AppData\Local\Temp\swx12748\VC~~\1020891029\Деталь2^Сборка1_СШ01-100_ВО Сушилка зерновая шахтного типа.sldprt"
    p = PathInfo()
    sarr.append(r"C:\Users\User\AppData\Local\Temp\swx12748\VC~~\1020891029\Деталь2^Сборка1_СШ01-100_ВО Сушилка зерновая шахтного типа.sldprt")
    p.dir = r"C:\Users\User\AppData\Local\Temp\swx12748\VC~~\1020891029"
    p.name = "Деталь2"
    p.at = "Сборка1_СШ01-100_ВО Сушилка зерновая шахтного типа"
    p.ext = "sldprt"
    p.id = ""
    p.id_base = ""
    p.rev = ""
    p.kind = ""
    p.desc = "Деталь2"
    parr.append(p)
    
    
    #"C:\Users\User\AppData\Local\Temp\swx12748\VC~~\1020891029\СШ01-100_ВО Сушилка^Сборка1_СШ01-100_ВО Сушилка зерновая шахтного типа.sldprt"
    p = PathInfo()
    sarr.append(r"C:\Users\User\AppData\Local\Temp\swx12748\VC~~\1020891029\СШ01-100_ВО Сушилка^Сборка1_СШ01-100_ВО Сушилка зерновая шахтного типа.sldprt")
    p.dir = r"C:\Users\User\AppData\Local\Temp\swx12748\VC~~\1020891029"
    p.name = "СШ01-100_ВО Сушилка"
    p.at = "Сборка1_СШ01-100_ВО Сушилка зерновая шахтного типа"
    p.ext = "sldprt"
    p.id = "СШ01-100"
    p.id_base = "СШ01"
    p.rev = "100"
    p.kind = "ВО"
    p.desc = "Сушилка"
    parr.append(p)
    
    
    Test(parr, sarr)


InitTest1()
InitTest2()

