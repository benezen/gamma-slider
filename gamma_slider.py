#!/usr/bin/python
#-*- coding: utf-8 -*-

import subprocess, wx

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, parent = None, title = "Gamma Slider")
		self.Bind(wx.EVT_CLOSE, self.OnClose)

		self.SetWindowStyle(wx.CAPTION | wx.MINIMIZE_BOX | wx.CLOSE_BOX)
		self.SetSize(wx.Size(300,120))
		self.mainPanel = wx.Panel(self)
		self.slider = wx.Slider(self.mainPanel, minValue = 8, maxValue = 16)
		self.text1 = wx.StaticText(self.mainPanel)
		
		self.slider.SetValue(10)
		self.text1.SetLabel("1.0")
		subprocess.call( "xgamma -gamma 1", shell=True )
		
		self.vtBoxSizer = wx.BoxSizer(wx.VERTICAL)
		self.vtBoxSizer.Add(self.slider, 0, wx.EXPAND|wx.ALL, 5)
		self.vtBoxSizer.Add(self.text1, 0, wx.EXPAND|wx.ALL, 5)
		self.mainPanel.SetSizer(self.vtBoxSizer)
		
		self.Bind(wx.EVT_SLIDER, self.OnSliderChange, self.slider)
		
	def OnSliderChange(self, e):
		givalue = float(float(self.slider.GetValue()) / float(10))
		gsvalue = str(givalue)
		cmd = "xgamma -gamma " + gsvalue
		subprocess.call( cmd, shell=True )
		self.text1.SetLabel(gsvalue)		
		
	def OnClose(self, event):
		subprocess.call( "xgamma -gamma 1", shell=True )
		self.Destroy()
					
if __name__ == "__main__":
	app = wx.App()
	frame = MyFrame()
	frame.Show()
	
	app.MainLoop()
