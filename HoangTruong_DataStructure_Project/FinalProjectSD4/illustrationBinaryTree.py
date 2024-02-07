import numpy
import ctypes
from tkinter import *
import clr
import os
"""
make sure to use PyCharm
make sure to use python environment Python 3.10+

Make sure that  you execute command in command prompt "pip install pythonnet" 
Make sure that  you execute command in command prompt "pip install numpy"    
Make sure that  you execute command in command prompt "pip install pillow". Then if it asks to update, type: "python.exe -m pip install --upgrade pip"

    Make sure that you open the project named "FinalProjectSD4" in the folder named "HoangTruong_DataStructure_Project" otherwise it won't work

    

    if you have error with "import clr", please change the python environment to Python 3.10. To change the python environment in Visual Studio:
    "Select the View -> Other Windows -> Python Environments menu command"

    After the step above, if you still have error, it's better for you to copy the absolute path of file "Project_Data_Structure_Application.dll"
    which is located in folder named "dlls". Then you paste as the arugument of function named "clr.AddReference(your_aboslute_dll_path)" which is
    above the line "from Project_Data_Structure_Application import Binary_Tree"
    if you have error with "clr doesnt have AddReference()", Select the View -> Other Windows -> Python Environments, then delete the clr if exists in python environment, because we use clr of pythonnet not from package named clr
"""
dll_path = os.path.join(os.path.dirname(__file__), "dlls/Project_Data_Structure_Application.dll")
clr.AddReference(dll_path)
from Project_Data_Structure_Application import Binary_Tree
expression = "(7*2)*3/4+8/2*3*(1-3%2)"
binaryTree = Binary_Tree()
root = binaryTree.ConvertMathExpressionToBinaryTree(expression)


print("Print In Order")
binaryTree.PrintInOrder(root)

def draw_tree(canvas, node, x, y, x_diff, y_diff):
    if node != None:
        canvas.create_rectangle(x-20, y-20, x+20, y+20, fill='white', outline='black')
        canvas.create_text(x, y, text=node.data)
        if node.left != None:
            canvas.create_line(x - 7, y + 7, x-x_diff, y+y_diff)
            draw_tree(canvas, node.left, x-x_diff, y+y_diff, x_diff/2, y_diff)
        if node.right != None:
            canvas.create_line(x + 7, y + 7, x+x_diff, y+y_diff)
            draw_tree(canvas, node.right, x+x_diff, y+y_diff, x_diff/2, y_diff)

illustration = Tk()
illustration.title("Convert math expression to binary tree")
illustration.geometry("550x500")
illustration.attributes("-topmost", True)
illustration.configure(bg="white")
canvas = Canvas(illustration, width=2000, height=2000)
canvas.pack()
draw_tree(canvas, root, 1000, 50, 400, 100)

illustration.mainloop()