import ui
import item
import uiToolTip
import player
import chat
import net
import localeInfo

class SelectMetinDetachWindow(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.curItemPos = 0
		self.curItemVnum = 0

		self.activeIdx = -1

		self.itemToolTip = uiToolTip.ItemToolTip()
		self.itemToolTip.HideToolTip()
		self.__LoadDialog()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadDialog(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/SelectMetinDetachWindow.py")

			self.board = self.GetChild("board")
			self.item = self.GetChild("item")
			self.metin_slot_bg = self.GetChild("metin_slot_background")
			self.metin_slot = self.GetChild("metin_slot")
			self.remove_btn = self.GetChild("remove_button")

		except:
			import exception
			exception.Abort("PopupDialog.LoadDialog.BindObject")

		self.item.SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowToolTip, -1)
		self.item.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.itemToolTip.HideToolTip)

		self.metin_slot.SetOverInItemEvent(ui.__mem_func__(self.__ShowToolTip))
		self.metin_slot.SetOverOutItemEvent(ui.__mem_func__(self.itemToolTip.HideToolTip))
		self.metin_slot.SetSelectItemSlotEvent(ui.__mem_func__(self.__OnClickSlot))
		self.metin_slot.SetUseSlotEvent(ui.__mem_func__(self.__OnClickSlot))

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

	def Destroy(self):
		self.Close()
		ui.ScriptWindow.Destroy(self)

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def __LoadItem(self, itemPos):
		self.activeIdx = -1
		self.curItemPos = itemPos
		self.curItemVnum = player.GetItemIndex(itemPos)

		self.itemToolTip.HideToolTip()

		item.SelectItem(1, 2, self.curItemVnum)
		self.item.LoadImage(item.GetIconImageFileName())

		self.metin_slot_bg.SetPosition(0, self.item.GetBottom() + 5)

		slotToReal = []
		metinSlots = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			socket = player.GetItemMetinSocket(itemPos, i)
			if socket > 2 and socket != 28960:
				metinSlots.append(socket)
				tchat("%d: %d" % (i, socket))
				slotToReal.append(i)
		self.metinSlots = metinSlots
		self.metinSlotsToReal = slotToReal

		self.metin_slot_bg.SetSize((32 + 5) * len(metinSlots) - 5, 32)
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			self.metin_slot.ClearSlot(i)
			if i < len(metinSlots):
				self.metin_slot.SetItemSlot(i, metinSlots[i])
				self.metin_slot.ShowSlotBaseImage(i)
				self.metin_slot.DeactivateSlot(i)
				tchat("SHOW %d: %d" % (i, socket))
			else:
				self.metin_slot.HideSlotBaseImage(i)
				tchat("HIDE %d: %d" % (i, socket))

		self.board.SetSize(self.GetWidth(), self.metin_slot_bg.GetBottom() + 24 + 20)
		self.SetSize(self.board.GetRealWidth(), self.board.GetRealHeight())

		self.remove_btn.UpdateRect()

	def OnUpdate(self):
		if player.GetItemIndex(self.curItemPos) != self.curItemVnum:
			self.Close()
			return

	def __ShowToolTip(self, index = -1):
		if index == -1:
			self.itemToolTip.SetInventoryItem(self.curItemPos)
		else:
			self.itemToolTip.SetItemToolTip(self.metinSlots[index])

	def __OnClickSlot(self, index):
		if self.activeIdx > -1:
			self.metin_slot.DeactivateSlot(self.activeIdx)
			if self.activeIdx == index:
				self.activeIdx = -1
				return

		self.activeIdx = index
		self.metin_slot.ActivateSlot(self.activeIdx)

	def __OnClickRemoveButton(self):
		if self.activeIdx == -1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SELECT_METIN_DETACH_REMOVE_SELECT_STONE)
			return

		net.SendUseDetachmentSinglePacket(self.scrollItemPos, self.curItemPos, self.metinSlotsToReal[self.activeIdx])
		self.Close()
