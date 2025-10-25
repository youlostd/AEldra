import ui
import grp
import app

import wndMgr

class TextBar(ui.Window):
	def __init__(self, width, height):
		ui.Window.__init__(self)
		self.handle = grp.CreateTextBar(width, height)

	def __del__(self):
		ui.Window.__del__(self)
		grp.DestroyTextBar(self.handle)
		
	def ClearBar(self):
		grp.ClearTextBar(self.handle)

	def SetClipRect(self, x1, y1, x2, y2):
		grp.SetTextBarClipRect(self.handle, x1, y1, x2, y2)

	def TextOut(self, x, y, text):
		grp.TextBarTextOut(self.handle, x, y, text)

	def OnRender(self):
		x, y = self.GetGlobalPosition()
		grp.RenderTextBar(self.handle, x, y)

	def SetTextColor(self, r, g, b):
		grp.TextBarSetTextColor(self.handle, r, g, b)

	def GetTextExtent(self, text):
		return grp.TextBarGetTextExtent(self.handle, text)

if app.ENABLE_ZODIAC:
	class ZodiacBoard(ui.Bar):
		FONT_HEIGHT	= 15
		LINE_HEIGHT	= FONT_HEIGHT + 5
		STEP_HEIGHT	= LINE_HEIGHT + 5
		LONG_TEXT_START_X	= 300

		def __init__(self):
			ui.Bar.__init__(self)

			self.AddFlag("not_pick")
			self.missionText = None
			self.missionFullText = None
			self.curPos = 0
			self.dstPos = -5
			self.nextScrollTime = 0
			self.flowMode = False
			self.ScrollStartTime = 0.0

			self.SetPosition(0, 100)
			self.SetSize(wndMgr.GetScreenWidth(), 35)
			self.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 0.5))
			self.SetWindowHorizontalAlignCenter()

			self.__CreateTextBar()

		def __del__(self):
			ui.Bar.__del__(self)

		def __CreateTextBar(self):
			x, y = self.GetGlobalPosition()

			self.textBar = BigTextBar(wndMgr.GetScreenWidth()*2, 300, self.FONT_HEIGHT)
			self.textBar.SetParent(self)
			self.textBar.SetPosition(6, 8)
			self.textBar.SetTextColor(242, 231, 193)
			self.textBar.SetClipRect(0, y, wndMgr.GetScreenWidth(), y+8+self.STEP_HEIGHT)
			self.textBar.Show()

		def CleanMission(self):
			self.missionText = None
			self.missionFullText = None
			self.textBar.ClearBar()
			self.Hide()

		def __RefreshBoard(self):
			self.textBar.ClearBar()

			if self.missionFullText:
				(text_width, text_height) = self.textBar.GetTextExtent(self.missionFullText)

				if text_width>wndMgr.GetScreenWidth():
					self.textBar.TextOut(0, (self.STEP_HEIGHT-8-text_height)/2, self.missionFullText)
					self.flowMode = True
				else:
					self.textBar.TextOut((wndMgr.GetScreenWidth()-text_width)/2, (self.STEP_HEIGHT-8-text_height)/2, self.missionFullText)
					self.flowMode = False

		def SetTip(self, text):
			self.__AppendText(text)
			self.__RefreshBoard()

			if self.flowMode:
				self.dstPos = -text_width
				self.curPos = self.LONG_TEXT_START_X
				self.textBar.SetPosition(3 + self.curPos, 8)
			else:
				self.dstPos = 0
				self.curPos = self.STEP_HEIGHT
				self.textBar.SetPosition(3, 8 + self.curPos)

			if not self.IsShow():
				self.Show()

		def __AppendText(self, text):
			if text == "":
				self.CleanMission()
				return

			self.missionText = text
			self.missionFullText = text

		def OnUpdate(self):
			if self.missionFullText == None:
				self.Hide()
				return

			if self.dstPos < self.curPos:
				self.curPos -= 1
				if self.flowMode:
					self.textBar.SetPosition(3 + self.curPos, 8)
				else:
					self.textBar.SetPosition(3, 8 + self.curPos)
			else:
				if self.flowMode:
					self.curPos = wndMgr.GetScreenWidth()

