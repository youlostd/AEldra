import ui
import player
import chr
import operator
import wndMgr
import cfg
import constInfo

COLORS = [
	0x7748911c,
	0x77858585,
	0x77824b63,
	0x77824b63,
	0x7721687b,
	0x77003c77,
	0x775a703d,
	0x774b4b83,
	0x772a2a26,
	0x77bdbd0b,
	0x7791004b,
]

class DmgMeter(ui.Bar):

	def Init(self):
		self.memberList = {}
		self.maxDmg = 0
		self.maxWidth = 210
		self.HEIGHT = 24
		self.list = ui.ListBoxEx()
		self.list.SetParent(self)
		self.list.SetSize(240,350)
		self.list.SetPosition(2,22)
		#self.list.SetItemSize(self.width,20)
		self.list.SetViewItemCount(21)
		self.list.SetItemStep(20)
		self.list.Show()
		
		self.exitBtn = ui.Button()
		self.exitBtn.SetParent(self)
		self.exitBtn.SetUpVisual("d:/ymir work/ui/public/close_button_01.sub")
		self.exitBtn.SetOverVisual("d:/ymir work/ui/public/close_button_02.sub")
		self.exitBtn.SetDownVisual("d:/ymir work/ui/public/close_button_03.sub")
		self.exitBtn.SetPosition(2,2)
		self.exitBtn.SetEvent(self.Close)
		self.exitBtn.Show()
		
		self.resetBtn = ui.Button()
		self.resetBtn.SetParent(self)
		self.resetBtn.SetUpVisual("d:/ymir work/ui/game/inventory/refresh_small_button_01.sub")
		self.resetBtn.SetOverVisual("d:/ymir work/ui/game/inventory/refresh_small_button_02.sub")
		self.resetBtn.SetDownVisual("d:/ymir work/ui/game/inventory/refresh_small_button_03.sub")
		self.resetBtn.SetPosition(2+20,2)
		self.resetBtn.SetEvent(self.Reset)
		self.resetBtn.SetToolTipText("Reset")
		self.resetBtn.Show()

	def Open(self):
		self.AddFlag("movable")
		self.SetColor(0x55000000)
		self.SetSize(250-46,self.HEIGHT)
		if constInfo.SAVE_WINDOW_POSITION:
			if int(cfg.Get(cfg.SAVE_GENERAL, "save_wnd_pos", "0")):
				x, y = map(int, cfg.Get(cfg.SAVE_GENERAL, "wnd_pos_dmg_mtr", "0 0").split(" "))
				if x and y:
					self.SetPosition(x, y)
				else:
					self.SetPosition(wndMgr.GetScreenWidth()-254,wndMgr.GetScreenHeight()-100)
		else:
			self.SetPosition(wndMgr.GetScreenWidth()-254,wndMgr.GetScreenHeight()-100)
		self.Show()

	def OnMoveWindow(self, x, y):
		if constInfo.SAVE_WINDOW_POSITION:
			cfg.Set(cfg.SAVE_GENERAL, "wnd_pos_dmg_mtr", ("%d %d") % (x, y))


	def BindInterface(self, interface):
		self.interface = interface
		
	def Update(self, dmg, vid):
		if vid != 0:
			if vid in self.memberList:
				self.memberList[vid] += dmg
			else:
				self.memberList[vid] = dmg
				self.HEIGHT += 20
				self.SetSize(250-36,self.HEIGHT)
				self.list.SetSize(240,self.HEIGHT)


		memberList_ordered = sorted(self.memberList.items(), key=operator.itemgetter(1), reverse=True)
		#self.maxDmg = memberList_ordered[0][1]
		self.maxDmg += dmg
		self.textList = []

		self.list.RemoveAllItems()
		i = 0
		for member in memberList_ordered:
			width = self.per_to_number(self.number_to_per(member[1],memberList_ordered[0][1]), self.maxWidth)
			tchat("%s: %d" % (member[0],width))
			bar = ui.Bar()
			bar.SetSize(width,20)
			bar.SetColor(COLORS[i])
			#bar.SetPercentage(member[1], self.maxDmg)

			text = ui.TextLine()
			text.SetParent(bar)
			text.SetText("%s %.0f%%" % (chr.GetNameByVID(member[0]), float(self.number_to_per(member[1],self.maxDmg))))

			text.SetPosition(10,3)
			text.Show()
			
			textDmg = ui.TextLine()
			textDmg.SetParent(bar)
			if member[1] > 1000 and member[1] < 1000000:
				textDmg.SetText("%.0fk" % (float(member[1]) / 1000.0))
			elif member[1] > 1000000 and member[1] < 1000000000:
				textDmg.SetText("%.0fM" % (float(member[1]) / 1000000.0))
			elif member[1] > 1000000000:
				textDmg.SetText("%.0f B" % (float(member[1]) / 1000000000.0))
			else:
				textDmg.SetText("%d" % member[1])

			textDmg.SetPosition(184,3)
			#textDmg.SetWindowHorizontalAlignRight()
			#textDmg.SetHorizontalAlignRight()
			textDmg.Show()
			self.textList.append(text)
			self.textList.append(textDmg)
			self.list.AppendItem(bar)
			#self.list.AppendItem(text)
			i += 1

	def LogOutPlayer(self, vid):
		if vid in self.memberList:
			del self.memberList[vid]
			self.HEIGHT -= 20
			self.Update(0,0)
			self.SetSize(250-36,self.HEIGHT)

	def Reset(self):
		self.HEIGHT = 24
		self.list.RemoveAllItems()
		self.memberList = {}
		self.maxDmg = 0
		self.SetSize(250-36,self.HEIGHT)

	def number_to_per(self, min, max):
		percentage = '{0:.2f}'.format((float(min) / float(max) * 100))
		return percentage

	def per_to_number(self, perc, num):
		percentage = (float(perc) * float(num) / 100)
		return int(percentage)

	def Close(self):
		self.Init()
		self.Hide()