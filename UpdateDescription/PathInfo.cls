VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "PathInfo"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
'Class Module PathInfo

Option Explicit

' path: dir/name^at.ext
Public dir As String    'directory path
Public name As String   'filename without ext
Public ext As String    'extension
Public at As String     'text after "^"

' name: id_kind desc
Public id As String    'identificatior
Public kind As String  'kind code
Public desc As String  'description
' id: idbase-rev
Public id_base As String
Public rev As String   'revision id (part of id after last "-")
'


Public Sub SetPath(path As String)

    Dim slash As Long
    Dim slash2 As Long
    Dim dot As Long
    Dim at As Long
    Dim rspace As Long
    
    
    'dir
    slash = InStrRev(path, "\")
    slash2 = InStrRev(path, "/")
    If slash < slash2 Then slash = slash2
    If slash > 0 Then
        Me.dir = Left(path, slash - 1)
    Else
        Me.dir = ""
    End If
    
    
    'ext
    dot = Strings.InStrRev(path, ".")
    at = Strings.InStrRev(path, "^")
    rspace = Strings.InStrRev(path, " ")
    If dot > slash And dot > at And dot > rspace Then
        Me.ext = Strings.Mid(path, dot + 1)
    Else
        Me.ext = ""
        dot = Len(path) + 1
    End If
    
    
    'at, name
    If at > slash Then
        Me.at = Strings.Mid(path, at + 1, dot - at - 1)
        Me.name = Mid(path, slash + 1, at - slash - 1)
    Else
        Me.at = ""
        Me.name = Mid(path, slash + 1, dot - slash - 1)
    End If
    
    Call SetName(Me.name)
    
End Sub

Private Sub SetName(ByVal name As String)
    
    Dim space As Long
    Dim underline As Long
    
    space = Strings.InStr(name, " ")
    underline = Strings.InStrRev(name, "_")
    
    If underline > 0 Then
        
        'desc
        If space > underline Then
            Me.desc = Mid(name, space + 1)
        Else
            Me.desc = ""
            space = Strings.Len(name) + 1
        End If
        
        'id, kind
        Me.id = Left(name, underline - 1)
        Me.kind = Mid(name, underline + 1, space - underline - 1)
        
    Else
        'kind
        Me.kind = ""
        
        'id, desc
        If space > 0 Then
            Me.id = Left(name, space - 1)
            Me.desc = Mid(name, space + 1)
        Else
            Me.id = ""
            Me.desc = name
        End If
        
    End If
    
    Call SetRev(Me.id)
    
End Sub

Private Sub SetRev(ByVal id As String)
    
    Dim rev As Long
    rev = Strings.InStrRev(name, "-")
    
    'id_base, rev
    If rev > 0 Then
        Me.id_base = Left(id, rev - 1)
        Me.rev = Mid(id, rev + 1)
    Else
        Me.id_base = id
        Me.rev = ""
    End If
    
End Sub

Public Function GetPath()
    GetPath = Me.dir + "\" + Me.GetFullName()
End Function

Public Function GetFullName() As String
    If at <> "" Then
        GetFullName = Me.name + "^" + Me.at + "." + Me.ext
    Else
        GetFullName = Me.name + "." + Me.ext
    End If
    
End Function

Public Sub Clear()
    Me.at = ""
    Me.desc = ""
    Me.dir = ""
    Me.ext = ""
    Me.id = ""
    Me.id_base = ""
    Me.kind = ""
    Me.name = ""
    Me.rev = ""
End Sub

Public Function ToString() As String
    Dim s As String
    s = "dir=" + Me.dir + vbNewLine
    s = s + "name=" + Me.name + vbNewLine
    s = s + "at=" + Me.at + vbNewLine
    s = s + "ext=" + Me.ext + vbNewLine
    
    s = s + "id=" + Me.id + vbNewLine
    s = s + "id_base=" + Me.id_base + vbNewLine
    s = s + "rev=" + Me.rev + vbNewLine
    s = s + "kind=" + Me.kind + vbNewLine
    s = s + "desc=" + Me.desc + vbNewLine
    
    ToString = s
End Function