class TipBoard(ui.Bar):
	SCROLL_WAIT_TIME = 3.0
	TIP_DURATION = 4.0
	STEP_HEIGHT = 17

	def __init__(self):
		ui.Bar.__init__(self)

		self.AddFlag("not_pick")
		self.tipList = []
		self.curPos = 0
		self.dstPos = 0
		self.nextScrollTime = 0
		
		self.textBarStartX = 10
		self.textBarStartY = 4
		
		self.width = 370		

		self.SetPosition(0, 70)
		self.SetSize(370, 20)
		
		#invisible background
		self.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 0.0))
		self.SetWindowHorizontalAlignCenter()
		
		self.__LoadBackgroundImage()
		self.__CreateTextBar()

	def __del__(self):
		ui.Bar.__del__(self)

	def __LoadBackgroundImage(self):
		self.imgBg = ui.ImageBox( )
		self.imgBg.SetParent( self )
		self.imgBg.SetPosition( 0, 0 )
		self.imgBg.LoadImage("d:/ymir work/ui/game/noticebar/msgbox.tga")
		self.imgBg.Show( )
		
	def __CreateTextBar(self):

		x, y = self.GetGlobalPosition()

		self.textBar = TextBar(370, 300)
		self.textBar.SetParent(self)
		self.textBar.SetPosition(self.textBarStartX, self.textBarStartY)
		self.textBar.SetClipRect(0, y, wndMgr.GetScreenWidth(), y+18)
		self.textBar.Show()
		
	def __CleanOldTip(self):
		leaveList = []
		for tip in self.tipList:
			madeTime = tip[0]
			if app.GetTime() - madeTime > self.TIP_DURATION:
				pass
			else:
				leaveList.append(tip)

		self.tipList = leaveList

		if not leaveList:
			self.textBar.ClearBar()
			self.Hide()
			return

		self.__RefreshBoard()

	def __RefreshBoard(self):

		self.textBar.ClearBar()

		index = 0
		for tip in self.tipList:
			text = tip[1]
			self.textBar.TextOut(0, index*self.STEP_HEIGHT, text)
			index += 1

	def SetTip(self, text):

		if not app.IsVisibleNotice():
			return

		curTime = app.GetTime()
		self.tipList.append((curTime, text))
		self.__RefreshBoard()

		self.nextScrollTime = app.GetTime() + 1.0

		if not self.IsShow():
			self.curPos = -self.STEP_HEIGHT
			self.dstPos = -self.STEP_HEIGHT
			self.textBar.SetPosition(self.textBarStartX, self.textBarStartY - self.curPos)
			self.Show()

	def OnUpdate(self):

		if not self.tipList:
			self.Hide()
			return

		if app.GetTime() > self.nextScrollTime:
			self.nextScrollTime = app.GetTime() + self.SCROLL_WAIT_TIME

			self.dstPos = self.curPos + self.STEP_HEIGHT

		if self.dstPos > self.curPos:
			self.curPos += 1
			self.textBar.SetPosition(self.textBarStartX, self.textBarStartY - self.curPos)

			if self.curPos > len(self.tipList)*self.STEP_HEIGHT:
				self.curPos = -self.STEP_HEIGHT
				self.dstPos = -self.STEP_HEIGHT

				self.__CleanOldTip()

class BigTextBar(TextBar):
	def __init__(self, width, height, fontSize):
		ui.Window.__init__(self)
		self.handle = grp.CreateBigTextBar(width, height, fontSize)

	def __del__(self):
		ui.Window.__del__(self)
		grp.DestoryBigTextBar(self.handle)
		self.handle = None


