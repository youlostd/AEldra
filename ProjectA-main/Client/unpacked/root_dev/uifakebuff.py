import ui
import player
import uiToolTip
import constInfo
import item
import localeInfo

if constInfo.CHANGE_SKILL_COLOR:
	import uiSkillColor

	CUSTOM_SKILL_STATUS = {
		6 : 0,
		7 : 0,
		8 : 0,
	}

	def SetUnlockedSkill(skill):
		global CUSTOM_SKILL_STATUS
		CUSTOM_SKILL_STATUS[skill] = 1


class FakeBuffSkillWindow(ui.BaseScriptWindow):

	SKILL_MAX_NUM = 255

	#################################################
	## MAIN FUNCTIONS
	#################################################

	def __init__(self):
		ui.BaseScriptWindow.__init__(self, "FakeBuffSkillWindow", self.__BindObject)
		self.__LoadWindow()

		self.toolTip = uiToolTip.SkillToolTip()

		if constInfo.CHANGE_SKILL_COLOR:
			self.skillColorWnd = uiSkillColor.SkillColorWindow()
			self.open_gui_btn = []
			self.__RefreshOpenGUIButton()

	def __BindObject(self):
		self._AddLoadObject("slot", "slot")
		self._AddLoadObject("InfoImage", "InfoImage")

	def __LoadWindow(self):
	#	self.main["close"].SAFE_SetEvent(self.Close)
		self.main["slot"].SetOverInItemEvent(ui.__mem_func__(self.ShowToolTip))
		self.main["slot"].SetOverOutItemEvent(ui.__mem_func__(self.HideToolTip))

		self.main["InfoImage"].SetStringEvent("MOUSE_OVER_IN", ui.__mem_func__(self.__OnMouseOverInInfo))
		self.main["InfoImage"].SetStringEvent("MOUSE_OVER_OUT", ui.__mem_func__(self.HideToolTip))
		self.main["InfoImage"].SetTop()
		if __SERVER__ == 2:
			self.main["InfoImage"].Hide()

		self.Refresh()

	def __OnMouseOverInInfo(self):
		self.toolTip.ClearToolTip()
		self.toolTip.AutoAppendTextLine(localeInfo.TOOLTIP_FAKEBUFF_3RD_SKILL)
		self.toolTip.AppendImage(item.GetIconImageFileName(95243))

	def __GetSkillData(self, vnum):
		skillLevel = player.GetFakeBuffSkillLevel(vnum)
		skillGrade = 0
		if skillLevel >= 50:
			skillGrade = player.SKILL_GRADE_LEGENDARY_MASTER
		elif skillLevel >= 40:
			skillGrade = player.SKILL_GRADE_PERFECT_MASTER
			skillLevel -= 40 - 1
		elif skillLevel >= 30:
			skillGrade = player.SKILL_GRADE_GRAND_MASTER
			skillLevel -= 30 - 1
		elif skillLevel >= 20:
			skillGrade = player.SKILL_GRADE_MASTER
			skillLevel -= 20 - 1
		else:
			skillGrade = player.SKILL_GRADE_NORMAL

		return skillLevel, skillGrade

	def Refresh(self):
		for i in xrange(self.SKILL_MAX_NUM):
			if self.main["slot"].HasSlot(i) and i != 95:
				skillLevel, skillGrade = self.__GetSkillData(i)
				self.main["slot"].SetCoverButton(i)
				self.main["slot"].SetSkillSlotNew(i, i, skillGrade, 0)
				self.main["slot"].SetSlotCountNew(i, skillGrade, skillLevel)
		self.main["slot"].RefreshSlot()

	def RefreshBySkill(self, skillVnum):
		skillLevel, skillGrade = self.__GetSkillData(skillVnum)
		self.main["slot"].SetSkillSlotNew(skillVnum, skillVnum, skillGrade, 0)
		self.main["slot"].SetSlotCountNew(skillVnum, skillGrade, skillLevel)
		self.main["slot"].RefreshSlot()

	def ShowToolTip(self, slotIdx):
		oldIQ = player.GetStatus(player.IQ)
		player.SetStatus(player.IQ, 90)

		skillVnum = slotIdx
		skillLevel, skillGrade = self.__GetSkillData(skillVnum)
		self.toolTip.SetSkillNew(0, skillVnum, skillGrade, skillLevel, True)

		player.SetStatus(player.IQ, oldIQ)

	def HideToolTip(self):
		self.toolTip.HideToolTip()

	def Close(self):
		self.HideToolTip()
		ui.BaseScriptWindow.Close(self)

	if constInfo.CHANGE_SKILL_COLOR:
		def __RefreshOpenGUIButton(self):
			posx, posy = 0, 0
			for i in xrange(3):
				if i == 1:
					posx = 84
				else:
					posx = 43

				if i == 0:
					posx = 43
				elif i == 1:
					posx = 84
				elif i == 2:
					posx = 125

				posy = 31

				if len(self.open_gui_btn) == i:
					btn = ui.Button()
					btn.SetParent(self)
					btn.SetUpVisual("d:/ymir work/ui/chat/color_icon.tga")
					btn.SetOverVisual("d:/ymir work/ui/chat/color_icon.tga")
					btn.SetDownVisual("d:/ymir work/ui/chat/color_icon.tga")
					btn.SetPosition(posx, posy)
					btn.SetEvent(lambda arg = i + 6: self.__OnPressOpenGUIButton(arg))
					btn.Show()

					self.open_gui_btn.append(btn)

		def __RefreshGUIButtons(self):
			if not len(self.open_gui_btn):
				return

			for x in xrange(3):
				if CUSTOM_SKILL_STATUS[x + 6]:
					self.open_gui_btn[x].Show()
				else:
					self.open_gui_btn[x].Hide()

		def __OnPressOpenGUIButton(self, arg):
			self.skillColorWnd.Open(arg)

		def OnUpdate(self):
			self.__RefreshGUIButtons()

		def Destroy2(self):
			ui.BaseScriptWindow.__del__(self)
			global CUSTOM_SKILL_STATUS
			CUSTOM_SKILL_STATUS = {
				6 : 0,
				7 : 0,
				8 : 0,
			}
			self.open_gui_btn = []
			self.skillColorWnd.Destroy()
			del self.skillColorWnd
