#! /usr/bin/env python

"""
    This code aims to implement a simple and didatic GUI using the wxPyhon package.
    Written by Gabriel Heberle on December 21st, 2021 (based on https://realpython.com/python-gui-with-wxpython/)
"""

import wx

class MyFrame(wx.Frame):
    def __init__(self) -> None:
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        
        my_button = wx.Button(panel, label='Press Me')
        my_button.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_button, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(my_sizer)

        self.Show()
    
    def on_press(self, event) -> None:
        value = self.text_ctrl.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f"You typed '{value}'")

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