class BigBoard(ui.Bar):
	SCROLL_WAIT_TIME = 5.0
	TIP_DURATION = 10.0
	FONT_WIDTH	= 18
	FONT_HEIGHT	= 18
	LINE_WIDTH  = 500
	LINE_HEIGHT	= FONT_HEIGHT + 5
	STEP_HEIGHT = LINE_HEIGHT * 2
	LINE_CHANGE_LIMIT_WIDTH = 350

	FRAME_IMAGE_FILE_NAME_LIST = [
		"d:/ymir work/ui/oxevent/frame_0.sub", 
		"d:/ymir work/ui/oxevent/frame_1.sub", 
		"d:/ymir work/ui/oxevent/frame_2.sub",
	]

	FRAME_IMAGE_STEP = 256

	FRAME_BASE_X = -20
	FRAME_BASE_Y = -12

	def __init__(self):
		ui.Bar.__init__(self)

		self.AddFlag("not_pick")
		self.tipList = []
		self.curPos = 0
		self.dstPos = 0
		self.nextScrollTime = 0

		self.SetPosition(0, 150)
		self.SetSize(512, 55)
		self.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 0.5))
		self.SetWindowHorizontalAlignCenter()

		self.__CreateTextBar()
		self.__LoadFrameImages()
		 

	def __LoadFrameImages(self):
		x = self.FRAME_BASE_X
		y = self.FRAME_BASE_Y
		self.imgList = []
		for imgFileName in self.FRAME_IMAGE_FILE_NAME_LIST:
			self.imgList.append(self.__LoadImage(x, y, imgFileName))
			x += self.FRAME_IMAGE_STEP

	def __LoadImage(self, x, y, fileName):
		img = ui.ImageBox()
		img.SetParent(self)
		img.AddFlag("not_pick")
		img.LoadImage(fileName)
		img.SetPosition(x, y)
		img.Show()
		return img
		
	def __del__(self):
		ui.Bar.__del__(self)

	def __CreateTextBar(self):

		x, y = self.GetGlobalPosition()

		self.textBar = BigTextBar(self.LINE_WIDTH, 300, self.FONT_HEIGHT)
		self.textBar.SetParent(self)
		self.textBar.SetPosition(6, 8)
		self.textBar.SetTextColor(242, 231, 193)
		self.textBar.SetClipRect(0, y+8, wndMgr.GetScreenWidth(), y+8+self.STEP_HEIGHT)
		self.textBar.Show()

	def __CleanOldTip(self):
		curTime = app.GetTime()
		leaveList = []
		for madeTime, text in self.tipList:
			if curTime + self.TIP_DURATION <= madeTime:				
				leaveList.append(tip)

		self.tipList = leaveList

		if not leaveList:
			self.textBar.ClearBar()
			self.Hide()
			return

		self.__RefreshBoard()

	def __RefreshBoard(self):

		self.textBar.ClearBar()

		if len(self.tipList) == 1:
			checkTime, text = self.tipList[0]
			(text_width, text_height) = self.textBar.GetTextExtent(text)
			self.textBar.TextOut((500-text_width)/2, (self.STEP_HEIGHT-8-text_height)/2, text)

		else:
			index = 0
			for checkTime, text in self.tipList:			
				(text_width, text_height) = self.textBar.GetTextExtent(text)	 
				self.textBar.TextOut((500-text_width)/2, index*self.LINE_HEIGHT, text)
				index += 1

	def SetTip(self, text):

		if not app.IsVisibleNotice():
			return		
		
		curTime = app.GetTime()
		self.__AppendText(curTime, text)
		self.__RefreshBoard()

		self.nextScrollTime = curTime + 1.0

		if not self.IsShow():
			self.curPos = -self.STEP_HEIGHT
			self.dstPos = -self.STEP_HEIGHT
			self.textBar.SetPosition(3, 8 - self.curPos)
			self.Show()

	def __AppendText(self, curTime, text):		
		import dbg		
		prevPos = 0
		while 1:
			curPos = text.find(" ", prevPos)
			if curPos < 0:
				break
			
			(text_width, text_height) = self.textBar.GetTextExtent(text[:curPos])
			if text_width > self.LINE_CHANGE_LIMIT_WIDTH:
				self.tipList.append((curTime, text[:prevPos]))
				self.tipList.append((curTime, text[prevPos:]))
				return

			prevPos = curPos + 1

		self.tipList.append((curTime, text))

	def OnUpdate(self):

		if not self.tipList:
			self.Hide()
			return

		if app.GetTime() > self.nextScrollTime:
			self.nextScrollTime = app.GetTime() + self.SCROLL_WAIT_TIME

			self.dstPos = self.curPos + self.STEP_HEIGHT

		if self.dstPos > self.curPos:
			self.curPos += 1
			self.textBar.SetPosition(3, 8 - self.curPos)

			if self.curPos > len(self.tipList)*self.LINE_HEIGHT:
				self.curPos = -self.STEP_HEIGHT
				self.dstPos = -self.STEP_HEIGHT

				self.__CleanOldTip()


