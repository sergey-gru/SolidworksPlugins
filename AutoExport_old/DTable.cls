VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "DTable"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
Option Explicit

Private col_name As Collection
Private col_def As Collection
Private rows As Collection
Private ncols As Long

'=====================
' INITIALIZATION
'=====================
Sub Class_Initialize()
    Set rows = New Collection
    Set col_name = New Collection
    Set col_def = New Collection
    ncols = 0
End Sub

Sub Clear()
    Dim i As Long, n As Long
    
    n = rows.Count
    For i = n To 1 Step -1
        Call rows.Remove(1)
    Next i
    
    n = ncols
    For i = n To 1 Step -1
        Call col_name.Remove(1)
        Call col_def.Remove(1)
    Next i
    
    ncols = 0
End Sub

Sub Reset(Optional rows As Long = 3, _
        Optional cols As Long = 3, _
        Optional ColDef As Variant = Null)
    
    Me.Clear
    
    Dim r As Long
    Dim c As Long
    
    For r = 1 To rows
        Me.AddRow
    Next r
    
    For c = 1 To cols
        Call Me.AddColumn("Column" + str(c), ColDef)
    Next c
End Sub

Sub SetRow(row As Long, arr() As Variant)
    Dim arr_i As Long
    Dim arr_n As Long
    Dim c As Long
    Dim nc As Long
    
    arr_i = LBound(arr)
    arr_n = UBound(arr)
    c = 1
    nc = ncols
    
    While c <= nc And arr_i <= arr_n:
        rows(row)(c) = arr(arr_i)
        c = c + 1
        arr_i = arr_i + 1
    Loop
End Sub

Sub SetColumn(col As Long, arr() As Variant)
    Dim arr_i As Long
    Dim arr_n As Long
    Dim r As Long
    Dim nr As Long
    
    arr_i = LBound(arr)
    arr_n = UBound(arr)
    r = 1
    nr = rows.Count
    
    While r <= nr And arr_i <= arr_n:
        rows(r)(col) = arr(arr_i)
        r = r + 1
        arr_i = arr_i + 1
    Loop
End Sub

'=====================
' INFO
'=====================
Property Get CountRows() As Long
    CountRows = rows.Count
End Property
Property Get CountColumns() As Long
    CountColumns = ncols
End Property
Property Get IsEmpty() As Boolean
    IsEmpty = (ncols = 0 And rows.Count = 0)
End Property

'=====================
' DATA ACCESS
'=====================
Property Get Item(row As Long, col As Long) As Variant
Attribute Item.VB_UserMemId = 0
    Item = rows(row)(col)
End Property
Property Let Item(row As Long, col As Long, value As Variant)
    Dim arr As Collection
    Set arr = rows.Item(row)
    Call arr.Add(value, Before:=col)
    Call arr.Remove(col + 1)
End Property

Property Get ColumnDefault(col As Long) As Variant
    ColumnDefault = col_def(col)
End Property
Property Let ColumnDefault(col As Long, value As Variant)
    Call col_def.Add(value, Before:=col)
    Call col_def.Remove(col + 1)
End Property

Property Get ColumnName(col As Long) As String
    ColumnName = col_name(col)
End Property
Property Let ColumnName(col As Long, value As String)
    Dim arr As Collection
    Set arr = col_name(col)
    Call arr.Add(value, Before:=col)
    Call arr.Remove(col + 1)
End Property
Function GetColumnNumber(ColName As String) As Long
    Dim i As Long
    For i = 1 To ncols
        If StrComp(col_name(i), ColName, vbBinaryCompare) = 0 Then
            GetColumnNumber = i
            Exit Function
        End If
    Next i
    GetColumnNumber = 0
End Function


'=====================
' DATA CHANGE
'=====================
Function AddRow(Optional Before As Long = 0)
    
    'Dim rc As Integer
    'rc = Me.GetCountRow
    Dim c As Long, nc As Long
    Dim rcol As New Collection
    nc = ncols
    
    For c = 1 To nc
        Call rcol.Add(col_def(c))
    Next c
    
    If Before = 0 Then
        Call rows.Add(rcol)
        AddRow = rows.Count
    Else
        Call rows.Add(rcol, Before:=Before)
        AddRow = Before
    End If
End Function

Function AddColumn(ByVal name As String, _
        Optional ColDef As Variant = Null, _
        Optional Before As Long = 0)

    Dim row As New Collection
    Dim r As Long
    
    ncols = ncols + 1
    If Before = 0 Then
        Call col_def.Add(ColDef)
        Call col_name.Add(name)
        For r = rows.Count To 1 Step -1
            Call rows(r).Add(ColDef)
        Next r
        AddColumn = ncols
    Else
        Call col_def.Add(ColDef, Before:=Before)
        Call col_name.Add(name, Before:=Before)
        For r = rows.Count To 1 Step -1
            Call rows(r).Add(ColDef, Before:=Before)
        Next r
        AddColumn = Before
    End If
    
End Function

Sub RemoveRow(row As Long)
    Call rows.Remove(row)
End Sub

Sub RemoveColumn(col As Long)
    Dim r As Long
    Dim nr As Long
    nr = rows.Count
    
    Call col_def.Remove(col)
    Call col_name.Remove(col)
    For r = 1 To nr
        Call rows(r).Remove(col)
    Next r
    
    ncols = ncols - 1
End Sub

Sub MoveRow(row As Long, _
        Optional row2_before As Long = 0)
        
    If row = row2_before Then Exit Sub
    
    Dim buf As Collection
    Set buf = rows(row)
    Call rows.Remove(row)
    
    If row_before = 0 Then
        Call rows.Add(buf)
    Else
        Call rows.Add(buf, Before:=row2_before)
    End If
End Sub

Sub MoveColumn(col As Long, _
        Optional col2_before As Long = 0)
        
    If col = col2_before Then Exit Sub
        
    Dim buf As Variant
    Dim buf_def As Variant
    Dim buf_name As String
    
    Dim r As Long
    Dim nr As Long
    nr = rows.Count
    
    buf_def = col_def(col)
    Call col_def.Remove(col)
    buf_name = col_name(col)
    Call col_name.Remove(col)
        
    If col_before = 0 Then
        
        Call col_def.Add(buf_def)
        Call col_name.Add(buf_def)
        
        For r = 1 To nr
            buf = rows(r)(col)
            Call rows(r).Remove(col)
            Call rows(r).Add(buf)
        Next r
    Else
    
        Call col_def.Add(buf_def, Before:=col2_before)
        Call col_name.Add(buf_def, Before:=col2_before)
        
        For r = 1 To nr
            buf = rows(r)(col)
            Call rows(r).Remove(col)
            Call rows.Add(buf, Before:=col2_before)
        Next r
    End If
End Sub



