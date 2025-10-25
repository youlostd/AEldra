import ui
import player
import uiToolTip
import protoData
import item
import net
import localeInfo
import uiCommon

class AttrTreeRefineWindow(ui.BaseScriptWindow):

	#################################################
	## MAIN FUNCTIONS
	#################################################

	def __init__(self):
		ui.BaseScriptWindow.__init__(self, "AttrTreeRefineWindow", self.__BindObject)

		self.popupWnd = uiCommon.PopupDialog()
		self.popupWnd.Close()

	def __BindObject(self):
		self._AddLoadObject("board", "board")
		self._AddLoadObject("from_bonus", "from_bonus")
		self._AddLoadObject("to_bonus", "to_bonus")
		self._AddLoadObject("price", "price")
		self._AddLoadObject("upgrade", "upgrade_button")
		self._AddLoadObject("cancel", "cancel_button")

	def Close(self):
		ui.BaseScriptWindow.Close(self)
		self.popupWnd.Close()

	def Open(self, row, col, price):
		if constInfo.RUNE_ENABLED:
			return
			
		proto = protoData.Get(protoData.ATTRTREE)
		try:
			proto = proto[row][col]
		except:
			import dbg
			dbg.TraceError("AttrTreeRefineWindow.Open : invalid cell (%d, %d)" % (row, col))
			return

		level = player.GetAttrtreeLevel(row, col)
		old_val = proto["value"] * level / player.ATTRTREE_LEVEL_NUM
		new_val = proto["value"] * (level + 1) / player.ATTRTREE_LEVEL_NUM

		self.main["from_bonus"].SetText(uiToolTip.GET_AFFECT_STRING(proto["type"], old_val))
		self.main["to_bonus"].SetText(uiToolTip.GET_AFFECT_STRING(proto["type"], new_val))
		self.main["price"].SetText(localeInfo.TOOLTIP_BUYPRICE % localeInfo.NumberToMoneyString(price))
		self.main["upgrade"].SAFE_SetEvent(self.__OnClickUpgrade, player.AttrtreeCellToID(row, col))
		self.main["cancel"].SAFE_SetEvent(self.Close)

		self.id = player.AttrtreeCellToID(row, col)
		self.price = price
		self.needItems = []

		self.childs = []
		self.y = 0

		self.__RefreshRect()
		ui.BaseScriptWindow.Open(self)

	#################################################
	## GENERAL FUNCTIONS
	#################################################

	def __RefreshRect(self):
		width = self.main["upgrade"].GetWidth() + 10 + self.main["cancel"].GetWidth()
		width = max(width, self.main["from_bonus"].GetTextWidth())
		width = max(width, self.main["to_bonus"].GetTextWidth())
		width = max(width, self.main["price"].GetWidth())
		for child in self.childs:
			width = max(width, child.GetRight())
		height = self.main["to_bonus"].GetBottom() + 5 + self.y + self.main["price"].GetTop()

		self.main["board"].SetSize(width + 10, height)
		self.SetSize(self.main["board"].GetRealWidth(), self.main["board"].GetRealHeight())

		self.SetCenterPosition()

	def __AddChild(self, obj):
		yStart = self.main["to_bonus"].GetBottom() + 5

		obj.SetParent(self.main["board"])
		obj.SetPosition(0, yStart + self.y)
		obj.Show()
		self.childs.append(obj)

		return obj

	def AddMaterial(self, vnum, count):
		imgSlot = self.__AddChild(ui.ImageBox())
		imgSlot.SetPosition(10, imgSlot.GetTop())
		imgSlot.LoadImage("d:/ymir work/ui/public/slot_base.sub")

		item.SelectItem(1, 2, vnum)
		img = ui.ImageBox()
		img.SetParent(imgSlot)
		img.LoadImage(item.GetIconImageFileName())
		img.Show()
		imgSlot.img = img

		text = self.__AddChild(ui.TextLine())
		text.SetPosition(imgSlot.GetRight() + 10, text.GetTop() + imgSlot.GetHeight() / 2)
		text.SetVerticalAlignCenter()
		if count > 1:
			text.SetText("%dx %s" % (count, item.GetItemName()))
		else:
			text.SetText("%s" % item.GetItemName())

		self.needItems.append([vnum, count])
		self.y += imgSlot.GetHeight() + 5
		self.__RefreshRect()

	#################################################
	## GENERAL FUNCTIONS
	#################################################

	def __OnClickUpgrade(self):
		# check requirements
		errText = localeInfo.ATTRTREE_UPGRADE_ERROR
		if player.GetElk() < self.price:
			self.popupWnd.SetText(errText % localeInfo.NumberToMoneyString(self.price))
			self.popupWnd.Open()
			return
		for itemData in self.needItems:
			if player.GetItemCountByVnum(itemData[0]) < itemData[1]:
				item.SelectItem(1, 2, itemData[0])
				self.popupWnd.SetText(errText % ("%dx %s" % (itemData[1], item.GetItemName())))
				self.popupWnd.Open()
				return

		# upgrade
		net.SendChatPacket("/attrtree_levelup %d" % self.id)
		self.Close()