class ReactBoard(ui.Bar):
	FONT_HEIGHT	= 15
	LINE_HEIGHT	= FONT_HEIGHT + 5
	STEP_HEIGHT	= LINE_HEIGHT + 5
	LONG_TEXT_START_X		= 300

	def __init__(self):
		ui.Bar.__init__(self)

		self.AddFlag("not_pick")
		self.missionText = None
		self.missionFullText = None
		self.curPos = 0
		self.dstPos = -5
		self.nextScrollTime = 0
		self.flowMode = False
		self.ScrollStartTime = 0.0

		self.SetPosition(0, 100)
		self.SetSize(wndMgr.GetScreenWidth(), 35)
		self.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 0.75))
		self.SetWindowHorizontalAlignCenter()

		self.__CreateTextBar()

	def __del__(self):
		ui.Bar.__del__(self)

	def __CreateTextBar(self):
		x, y = self.GetGlobalPosition()

		# self.textBar = BigTextBar(wndMgr.GetScreenWidth()*2, 300, self.FONT_HEIGHT)
		# self.textBar.SetParent(self)
		# self.textBar.SetPosition(6, 8)
		# self.textBar.SetTextColor(242, 231, 193)
		# self.textBar.SetClipRect(0, y, wndMgr.GetScreenWidth(), y+8+self.STEP_HEIGHT)
		# self.textBar.Show()
		self.textBar = ui.MakeTextLine(self)
		# self.textBar.SetPosition(0, -20)
		self.textBar.SetFontName("Arial:20")
		self.textBar.SetPackedFontColor(grp.GenerateColor(1.0, 0.74, 0.0, 1.0))
		self.textBar.SetOutline()

	def CleanMission(self):
		self.missionText = None
		self.missionFullText = None
		# self.textBar.ClearBar()
		self.Hide()

	def __RefreshBoard(self):
		# self.textBar.ClearBar()

		if self.missionFullText:
			# (text_width, text_height) = self.textBar.GetTextExtent(self.missionFullText)
			(text_width, text_height) = 500, 200

			if text_width>wndMgr.GetScreenWidth():
				# self.textBar.TextOut(0, (self.STEP_HEIGHT-8-text_height)/2, self.missionFullText)
				self.flowMode = True
			else:
				# self.textBar.TextOut((wndMgr.GetScreenWidth()-text_width)/2, (self.STEP_HEIGHT-8-text_height)/2, self.missionFullText)
				self.flowMode = False

			self.textBar.SetText(self.missionFullText)

	def SetTip(self, text):
		self.__AppendText(text)
		self.__RefreshBoard()

		if self.flowMode:
			self.dstPos = -text_width
			self.curPos = self.LONG_TEXT_START_X
			self.textBar.SetPosition(3 + self.curPos, 0)
		else:
			self.dstPos = 0
			self.curPos = self.STEP_HEIGHT
			self.textBar.SetPosition(3, 0 + self.curPos)

		if not self.IsShow():
			self.Show()

	def __AppendText(self, text):
		if text == "":
			self.CleanMission()
			return

		self.missionText = text
		self.missionFullText = text

	def OnUpdate(self):
		if self.missionFullText == None:
			self.Hide()
			return

		if self.dstPos < self.curPos:
			self.curPos -= 1
			if self.flowMode:
				self.textBar.SetPosition(3 + self.curPos, 0)
			else:
				self.textBar.SetPosition(3, 0 + self.curPos)
		else:
			if self.flowMode:
				self.curPos = wndMgr.GetScreenWidth()



if __name__ == "__main__":	
	import app
	import wndMgr
	import systemSetting
	import mouseModule
	import grp
	import ui
	
	#wndMgr.SetOutlineFlag(True)

	app.SetMouseHandler(mouseModule.mouseController)
	app.SetHairColorEnable(True)
	wndMgr.SetMouseHandler(mouseModule.mouseController)
	wndMgr.SetScreenSize(systemSetting.GetWidth(), systemSetting.GetHeight())
	app.Create("METIN2 CLOSED BETA", systemSetting.GetWidth(), systemSetting.GetHeight(), 1)
	mouseModule.mouseController.Create()

	wnd = BigBoard()
	wnd.Show()
	wnd.SetTip("안녕하세요")
	wnd.SetTip("저는 빗자루 입니다")

	app.Loop()

