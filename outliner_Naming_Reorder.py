# -!- coding: utf-8 -!-
# Time    : 2020/06/12

"""在大纲视图中排序用的沙雕玩意。。直接运行或者加到工具架上"""
"""Just for reorder in outliner or whatever,,,,,run in script editor or add to the shelf.."""


def outliner_Naming_Reorder( ):
    selectedobject = cmds.ls(selection = True)
    selectedobject.sort()
    for indObj in selectedobject:
        cmds.reorder( indObj , back=True)

outliner_Naming_Reorder()

# def outliner_Naming_Reorder_toggle(invert ):
#     selectedobject = cmds.ls(selection = True)
#     selectedobject.sort()
#     if invert:
#         for indObj in selectedobject:
#             cmds.reorder( indObj , front=True)
#     else :
#         for indObj in selectedobject:
#             cmds.reorder( indObj , back=True)
#     print invert

# try:
#     outliner_Naming_Reorder_invert = not outliner_Naming_Reorder_invert
# except:
#     outliner_Naming_Reorder_invert = False

outliner_Naming_Reorder_toggle(outliner_Naming_Reorder_invert)