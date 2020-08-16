# -!- coding: utf-8 -!-
# Author  : AWACS
# Time    : 2020/06/12

# ------------------------------------

""" batch change place2dTexture Node for texture in Hypershade Editor,
if you think the default command that come with maya:
---(hold middle mouse button + Ctrl key ,and drag a place2dTexture to the texture node to plug all those slot)
is kind of trouble, or you have too many texture node to operating,here's the solution,a command with maya gui.

- How to install : you can simply run this in script editor of maya,or add it in the shelf,
or run as file like add this in the shelf :

import sys
sys.path.append( your script path(add quotation marks(") on the both side of your path ) )
import Batch_Change_Place2D_GUI
reload (Batch_Change_Place2D_GUI)

- How to use : just select place2d node to confirm,and select the multiple texture node to excute
"""
# ------------------------------------

"""在Hypershade批量替换place2dTexture节点
如果你觉得maya自带的命令：
---(按住鼠标中键+Ctrl，拽住place2dTexture节点，来连接到各种贴图节点)
有点麻烦的话，或者是你有太多贴图节点要连了，
这里是解决方案，一个有maya界面的命令

- 安装方式：你可以直接在maya的script editor里直接运行，或者添加到工具架，再或者在工具架上添加这个来以文件方式运行：

import sys
sys.path.append( 你的脚本路径(需要添加引号(")在路径两侧) )
import Batch_Change_Place2D_GUI
reload (Batch_Change_Place2D_GUI)

- 使用方式：选择好place2dTexture节点，然后点确认(Confirm)，然后选好贴图节点执行连接就行了
"""

import maya.cmds as cmds

def Batch_Change_Place2D_GUI():
    if cmds.window('Batch_Change_Place2D', q=1, ex=1 ):
        cmds.deleteUI('Batch_Change_Place2D')
    TOOL_T = cmds.window('Batch_Change_Place2D' )
    cmds.showWindow('Batch_Change_Place2D')
    cmds.columnLayout()
    cmds.rowLayout(nc=6)
    cmds.text(l="1: ")
    cmds.text(l=" Select Place2D Node :   ")
    cmds.textField('InputPlace2D', w=200, text = "")
    cmds.button(c=lambda *args:  SetInputPlace2D(), l="Confirm", w=60)
    cmds.setParent('..')
    cmds.rowLayout(nc=6)
    cmds.text(l="2: ")
    cmds.button(c=lambda *args: excute_Batch_Change_Place2d() , l="Select Target tex Node And Excute", w=200)
    cmds.setParent('..')

def SetInputPlace2D():
    Selection = cmds.ls(selection = True)
    if cmds.objExists(Selection[0]):
        cmds.textField('InputPlace2D', e = 1, tx = Selection[0])
        print ("// InputPlace2D Selected : " + Selection[0])

def UV_Node_Exchange( UVNODE , TEXNODE ):
	#plug_the_place2dTexture_Node_to_the_texfile_node
	AttrList = [
		['.outUV','.uvCoord'],
		['.outUvFilterSize','.uvFilterSize'],
		['.coverage','.coverage'],
		['.translateFrame','.translateFrame'],
		['.rotateFrame','.rotateFrame'],
		['.mirrorU','.mirrorU'],
		['.mirrorV','.mirrorV'],
		['.stagger','.stagger'],
		['.wrapU','.wrapU'],
		['.wrapV','.wrapV'],
		['.repeatUV','.repeatUV'],
		['.vertexUvOne','.vertexUvOne'],
		['.vertexUvTwo','.vertexUvTwo'],
		['.vertexUvThree','.vertexUvThree'],
		['.vertexCameraOne','.vertexCameraOne'],
		['.noiseUV','.noiseUV'],
		['.offset','.offset'],
		['.rotateUV','.rotateUV'],
		]
	for i in AttrList:
		try:
			cmds.connectAttr( UVNODE + i[0], TEXNODE + i[1], force=1)
		except:
			pass

def UV_Node_Exchange_old( UVNODE , TEXNODE ):
	#plug_the_place2dTexture_Node_to_the_texfile_node
	cmds.connectAttr( UVNODE + '.outUV', TEXNODE + '.uvCoord', force=1)
	cmds.connectAttr( UVNODE + '.outUvFilterSize', TEXNODE + '.uvFilterSize', force=1)
	cmds.connectAttr( UVNODE + '.coverage', TEXNODE + '.coverage', force=1)
	cmds.connectAttr( UVNODE + '.translateFrame', TEXNODE + '.translateFrame', force=1)
	cmds.connectAttr( UVNODE + '.rotateFrame', TEXNODE + '.rotateFrame', force=1)
	cmds.connectAttr( UVNODE + '.mirrorU', TEXNODE + '.mirrorU', force=1)
	cmds.connectAttr( UVNODE + '.mirrorV', TEXNODE + '.mirrorV', force=1)
	cmds.connectAttr( UVNODE + '.stagger', TEXNODE + '.stagger', force=1)
	cmds.connectAttr( UVNODE + '.wrapU', TEXNODE + '.wrapU', force=1)
	cmds.connectAttr( UVNODE + '.wrapV', TEXNODE + '.wrapV', force=1)
	cmds.connectAttr( UVNODE + '.repeatUV', TEXNODE + '.repeatUV', force=1)
	cmds.connectAttr( UVNODE + '.vertexUvOne', TEXNODE + '.vertexUvOne', force=1)
	cmds.connectAttr( UVNODE + '.vertexUvTwo', TEXNODE + '.vertexUvTwo', force=1)
	cmds.connectAttr( UVNODE + '.vertexUvThree', TEXNODE + '.vertexUvThree', force=1)
	cmds.connectAttr( UVNODE + '.vertexCameraOne', TEXNODE + '.vertexCameraOne', force=1)
	cmds.connectAttr( UVNODE + '.noiseUV', TEXNODE + '.noiseUV', force=1)
	cmds.connectAttr( UVNODE + '.offset', TEXNODE + '.offset', force=1)
	cmds.connectAttr( UVNODE + '.rotateUV', TEXNODE + '.rotateUV', force=1)

def excute_Batch_Change_Place2d( ):
	Selection = cmds.ls(selection = True)
	InputPlace2D = cmds.textField('InputPlace2D' , query=1, text = 1)
	for i in Selection:
		try:
			UV_Node_Exchange( InputPlace2D , i )
		except:
			print("Change_Failed")
	print("completed")

Batch_Change_Place2D_GUI()