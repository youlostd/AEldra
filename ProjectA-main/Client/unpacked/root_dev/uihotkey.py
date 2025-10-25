import ui
import chat
import app
import grp
import cfg
import wndMgr
import localeInfo
import constInfo

class HotkeyWindow(ui.ScriptWindow):

	#################################################
	## MAIN FUNCTIONS
	#################################################

	STATE_NONE = 0
	STATE_SELECT_HOTKEY = 1

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.index = -1
		self.state = self.STATE_NONE

		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/HotkeyWindow.py")
		except:
			import exception
			exception.Abort("HotkeyWindow.LoadDialog.LoadScript")

		try:
			GetObject=self.GetChild
			self.board = GetObject("board")

			self.main = {
				"text" : GetObject("text"),
				"hotkey" : GetObject("hotkey_button"),
			}

		except:
			import exception
			exception.Abort("HotkeyWindow.LoadDialog.BindObject")

		self.board.SetCloseEvent(ui.__mem_func__(self.Close))
		self.main["hotkey"].SAFE_SetEvent(self.OnClickHotkeyButton)

	def Destroy(self):
		self.Close()
		ui.ScriptWindow.Destroy(self)

	def Open(self, index):
		self.index = index.replace(' ','')
		self.state = self.STATE_NONE
		self.Refresh()

		self.SetCenterPosition()
		self.Show()
		self.SetTop()

	def Close(self):
		self.Unlock()
		self.Hide()

	def OnPressEscapeKey(self):
		if self.state == self.STATE_SELECT_HOTKEY:
			self.state = self.STATE_NONE
			self.Refresh()
			self.Unlock()
		else:
			self.Close()
		return True

	def RefreshText(self, isCtrl, isAlt, key):
		if key == 0 and self.state == self.STATE_NONE:
			self.main["text"].SetText(localeInfo.HOTKEY_BUTTON_DISABLE_TEXT)
		else:
			if key != 0 and key in localeInfo.AVAIL_KEY_LIST:
				text = localeInfo.AVAIL_KEY_LIST[key]
			else:
				text = "?"
			if isAlt:
				text = localeInfo.HOTKEY_ALT + " + " + text
			if isCtrl:
				text = localeInfo.HOTKEY_CONTROL + " + " + text

			self.main["text"].SetText(text)

	def Refresh(self):
		if self.state == self.STATE_NONE:
			try:
				isCtrl = int(cfg.Get(cfg.SAVE_PLAYER, "hotkey_ctrl_%s" % self.index, "0"))
				isAlt = int(cfg.Get(cfg.SAVE_PLAYER, "hotkey_alt_%s" % self.index, "0"))
				key = int(cfg.Get(cfg.SAVE_PLAYER, "hotkey_%s" % self.index, "0"))
			except:
				isCtrl, isAlt, key = (0, 0, 0)
			self.RefreshText(isCtrl, isAlt, key)

			self.main["hotkey"].SetText(localeInfo.HOTKEY)
			self.main["hotkey"].Enable()

		elif self.state == self.STATE_SELECT_HOTKEY:
			isCtrl = app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL)
			isAlt = app.IsPressed(app.DIK_LALT)
			self.RefreshText(isCtrl, isAlt, 0)

			if self.main["hotkey"].IsEnabled():
				self.main["hotkey"].SetText(localeInfo.HOTKEY_BUTTON_DISABLE_TEXT)
				self.main["hotkey"].Disable()

	def OnKeyUp(self, key):
		if self.state == self.STATE_SELECT_HOTKEY:
			if key in localeInfo.AVAIL_KEY_LIST:
				tchat ("KEY FOUND %d %s" % (key, localeInfo.AVAIL_KEY_LIST[key]))
				isCtrl = app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL)
				isAlt = app.IsPressed(app.DIK_LALT)

				if key in constInfo.HOTKEYS and not isCtrl and not isAlt:
					chat.AppendChat(1, localeInfo.HOTKEY_USED)
					return True

				cfg.Set(cfg.SAVE_PLAYER, "hotkey_ctrl_%s" % self.index, str(isCtrl))
				cfg.Set(cfg.SAVE_PLAYER, "hotkey_alt_%s" % self.index, str(isAlt))
				cfg.Set(cfg.SAVE_PLAYER, "hotkey_%s" % self.index, str(key))

				self.state = self.STATE_NONE
				self.Refresh()
				self.Unlock()
				chat.AppendChat(1, localeInfo.RESTART_OR_WARP_REQUIRED)
				return True

			elif key == 211: # KEY_DELETE
				cfg.Set(cfg.SAVE_PLAYER, "hotkey_ctrl_%s" % self.index, "")
				cfg.Set(cfg.SAVE_PLAYER, "hotkey_alt_%s" % self.index, "")
				cfg.Set(cfg.SAVE_PLAYER, "hotkey_%s" % self.index, "")

				self.state = self.STATE_NONE
				self.Refresh()
				self.Unlock()

				return True
			elif key not in (app.DIK_LCONTROL, app.DIK_RCONTROL, app.DIK_LALT):
				chat.AppendChat(1, "Invalid Key")

		return False

	def OnClickHotkeyButton(self):
		self.state = self.STATE_SELECT_HOTKEY
		self.Refresh()

		self.SetTop()
		self.Lock()

	def OnUpdate(self):
		if self.state == self.STATE_SELECT_HOTKEY:
			self.Refresh()

	def OnRender(self):
		if self.state == self.STATE_SELECT_HOTKEY:
			grp.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 0.5))
			grp.RenderBar(0, 0, wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())