class AttrTreeWindow(ui.BaseScriptWindow):

	PATH = "d:/ymir work/ui/game/attrtree/"

	#################################################
	## MAIN FUNCTIONS
	#################################################

	def __init__(self):
		ui.BaseScriptWindow.__init__(self, "AttrTreeWindow", self.__BindObject)
		self.__LoadWindow()

		refineWnd = AttrTreeRefineWindow()
		refineWnd.Close()
		self.refineWnd = refineWnd

		self.toolTip = uiToolTip.ItemToolTip()
		self.toolTip.HideToolTip()

	def __BindObject(self):
		self._AddLoadObject("close", "close_btn")

		for row in xrange(player.ATTRTREE_ROW_NUM):
			bindData = {
				"title" : "title_%d" % (row + 1),
			}
			for col in xrange(player.ATTRTREE_COL_NUM):
				bindData["ball%d" % col] = "ball_%d_%d" % (row + 1, col + 1)
				if col > 0:
					bindData["connect%d" % col] = "connect_%d_%d" % (row + 1, col + 1)

			self._AddLoadObject("row%d" % row, bindData)

	def __LoadWindow(self):
		self.main["close"].SAFE_SetEvent(self.Close)

		for row in xrange(player.ATTRTREE_ROW_NUM):
			objRow = self.main["row%d" % row]
			for col in xrange(player.ATTRTREE_COL_NUM):
				objRow["ball%d" % col].SAFE_SetOverInEvent(self.__OnOverBall, row, col)
				objRow["ball%d" % col].SAFE_SetOverOutEvent(self.__OnOutBall)
				objRow["ball%d" % col].SAFE_SetEvent(self.__OnClickBall, row, col)

		self.Refresh()

	def Destroy(self):
		ui.BaseScriptWindow.Destroy(self)
		self.refineWnd = None

	def Close(self):
		self.toolTip.HideToolTip()
		ui.BaseScriptWindow.Close(self)
		self.refineWnd.Close()

	#################################################
	## HELPER FUNCTIONS
	#################################################

	def __SetConnector(self, obj, active):
		if active:
			obj.LoadImage(self.PATH + "connect_1.tga")
		else:
			obj.LoadImage(self.PATH + "connect_0.tga")

	def __SetBall(self, obj, level):
		obj.SetUpVisual(self.PATH + "ball_%d_1.tga" % level)
		obj.SetOverVisual(self.PATH + "ball_%d_2.tga" % level)
		obj.SetDownVisual(self.PATH + "ball_%d_3.tga" % level)
		obj.SetDisableVisual(self.PATH + "ball_%d_1.tga" % level)

	#################################################
	## EVENT FUNCTIONS
	#################################################

	def __OnOverBall(self, row, col):
		proto = protoData.Get(protoData.ATTRTREE)
		try:
			proto = proto[row][col]
		except:
			import dbg
			dbg.TraceError("AttrTreeRefineWindow.Open : invalid cell (%d, %d)" % (row, col))
			return

		level = player.GetAttrtreeLevel(row, col)
		val = proto["value"] * level / player.ATTRTREE_LEVEL_NUM

		self.toolTip.ClearToolTip()
		color = self.toolTip.GetAttributeColor(0, val)
		self.toolTip.AppendTextLine(uiToolTip.GET_AFFECT_STRING(proto["type"], val), color)
		if level < player.ATTRTREE_LEVEL_NUM:
			val = proto["value"] * (level + 1) / player.ATTRTREE_LEVEL_NUM
			self.toolTip.AppendTextLine(uiToolTip.GET_AFFECT_STRING(proto["type"], val), self.toolTip.SPECIAL_POSITIVE_COLOR_LOW)
		self.toolTip.ShowToolTip()

	def __OnOutBall(self):
		self.toolTip.HideToolTip()

	def __OnClickBall(self, row, col):
		net.SendChatPacket("/attrtree_level_info %d" % player.AttrtreeCellToID(row, col))

	#################################################
	## REFRESH FUNCTIONS
	#################################################

	def Refresh(self):
		for row in xrange(player.ATTRTREE_ROW_NUM):
			for col in xrange(player.ATTRTREE_COL_NUM):
				self.RefreshCell(row, col)

	def RefreshCell(self, row, col):
		level = player.GetAttrtreeLevel(row, col)

		rowObj = self.main["row%d" % row]
		ball = rowObj["ball%d" % col]
		nextBall = rowObj.get("ball%d" % (col + 1), None)
		connect = rowObj.get("connect%d" % col, None)

		# check next enabled
		if nextBall:
			nextLevel = player.GetAttrtreeLevel(row, col + 1)
			# nextBall.SetEnabled(level > 0 and nextLevel < player.ATTRTREE_LEVEL_NUM)
			nextBall.SetEnabled(level >= player.ATTRTREE_LEVEL_NUM and nextLevel < player.ATTRTREE_LEVEL_NUM)

		# check connect
		if connect:
			self.__SetConnector(connect, level > 0)

		# set own level
		self.__SetBall(ball, level)
		if level >= player.ATTRTREE_LEVEL_NUM:
			ball.Disable()

	#################################################
	## REFINE FUNCTIONS
	#################################################

	def OpenRefineDialog(self, row, col, price):
		self.refineWnd.Open(row, col, price)

	def AppendRefineMaterial(self, vnum, count):
		self.refineWnd.AddMaterial(vnum, count)
