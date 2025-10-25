import ui
import player
import uiToolTip
import localeInfo
import item
import net

class PetWindow(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/PetWindow.py")
		except:
			import exception
			exception.Abort("PetWindow.LoadWindow.LoadObject")

		try:
			self.board = self.GetChild("board")
			self.name = self.GetChild("name_text")
			self.level = self.GetChild("Level_Value")
			self.exp = self.GetChild("Exp_Value")
			self.need_exp = self.GetChild("RestExp_Value")
			self.statMain = self.GetChild("StatMain")
			self.statPoints = self.GetChild("StatPoints")
			self.stats = [self.GetChild("Stat%d_Value" % (i + 1)) for i in xrange(player.ANIMAL_STAT_COUNT)]
			self.statPlusBtn = [self.GetChild("Stat%d_PlusBtn" % (i + 1)) for i in xrange(player.ANIMAL_STAT_COUNT)]
		except:
			import exception
			exception.Abort("PetWindow.LoadWindow.BindObject")

		self.board.SetCloseEvent(self.Close)

		for i in xrange(player.ANIMAL_STAT_COUNT):
			self.statPlusBtn[i].SAFE_SetEvent(self.__OnStatUp, player.ANIMAL_STAT_1 + i)

		self.Refresh()

	def Destroy(self):
		self.Close()
		ui.ScriptWindow.Destroy(self)

	def __SelectAnimal(self):
		player.AnimalSelectType(player.ANIMAL_TYPE_PET)

	def CanOpen(self):
		self.__SelectAnimal()
		return player.AnimalIsSummoned()

	def Open(self):
		self.SetTop()
		self.SetCenterPosition()
		self.Show()

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()

	def __OnStatUp(self, index):
		net.SendChatPacket("/animal_stat_up pet " + str(index))

	def Refresh(self):
		if not self.CanOpen():
			self.Close()
			return

		self.__SelectAnimal()
		self.name.SetText(player.AnimalGetName())
		self.level.SetText(player.AnimalGetLevel())
		self.exp.SetText(player.AnimalGetExp())
		self.need_exp.SetText(player.AnimalGetMaxExp() - player.AnimalGetExp())
		self.statMain.SetText(localeInfo.PET_STAT_MAIN % uiToolTip.ItemToolTip.AFFECT_DICT[item.APPLY_MAX_HP](player.AnimalGetStat(player.ANIMAL_STAT_MAIN)))
		if player.AnimalGetStatPoints() > 0:
			self.statPoints.SetText(localeInfo.PET_STAT_POINTS % player.AnimalGetStatPoints())
			self.statPoints.SetPosition(5 + self.statPoints.GetWidth(), self.statPoints.GetTop())
		else:
			self.statPoints.SetText("")
		for i in xrange(player.ANIMAL_STAT_COUNT):
			self.stats[i].SetText(player.AnimalGetStat(player.ANIMAL_STAT_1 + i))
			if player.AnimalGetStatPoints() > 0:
				self.statPlusBtn[i].Show()
			else:
				self.statPlusBtn[i].Hide()

class MountWindow(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/MountWindow.py")
		except:
			import exception
			exception.Abort("MountWindow.LoadWindow.LoadObject")

		try:
			self.board = self.GetChild("board")
			self.name = self.GetChild("name_text")
			self.level = self.GetChild("Level_Value")
			self.exp = self.GetChild("Exp_Value")
			self.need_exp = self.GetChild("RestExp_Value")
			self.statPoints = self.GetChild("StatPoints")
			self.stats = [self.GetChild("Stat%d_Value" % (i + 1)) for i in xrange(player.ANIMAL_STAT_COUNT)]
			self.statPlusBtn = [self.GetChild("Stat%d_PlusBtn" % (i + 1)) for i in xrange(player.ANIMAL_STAT_COUNT)]
		except:
			import exception
			exception.Abort("MountWindow.LoadWindow.BindObject")

		self.board.SetCloseEvent(self.Close)

		for i in xrange(player.ANIMAL_STAT_COUNT):
			self.statPlusBtn[i].SAFE_SetEvent(self.__OnStatUp, player.ANIMAL_STAT_1 + i)

		self.Refresh()

	def Destroy(self):
		self.Close()
		ui.ScriptWindow.Destroy(self)

	def __SelectAnimal(self):
		player.AnimalSelectType(player.ANIMAL_TYPE_MOUNT)

	def CanOpen(self):
		self.__SelectAnimal()
		return player.AnimalIsSummoned()

	def Open(self):
		self.SetTop()
		self.SetCenterPosition()
		self.Show()

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()

	def __OnStatUp(self, index):
		net.SendChatPacket("/animal_stat_up mount " + str(index))

	def Refresh(self):
		if not self.CanOpen():
			self.Close()
			return

		self.__SelectAnimal()
		self.name.SetText(player.AnimalGetName())
		self.level.SetText(player.AnimalGetLevel())
		self.exp.SetText(player.AnimalGetExp())
		self.need_exp.SetText(player.AnimalGetMaxExp() - player.AnimalGetExp())
		if player.AnimalGetStatPoints() > 0:
			self.statPoints.SetText(localeInfo.PET_STAT_POINTS % player.AnimalGetStatPoints())
			self.statPoints.SetPosition(5 + self.statPoints.GetWidth(), self.statPoints.GetTop())
		else:
			self.statPoints.SetText("")
		for i in xrange(player.ANIMAL_STAT_COUNT):
			self.stats[i].SetText("%d%%" % player.AnimalGetStat(player.ANIMAL_STAT_1 + i))
			if player.AnimalGetStatPoints() > 0:
				self.statPlusBtn[i].Show()
			else:
				self.statPlusBtn[i].Hide()
