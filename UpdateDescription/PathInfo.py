# -*- coding: utf-8 -*-


class PathInfo:
    """Class represents structure of filename \
and provides parsing algorithms"""
    
    # path: dir/name^at.ext
    dir: str    #directory path
    name: str   #filename without ext
    ext: str    #extension
    at: str     #text after "^"
    
    # name: id_kind desc
    id: str    #identificatior
    kind: str  #kind code
    desc: str  #description
    
    # id: idbase-rev
    id_base: str
    rev: str   #revision id (part of id after last "-")
    
    def __init__(self, path:str = None):
        if path == None:
            self.Clear()
        else:
            self.SetPath(path)
    
    def __eq__(self, other):
        return self.dir == other.dir and \
                self.name == other.name and \
                self.ext == other.ext and \
                self.at == other.at and \
                self.id == other.id and \
                self.kind == other.kind and \
                self.desc == other.desc
    
    def __str__(self) -> str:
        """Returns string explaination of this structure"""
        
        s:str = "dir=" + self.dir
        s = s + "\nname=" + self.name 
        s = s + "\nat=" + self.at 
        s = s + "\next=" + self.ext 

        s = s + "\nid=" + self.id 
        s = s + "\nid_base=" + self.id_base 
        s = s + "\nrev=" + self.rev 
        s = s + "\nkind=" + self.kind 
        s = s + "\ndesc=" + self.desc + "\n"
        return s
        
    def GetPath(self) -> str:
        return self.dir + "\\" + self.GetFullName()
    
    def GetFullName(self) -> str:
        if self.at != "":
            return self.name + "^" + self.at + "." + self.ext
        else:
            return self.name + "." + self.ext
    
    def Clear(self):
        self.at = ""
        self.desc = ""
        self.dir = ""
        self.ext = ""
        self.id = ""
        self.id_base = ""
        self.kind = ""
        self.name = ""
        self.rev = ""
    
    def SetPath(self, path: str):
        """Setting the full path and parse"""
        
        #dir
        slash: int = path.rfind("\\")
        slash2: int = path.rfind("/")
        if slash < slash2: slash = slash2
        if slash >= 0:
            self.dir = path[:slash]
        else:
            self.dir = ""

        #ext
        dot:int = path.rfind(".")
        at:int  = path.rfind("^")
        rspace:int  = path.rfind(" ")
        if dot > slash and dot > at and dot > rspace :
            self.ext = path[dot + 1:]
        else:
            self.ext = ""
            dot = len(path)

        #at, name
        if at > slash :
            self.at = path[at + 1:dot]
            self.name = path[slash + 1:at]
        else:
            self.at = ""
            self.name = path[slash + 1:dot]

        self.SetName(self.name)

    def SetName(self, name: str):

        space: int = name.find(" ")
        underline: int = name.find("_")

        if underline >= 0 :
            #desc
            if space > underline :
                self.desc = name[space + 1:]
            else:
                self.desc = ""
                space = len(name)
            #id, kind
            self.id = name[:underline]
            self.kind = name[underline + 1:space]

        else:
            #kind
            self.kind = ""
            #id, desc
            if space >= 0 :
                self.id = name[:space]
                self.desc = name[space + 1:]
            else:
                self.id = ""
                self.desc = name

        self.SetRev(self.id)


    def SetRev(self, id: str):

        rev: int = id.rfind("-")

        #id_base, rev
        if rev >= 0 :
            self.id_base = id[:rev]
            self.rev = id[rev + 1:]
        else:
            self.id_base = id
            self.rev = ""

