import ui
import net
import mouseModule
import player
import snd
import localeInfo
import item
import grp
import uiScriptLocale
import uiToolTip
import constInfo
import cfg

class CubeResultWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/CubeResultWindow.py")
		except:
			import exception
			exception.Abort("CubeResultWindow.LoadDialog.LoadScript")

		try:
			GetObject=self.GetChild
			# self.titleBar = GetObject("TitleBar")
			self.btnClose = GetObject("CloseButton")
			self.cubeSlot = GetObject("CubeSlot")

		except:
			import exception
			exception.Abort("CubeWindow.LoadDialog.BindObject")

		self.cubeSlot.SetOverInItemEvent(ui.__mem_func__(self.__OnOverInItem))
		self.cubeSlot.SetOverOutItemEvent(ui.__mem_func__(self.__OnOverOutItem))
		# self.titleBar.SetCloseEvent(ui.__mem_func__(self.__OnCloseButtonClick))
		self.btnClose.SetEvent(ui.__mem_func__(self.__OnCloseButtonClick))
		self.itemVnum = 0

	def Destroy(self):
		self.ClearDictionary()
		# self.titleBar = None
		self.btnClose = None
		self.cubeSlot = None
		self.tooltipItem = None
		self.itemVnum = 0
		ui.ScriptWindow.Destroy(self)

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem

	def SetCubeResultItem(self, itemVnum, count):
		self.itemVnum = itemVnum

		if 0 == count:
			count = 1

		self.cubeSlot.SetItemSlot(0, itemVnum, count)

	def Open(self):
		self.Show()

	def Close(self):
		self.Hide()

	def __OnCloseButtonClick(self):
		self.Close()

	def __OnOverInItem(self, slotIndex):
		if self.tooltipItem:
			if 0 != self.itemVnum:
				self.tooltipItem.SetItemToolTip(self.itemVnum)

	def __OnOverOutItem(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def OnPressEscapeKey(self):
		if 0 != self.eventClose:
			self.eventClose()
		return True

	if constInfo.SAVE_WINDOW_POSITION:
		def OnMoveWindow(self, x, y):
			if constInfo.SAVE_WINDOW_POSITION:
				cfg.Set(cfg.SAVE_GENERAL, "wnd_pos_cube_r", ("%d %d") % (x, y))

		def Show(self):
			if int(cfg.Get(cfg.SAVE_GENERAL, "save_wnd_pos", "0")):
				x, y = map(int, cfg.Get(cfg.SAVE_GENERAL, "wnd_pos_cube_r", "0 0").split(" "))
				if x and y:
					self.SetPosition(x, y)
			ui.ScriptWindow.Show(self)



class CubeWindow(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.xShopStart = 0
		self.yShopStart = 0
		self.isUsable	= False
		self.defaultText = ""
		self.resultChances = [None,None,None]

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/CubeWindow.py")			
		except:
			import exception
			exception.Abort("CubeWindow.LoadDialog.LoadScript")

		try:
			GetObject=self.GetChild
			# self.titleBar = GetObject("TitleBar")
			self.titleText = GetObject("TitleName")
			self.btnAccept = GetObject("AcceptButton")
			self.btnCancel = GetObject("CancelButton")
			self.btnClose = GetObject("CloseButton")
			self.cubeSlot = GetObject("CubeSlot")
			self.needMoney = GetObject("NeedMoney")
			self.btnMakeAll = GetObject("MakeAll")
			self.btnMakeAll.SetEvent(ui.__mem_func__(self.__OnMakeAllClick))
			if not constInfo.CUBE_MAKE_ALL:
				self.btnMakeAll.Hide()
                
			self.contentScrollbar = GetObject("contentScrollbar")
			self.resultSlots = [GetObject("result1"), GetObject("result2"), GetObject("result3")]
			self.resultChances = [GetObject("result_chance_1"), GetObject("result_chance_2"), GetObject("result_chance_3")]

			if __SERVER__ == 1:
				pass
			else:
				for i in xrange(3):
					if self.resultChances[i]:
						self.resultChances[i].Hide()

			self.materialSlots = [ 
				[GetObject("material11"), GetObject("material12"), GetObject("material13"), GetObject("material14"), GetObject("material15")],
				[GetObject("material21"), GetObject("material22"), GetObject("material23"), GetObject("material24"), GetObject("material25")],
				[GetObject("material31"), GetObject("material32"), GetObject("material33"), GetObject("material34"), GetObject("material35")],
			]

			self.defaultText = self.titleText.GetText()

			row = 0
			for materialRow in self.materialSlots:
				j = 0
				for material in materialRow:
					material.SetOverInItemEvent(lambda trash = 0, rowIndex = row,  col = j: self.__OverInMaterialSlot(trash, rowIndex, col))
					material.SetSelectItemSlotEvent(lambda trash = 0, rowIndex = row,  col = j: self.__OnSelectMaterialSlot(trash, rowIndex, col))
					material.SetOverOutItemEvent(lambda : self.__OverOutMaterialSlot())
					material.itemVnumStart = 0
					j = j + 1
				row = row + 1

			row = 0
			for resultSlot in self.resultSlots:
				resultSlot.SetOverInItemEvent(lambda trash = 0, rowIndex = row: self.__OverInCubeResultSlot(trash, rowIndex))
				resultSlot.SetOverOutItemEvent(lambda : self.__OverOutMaterialSlot())
				row = row + 1

		except:
			import exception
			exception.Abort("CubeWindow.LoadDialog.BindObject")

		self.contentScrollbar.SetScrollStep(0.15)
		self.contentScrollbar.SetScrollEvent(ui.__mem_func__(self.OnScrollResultList))
		self.cubeSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.__OnSelectEmptySlot))
		self.cubeSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.__OnSelectItemSlot))
		self.cubeSlot.SetOverInItemEvent(ui.__mem_func__(self.__OnOverInItem))
		self.cubeSlot.SetOverOutItemEvent(ui.__mem_func__(self.__OnOverOutItem))
		
		# self.titleBar.SetCloseEvent(ui.__mem_func__(self.__OnCloseButtonClick))
		self.btnCancel.SetEvent(ui.__mem_func__(self.__OnCloseButtonClick))
		self.btnAccept.SetEvent(ui.__mem_func__(self.__OnAcceptButtonClick))
		self.btnClose.SetEvent(ui.__mem_func__(self.__OnCloseButtonClick))

		self.cubeItemInfo = {}
		self.cubeResultInfos = []
		self.cubeMaterialInfos = {}

		self.tooltipItem = None

		self.firstSlotIndex = 0
		self.RESULT_SLOT_COUNT = len(self.resultSlots)
		self.SLOT_SIZEX	= 32
		self.SLOT_SIZEY	= 32
		self.CUBE_SLOT_COUNTX = 8
		self.CUBE_SLOT_COUNTY = 3

	def SetTitleText(self, text):
		if text == "":
			text = self.defaultText
		self.titleText.SetText(text)

	def SetItemToolTip(self, itemTooltip):
		self.tooltipItem = itemTooltip

	def GetResultCount(self):
		return len(self.cubeResultInfos)

	def OnScrollResultList(self):
		count = self.GetResultCount()
		scrollLineCount = max(0, count - self.RESULT_SLOT_COUNT)
		startIndex = int(scrollLineCount * self.contentScrollbar.GetPos())

		if startIndex != self.firstSlotIndex:
			self.firstSlotIndex = startIndex
			self.Refresh()

	def __OnMakeAllClick(self):
		net.SendChatPacket("/cube make all")

	def OnMouseWheel(self, len):
		lineCount = self.GetResultCount()
		if self.IsInPosition() and self.contentScrollbar.IsShow() and lineCount > 0:
			dir = constInfo.WHEEL_TO_SCROLL(len)
			new_pos = self.contentScrollbar.GetPos() + ((1.0 / lineCount) * dir)
			new_pos = max(0.0, new_pos)
			new_pos = min(1.0, new_pos)
			self.contentScrollbar.SetPos(new_pos)
			return True
		return False

	def AddCubeResultItem(self, itemVnum, count, chance):
		self.cubeResultInfos.append((itemVnum, count, chance))
		#self.Refresh()

	def AddMaterialInfo(self, itemIndex, orderIndex, itemVnumStart, itemVnumEnd, itemCount):
		if itemIndex not in self.cubeMaterialInfos:
			self.cubeMaterialInfos[itemIndex] = [[], [], [], [], []]

		self.cubeMaterialInfos[itemIndex][orderIndex].append({"vnum_start":itemVnumStart, "vnum_end":itemVnumEnd, "count":itemCount, "vnum_cur":itemVnumStart, "delay":0})
		#print "AddMaterialInfo", itemIndex, orderIndex, itemVnum, itemCount, self.cubeMaterialInfos

	def ClearCubeResultItem(self):
		self.cubeResultInfos = []
		self.Refresh()

	def Destroy(self):
		self.ClearDictionary()
		
		# self.titleBar = None
		self.btnAccept = None
		self.btnCancel = None
		self.btnClose = None
		self.cubeSlot = None
		self.tooltipItem = None
		self.needMoney = None

		ui.ScriptWindow.Destroy(self)

	def __OverOutMaterialSlot(self):
		self.tooltipItem.SetCannotUseItemForceSetDisableColor(True)
		self.tooltipItem.HideToolTip()

	def __OverInCubeResultSlot(self, trash, resultIndex):
		self.tooltipItem.ClearToolTip()
		self.tooltipItem.SetCannotUseItemForceSetDisableColor(True)

		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(0)
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append((0, 0))

		#print "resultIndex, firstSlotIndex", resultIndex, self.firstSlotIndex

		resultIndex = resultIndex + self.firstSlotIndex
		itemVnum, itemCount, chance = self.cubeResultInfos[resultIndex]

		self.tooltipItem.AddItemData(itemVnum, metinSlot, attrSlot)
		

	# ��Ḧ Ŭ���ϸ� �κ��丮���� �ش� �������� ã�Ƽ� �����.
	def __OnSelectMaterialSlot(self, trash, resultIndex, materialIndex):
		resultIndex = resultIndex + self.firstSlotIndex
		if resultIndex not in self.cubeMaterialInfos:
			return

		materialInfo = self.cubeMaterialInfos[resultIndex]
		materialCount = len(materialInfo[materialIndex])

		if 0 == materialCount:
			return

		for curMaterial in materialInfo[materialIndex]:
			bAddedNow = False	# �̹��� Ŭ�������ν� �������� �߰��Ǿ���?
			item.SelectItem(1, 2, curMaterial["vnum_cur"])
			itemSizeX, itemSizeY = item.GetItemSize(1,2,3)

			# ������ �ʿ��� ��ŭ�� ��Ḧ ������ �ִ°�?
			if player.GetItemCountByVnumRange(curMaterial["vnum_start"], curMaterial["vnum_end"]) >= curMaterial["count"]:
				for i in xrange(player.INVENTORY_SLOT_COUNT):
					vnum = player.GetItemIndex(i)
					count= player.GetItemCount(i)

					if vnum >= curMaterial["vnum_start"] and vnum <= curMaterial["vnum_end"] and count >= curMaterial["count"]:
						# �̹� ���� �������� ��ϵǾ� �ִ��� �˻��ϰ�, ���ٸ� �߰���
						bAlreadyExists = False
						for slotPos, invenPos in self.cubeItemInfo.items():
							if invenPos == i:
								bAlreadyExists = True

						if True == bAlreadyExists:
							continue #continue inventory iterating

						#print "Cube Status : ", self.cubeItemInfo

						# ���� �����ϸ� ť�꿡 ��ϵ��� ���� �������̹Ƿ�, �� ť�� ���Կ� �ش� ������ �߰�
						bCanAddSlot = False
						for slotPos in xrange(self.cubeSlot.GetSlotCount()):
							# �� ť�� ������ ����ִ°�?
							if not slotPos in self.cubeItemInfo:
								upperColumnItemSizeY = -1
								currentSlotLine = int(slotPos / self.CUBE_SLOT_COUNTX)
								cubeColumn = int(slotPos % self.CUBE_SLOT_COUNTX)


								# ���� ť�꿡 3ĭ¥�� �������� ��ϵǾ� �ִٸ�, �� ��(column)�� �� �̻� �� �͵� ���� �Ѿ��
								if cubeColumn in self.cubeItemInfo:
									columnVNUM = player.GetItemIndex(self.cubeItemInfo[cubeColumn])
									item.SelectItem(1, 2, columnVNUM)
									columnItemSizeX, columnItemSizeY = item.GetItemSize(1,2,3)

									if 3 == columnItemSizeY:
										continue #continue cube slot iterating

								if 0 < currentSlotLine and slotPos - self.CUBE_SLOT_COUNTX in self.cubeItemInfo:
									upperColumnVNUM = player.GetItemIndex(self.cubeItemInfo[slotPos - self.CUBE_SLOT_COUNTX])
									item.SelectItem(1, 2, upperColumnVNUM)
									columnItemSizeX, upperColumnItemSizeY = item.GetItemSize(1,2,3)
								
								# 1ĭ¥�� �������� �ٷ� ���ٿ� ��ĭ¥�� �������� �־�� ��
								if 1 == itemSizeY: 
									if 0 == currentSlotLine:
										bCanAddSlot = True
									elif 1 == currentSlotLine and 1 == upperColumnItemSizeY:
										bCanAddSlot = True
									elif 2 == currentSlotLine:
										bCanAddSlot = True
								# 2ĭ¥�� �������� ���Ʒ��� ����־�� ��
								elif 2 == itemSizeY:
									if 0 == currentSlotLine and not cubeColumn + self.CUBE_SLOT_COUNTX in self.cubeItemInfo:
										bCanAddSlot = True
									elif 1 == currentSlotLine and 1 == upperColumnItemSizeY and not cubeColumn + (self.CUBE_SLOT_COUNTX * 2) in self.cubeItemInfo:
										bCanAddSlot = True
								# 3ĭ¥�� �������� �ش� Column ��ü�� ��� ����־�� ��
								else:
									if not cubeColumn in self.cubeItemInfo and not cubeColumn + self.CUBE_SLOT_COUNTX in self.cubeItemInfo and not cubeColumn + (self.CUBE_SLOT_COUNTX * 2) in self.cubeItemInfo:
										bCanAddSlot = True

								if True == bCanAddSlot:
									self.cubeItemInfo[slotPos] = i
									self.cubeSlot.SetItemSlot(slotPos, vnum, count)
									net.SendChatPacket("/cube add %d %d" % (slotPos, i))
									
									bAddedNow = True

							if True == bAddedNow:
								break #break cube slot iterating

						if True == bAddedNow:
							break #break inventory iterating

				if True == bAddedNow:
					break #break material iterating

				

	def __OverInMaterialSlot(self, trash, resultIndex, col):
		self.tooltipItem.ClearToolTip()
		self.tooltipItem.SetCannotUseItemForceSetDisableColor(False)

		resultIndex = resultIndex + self.firstSlotIndex

		if resultIndex not in self.cubeMaterialInfos:
			return

		i = 0
		materialInfo = self.cubeMaterialInfos[resultIndex]
		materialCount = len(materialInfo[col])

		for curMaterial in materialInfo[col]:
			colorEnough = grp.GenerateColor(0.5411, 0.7254, 0.5568, 1.0)
			colorNeed = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)
			color = colorNeed

			item.SelectItem(1, 2, curMaterial["vnum_start"])
			if curMaterial["vnum_start"] != curMaterial["vnum_end"]:
				# check if metin
				if item.GetItemType() == item.ITEM_TYPE_METIN and item.SelectItem(1, 2, curMaterial["vnum_end"]) and item.GetItemType() == item.ITEM_TYPE_METIN:
					if player.GetItemCountByVnumRange(curMaterial["vnum_start"], curMaterial["vnum_end"]) >= curMaterial["count"]:
						color = colorEnough
					level_start = (curMaterial["vnum_start"] % 1000) / 100
					level_end = (curMaterial["vnum_end"] % 1000) / 100
					if level_start == level_end:
						self.tooltipItem.AppendTextLine(localeInfo.CUBE_STONE_MATERIAL_SINGLE % level_start)
					else:
						self.tooltipItem.AppendTextLine((localeInfo.CUBE_STONE_MATERIAL_RANGE % (level_start, level_end)))
					continue

				item.SelectItem(1, 2, curMaterial["vnum_start"])

			if player.GetItemCountByVnum(curMaterial["vnum_cur"]) >= curMaterial["count"]:
				color = colorEnough
			self.tooltipItem.AppendTextLine("%s" % (item.GetItemName()), color).SetFeather()
			
			if i < materialCount - 1:
				self.tooltipItem.AppendTextLine(uiScriptLocale.CUBE_REQUIRE_MATERIAL_OR)
				
			i = i + 1

		self.tooltipItem.Show()
	
	def Open(self):
		self.cubeItemInfo = {}
		self.cubeResultInfos = []
		self.cubeMaterialInfos = {}

		self.Refresh()
		self.Show()

		self.isUsable	= True
		(self.xShopStart, self.yShopStart, z) = player.GetMainCharacterPosition()

	def UpdateInfo(self, gold, itemVnum, count):
		if self.needMoney:
			self.needMoney.SetText(localeInfo.NumberToMoneyString(gold))

		self.Refresh()

	def OnPressEscapeKey(self):
		self.__OnCloseButtonClick()
		return True
	
	def Close(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

		self.Hide()
		self.cubeItemInfo = {}
		self.cubeMaterialInfos = {}
		self.cubeResultInfos = {}
		self.firstSlotIndex = 0
		self.contentScrollbar.SetPos(0)

		if self.needMoney:
			self.needMoney.SetText("0")		

	def Clear(self):
		self.Refresh()

	def Refresh(self):
		for slotPos in xrange(self.cubeSlot.GetSlotCount()):

			if not slotPos in self.cubeItemInfo:
				self.cubeSlot.ClearSlot(slotPos)
				continue

			invenPos = self.cubeItemInfo[slotPos]
			itemCount = player.GetItemCount(invenPos)
			if itemCount > 0:
				self.cubeSlot.SetItemSlot(slotPos, player.GetItemIndex(invenPos), itemCount)
			else:
				del self.cubeItemInfo[slotPos]
				self.cubeSlot.ClearSlot(slotPos)

		i = 0
		for itemVnum, count, chance in self.cubeResultInfos[self.firstSlotIndex:]:
			currentSlot = self.resultSlots[i]

			item.SelectItem(1, 2, itemVnum)
			
			currentSlot.SetItemSlot(0, itemVnum, count)
			currentSlot.Show()

			# Center Align
			item.SelectItem(1, 2, itemVnum)
			sizeX, sizeY = item.GetItemSize(1,2,3)
			localX, localY = currentSlot.GetLocalPosition()

			currentSlot.SetSize(self.SLOT_SIZEX, self.SLOT_SIZEY * sizeY)

			adjustLocalY = 0
			if sizeY < 3:
				adjustLocalY = int(32 / sizeY)

			currentSlot.SetPosition(localX, 0 + adjustLocalY)

			resultChance = self.resultChances[i]

			if resultChance:
				resultChance.SetText("%d%%" % chance)

			i = i + 1

			if 3 <= i:
				break

		for j in xrange(i, len(self.resultSlots)):
			self.resultSlots[j].Hide()

		#print "self.cubeMaterialInfos : ", self.cubeMaterialInfos
		if self.firstSlotIndex in self.cubeMaterialInfos:
			for i in xrange(self.RESULT_SLOT_COUNT):
				#print "Refresh ::: ", materialList
				j = 0
				if self.firstSlotIndex + i < len(self.cubeMaterialInfos):
					materialList = self.cubeMaterialInfos[self.firstSlotIndex + i]
					for materialInfo in materialList:
						if 0 < len(materialInfo):
							currentSlot = self.materialSlots[i][j]
							curMaterial = materialInfo[0]

							if len(materialInfo) > 1:
								self.resultChances[i].SetText("") #Hide hotfix different % chances (OR items)

							currentSlot.SetItemSlot(0, curMaterial["vnum_cur"], curMaterial["count"])
							j = j + 1

							# Center Align
							item.SelectItem(1, 2, curMaterial["vnum_cur"])
							sizeX, sizeY = item.GetItemSize(1,2,3)
							localX, localY = currentSlot.GetLocalPosition()

							currentSlot.SetSize(self.SLOT_SIZEX, self.SLOT_SIZEY * sizeY)

							adjustLocalY = 0
							if sizeY < 3 and sizeY > 0:
								adjustLocalY = int(32 / sizeY)

							currentSlot.SetPosition(localX, 0 + adjustLocalY)

							if player.GetItemCountByVnum(curMaterial["vnum_cur"]) >= curMaterial["count"]:
								currentSlot.SetUnusableSlot(0, False)
								currentSlot.SetUnusableSlotWorld(0, True)
							else:
								currentSlot.SetUnusableSlot(0, True)
								currentSlot.SetUnusableSlotWorld(0, False)

				for k in xrange(5):
					if k >= j:
						self.materialSlots[i][k].ClearSlot(0)

				if self.RESULT_SLOT_COUNT <= i:
					tchat("ABC")
					break

		self.cubeSlot.RefreshSlot()

	def __OnCloseButtonClick(self):
		if self.isUsable:
			self.isUsable = False
			net.SendChatPacket("/cube close")

		self.Close()

	def __OnAcceptButtonClick(self):
		if len(self.cubeItemInfo) == 0:
			return
		net.SendChatPacket("/cube make")			
		
	def __OnSelectEmptySlot(self, selectedSlotPos):

		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			mouseModule.mouseController.DeattachObject()

			inventoryList = (player.SLOT_TYPE_INVENTORY, player.SLOT_TYPE_UPPITEM_INVENTORY, player.SLOT_TYPE_SKILLBOOK_INVENTORY, player.SLOT_TYPE_STONE_INVENTORY, player.SLOT_TYPE_ENCHANT_INVENTORY)

			if player.ENABLE_COSTUME_INVENTORY:
				inventoryList += (player.SLOT_TYPE_COSTUME_INVENTORY,)

			if attachedSlotType not in inventoryList:
				return

			for slotPos, invenPos in self.cubeItemInfo.items():
				if invenPos == attachedSlotPos:
					del self.cubeItemInfo[slotPos]
			
			self.cubeItemInfo[selectedSlotPos] = attachedSlotPos
			net.SendChatPacket("/cube add %d %d" % (selectedSlotPos, attachedSlotPos))

			self.Refresh()

	def __OnSelectItemSlot(self, selectedSlotPos):

		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			snd.PlaySound("sound/ui/loginfail.wav")
			mouseModule.mouseController.DeattachObject()

		else:
			if not selectedSlotPos in self.cubeItemInfo:
				return

			snd.PlaySound("sound/ui/drop.wav")

			net.SendChatPacket("/cube del %d " % selectedSlotPos)
			del self.cubeItemInfo[selectedSlotPos]

			self.Refresh()

	def __OnOverInItem(self, slotIndex):
		if self.tooltipItem:
			if self.cubeItemInfo.has_key(slotIndex):
				self.tooltipItem.SetInventoryItem(self.cubeItemInfo[slotIndex])

	def __OnOverOutItem(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def OnUpdate(self):
		USE_SHOP_LIMIT_RANGE = 1000

		(x, y, z) = player.GetMainCharacterPosition()
		if abs(x - self.xShopStart) > USE_SHOP_LIMIT_RANGE or abs(y - self.yShopStart) > USE_SHOP_LIMIT_RANGE:
			self.__OnCloseButtonClick()

		if self.firstSlotIndex in self.cubeMaterialInfos:
			for i in xrange(self.RESULT_SLOT_COUNT):
				if self.firstSlotIndex + i >= len(self.cubeMaterialInfos):
					break

				materialList = self.cubeMaterialInfos[self.firstSlotIndex + i]
				j = 0
				for materialInfo in materialList:
					if 0 < len(materialInfo):
						currentSlot = self.materialSlots[i][j]
						curMaterial = materialInfo[0]

						if curMaterial["vnum_start"] != curMaterial["vnum_end"]:
							curMaterial["delay"] += 1
							if curMaterial["delay"] >= 50:
								curMaterial["delay"] = 0
								curMaterial["vnum_cur"] += 1
								while curMaterial["vnum_cur"] <= curMaterial["vnum_end"]:
									if item.SelectItem(1, 2, curMaterial["vnum_cur"]):
										sizeX, sizeY = item.GetItemSize(1,2,3)
										if sizeY != 0:
											break
									curMaterial["vnum_cur"] += 1
								if curMaterial["vnum_cur"] > curMaterial["vnum_end"]:
									curMaterial["vnum_cur"] = curMaterial["vnum_start"]
								currentSlot.SetItemSlot(0, curMaterial["vnum_cur"], curMaterial["count"])

						j = j + 1

		self.Refresh()

	if constInfo.SAVE_WINDOW_POSITION:
		def OnMoveWindow(self, x, y):
			if constInfo.SAVE_WINDOW_POSITION:
				cfg.Set(cfg.SAVE_GENERAL, "wnd_pos_cube", ("%d %d") % (x, y))

		def Show(self):
			if int(cfg.Get(cfg.SAVE_GENERAL, "save_wnd_pos", "0")):
				x, y = map(int, cfg.Get(cfg.SAVE_GENERAL, "wnd_pos_cube", "0 0").split(" "))
				if x and y:
					self.SetPosition(x, y)
			ui.ScriptWindow.Show(self)
