import ui
import localeInfo
import player
import skill
import app
import net

class PassiveSkillWindow(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.AddFlag("movable")
		self.AddFlag("float")

		self.bg = ui.ExpandedImageBox()
		self.bg.SetParent(self)
		self.bg.LoadImage("D:/Ymir Work/ui/interface/special_skill_window_bg.tga")
		self.bg.Show()
		
		self.SetSize(self.bg.GetWidth(), self.bg.GetHeight())
		#self.SetSize(self.base.GetRealWidth(), self.base.GetRealHeight())

		self.skillSlot = ui.SlotWindow()
		self.skillSlot.SetParent(self.bg)
		self.skillSlot.SetSize(self.bg.GetWidth(), self.bg.GetHeight())
		self.skillSlot.SetPosition(0, 0)
		self.skillSlot.AppendSlot(50, 116, 67, 32, 32)
		self.skillSlot.AppendSlot(51, 170, 87, 32, 32)
		self.skillSlot.AppendSlot(52, 196, 142, 32, 32)
		self.skillSlot.AppendSlot(53, 170, 196, 32, 32)
		self.skillSlot.AppendSlot(54, 116, 216, 32, 32)
		self.skillSlot.AppendSlot(55, 62, 196, 32, 32)
		self.skillSlot.AppendSlot(56, 35, 142, 32, 32)
		self.skillSlot.AppendSlot(57, 62, 87, 32, 32)
		self.skillSlot.AppendSlot(58, 116, 142, 32, 32)
		#self.skillSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.OnSelectEmptySlot))
		#self.skillSlot.SetUnselectItemSlotEvent(ui.__mem_func__(self.OnSelectItemSlot))
		self.skillSlot.SetSlotBaseImage("d:/ymir work/ui/public/Slot_Base.sub", 1.0, 1.0, 1.0, 0.0)
		self.skillSlot.AppendSlotButton("d:/ymir work/ui/game/windows/btn_plus_up.sub",\
										"d:/ymir work/ui/game/windows/btn_plus_over.sub",\
										"d:/ymir work/ui/game/windows/btn_plus_down.sub")

		self.skillSlot.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		self.skillSlot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		self.skillSlot.SetPressedSlotButtonEvent(ui.__mem_func__(self.OnPressedSlotButton))
		self.skillSlot.Show()

		titleBar = ui.TitleBar()
		titleBar.SetParent(self.bg)
		titleBar.MakeTitleBar(0, "red")
		if app.GetSelectedDesignName() != "illumina":
			titleBar.SetPosition(8, 7)
		else:
			titleBar.SetPosition(8, 11)
		titleBar.Show()
		titleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		titleBar.SetWidth(self.bg.GetWidth()-15)

		titleName = ui.TextLine()
		titleName.SetParent(titleBar)
		titleName.SetPosition(0, 4)
		if app.GetSelectedDesignName() != "illumina":
			titleName.SetPosition(0, 4)
		else:
			titleName.SetPosition(0, 7)
		titleName.SetWindowHorizontalAlignCenter()
		titleName.SetHorizontalAlignCenter()
		titleName.Show()
		titleName.SetText(localeInfo.SPECIAL_SKILL_TITLE)

		self.titleBar = titleBar
		self.titleName = titleName

		self.SetCenterPosition()
		self.Hide()

		self.toolTip = None

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def SetToolTip(self, toolTipSkill):
		self.toolTip = toolTipSkill

	def OnPressedSlotButton(self, slotNumber):
		skillIndex = player.GetSkillIndex(slotNumber)
		net.SendChatPacket("/skillup " + str(skillIndex))

	def OverInItem(self, slotNumber):
		if not self.toolTip:
			return

		skillIndex = player.GetSkillIndex(slotNumber)
		if not skillIndex:
			return
		skillLevel = player.GetSkillLevel(slotNumber)
		skillGrade = player.GetSkillGrade(slotNumber)

		self.toolTip.SetSkillNew(slotNumber, skillIndex, skillGrade, skillLevel)

	def OverOutItem(self):
		if self.toolTip:
			self.toolTip.HideToolTip()

	def RefleshSkill(self):
		self.skillSlot.HideAllSlotButton()
		for i in xrange(50, 59):
			skillIndex = player.GetSkillIndex(i)
			if not skillIndex:
				continue
			skillGrade = player.GetSkillGrade(i)
			skillLevel = player.GetSkillLevel(i)

			self.skillSlot.SetSkillSlotNew(i, skillIndex, skillGrade, skillLevel)
			self.skillSlot.SetSlotCountNew(i, skillGrade, skillLevel)
			player.SKILL_ACTIVE
			if player.GetStatus(player.SKILL_ACTIVE) > 0 and skillGrade == 0 and skillLevel < 20 and player.GetStatus(player.LEVEL) >= skill.GetSkillLevelLimit(skillIndex):
				self.skillSlot.ShowSlotButton(i)

		self.skillSlot.RefreshSlot()

	def Close(self):
		self.Hide()
