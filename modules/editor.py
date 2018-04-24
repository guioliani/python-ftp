import wx
import wx.lib.dialogs
import wx.stc as stc
import os

faces = {
	'mono': 'Courier New',
	'times': 'Times New Roamn',
	'helv': 'Arial',
	'other': 'Comic Sans MS',
	'size': 10,
	'size2': 8,
}

class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		self.dirname = ''
		self.filename = ''
		self.leftMarginWidth = 25
		self.lineNumbersEnabled = True

		wx.Frame.__init__(self, parent, title = title, size=(800, 600))
		self.control = stc.StyledTextCtrl(self, style=wx.TE_MULTILINE | wx.TE_WORDWRAP)

		self.control.CmdKeyAssign(ord('='), stc.STC_SCMOD_CTRL, stc.STC_CMD_ZOOMIN)#zoom in
		self.control.CmdKeyAssign(ord('-'), stc.STC_SCMOD_CTRL, stc.STC_CMD_ZOOMOUT)#zoom out

		self.control.SetViewWhiteSpace(False)
		self.control.SetMargins(5, 0)
		self.control.SetMarginType(1, stc.STC_MARGIN_NUMBER)
		self.control.SetMarginWidth(1, self.leftMarginWidth)

		self.CreateStatusBar()
		self.StatusBar.SetBackgroundColour((220, 220, 220))

		#menu file
		filemenu = wx.Menu()
		menuNew = filemenu.Append(wx.ID_NEW, "&New", " Create a new document")
		menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", " Open an existing document")
		menuSave = filemenu.Append(wx.ID_SAVE, "&Save", " Save the curent document")
		menuSaveAs = filemenu.Append(wx.ID_SAVEAS, "Save &As", " Save a new document")
		filemenu.AppendSeparator()
		menuClose = filemenu.Append(wx.ID_EXIT, "&Close", " Close the application")

		#menu edit
		editmenu = wx.Menu()
		menuUndo = editmenu.Append(wx.ID_UNDO, "&Undo", " Undo last action")
		menuRedo = editmenu.Append(wx.ID_REDO, "&Redo", " Redo last action")
		editmenu.AppendSeparator()
		menuSelectAll = editmenu.Append(wx.ID_SELECTALL, "&Select All", " Select the entire document")
		menuCopy = editmenu.Append(wx.ID_COPY, "&Copy", " Copy selected text")
		menuCut = editmenu.Append(wx.ID_CUT, "C&ut", " Cut selected text")
		menuPaste = editmenu.Append(wx.ID_PASTE, "&Paste", " Paste text from the clipboard")

		prefmenu = wx.Menu()
		menuLineNumbers = prefmenu.Append(wx.ID_ANY, "Toggle &Line Numbers", " Show/Hide line numbers column")

		helpmenu = wx.Menu()
		menuHowTo = helpmenu.Append(wx.ID_ANY, "&How to...", " Get help using the editor")
		helpmenu.AppendSeparator()
		menuAbout = helpmenu.Append(wx.ID_ABOUT, "&About", " Read about the editor and its making")

		menuBar = wx.MenuBar()
		menuBar.Append(filemenu, "&File")
		menuBar.Append(editmenu, "&Edit")
		menuBar.Append(prefmenu, "&Preferences")
		menuBar.Append(helpmenu, "&Help")
		self.SetMenuBar(menuBar)

		self.Bind(wx.EVT_MENU, self.OnNew, menuNew)
		self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
		self.Bind(wx.EVT_MENU, self.OnSave, menuSave)
		self.Bind(wx.EVT_MENU, self.OnSaveAs, menuSaveAs)
		self.Bind(wx.EVT_MENU, self.OnClose, menuClose)

		self.Bind(wx.EVT_MENU, self.OnUndo, menuUndo)
		self.Bind(wx.EVT_MENU, self.OnRedo, menuRedo)
		self.Bind(wx.EVT_MENU, self.OnSelectAll, menuSelectAll)
		self.Bind(wx.EVT_MENU, self.OnCopy, menuCopy)
		self.Bind(wx.EVT_MENU, self.OnCut, menuCut)
		self.Bind(wx.EVT_MENU, self.OnPaste, menuPaste)

		self.Bind(wx.EVT_MENU, self.OnToggleLineNumbers, menuLineNumbers)
		self.Bind(wx.EVT_MENU, self.OnHowTo, menuHowTo)
		self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)



		self.Show()

	def OnNew(self, e):
		self.filename = ''
		self.control.SetValue("")
	def OnOpen(self, e):
		dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.FD_OPEN)
		if(dlg.ShowModal() == wx.ID_OK):
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
			f = open(os.path.join(self.dirname, self.filename), 'r')
			self.control.SetValue(f.read())
			f.close()
		dlg.Destroy()

	def OnSave(self, e):
		try:
			f = open(os.path.join(self.dirname, self.filename), 'w')
			f.write(self.control.GetValue())
			f.close()
		except:
			try:
				dlg = wx.FileDialog(self, "Save file as", self.dirname, "Untitled", "*.*", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
				if(dlg.ShowModal() == wx.ID_OK):
					self.filename = dlg.GetFilename()
					self.dirname = dlg.GetDirectory()
					f = open(os.path.join(self.dirname, self.filename), 'w')
					f.write(self.control.GetValue())
					f.close()
				dlg.Destroy()
			except:
				pass

	def OnSaveAs(self, e):
		try:
			dlg = wx.FileDialog(self, "Save file as", self.dirname, "Untitled", "*.*", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
			if(dlg.ShowModal() == wx.ID_OK):
				self.filename = dlg.GetFilename()
				self.dirname = dlg.GetDirectory()
				f = open(os.path.join(self.dirname, self.filename), 'w')
				f.write(self.control.GetValue())
				f.close()
			dlg.Destroy()
		except:
			pass

	def OnClose(self, e):
		self.close(True)

	def OnUndo(self, e):
		self.control.Undo()

	def OnRedo(self, e):
		self.control.Redo()

	def OnSelectAll(self, e):
		self.control.SelectAll()

	def OnCopy(self, e):
		self.control.Copy()

	def OnCut(self, e):
		self.control.Cut()

	def OnPaste(self, e):
		self.control.Paste()

	def OnToggleLineNumbers(self, e):
		if(self.lineNumbersEnabled):
			self.control.SetMarginWidth(1, 0)
			self.lineNumbersEnabled = False
		else:
			self.control.SetMarginWidth(1, self.leftMarginWidth)
			self.lineNumbersEnabled = True

	def OnHowTo(self, e):
		dlg = wx.lib.dialogs.ScrolledMessageDialog(self, "this is how to", "How To", size=(400, 400))
		dlg.ShowModal()
		dlg.Destroy()

	def OnAbout(self, e):
		dlg = wx.MessageDialog(self, "text editor made in python", "About", wx.OK)
		dlg.ShowModal()
		dlg.Destroy()


app = wx.App()
frame = MainWindow(None, "Editor de texto")
app.MainLoop()