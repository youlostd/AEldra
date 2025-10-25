import ui
import net
import chat
import player
import app
import localeInfo
import ime
import chr
import constInfo
if constInfo.WHISPER_MANAGER:
	import whispermgr

class WhisperButton(ui.Button):
	def __init__(self):
		ui.Button.__init__(self, "TOP_MOST")

	def __del__(self):
		ui.Button.__del__(self)

	def SetToolTipText(self, text, x=0, y = 32):
		ui.Button.SetToolTipText(self, text, x, y)
		#self.ToolTipText.SetFontName( constInfo.GetChoosenFontName( ) )
		self.ShowToolTip()

	def SetToolTipTextWithColor(self, text, color, x=0, y = 32):
		ui.Button.SetToolTipText(self, text, x, y)
		self.ToolTipText.SetPackedFontColor(color)
		self.ShowToolTip()

	def HideToolTip(self):
		self.ShowToolTip()

class WhisperDialog(ui.ScriptWindow):

	FLAG_IMAGE_FILE_NAME = "icon/flag/%s_small.tga"

	class TextRenderer(ui.Window):
		def SetTargetName(self, targetName):
			self.targetName = targetName

		def OnRender(self):
			(x, y) = self.GetGlobalPosition()
			chat.RenderWhisper(self.targetName, x, y)

	class ResizeButton(ui.DragButton):

		def __init__(self):
			ui.DragButton.__init__(self)

		def __del__(self):
			ui.DragButton.__del__(self)

		def OnMouseOverIn(self):
			app.SetCursor(app.HVSIZE)

		def OnMouseOverOut(self):
			app.SetCursor(app.NORMAL)

	def __init__(self, eventMinimize, eventClose):
		print "NEW WHISPER DIALOG  ----------------------------------------------------------------------------"
		ui.ScriptWindow.__init__(self)
		self.targetName = ""
		self.lang = -1
		self.eventMinimize = eventMinimize
		self.eventClose = eventClose
		self.eventAcceptTarget = None
	def __del__(self):
		print "---------------------------------------------------------------------------- DELETE WHISPER DIALOG"
		ui.ScriptWindow.__del__(self)		

	def LoadDialog(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/WhisperDialog.py")
		except:
			import exception
			exception.Abort("WhisperDialog.LoadDialog.LoadScript")

		try:
			GetObject=self.GetChild
			self.titleName = GetObject("titlename")
			self.titleNameEdit = GetObject("titlename_edit")
			self.closeButton = GetObject("closebutton")
			self.scrollBar = GetObject("scrollbar")
			self.chatLine = GetObject("chatline")
			self.minimizeButton = GetObject("minimizebutton")
			self.ignoreButton = GetObject("ignorebutton")
			self.reportViolentWhisperButton = GetObject("reportviolentwhisperbutton")
			self.acceptButton = GetObject("acceptbutton")
			self.sendButton = GetObject("sendbutton")
			self.board = GetObject("board")
			self.editBar = GetObject("editbar")
			self.gamemasterMark = GetObject("gamemastermark")
			self.lang_flag = GetObject("lang_flag")
		except:
			import exception
			exception.Abort("DialogWindow.LoadDialog.BindObject")

		self.gamemasterMark.Hide()
		self.titleName.SetText("")
		self.titleNameEdit.SetText("")
		self.minimizeButton.SetEvent(ui.__mem_func__(self.Minimize))
		self.closeButton.SetEvent(ui.__mem_func__(self.Close))
		self.scrollBar.SetPos(1.0)
		self.scrollBar.SetScrollEvent(ui.__mem_func__(self.OnScroll))
		self.chatLine.SetReturnEvent(ui.__mem_func__(self.SendWhisper))
		self.chatLine.SetEscapeEvent(ui.__mem_func__(self.Minimize))
		self.chatLine.SetMultiLine()
		self.sendButton.SetEvent(ui.__mem_func__(self.SendWhisper))
		self.titleNameEdit.SetReturnEvent(ui.__mem_func__(self.AcceptTarget))
		self.titleNameEdit.SetEscapeEvent(ui.__mem_func__(self.Close))
		self.ignoreButton.SetToggleDownEvent(ui.__mem_func__(self.IgnoreTarget))
		self.ignoreButton.SetToggleUpEvent(ui.__mem_func__(self.IgnoreTarget))
		self.reportViolentWhisperButton.SetEvent(ui.__mem_func__(self.ReportViolentWhisper))
		self.acceptButton.SetEvent(ui.__mem_func__(self.AcceptTarget))

		self.textRenderer = self.TextRenderer()
		self.textRenderer.SetParent(self)
		self.textRenderer.SetPosition(20, 28)
		self.textRenderer.SetTargetName("")
		self.textRenderer.Show()

		self.resizeButton = self.ResizeButton()
		self.resizeButton.SetParent(self)
		self.resizeButton.SetSize(20, 20)
		self.resizeButton.SetPosition(280, 180)
		self.resizeButton.SetMoveEvent(ui.__mem_func__(self.ResizeWhisperDialog))
		self.resizeButton.Show()

		self.ResizeWhisperDialog()

	def Destroy(self):

		self.eventMinimize = None
		self.eventClose = None
		self.eventAcceptTarget = None

		self.ClearDictionary()
		self.scrollBar.Destroy()
		self.titleName = None
		self.titleNameEdit = None
		self.closeButton = None
		self.scrollBar = None
		self.chatLine = None
		self.sendButton = None
		self.ignoreButton = None
		self.reportViolentWhisperButton = None
		self.acceptButton = None
		self.minimizeButton = None
		self.textRenderer = None
		self.board = None
		self.editBar = None
		self.resizeButton = None
		self.lang_flag = None

	def ResizeWhisperDialog(self):
		(xPos, yPos) = self.resizeButton.GetLocalPosition()
		if xPos < 280:
			self.resizeButton.SetPosition(280, yPos)
			return
		if yPos < 150:
			self.resizeButton.SetPosition(xPos, 150)
			return
		self.SetWhisperDialogSize(xPos + 20, yPos + 20)

	def SetWhisperDialogSize(self, width, height):
		try:
			max = int((width-90)/6) * 3 - 6

			self.board.SetSize(width, height)
			self.scrollBar.SetPosition(width-25, 35)
			self.scrollBar.SetScrollBarSize(height-100)
			self.scrollBar.SetPos(1.0)
			self.editBar.SetSize(width-18, 50)
			self.chatLine.SetSize(width-90, 40)
			self.chatLine.SetLimitWidth(width-90)
			self.SetSize(width, height)

			if 0 != self.targetName:
				chat.SetWhisperBoxSize(self.targetName, width - 50, height - 90)			
			
			self.textRenderer.SetPosition(20, 28)
			self.scrollBar.SetPosition(width-25, 35)
			self.editBar.SetPosition(10, height-60)
			self.sendButton.SetPosition(width-80, 10)
			self.minimizeButton.SetPosition(width-42, 12)
			self.closeButton.SetPosition(width-24, 12)

			self.SetChatLineMax(max)

		except:
			import exception
			exception.Abort("WhisperDialog.SetWhisperDialogSize.BindObject")

	def SetChatLineMax(self, max):
		self.chatLine.SetMax(max)

		from grpText import GetSplitingTextLine

		text = self.chatLine.GetText()
		if text:
			self.chatLine.SetText(GetSplitingTextLine(text, max, 0))

	def OpenWithTarget(self, targetName):
		chat.CreateWhisper(targetName)
		chat.SetWhisperBoxSize(targetName, self.GetWidth() - 60, self.GetHeight() - 90)
		self.chatLine.SetFocus()
		self.titleName.SetText(targetName)
		self.targetName = targetName
		self.textRenderer.SetTargetName(targetName)
		self.titleNameEdit.Hide()
		self.ignoreButton.Hide()
		self.reportViolentWhisperButton.Hide()
		self.acceptButton.Hide()
		if player.GetName().startswith('['):
			self.acceptButton.Show()
			self.acceptButton.SetPosition(170, 5)
			self.acceptButton.SetText("Copy")
		self.lang_flag.Hide()
		self.gamemasterMark.Hide()
		self.minimizeButton.Show()
		if targetName not in constInfo.PLAYER_LANG_DATA:
			net.SendPlayerInformation(targetName)

	def OpenWithoutTarget(self, event):
		self.eventAcceptTarget = event
		self.titleName.SetText("")
		self.titleNameEdit.SetText("")
		self.titleNameEdit.SetFocus()
		self.targetName = 0
		self.titleNameEdit.Show()
		self.ignoreButton.Hide()
		self.reportViolentWhisperButton.Hide()
		self.acceptButton.Show()
		self.minimizeButton.Hide()
		self.gamemasterMark.Hide()
		self.lang_flag.Hide()

	def OnUpdate(self):
		if not self.lang_flag.IsShow() and self.lang == -1 and self.targetName and self.targetName in constInfo.PLAYER_LANG_DATA:
			self.lang = constInfo.PLAYER_LANG_DATA[self.targetName]
			self.lang_flag.LoadImage(self.FLAG_IMAGE_FILE_NAME % app.GetShortLanguageName(self.lang))
			self.lang_flag.Show()
			self.lang_flag.SetPosition(10 + 130 + 5, 10)

		if self.gamemasterMark.IsShow():
			if not self.targetName or not self.targetName.startswith('['):
				self.gamemastermark.Hide()

	def SetGameMasterLook(self):
		if not self.titleName.GetText().startswith('['):
			tchat("Not gm name, no gm flag pn")
			return

		self.gamemasterMark.Show()
		self.reportViolentWhisperButton.Hide()

	def Minimize(self):
		self.titleNameEdit.KillFocus()
		self.chatLine.KillFocus()
		self.Hide()

		if None != self.eventMinimize:
			self.eventMinimize(self.targetName)

	def Close(self):
		if constInfo.WHISPER_MANAGER:
			whispermgr.ClearWhisper(self.targetName)
		chat.ClearWhisper(self.targetName)
		self.titleNameEdit.KillFocus()
		self.chatLine.KillFocus()
		self.Hide()

		if None != self.eventClose:
			self.eventClose(self.targetName)

	def ReportViolentWhisper(self):
		net.SendChatPacket("/reportviolentwhisper " + self.targetName)

	def IgnoreTarget(self):
		net.SendChatPacket("/ignore " + self.targetName)

	def AcceptTarget(self):
		if self.targetName and (test_server or player.GetName().startswith('[')):
			from os import system
			system("echo|set /p=\"%s\" | clip" % self.targetName)
			chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, self.targetName, "Name copied to clipboard")
			return
			
		name = self.titleNameEdit.GetText()
		if len(name) <= 0:
			self.Close()
			return

		if None != self.eventAcceptTarget:
			self.titleNameEdit.KillFocus()
			self.eventAcceptTarget(name)
			if name not in constInfo.PLAYER_LANG_DATA:
				net.SendPlayerInformation(name)
			if self.targetName.startswith('['):
				chat.AppendWhisper(chat.WHISPER_TYPE_GM,self.targetName,"System : " + localeInfo.CHAT_GM_INSTANT_QUESTION)

	def OnScroll(self):
		chat.SetWhisperPosition(self.targetName, self.scrollBar.GetPos())

	def OnMouseWheel(self, len):
		lineCount = chat.GetWhisperLineCount(self.targetName)
		if self.IsInPosition() and self.scrollBar.IsShow() and lineCount > 0:
			dir = constInfo.WHEEL_TO_SCROLL(len)
			new_pos = self.scrollBar.GetPos() + ((1.0 / lineCount) * dir)
			new_pos = max(0.0, new_pos)
			new_pos = min(1.0, new_pos)
			self.scrollBar.SetPos(new_pos)
			return True
		return False

	def SendWhisper(self):
		text = self.chatLine.GetText()
		textLength = len(text)

		if textLength > 0:
			if self.targetName[0].startswith("[") and chat.GetWhisperLineCount(self.targetName) == 0:
				text2=text.lower()
				if text2 in ("hi", "hey", "huhu", "hallo", "hello",\
						"ola", "olah", "salute", "sa", "s.a",\
						"selamın aleyküm", "selamun aleyküm", "selamın aleykum",\
						"selamun aleykum", "merhabalar", "merhaba", "meraba",\
						"selam", "selamlar", "salut", "esti", 'Buna',\
						'Buna ziua', 'Buna seara', 'Buna', 'Ce faci?', 'Buna, esti?',\
						'Salut, esti', 'Bro, esti?', 'Bro, salut'):
				
					chat.AppendWhisper(chat.WHISPER_TYPE_GM,self.targetName,"System : " + localeInfo.CHAT_GM_INSTANT_QUESTION)
					self.chatLine.SetText("")
					return

			link = self.interface.GetLink(text)
			if link != "":
				if not player.IsGameMaster():
					text = text.replace(link, "|cFF00C0FC|h|Hweb:" + link.replace("://", "XxX") + "|h" + link + "|h|r")
				else:
					text = text.replace(link, "|cFF00C0FC|h|Hsysweb:" + link.replace("://", "XxX") + "|h" + link + "|h|r")

			net.SendWhisperPacket(self.targetName, text, False)
			self.chatLine.SetText("")

			chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, player.GetName() + " : " + text)
			# tchat("count: %d" % chat.GetWhisperLineCount(self.targetName))

	def OnTop(self):
		self.chatLine.SetFocus()
		
	def BindInterface(self, interface):
		self.interface = interface
		
	def OnMouseLeftButtonDown(self):
		hyperlink = ui.GetHyperlink()
		if hyperlink:
			if app.IsPressed(app.DIK_LALT):
				link = chat.GetLinkFromHyperlink(hyperlink)
				ime.PasteString(link)
			else:
				self.interface.MakeHyperlinkTooltip(hyperlink)
