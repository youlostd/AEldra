import ui
import net
import cfg
import datetime
import app
import chat
import localeInfo


IMAGE_POSITIONS = [
	[59, 66],
	[141, 66],
	[223, 66],
	[305, 66],
	[387, 66],
	[469, 66],
	[19, 165],
	[98, 165],
	[176, 165],
	[357, 165],
	[435, 165],
	[513, 165],
	[19, 267],
	[98, 267],
	[167, 267],
	[357, 267],
	[435, 267],
	[513, 267],
	[98, 368],
	[183, 368],
	[268, 368],
	[352, 368],
	[437, 368],
	[246, 192],
]


class XmasEventWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/xmasevent.py")
		except:
			import exception
			exception.Abort("XmasEventWindow.LoadWindow.LoadObject")

		try:
			self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
		except:
			import exception
			exception.Abort("XmasEventWindow.LoadWindow.BindObject")

		self.images = []
		for x in xrange(len(IMAGE_POSITIONS)):
			image = ui.MakeImageBox(self, "d:/ymir work/ui/xmas/%d.tga" % (x + 1), IMAGE_POSITIONS[x][0], IMAGE_POSITIONS[x][1])
			time = datetime.datetime.now()
			arg = int(cfg.Get(cfg.SAVE_GENERAL, "xmas_%d_reward_%d" % (time.year, x), "0"))
			if arg:
				if x == 23:
					image.LoadImage("d:/ymir work/ui/xmas/24_green.tga")
				else:
					image.LoadImage("d:/ymir work/ui/xmas/green.tga")
			image.SAFE_SetStringEvent("MOUSE_LEFT_DOWN", self.OnClickImage, -1 if arg else x)
			self.images.append(image)

		self.timeOpened = 0

	def OnClickImage(self, arg):
		if arg == -1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.XMAS_EVENT_RECIVED_GIFT)
			return

		if self.timeOpened + 10 > app.GetTime():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.XMAS_EVENT_WAIT_TIMER)
			return

		time = datetime.datetime.now()
		net.SendChatPacket("/xmas_reward %d" % arg)
		self.timeOpened = app.GetTime()

	def RecivedReward(self, index):
		if index == 23:
			self.images[index].LoadImage("d:/ymir work/ui/xmas/24_green.tga")
		else:
			self.images[index].LoadImage("d:/ymir work/ui/xmas/green.tga")
		time = datetime.datetime.now()
		cfg.Set(cfg.SAVE_GENERAL, "xmas_%d_reward_%d" % (time.year, index), 1)

	def Open(self):
		self.Show()

	def Close(self):
		self.Hide()

	def Destroy(self):
		self.ClearDictionary()
		self.images = []

	def OnPressEscapeKey(self):
		self.Close()
		return True
