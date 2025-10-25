import ui
import item
import uiToolTip
import player
import chat
import net
import localeInfo

class SelectAttrRemoveWindow(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.curItemPos = 0
		self.curItemVnum = 0

		self.itemToolTip = uiToolTip.ItemToolTip()
		self.itemToolTip.HideToolTip()
		self.__LoadDialog()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadDialog(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/SelectAttrRemoveWindow.py")

			self.board = self.GetChild("board")
			self.item = self.GetChild("item")
			self.listBox = self.GetChild("attr_list_box")
			self.listBoxBG = self.GetChild("attr_list_box_bg")
			self.remove_btn = self.GetChild("remove_button")

		except:
			import exception
			exception.Abort("PopupDialog.LoadDialog.BindObject")

		self.item.SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowToolTip)
		self.item.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.itemToolTip.HideToolTip)

		self.remove_btn.SAFE_SetEvent(self.__OnClickRemoveButton)

		self.board.SetCloseEvent(ui.__mem_func__(self.Close))

	def Open(self, scrollItemPos, itemPos):
		self.scrollItemPos = scrollItemPos
		self.__LoadItem(itemPos)

		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.Hide()
		self.itemToolTip.HideToolTip()
		self.listBox.RemoveAllItems()

	def Destroy(self):
		self.Close()
		ui.ScriptWindow.Destroy(self)

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def __LoadItem(self, itemPos):
		self.curItemPos = itemPos
		self.curItemVnum = player.GetItemIndex(itemPos)

		self.itemToolTip.HideToolTip()

		item.SelectItem(1, 2, self.curItemVnum)
		self.item.LoadImage(item.GetIconImageFileName())

		self.listBoxBG.SetPosition(0, self.item.GetBottom() + 5)

		maxTextWidth = 0
		maxTextHeight = 0
		self.listBox.RemoveAllItems()
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			(attrType, val) = player.GetItemAttribute(itemPos, i)
			if attrType > 0 :
				apItem = ui.ListBoxEx.Item()
				text = ui.TextLine()
				text.SetParent(apItem)
				text.SetHorizontalAlignCenter()
				text.SetText(uiToolTip.GET_AFFECT_STRING(attrType, val))
				text.Show()
				apItem.text = text
				apItem.pos = i

				self.listBox.AppendItem(apItem)

				maxTextWidth = max(maxTextWidth, text.GetTextSize()[0])
				maxTextHeight = max(maxTextHeight, text.GetTextSize()[1])

		self.listBoxBG.SetSize(maxTextWidth + 20, (maxTextHeight + 3) * self.listBox.GetItemCount() + 2 + 15)
		self.listBox.SetItemSize(maxTextWidth, maxTextHeight)
		self.listBox.SetItemStep(maxTextHeight + 3)

		for i in xrange(self.listBox.GetItemCount()):
			apItem = self.listBox.GetItemAtIndex(i)
			apItem.SetSize(maxTextWidth, maxTextHeight)
			apItem.text.SetPosition(maxTextWidth / 2, 0)

		
		self.listBox.SetPosition(10, 10)

		windowWidth = max(self.remove_btn.GetWidth(), self.listBoxBG.GetWidth())
		self.board.SetSize(windowWidth, self.listBoxBG.GetBottom() + 24 + 20)
		self.SetSize(self.board.GetRealWidth(), self.board.GetRealHeight())

		self.remove_btn.UpdateRect()

	def OnUpdate(self):
		if player.GetItemIndex(self.curItemPos) != self.curItemVnum:
			self.Close()

	def __ShowToolTip(self):
		self.itemToolTip.SetInventoryItem(self.curItemPos)

	def __OnClickRemoveButton(self):
		currItem = self.listBox.GetSelectedItem()
		if not currItem:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SELECT_ATTR_DETACH_REMOVE_SELECT_ATTR)
			return

		net.SendUseDetachmentSinglePacket(self.scrollItemPos, self.curItemPos, currItem.pos)
		self.Close()
