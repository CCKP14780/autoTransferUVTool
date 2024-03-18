import maya.cmds as cmds

def transferUI():
    if cmds.window('transferUIWindow',q = True, ex = True):
        cmds.deleteUI('transferUIWindow',window = True)
       
    cmds.window('transferUIWindow',title='Auto Transfer UV')
    cmds.showWindow('transferUIWindow') 
    cmds.window('transferUIWindow',e = True, wh=[300,100])
    
    cmds.columnLayout(adj = True)
    
    cmds.frameLayout(label='Get Parent UV')
    cmds.rowLayout(numberOfColumns = 2)
    cmds.textField('parent_textField')
    cmds.button(l = 'GET', c = getParent)
    cmds.setParent('..')
    
    cmds.button(l = 'TRANSFER UV', c = autoTransferUV)

def getParent(*args1):
    sels = cmds.ls(sl = True)
    if sels:
        sels = cmds.textField('parent_textField', e = True, tx = sels[0])
    else:
        sels = cmds.textField('parent_textField', e = True, tx = '')

def autoTransferUV(*args):
    objParent = cmds.textField('parent_textField',q = True, tx = True)
    sel = cmds.ls(sl = True)

    for s in sel:
        print(s);
        #transferAttributes -transferPositions 0 -transferNormals 0 -transferUVs 2 -transferColors 2 -sampleSpace 5 -sourceUvSpace "map1" -targetUvSpace "map1" -searchMethod 3-flipUVs 0 -colorBorders 1 ;
        cmds.transferAttributes(objParent, s, transferUVs = 2, transferColors = 2, sampleSpace = 5, searchMethod=3, colorBorders=1,flipUVs=0)
        cmds.DeleteHistory() 
    
transferUI();