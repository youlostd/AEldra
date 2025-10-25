import ui
import inGameWikiUI
import wiki
import item
import nonplayer

class InGameWiki(ui.Window):
	def __init__(self):
		self.searchEdit = None
		super(InGameWiki, self).__init__()
		self.objList = {}
		self.windowHistory = []
		self.currSelected = 0

		wiki.RegisterClass(self)
		self.SetWindowName("InGameWiki")

		self.BuildUI()
		self.SetCenterPosition()
		self.Hide()

	def __del__(self):
		wiki.UnregisterClass()
		super(InGameWiki, self).__del__()

	def Show(self):
		super(InGameWiki, self).Show()
		wiki.ShowModelViewManager(True)

	def Hide(self):
		super(InGameWiki, self).Hide()
		wiki.ShowModelViewManager(False)
		if self.searchEdit:
			self.searchEdit.KillFocus()

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		#self.customPageWindow.LoadFile("testload.txt")
		return True

	def BINARY_LoadInfo(self, objID, vnum):
		if objID in self.objList:
			self.objList[objID].NoticeMe()

	def BuildUI(self):
		inGameWikiUI.InitMainWindow(self)
		inGameWikiUI.BuildBaseMain(self)

	def OpenSpecialPage(self, oldWindow, vnum, isMonster = False):
		del self.windowHistory[self.currSelected + 1:]

		if oldWindow:
			del self.windowHistory[:]
			self.currSelected = 0
			self.windowHistory.append(oldWindow)
		if len(self.windowHistory) > 0:
			self.windowHistory[-1].Hide()

		newSpec = inGameWikiUI.SpecialPageWindow(vnum, isMonster)
		newSpec.AddFlag("attach")
		newSpec.SetParent(self)
		newSpec.SetPosition(inGameWikiUI.mainBoardPos[0] + 7, inGameWikiUI.mainBoardPos[1] + 7)
		newSpec.Show()

		self.windowHistory.append(newSpec)
		self.currSelected = self.windowHistory.index(newSpec)
		if self.currSelected > 0:
			self.prevButt.Enable()
		else:
			self.prevButt.Disable()
		self.nextButt.Disable()

	def OnPressNameEscapeKey(self):
		wnd = self.searchEdit
		if not wnd.IsShowCursor() or wnd.GetText() == "":
			self.OnPressEscapeKey()
		else:
			wnd.SetText("")
			self.searchEditHint.SetText("")

	def Search_RefreshTextHint(self):
		self.searchEdit.SetFontColor(0.8549, 0.8549, 0.8549)
		self.searchEditHint.SetText("")

		if self.searchEdit.GetText():
			if not item.SelectByNamePart(self.searchEdit.GetText(), True):
				mobVnum = nonplayer.GetVnumByNamePart(self.searchEdit.GetText())
				if not mobVnum:
					self.searchEdit.SetFontColor(1.0, 0.2, 0.2)
				else:
					itemName = nonplayer.GetMonsterName(mobVnum)
					self.searchEditHint.SetText(self.searchEdit.GetText() + " " + itemName[len(self.searchEdit.GetText()):])
			else:
				itemName = item.GetItemName()
				self.searchEditHint.SetText(self.searchEdit.GetText() + " " + itemName[len(self.searchEdit.GetText()):])

	def OnUpdate(self):
		(start, end) = self.searchEdit.GetRenderPos()
		if start:
			self.searchEditHint.SetFixedRenderPos(start, end)
		else:
			self.searchEditHint.SetFixedRenderPos(start, 17)

	def Search_CompleteTextSearch(self):
		if self.searchEditHint.GetText():
			oldText = self.searchEdit.GetText()
			self.searchEdit.SetText(oldText + self.searchEditHint.GetText()[len(oldText)+1:])
			self.searchEdit.SetEndPosition()
			self.Search_RefreshTextHint()

	def StartSearch(self):
		if self.searchEdit.GetText():
			if not item.SelectByNamePart(self.searchEdit.GetText(), True):
				mobVnum = nonplayer.GetVnumByNamePart(self.searchEdit.GetText())
				if mobVnum:
					self.CloseBaseWindows()
					self.OpenSpecialPage(None, mobVnum, True)
			else:
				self.CloseBaseWindows()
				self.OpenSpecialPage(None, int(item.GetItemVnum() / 10) * 10, False)

	def GoToLanding(self):
		self.CloseBaseWindows()
		self.categ.NotifyCategorySelect(None)
		self.customPageWindow.LoadFile("landingpage.txt")

	def OnPressNextButton(self):
		if len(self.windowHistory) - 1 > self.currSelected:
			self.windowHistory[self.currSelected].Hide()
			self.currSelected += 1
			self.windowHistory[self.currSelected].OpenWindow()

			self.prevButt.Enable()
			if len(self.windowHistory) - 1 == self.currSelected:
				self.nextButt.Disable()

	def OnPressPrevButton(self):
		if self.currSelected > 0:
			self.windowHistory[self.currSelected].Hide()
			self.currSelected -= 1
			self.windowHistory[self.currSelected].OpenWindow()

			self.nextButt.Enable()
			if self.currSelected == 0:
				self.prevButt.Disable()

	def CloseBaseWindows(self):
		self.mainWeaponWindow.Hide()
		self.mainChestWindow.Hide()
		self.mainBossWindow.Hide()
		self.customPageWindow.Hide()
		self.costumePageWindow.Hide()
		
		del self.windowHistory[:]
		self.prevButt.Disable()
		self.nextButt.Disable()
		self.currSelected = 0