# -*- coding: utf-8 -*-
import app
import ime
import grp
import snd
import wndMgr
import item
import skill
import localeInfo
import timer
import dbg
import constInfo
import player

# MARK_BUG_FIX
import guild
# END_OF_MARK_BUG_FIX

from _weakref import proxy

TITLE_COLOR = grp.GenerateColor(1.0, 1.0, 130.0 / 255.0, 1.0)
GOLD_COLOR = 0xFFD2A147

BACKGROUND_COLOR = grp.GenerateColor(0.0, 0.0, 0.0, 1.0)
DARK_COLOR = grp.GenerateColor(0.2, 0.2, 0.2, 1.0)
BRIGHT_COLOR = grp.GenerateColor(0.7, 0.7, 0.7, 1.0)

if localeInfo.IsCANADA():
	SELECT_COLOR = grp.GenerateColor(0.9, 0.03, 0.01, 0.4)
else:
	SELECT_COLOR = grp.GenerateColor(0.0, 0.0, 0.5, 0.3)

WHITE_COLOR = grp.GenerateColor(1.0, 1.0, 1.0, 0.5)
HALF_WHITE_COLOR = grp.GenerateColor(1.0, 1.0, 1.0, 0.2)

TRANSPARENT = grp.GenerateColor(1.0, 1.0, 1.0, 0.0)

createToolTipWindowDict = {}
def RegisterToolTipWindow(type, createToolTipWindow):
	createToolTipWindowDict[type]=createToolTipWindow

app.SetDefaultFontName(localeInfo.UI_DEF_FONT)

## Window Manager Event List##
##############################
## "OnMouseLeftButtonDown"
## "OnMouseLeftButtonUp"
## "OnMouseLeftButtonDoubleClick"
## "OnMouseRightButtonDown"
## "OnMouseRightButtonUp"
## "OnMouseRightButtonDoubleClick"
## "OnMouseDrag"
## "OnSetFocus"
## "OnKillFocus"
## "OnMouseOverIn"
## "OnMouseOverOut"
## "OnRender"
## "OnUpdate"
## "OnKeyDown"
## "OnKeyUp"
## "OnTop"
## "OnIMEUpdate" ## IME Only
## "OnIMETab"    ## IME Only
## "OnIMEReturn" ## IME Only
##############################
## Window Manager Event List##


class __mem_func__:
	class __noarg_call__:
		def __init__(self, cls, obj, func):
			self.cls=cls
			self.obj=proxy(obj)
			self.func=proxy(func)

		def __call__(self, *arg):
			return self.func(self.obj)

	class __arg_call__:
		def __init__(self, cls, obj, func):
			self.cls=cls
			self.obj=proxy(obj)
			self.func=proxy(func)

		def __call__(self, *arg):
			return self.func(self.obj, *arg)

	def __init__(self, mfunc):
		if mfunc.im_func.func_code.co_argcount>1:
			self.call=__mem_func__.__arg_call__(mfunc.im_class, mfunc.im_self, mfunc.im_func)
		else:
			self.call=__mem_func__.__noarg_call__(mfunc.im_class, mfunc.im_self, mfunc.im_func)

	def __call__(self, *arg):
		return self.call(*arg)

class Window(object):
	def NoneMethod(cls):
		pass

	NoneMethod = classmethod(NoneMethod)

	def __init__(self, layer = "UI"):
		self.hWnd = None
		self.parentWindow = 0
		self.RegisterWindow(layer)
		self.Hide()

		self.mouseLeftButtonDownEvent = None
		self.mouseLeftButtonDownArgs = None
		self.mouseLeftButtonUpEvent = None
		self.mouseLeftButtonUpArgs = None

		self.overInEvent = None
		self.overInArgs = None

		self.overOutEvent = None
		self.overOutArgs = None

		self.alphaLoop = None

	def __del__(self):
		wndMgr.Destroy(self.hWnd)

	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.Register(self, layer)

	def Destroy(self):
		pass

	def GetWindowHandle(self):
		return self.hWnd

	def AddFlag(self, style):
		wndMgr.AddFlag(self.hWnd, style)

	def IsRTL(self):
		return wndMgr.IsRTL(self.hWnd)

	def SetWindowName(self, Name):
		wndMgr.SetName(self.hWnd, Name)

	def SetParent(self, parent):		
		wndMgr.SetParent(self.hWnd, parent.hWnd)

	def SetParentProxy(self, parent):
		self.parentWindow=proxy(parent)
		wndMgr.SetParent(self.hWnd, parent.hWnd)

	def GetParentProxy(self):
		return self.parentWindow

	def GetRenderBox(self):
		return wndMgr.GetRenderBox(self.hWnd)

	def SetInsideRender(self, val):
		wndMgr.SetInsideRender(self.hWnd, val)

	def SetPickAlways(self):
		wndMgr.SetPickAlways(self.hWnd)

	def SetWindowHorizontalAlignLeft(self):
		wndMgr.SetWindowHorizontalAlign(self.hWnd, wndMgr.HORIZONTAL_ALIGN_LEFT)

	def SetWindowHorizontalAlignCenter(self):
		wndMgr.SetWindowHorizontalAlign(self.hWnd, wndMgr.HORIZONTAL_ALIGN_CENTER)

	def SetWindowHorizontalAlignRight(self):
		wndMgr.SetWindowHorizontalAlign(self.hWnd, wndMgr.HORIZONTAL_ALIGN_RIGHT)

	def SetWindowVerticalAlignTop(self):
		wndMgr.SetWindowVerticalAlign(self.hWnd, wndMgr.VERTICAL_ALIGN_TOP)

	def SetWindowVerticalAlignCenter(self):
		wndMgr.SetWindowVerticalAlign(self.hWnd, wndMgr.VERTICAL_ALIGN_CENTER)

	def SetWindowVerticalAlignBottom(self):
		wndMgr.SetWindowVerticalAlign(self.hWnd, wndMgr.VERTICAL_ALIGN_BOTTOM)

	def SetTop(self):
		wndMgr.SetTop(self.hWnd)

	def Show(self):
		wndMgr.Show(self.hWnd)

	def Hide(self):
		wndMgr.Hide(self.hWnd)

	def SetVisible(self, is_show):
		if is_show:
			self.Show()
		else:
			self.Hide()

	def Lock(self):
		wndMgr.Lock(self.hWnd)

	def Unlock(self):
		wndMgr.Unlock(self.hWnd)

	def IsShow(self):
		return wndMgr.IsShow(self.hWnd)

	def UpdateRect(self):
		wndMgr.UpdateRect(self.hWnd)

	def SetSize(self, width, height):
		wndMgr.SetWindowSize(self.hWnd, width, height)

	def GetWidth(self):
		return wndMgr.GetWindowWidth(self.hWnd)

	def GetHeight(self):
		return wndMgr.GetWindowHeight(self.hWnd)

	def GetLocalPosition(self):
		return wndMgr.GetWindowLocalPosition(self.hWnd)

	def GetGlobalPosition(self):
		return wndMgr.GetWindowGlobalPosition(self.hWnd)

	def GetMouseLocalPosition(self):
		return wndMgr.GetMouseLocalPosition(self.hWnd)

	def GetRect(self):
		return wndMgr.GetWindowRect(self.hWnd)

	def SetPosition(self, x, y):
		wndMgr.SetWindowPosition(self.hWnd, x, y)

	def SetCenterPosition(self, x = 0, y = 0):
		self.SetPosition((wndMgr.GetScreenWidth() - self.GetWidth()) / 2 + x, (wndMgr.GetScreenHeight() - self.GetHeight()) / 2 + y)

	def IsFocus(self):
		return wndMgr.IsFocus(self.hWnd)

	def SetFocus(self):
		wndMgr.SetFocus(self.hWnd)

	def KillFocus(self):
		wndMgr.KillFocus(self.hWnd)

	def GetChildCount(self):
		return wndMgr.GetChildCount(self.hWnd)

	def IsIn(self, checkChilds = False):
		return wndMgr.IsIn(self.hWnd, checkChilds)

	def IsInPosition(self):
		xMouse, yMouse = wndMgr.GetMousePosition()
		x, y = self.GetGlobalPosition()
		return xMouse >= x and xMouse < x + self.GetWidth() and yMouse >= y and yMouse < y + self.GetHeight()

	def GetLeft(self, compareParent = None):
		if compareParent:
			x, y = self.GetGlobalPosition()
			par_x, par_y = compareParent.GetGlobalPosition()
			return x - par_x
		else:
			x, y = self.GetLocalPosition()
			return x

	def GetGlobalLeft(self):
		x, y = self.GetGlobalPosition()
		return x

	def GetTop(self, compareParent = None):
		if compareParent:
			x, y = self.GetGlobalPosition()
			par_x, par_y = compareParent.GetGlobalPosition()
			return y - par_y
		else:
			x, y = self.GetLocalPosition()
			return y

	def GetGlobalTop(self):
		x, y = self.GetGlobalPosition()
		return y

	def GetRight(self):
		return self.GetLeft() + self.GetWidth()

	def GetBottom(self):
		return self.GetTop() + self.GetHeight()

	def SetMouseLeftButtonDownEvent(self, event, *args):
		self.mouseLeftButtonDownEvent = event
		self.mouseLeftButtonDownArgs = args

	def OnMouseLeftButtonDown(self):
		if self.mouseLeftButtonDownEvent:
			apply(self.mouseLeftButtonDownEvent, self.mouseLeftButtonDownArgs)

	def SetMouseLeftButtonUpEvent(self, event, *args):
		self.mouseLeftButtonUpEvent = event
		self.mouseLeftButtonUpArgs = args

	def OnMouseLeftButtonUp(self):
		if self.mouseLeftButtonUpEvent:
			apply(self.mouseLeftButtonUpEvent, self.mouseLeftButtonUpArgs)

	def SetAlpha(self, alpha):
		wndMgr.SetAlpha(self.hWnd, alpha)

	def GetAlpha(self):
		return wndMgr.GetAlpha(self.hWnd)

	def SetAllAlpha(self, alpha):
		wndMgr.SetAllAlpha(self.hWnd, alpha)

	def SAFE_SetOverInEvent(self, func, *args):
		self.overInEvent = __mem_func__(func)
		self.overInArgs = args

	def SetOverInEvent(self, func, *args):
		self.overInEvent = func
		self.overInArgs = args

	def SAFE_SetOverOutEvent(self, func, *args):
		self.overOutEvent = __mem_func__(func)
		self.overOutArgs = args

	def SetOverOutEvent(self, func, *args):
		self.overOutEvent = func
		self.overOutArgs = args

	def OnMouseOverIn(self):
		if self.overInEvent:
			apply(self.overInEvent, self.overInArgs)

	def OnMouseOverOut(self):
		if self.overOutEvent:
			apply(self.overOutEvent, self.overOutArgs)

	def SetAlphaLoop(self, first_sleep, increase_time, decrease_time, alpha_start, alpha_end, alpha_end_sleep, finish_sleep, repeat = True):
		self.alphaLoop = {
			"time" : app.GetTime() + first_sleep,
			"inc_time" : increase_time,
			"dec_time" : decrease_time,
			"start" : alpha_start,
			"end" : alpha_end,
			"end_sleep" : alpha_end_sleep,
			"sleep" : finish_sleep,
			"show" : True,
			"repeat" : repeat,
			"stop" : False,
		}

	def ClearAlphaLoop(self):
		self.alphaLoop = None

	def HideAlphaLoop(self):
		if self.IsAlphaLoop():
			self.alphaLoop["show"] = False

	def ShowAlphaLoop(self):
		if self.IsAlphaLoop():
			self.alphaLoop["show"] = True

	def StopAlphaLoop(self):
		if self.alphaLoop:
			self.alphaLoop["stop"] = True

	def IsAlphaLoop(self):
		return self.alphaLoop != None

	def __UpdateAlphaLoop(self):
		if not self.IsAlphaLoop():
			return

		curTime = app.GetTime()
		startTime = self.alphaLoop["time"]
		if curTime < startTime:
			if self.alphaLoop["stop"]:
				self.ClearAlphaLoop()
			return

		alpha = 1.0

		if curTime < startTime + self.alphaLoop["inc_time"]:
			pct = float(curTime - startTime) / float(self.alphaLoop["inc_time"])
			alpha = self.alphaLoop["start"] + (self.alphaLoop["end"] - self.alphaLoop["start"]) * pct
			if self.alphaLoop["show"]:
				self.SetAlpha(alpha)
	#		tchat("[1] => %f" % alpha)
			return
		startTime += self.alphaLoop["inc_time"]

		if curTime < startTime + self.alphaLoop["end_sleep"]:
			alpha = self.alphaLoop["end"]
			if self.alphaLoop["show"]:
				self.SetAlpha(alpha)
	#		tchat("[2] => %f" % alpha)
			return
		startTime += self.alphaLoop["end_sleep"]

		if curTime < startTime + self.alphaLoop["dec_time"]:
			pct = float(curTime - startTime) / float(self.alphaLoop["dec_time"])
			alpha = self.alphaLoop["end"] - (self.alphaLoop["end"] - self.alphaLoop["start"]) * pct
			if self.alphaLoop["show"]:
				self.SetAlpha(alpha)
	#		tchat("[3] => %f" % alpha)
			return
		startTime += self.alphaLoop["dec_time"]

		if curTime < startTime + self.alphaLoop["sleep"]:
			alpha = self.alphaLoop["start"]
			if self.alphaLoop["show"]:
				self.SetAlpha(alpha)
	#		tchat("[4] => %f" % alpha)
			return
		startTime += self.alphaLoop["sleep"]

		if self.alphaLoop["repeat"] and not self.alphaLoop["stop"]:
			self.alphaLoop["time"] = startTime
			self.__UpdateAlphaLoop()

		else:
			self.ClearAlphaLoop()

class ListBoxEx(Window):
	class Item(Window):
		def __init__(self):
			Window.__init__(self)

			self.SetWindowName("NONAME_ListBoxEx_Item")

		def __del__(self):
			Window.__del__(self)

		def SetParent(self, parent):
			Window.SetParent(self, parent)
			self.parent=proxy(parent)

		def OnMouseLeftButtonDown(self):
			self.parent.SelectItem(self)

		def OnRender(self):
			if self.parent.GetSelectedItem()==self:
				self.OnSelectedRender()

		def OnSelectedRender(self):
			x, y = self.GetGlobalPosition()
			grp.SetColor(grp.GenerateColor(0.0, 0.0, 0.7, 0.7))
			grp.RenderBar(x, y, self.GetWidth(), self.GetHeight())

	def __init__(self):
		Window.__init__(self)

		self.viewItemCount=10
		self.basePos=0
		self.itemHeight=16
		self.itemStep=20
		self.selItem=0
		self.selItemIdx=0
		self.itemList=[]
		self.onSelectItemEvent = lambda *arg: None

		if localeInfo.IsARABIC():
			self.itemWidth=130
		else:
			self.itemWidth=100

		self.scrollBar=None
		self.__UpdateSize()

		self.SetWindowName("NONAME_ListBoxEx")

	def __del__(self):
		Window.__del__(self)

	def __UpdateSize(self):
		height=self.itemStep*self.__GetViewItemCount()

		self.SetSize(self.itemWidth, height)

	def IsEmpty(self):
		if len(self.itemList)==0:
			return 1
		return 0

	def SetItemStep(self, itemStep):
		self.itemStep=itemStep
		self.__UpdateSize()

	def SetItemSize(self, itemWidth, itemHeight):
		self.itemWidth=itemWidth
		self.itemHeight=itemHeight
		self.__UpdateSize()

	def GetItemHeight(self):
		return self.itemHeight

	def GetItemWidth(self):
		return self.itemWidth

	def SetViewItemCount(self, viewItemCount):
		self.viewItemCount=viewItemCount
		self.__UpdateSize()

	def SetSelectEvent(self, event):
		self.onSelectItemEvent = event

	def SetBasePos(self, basePos):
		for oldItem in self.itemList[self.basePos:self.basePos+self.viewItemCount]:
			oldItem.Hide()

		self.basePos=basePos

		pos=basePos
		for newItem in self.itemList[self.basePos:self.basePos+self.viewItemCount]:
			(x, y)=self.GetItemViewCoord(pos, newItem.GetWidth())
			newItem.SetPosition(x, y)
			newItem.Show()
			pos+=1

	def GetBasePos(self):
		return self.basePos

	def GetItemIndex(self, argItem):
		return self.itemList.index(argItem)

	def GetSelectedItem(self):
		return self.selItem

	def GetSelectedItemIndex(self):
		return self.selItemIdx

	def SelectIndex(self, index):

		if index >= len(self.itemList) or index < 0:
			self.selItem = None
			self.selItemIdx = None
			return

		try:
			self.selItem=self.itemList[index]
			self.selItemIdx = index
			self.onSelectItemEvent(self.selItem)
		except:
			pass

	def ReplaceItemAtIndex(self, index, item):
		item.SetParent(self)
		item.SetSize(self.itemWidth, self.itemHeight)
		
		if self.__IsInViewRange(index):
			(x,y) = self.GetItemViewCoord(index, item.GetWidth())
			item.SetPosition(x, y)
			item.Show()
		else:
			item.Hide()
		
		self.itemList[index] = item

	def GetItemAtIndex(self, index):
		if index > (len(self.itemList) - 1):
			return None
		return self.itemList[index]

	def SelectItem(self, selItem):
		self.selItem=selItem
		self.selItemIdx=self.GetItemIndex(selItem)
		self.onSelectItemEvent(selItem)

	def RemoveAllItems(self):
		self.basePos=0
		self.selItem=None
		self.selItemIdx=None
		self.itemList=[]

		if self.scrollBar:
			self.scrollBar.SetPos(0)

	def RemoveItem(self, delItem):
		if delItem==self.selItem:
			self.selItem=None
			self.selItemIdx=None

		self.itemList.remove(delItem)

	def AppendItem(self, newItem, isFront = False, update = True):
		newItem.SetParent(self)
		newItem.SetSize(self.itemWidth, self.itemHeight)

		pos=len(self.itemList)
		if isFront:
			pos = 0

		if update:
			if self.__IsInViewRange(pos):
				(x, y)=self.GetItemViewCoord(pos, newItem.GetWidth())
				newItem.SetPosition(x, y)
				newItem.Show()
			else:
				newItem.Hide()

		if isFront:
			self.itemList.insert(0, newItem)

			if update:
				for i in xrange(1, len(self.itemList)):
					curItem = self.itemList[i]
					if self.__IsInViewRange(i):
						(x, y)=self.GetItemViewCoord(i, newItem.GetWidth())
						curItem.SetPosition(x, y)
						curItem.Show()
					else:
						curItem.Hide()

		else:
			self.itemList.append(newItem)

	def SetScrollBar(self, scrollBar):
		scrollBar.SetScrollEvent(__mem_func__(self.__OnScroll))
		self.scrollBar=scrollBar

	def __OnScroll(self):
		self.SetBasePos(int(self.scrollBar.GetPos()*self.__GetScrollLen()))

	def __GetScrollLen(self):
		scrollLen=self.__GetItemCount()-self.__GetViewItemCount()
		if scrollLen<0:
			return 0

		return scrollLen

	def __GetViewItemCount(self):
		return self.viewItemCount

	def __GetItemCount(self):
		return len(self.itemList)

	def GetScrollLen(self):
		return self.__GetScrollLen()

	def GetViewItemCount(self):
		return self.viewItemCount

	def GetItemCount(self):
		return len(self.itemList)

	def GetItemStep(self):
		return self.itemStep

	def GetItemViewCoord(self, pos, itemWidth):
		if localeInfo.IsARABIC():
			return (self.GetWidth()-itemWidth-10, (pos-self.basePos)*self.itemStep)
		else:
			return (0, (pos-self.basePos)*self.itemStep)

	def __IsInViewRange(self, pos):
		if pos<self.basePos:
			return 0
		if pos>=self.basePos+self.viewItemCount:
			return 0
		return 1

class ListBoxExNew(Window):
	class Item(Window):
		def __init__(self):
			Window.__init__(self)

			self.realWidth = 0
			self.realHeight = 0

			self.removeTop = 0
			self.removeBottom = 0

			self.SetWindowName("NONAME_ListBoxExNew_Item")

		def __del__(self):
			Window.__del__(self)

		def SetParent(self, parent):
			Window.SetParent(self, parent)
			self.parent=proxy(parent)

		def SetSize(self, width, height):
			self.realWidth = width
			self.realHeight = height
			Window.SetSize(self, width, height)

		def SetRemoveTop(self, height):
			self.removeTop = height
			self.RefreshHeight()

		def SetRemoveBottom(self, height):
			self.removeBottom = height
			self.RefreshHeight()

		def SetCurrentHeight(self, height):
			Window.SetSize(self, self.GetWidth(), height)

		def GetCurrentHeight(self):
			return Window.GetHeight(self)

		def ResetCurrentHeight(self):
			self.removeTop = 0
			self.removeBottom = 0
			self.RefreshHeight()

		def RefreshHeight(self):
			self.SetCurrentHeight(self.GetHeight() - self.removeTop - self.removeBottom)

		def GetHeight(self):
			return self.realHeight

	def __init__(self, stepSize, viewSteps):
		Window.__init__(self)

		self.viewItemCount=10
		self.basePos=0
		self.baseIndex=0
		self.maxSteps=0
		self.viewSteps = viewSteps
		self.stepSize = stepSize
		self.itemList=[]

		self.scrollBar=None

		self.SetWindowName("NONAME_ListBoxEx")

	def __del__(self):
		Window.__del__(self)

	def IsEmpty(self):
		if len(self.itemList)==0:
			return 1
		return 0

	def __CheckBasePos(self, pos):
		self.viewItemCount = 0

		start_pos = pos

		height = 0
		while height < self.GetHeight():
			if pos >= len(self.itemList):
				return start_pos == 0
			height += self.itemList[pos].GetHeight()
			pos += 1
			self.viewItemCount += 1
		return height == self.GetHeight()

	def SetBasePos(self, basePos, forceRefresh = True):
		if forceRefresh == False and self.basePos == basePos:
			return

		for oldItem in self.itemList[self.baseIndex:self.baseIndex+self.viewItemCount]:
			oldItem.ResetCurrentHeight()
			oldItem.Hide()

		self.basePos=basePos

		baseIndex = 0
		while basePos > 0:
			basePos -= self.itemList[baseIndex].GetHeight() / self.stepSize
			if basePos < 0:
				self.itemList[baseIndex].SetRemoveTop(self.stepSize * abs(basePos))
				break
			baseIndex += 1
		self.baseIndex = baseIndex

		stepCount = 0
		self.viewItemCount = 0
		while baseIndex < len(self.itemList):
			stepCount += self.itemList[baseIndex].GetCurrentHeight() / self.stepSize
			self.viewItemCount += 1
			if stepCount > self.viewSteps:
				self.itemList[baseIndex].SetRemoveBottom(self.stepSize * (stepCount - self.viewSteps))
				break
			elif stepCount == self.viewSteps:
				break
			baseIndex += 1

		y = 0
		for newItem in self.itemList[self.baseIndex:self.baseIndex+self.viewItemCount]:
			newItem.SetPosition(0, y)
			newItem.Show()
			y += newItem.GetCurrentHeight()

	def GetItemIndex(self, argItem):
		return self.itemList.index(argItem)

	def GetSelectedItem(self):
		return self.selItem

	def GetSelectedItemIndex(self):
		return self.selItemIdx

	def RemoveAllItems(self):
		self.itemList=[]
		self.maxSteps=0

		if self.scrollBar:
			self.scrollBar.SetPos(0)

	def RemoveItem(self, delItem):
		self.maxSteps -= delItem.GetHeight() / self.stepSize
		self.itemList.remove(delItem)

	def AppendItem(self, newItem):
		if newItem.GetHeight() % self.stepSize != 0:
			import dbg
			dbg.TraceError("Invalid AppendItem height %d stepSize %d" % (newItem.GetHeight(), self.stepSize))
			return

		self.maxSteps += newItem.GetHeight() / self.stepSize
		newItem.SetParent(self)
		self.itemList.append(newItem)

	def SetScrollBar(self, scrollBar):
		scrollBar.SetScrollEvent(__mem_func__(self.__OnScroll))
		self.scrollBar=scrollBar

	def __OnScroll(self):
		self.SetBasePos(int(self.scrollBar.GetPos()*self.__GetScrollLen()), False)

	def __GetScrollLen(self):
		scrollLen=self.maxSteps-self.viewSteps
		if scrollLen<0:
			return 0

		return scrollLen

	def __GetViewItemCount(self):
		return self.viewItemCount

	def __GetItemCount(self):
		return len(self.itemList)

	def GetScrollLen(self):
		return self.__GetScrollLen()

	def GetViewItemCount(self):
		return self.viewItemCount

	def GetItemCount(self):
		return len(self.itemList)

class CandidateListBox(ListBoxEx):

	HORIZONTAL_MODE = 0
	VERTICAL_MODE = 1

	class Item(ListBoxEx.Item):
		def __init__(self, text):
			ListBoxEx.Item.__init__(self)

			self.textBox=TextLine()
			self.textBox.SetParent(self)
			self.textBox.SetText(text)
			self.textBox.Show()

		def __del__(self):
			ListBoxEx.Item.__del__(self)

	def __init__(self, mode = HORIZONTAL_MODE):
		ListBoxEx.__init__(self)
		self.itemWidth=32
		self.itemHeight=32
		self.mode = mode

	def __del__(self):
		ListBoxEx.__del__(self)

	def SetMode(self, mode):
		self.mode = mode

	def AppendItem(self, newItem):
		ListBoxEx.AppendItem(self, newItem)

	def GetItemViewCoord(self, pos):
		if self.mode == self.HORIZONTAL_MODE:
			return ((pos-self.basePos)*self.itemStep, 0)
		elif self.mode == self.VERTICAL_MODE:
			return (0, (pos-self.basePos)*self.itemStep)

class TextLine(Window):
	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)
		self.max = 0
		self.SetFontName( constInfo.GetChoosenFontName( ) )
		#self.SetFontName(localeInfo.UI_DEF_FONT)
		self.textColorDict = {}

	def __del__(self):
		Window.__del__(self)

	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.RegisterTextLine(self, layer)

	def GetRenderPos(self):
		return wndMgr.GetRenderPos(self.hWnd)

	def SetFixedRenderPos(self, startPos, endPos):
		wndMgr.SetFixedRenderPos(self.hWnd, startPos, endPos)

	def SetMax(self, max):
		wndMgr.SetMax(self.hWnd, max)

	def SetLimitWidth(self, width):
		wndMgr.SetLimitWidth(self.hWnd, width)

	def SetMultiLine(self, val = True):
		wndMgr.SetMultiLine(self.hWnd, val)

	def SetHorizontalAlignArabic(self):
		wndMgr.SetHorizontalAlign(self.hWnd, wndMgr.TEXT_HORIZONTAL_ALIGN_ARABIC)

	def SetHorizontalAlignLeft(self):
		wndMgr.SetHorizontalAlign(self.hWnd, wndMgr.TEXT_HORIZONTAL_ALIGN_LEFT)

	def SetHorizontalAlignRight(self):
		wndMgr.SetHorizontalAlign(self.hWnd, wndMgr.TEXT_HORIZONTAL_ALIGN_RIGHT)

	def SetHorizontalAlignCenter(self):
		wndMgr.SetHorizontalAlign(self.hWnd, wndMgr.TEXT_HORIZONTAL_ALIGN_CENTER)

	def SetVerticalAlignTop(self):
		wndMgr.SetVerticalAlign(self.hWnd, wndMgr.TEXT_VERTICAL_ALIGN_TOP)

	def SetVerticalAlignBottom(self):
		wndMgr.SetVerticalAlign(self.hWnd, wndMgr.TEXT_VERTICAL_ALIGN_BOTTOM)

	def SetVerticalAlignCenter(self):
		wndMgr.SetVerticalAlign(self.hWnd, wndMgr.TEXT_VERTICAL_ALIGN_CENTER)

	def SetSecret(self, Value=True):
		wndMgr.SetSecret(self.hWnd, Value)

	def SetOutline(self, Value=True):
		wndMgr.SetOutline(self.hWnd, Value)

	def SetFeather(self, value=True):
		wndMgr.SetFeather(self.hWnd, value)

	def SetFontName(self, fontName):
		wndMgr.SetFontName(self.hWnd, fontName)

	def SetDefaultFontName(self):
		wndMgr.SetFontName(self.hWnd, localeInfo.UI_DEF_FONT)

	def SetFontColor(self, red, green, blue):
		wndMgr.SetFontColor(self.hWnd, red, green, blue)

	def SetPackedFontColor(self, color):
		wndMgr.SetFontColor(self.hWnd, color)

	def RegisterPackedFontColor(self, name, color):
		self.textColorDict[name] = color

	def SetRegisteredColor(self, name):
		if self.textColorDict.has_key(name):
			self.SetPackedFontColor(self.textColorDict[name])

	def GetRegisteredColor(self, name):
		if self.textColorDict.has_key(name):
			return self.textColorDict[name]

		return None

	def SetOutlineColor(self, red, green, blue):
		wndMgr.SetOutlineColor(self.hWnd, red, green, blue)

	def SetPackedOutlineColor(self, color):
		wndMgr.SetOutlineColor(self.hWnd, color)

	def SetText(self, text):
		#if localeInfo.IsARABIC():
		#	import sys
		#	reload(sys)  
		#	sys.setdefaultencoding('utf8')
		#	import re
		#	# if re.match('/^[ A-Za-z0-9()[\]+-*/%]*$/', text):
		#	text = unicode(text[::-1])
		wndMgr.SetText(self.hWnd, str(text))

	def GetText(self):
		return wndMgr.GetText(self.hWnd)

	def __GetNumberText(self, text):
		try:
			text = text.replace("k", "000")
			return int(text)
		except:
			return 0

	def GetNumberText(self):
		text = self.GetText()
		if not text:
			if self.overLay.GetText():
				return self.__GetNumberText(self.overLay.GetText())
			else:
				return 0

		return self.__GetNumberText(text)

	def GetTextSize(self):
		return wndMgr.GetTextSize(self.hWnd)

	def GetTextWidth(self):
		w, h = self.GetTextSize()
		return w

	def GetTextHeight(self):
		w, h = self.GetTextSize()
		return h
		
	def AdjustSize(self):
		x, y = self.GetTextSize()
		wndMgr.SetWindowSize(self.hWnd, x, y)

	def GetRight(self):
		return self.GetLeft() + self.GetTextWidth()

	def GetBottom(self):
		return self.GetTop() + self.GetTextHeight()

	def ShowPercentage(self, xStartPct, xEndPct, yEndPct = 1.0, yStartPct = 0.0):
		wndMgr.SetRenderingRect(self.hWnd, xStartPct, yStartPct, xEndPct, yEndPct)

	if app.ARABIC_LANG and app.GetLanguage() == app.LANG_ARABIC:
		def SetInverse(self):
			wndMgr.SetInverse(self.hWnd)

class ExtendedTextLine(Window):

	OBJECT_TYPE_IMAGE = 0
	OBJECT_TYPE_TEXT = 1
	OBJECT_TYPE_HEIGHT = 2
	OBJECT_TYPE_WIDTH = 3

	OBJECT_TAGS = {
		OBJECT_TYPE_IMAGE : "IMAGE",
		OBJECT_TYPE_TEXT : "TEXT",
		OBJECT_TYPE_HEIGHT : "HEIGHT",
		OBJECT_TYPE_WIDTH : "WIDTH",
	}

	def __init__(self):
		Window.__init__(self)

		self.inputText = ""
		self.childrenList = []

		self.limitWidth = 0
		self.x = 0
		self.maxHeight = 0
		self.extraHeight = 0

	def __del__(self):
		Window.__del__(self)

	def SetLimitWidth(self, width):
		self.limitWidth = width
		if self.inputText != "":
			self.SetText(self.inputText)

	def IsText(self, text):
		return self.inputText == text

	def SetText(self, text):
		self.childrenList = []
		self.x = 0
		self.maxHeight = 0
		self.extraHeight = 0

		charIndex = 0
		currentWord = ""

		textLine = None

		while charIndex < len(text):
			c = text[charIndex:charIndex+1] 

			# tags
			if c == "<":
				if textLine:
					self.childrenList.append(textLine)
					self.x += textLine.GetTextWidth()
					self.maxHeight = max(self.maxHeight, textLine.GetTextHeight() + 2)
					textLine = None

				tagStart = charIndex
				tagEnd = text[tagStart:].find(">")
				if tagEnd == -1:
					tagEnd = len(text)
				else:
					tagEnd += tagStart

				tagNameStart = charIndex + 1
				tagNameEnd = text[tagNameStart:].find(" ")
				if tagNameEnd == -1 or tagNameEnd > tagEnd:
					tagNameEnd = tagEnd
				else:
					tagNameEnd += tagNameStart
				tag = text[tagNameStart:tagNameEnd]

				content = {}
				tagContentPos = tagNameEnd + 1
				while tagContentPos < tagEnd:
					tagContentStart = -1
					for i in xrange(tagContentPos, tagEnd):
						if text[i:i+1] != " " and text[i:i+1] != "\t":
							tagContentStart = i
							break
					if tagContentStart == -1:
						break

					tagContentPos = text[tagContentStart:].find("=") + tagContentStart
					tagKey = text[tagContentStart:tagContentPos]

					tagContentPos += 1

					tagContentEnd = -1
					isBreakAtSpace = True
					for i in xrange(tagContentPos, tagEnd+1):
						if isBreakAtSpace == True and (text[i:i+1] == " " or text[i:i+1] == "\t" or text[i:i+1] == ">"):
							tagContentEnd = i
							break
						elif text[i:i+1] == "\"":
							if isBreakAtSpace == True:
								isBreakAtSpace = False
								tagContentPos = i + 1
							else:
								tagContentEnd = i
								break
					if tagContentEnd == -1:
						break

					tagValue = text[tagContentPos:tagContentEnd]
					content[tagKey] = tagValue

					tagContentPos = text[tagContentEnd:].find(" ")
					if tagContentPos == -1:
						tagContentPos = tagContentEnd
					else:
						tagContentPos += tagContentEnd

				bRet = True
				for key in self.OBJECT_TAGS:
					if self.OBJECT_TAGS[key] == tag.upper():
						bRet = self.__ComputeTag(key, content)
						break

				if bRet == False:
					break

				charIndex = tagEnd + 1
				continue

			# text
			if not textLine:
				textLine = TextLine()
				textLine.SetParent(self)
				textLine.SetPosition(self.x, 0)
				textLine.SetWindowVerticalAlignCenter()
				textLine.SetVerticalAlignCenter()
				textLine.Show()
			subtext = textLine.GetText()
			textLine.SetText(subtext + c)
			if textLine.GetTextWidth() + self.x >= self.limitWidth and self.limitWidth != 0:
				if subtext != "":
					textLine.SetText(subtext)
					self.childrenList.append(textLine)
					self.x += textLine.GetTextWidth()
					self.maxHeight = max(self.maxHeight, textLine.GetTextHeight() + 2)
					textLine = None
				else:
					textLine = None
				break

			# increase char index
			charIndex += 1

		if textLine:
			self.childrenList.append(textLine)
			self.x += textLine.GetTextWidth()
			self.maxHeight = max(self.maxHeight, textLine.GetTextHeight() + 2)
			textLine = None

		self.inputText = text[:charIndex]
		self.SetSize(self.x, self.maxHeight + self.extraHeight)
		self.UpdateRect()

		return charIndex

	def __ComputeTag(self, index, content):
		# tag <IMAGE []>
		if index == self.OBJECT_TYPE_IMAGE:
			if not content.has_key("path"):
				dbg.TraceError("Cannot read image tag : no path given")
				return False

			image = ImageBox()
			image.SetParent(self)
			image.SetPosition(self.x, 0)
			image.SetWindowVerticalAlignCenter()
			image.LoadImage(content["path"])
			image.Show()

			if content.has_key("align") and content["align"].lower() == "center":
				image.SetPosition(self.limitWidth / 2 - image.GetWidth() / 2, 0)
			else:
				if self.x + image.GetWidth() >= self.limitWidth and self.limitWidth != 0:
					return False
				self.x += image.GetWidth()

			self.childrenList.append(image)
			self.maxHeight = max(self.maxHeight, image.GetHeight())

			return True

		# tag <TEXT []>
		elif index == self.OBJECT_TYPE_TEXT:
			if not content.has_key("text"):
				dbg.TraceError("Cannot read text tag : no text given")
				return False

			textLine = TextLine()
			textLine.SetParent(self)
			textLine.SetPosition(self.x, 0)
			textLine.SetWindowVerticalAlignCenter()
			textLine.SetVerticalAlignCenter()
			if content.has_key("r") and content.has_key("g") and content.has_key("b"):
				textLine.SetFontColor(int(content["r"]) / 255.0, int(content["g"]) / 255.0, int(content["b"]) / 255.0)
			elif content.has_key("color"):
				textLine.SetPackedFontColor(int(content["color"], 0))
			isLarge = False
			if content.has_key("font_size"):
				if content["font_size"].lower() == "large":
					isLarge = True
					textLine.SetFontName(localeInfo.UI_DEF_FONT_LARGE)
			if content.has_key("bold"):
				if content["bold"] == "1" or content["bold"].lower() == "true":
					if isLarge:
						textLine.SetFontName(localeInfo.UI_DEF_FONT_LARGE_BOLD)
					else:
						textLine.SetFontName(localeInfo.UI_DEF_FONT_BOLD)
			if content.has_key("outline") and content["outline"] == "1":
				textLine.SetOutline()
			textLine.SetText(content["text"])
			textLine.Show()

			if self.x + textLine.GetTextWidth() >= self.limitWidth and self.limitWidth != 0:
				return False

			self.childrenList.append(textLine)
			self.x += textLine.GetTextWidth()
			self.maxHeight = max(self.maxHeight, textLine.GetTextHeight() + 2)

			return True

		# tag <HEIGHT []>
		elif index == self.OBJECT_TYPE_HEIGHT:
			if not content.has_key("size"):
				dbg.TraceError("Cannot read height tag : no size given")
				return False

			self.extraHeight += int(content["size"])

			return True

		# tag <WIDTH []>
		elif index == self.OBJECT_TYPE_WIDTH:
			if not content.has_key("size"):
				dbg.TraceError("Cannot read width tag : no size given")
				return False

			self.x += int(content["size"])

			return True

		return False

class MultiTextLine(Window):

	RETURN_STRING = "[ENTER]"
	LINE_HEIGHT = 17

	def __init__(self):
		Window.__init__(self)

		self.isSetFontColor = False
		self.r = 0.0
		self.g = 0.0
		self.b = 0.0
		self.packedFontColor = -1

		self.lines = []
		self.hAlignCenter = False
		self.vAlignCenter = False
		self.windowVAlignCenter = False
		self.isOutline = False
		self.text = ""
		self.basePos = 0
		self.maxTextWidth = 0
		self.realX = 0
		self.realY = 0

		self.SetWindowName("NONAME_MultiTextLine")

	def __del__(self):
		Window.__del__(self)

	def SetWidth(self, width):
		self.SetSize(width, self.GetHeight())
		self.SetText(self.GetText())

	def SetHeight(self, height):
		self.SetSize(self.GetWidth(), height)
		self.SetText(self.GetText())

	def NewTextLine(self):
		line = TextLine()
		line.xRect = 0.0
		line.SetParent(self)
		if self.hAlignCenter == True:
			line.SetWindowHorizontalAlignCenter()
			line.SetHorizontalAlignCenter()
		if self.vAlignCenter == True:
			line.SetVerticalAlignCenter()
		if self.isSetFontColor == True:
			if self.packedFontColor > -1:
				line.SetPackedFontColor(self.packedFontColor)
			else:
				line.SetFontColor(self.r, self.g, self.b)
		if self.isOutline == True:
			line.SetOutline()
		line.Show()
		self.lines.append(line)

		return self.lines[len(self.lines) - 1]

	def Clear(self):
		self.text = ""
		self.lines = []

	def SetTextHorizontalAlignCenter(self):
		self.hAlignCenter = True
		self.SetText(self.GetText())

	def SetTextVerticalAlignCenter(self):
		self.vAlignCenter = True
		self.SetText(self.GetText())

	def SetOutline(self):
		self.isOutline = True
		self.SetText(self.GetText())

	def SetFontColor(self, r, g, b):
		self.isSetFontColor = True
		self.r = r
		self.g = g
		self.b = b

	def SetPackedFontColor(self, color):
		self.isSetFontColor = True
		self.packedFontColor = color

	def SetText(self, text):
		self.Clear()

		self.text = text
		self.maxTextWidth = 0

		line = self.NewTextLine()
		pos = 0
		newStartPos = 0
		while pos < len(text):
			line.SetText(text[:pos+1])

			newLine = False
			if len(text) >= pos + len(self.RETURN_STRING):
				if text[pos:pos+len(self.RETURN_STRING)] == self.RETURN_STRING:
					newLine = True
					newStartPos = pos+len(self.RETURN_STRING)
			if newLine == False and pos > 0:
				if line.GetTextWidth() > self.GetWidth() and self.GetWidth() > 0:
					newLine = True

					curText = text[:pos+1]
					breakPos = curText.rfind(" ")
					if breakPos == -1:
						if curText.find(":httpXxX") != -1:
							newLine = False
						else:
							breakPos = curText.rfind(".")
							if breakPos == -1:
								breakPos = curText.rfind(",")
								if breakPos == -1:
									breakPos = curText.rfind(";")
									if breakPos == -1:
										breakPos = curText.rfind(":")
							if breakPos != -1:
								breakPos += 1
					if breakPos != -1:
						pos = breakPos
						newStartPos = pos
					else:
						newStartPos = pos

			if newLine == True:
				line.SetText(text[:pos])
				if line.GetTextWidth() > self.GetWidth() and self.GetWidth() > 0:
					line.ShowPercentage(0.0, 1.0 - (line.GetTextWidth() - self.GetWidth()) / float(line.GetTextWidth()))
					line.xRect = -(line.GetTextWidth() - self.GetWidth()) / float(line.GetTextWidth())

				line = self.NewTextLine()
				text = text[newStartPos:]
				if text[:1] == " ":
					text = text[1:]
				pos = 0
			else:
				pos += 1
				if pos >= len(text):
					if line.GetTextWidth() > self.GetWidth() and self.GetWidth() > 0:
						line.ShowPercentage(0.0, 1.0 - (line.GetTextWidth() - self.GetWidth()) / float(line.GetTextWidth()))
						line.xRect = -(line.GetTextWidth() - self.GetWidth()) / float(line.GetTextWidth())

			self.maxTextWidth = max(self.maxTextWidth, line.GetTextWidth())
			if self.GetWidth() > 0 and self.maxTextWidth > self.GetWidth():
				self.maxTextWidth = self.GetWidth()

		self.ShowBetween(self.GetLineCount() - self.GetViewLineCount(), self.GetLineCount() - 1)
		#self.SetSize(self.GetWidth(), len(self.lines) * self.LINE_HEIGHT)

		self.SetPosition(self.realX, self.realY)

	def GetMaxTextWidth(self):
		return self.maxTextWidth

	def GetLine(self, index):
		if index < 0 or index >= len(self.lines):
			return None
		return self.lines[index]

	def GetLastLine(self):
		return self.GetLine(len(self.lines) - 1)

	def GetLineCount(self):
		return len(self.lines)

	def GetViewLineCount(self):
		if self.GetHeight() == 0:
			return self.GetLineCount()
		return self.GetHeight() / self.LINE_HEIGHT

	def SetBasePos(self, basePos):
		self.basePos = basePos

		self.ShowBetween(self.basePos, self.basePos + self.GetViewLineCount() - 1)

	def GetBasePos(self):
		return self.basePos

	def ShowBetween(self, start, end):
		start = max(0, start)
		end = min(self.GetLineCount() - 1, end)

		height = self.GetHeight()
		if height == 0:
			height = self.GetLineCount() * self.LINE_HEIGHT

		for i in xrange(len(self.lines)):
			if i < start or i > end:
				self.lines[i].Hide()
			else:
				self.lines[i].SetPosition(0, (i - start) * self.LINE_HEIGHT)
				self.lines[i].Show()

	def GetRealHeight(self):
		if self.GetHeight() > 0:
			return self.GetHeight()

		return self.GetLineCount() * self.LINE_HEIGHT

	def SetWindowVerticalAlignCenter(self):
		Window.SetWindowVerticalAlignCenter(self)
		self.windowVAlignCenter = True

		if self.GetHeight() == 0:
			self.SetPosition(self.realX, self.realY)

	def SetPosition(self, x, y):
		self.realX = x
		self.realY = y
		if self.windowVAlignCenter and self.GetHeight() == 0:
			Window.SetPosition(self, x, y - self.GetRealHeight() / 2)
		else:
			Window.SetPosition(self, x, y)

	def GetBottom(self):
		return self.GetTop() + self.GetRealHeight()

	def GetText(self):
		return self.text

	def SetYRenderingRect(self, sy, ey):
		sy = max(0, sy)
		ey = min(self.GetRealHeight(), ey)

		for i in xrange(len(self.lines)):
			line = self.lines[i]
			if sy >= line.GetBottom() or ey <= line.GetTop() or ey <= sy:
				line.SetRenderingRect(0.0, 0.0, line.xRect, -1.0)
			elif line.GetTextHeight() > 0:
				line.SetRenderingRect(0.0, -min(1.0, float(max(0, sy - line.GetTop())) / line.GetTextHeight()), line.xRect, max(-1.0, float(min(0, ey - line.GetTop() - line.GetTextHeight())) / line.GetTextHeight()))

	def SetPackedFontColor(self, color, lineIdx = -1):
		if lineIdx == -1:
			for line in self.lines:
				line.SetPackedFontColor(color)
		else:
			self.lines[lineIdx].SetPackedFontColor(color)

	def SetFontName(self, fontName):
		for line in self.lines:
			line.SetFontName(fontName)

	def SetLineHeight(self, height):
		self.LINE_HEIGHT = height

class CheckBox(Window):

	STATE_UNSELECTED = 0
	STATE_SELECTED = 1

	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)

		self.state = self.STATE_UNSELECTED
		self.eventFunc = None
		self.eventArgs = None

	#	self.btnBox = {
	#		self.STATE_UNSELECTED : self.__init_MakeButton("d:/ymir work/ui/public/checkbox_unselected_%s.sub"),
	#		self.STATE_SELECTED : self.__init_MakeButton("d:/ymir work/ui/public/checkbox_selected_%s.sub"),
	#	}
		if app.GetSelectedDesignName() != "illumina":
			self.btnBox = {
				self.STATE_UNSELECTED : self.__init_MakeButton("d:/ymir work/ui/checkbox/checkbox_new_unselected.tga"),
				self.STATE_SELECTED : self.__init_MakeButton("d:/ymir work/ui/checkbox/checkbox_new_selected.tga", "d:/ymir work/ui/checkbox/checkbox_new_selected.tga"),
			}
		else:
			self.btnBox = {
				self.STATE_UNSELECTED : self.__init_MakeButton("d:/ymir work/ui/checkbox/checkbox_new_unselected.tga"),
				self.STATE_SELECTED : self.__init_MakeButton("d:/ymir work/ui/checkbox/checkbox_new_selected.tga", "d:/ymir work/ui/checkbox/checkbox_new_selected.tga"),
			}

		text = TextLine()
		text.SetParent(self)
		text.SetWindowVerticalAlignCenter()
		text.SetVerticalAlignCenter()
		text.Show()
		self.text = text

		self.__Refresh()

		self.SetWindowName("NONAME_CheckBox")

	def __del__(self):
		Window.__del__(self)

	def __ConvertPath(self, path, subStr):
		if path.find("%s") != -1:
			return path % subStr
		else:
			return path

	def __init_MakeButton(self, path, disablePath = None):
		btn = Button()
		btn.SetParent(self)
		btn.SetWindowVerticalAlignCenter()
		btn.SetUpVisual(self.__ConvertPath(path, "01"))
		btn.SetOverVisual(self.__ConvertPath(path, "02"))
		btn.SetDownVisual(self.__ConvertPath(path, "03"))
		if disablePath:
			btn.SetDisableVisual(disablePath)
		else:
			btn.SetDisableVisual(self.__ConvertPath(path, "01"))
		btn.SAFE_SetEvent(self.OnClickButton)
		btn.baseWidth = btn.GetWidth()
		return btn

	def __UpdateRect(self):
		if self.text.GetText():
			width = self.btnBox[self.state].baseWidth + 5 + self.text.GetTextWidth()
		else:
			width = self.btnBox[self.state].baseWidth
		height = max(self.btnBox[self.state].GetHeight(), self.text.GetTextHeight())
		self.SetSize(width, height)

		self.btnBox[self.state].SetSize(width, self.btnBox[self.state].GetHeight())
		self.text.SetPosition(self.btnBox[self.state].baseWidth + 5, 0)

		self.text.UpdateRect()
		self.btnBox[self.state].UpdateRect()
		self.UpdateRect()

	def __Refresh(self):
		self.__UpdateRect()

		self.btnBox[self.STATE_UNSELECTED].SetVisible(self.state == self.STATE_UNSELECTED)
		self.btnBox[self.STATE_SELECTED].SetVisible(self.state == self.STATE_SELECTED)

	def OnClickButton(self):
		if self.state == self.STATE_UNSELECTED:
			self.state = self.STATE_SELECTED
		else:
			self.state = self.STATE_UNSELECTED
		self.__Refresh()

		if self.eventFunc:
			apply(self.eventFunc, self.eventArgs)

	def SetChecked(self, state):
		self.state = state
		self.__Refresh()

	def IsChecked(self):
		return self.state != self.STATE_UNSELECTED

	def SetText(self, text):
		self.text.SetText(text)
		self.__UpdateRect()

	def SetEvent(self, event, *args):
		self.eventFunc = event
		self.eventArgs = args

	def SAFE_SetEvent(self, event, *args):
		self.eventFunc = __mem_func__(event)
		self.eventArgs = args

	def Disable(self):
		self.btnBox[self.STATE_UNSELECTED].Disable()
		self.btnBox[self.STATE_SELECTED].Disable()

	def Enable(self):
		self.btnBox[self.STATE_UNSELECTED].Enable()
		self.btnBox[self.STATE_SELECTED].Enable()

class EmptyCandidateWindow(Window):
	def __init__(self):
		Window.__init__(self)

	def __del__(self):
		Window.__init__(self)

	def Load(self):
		pass

	def SetCandidatePosition(self, x, y, textCount):
		pass

	def Clear(self):
		pass

	def Append(self, text):
		pass

	def Refresh(self):
		pass

	def Select(self):
		pass

class EditLine(TextLine):
	candidateWindowClassDict = {}

	def __init__(self):
		TextLine.__init__(self)
		ime.EnablePaste(1)
		self.eventReturn = Window.NoneMethod
		self.eventEscape = None
		self.argsEscape = None
		self.eventTab = None
		self.eventUpdate = None
		self.numberMode = False
		self.useIME = True

		self.bCodePage = False

		self.candidateWindowClass = None
		self.candidateWindow = None

		self.readingWnd = ReadingWnd()
		self.readingWnd.Hide()

		self.overLay = TextLine()
		self.overLay.SetParent(self)
		self.overLay.SetPosition(0, 0)
		self.overLay.SetPackedFontColor(WHITE_COLOR)
		self.overLay.Hide()

		if app.ARABIC_LANG and app.GetLanguage() == app.LANG_ARABIC:
			TextLine.SetInverse(self)

	def __del__(self):
		TextLine.__del__(self)

		self.eventReturn = Window.NoneMethod
		self.eventEscape = Window.NoneMethod
		self.eventTab = None

	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.RegisterTextLine(self, layer)

	def SAFE_SetReturnEvent(self, event):
		self.eventReturn = __mem_func__(event)		

	def SetReturnEvent(self, event):
		self.eventReturn = event

	def SetEscapeEvent(self, event, *args):
		self.eventEscape = event
		self.argsEscape = args

	def SetTabEvent(self, event):
		self.eventTab = event

	def SetOverlayText(self, text):
		self.overLay.SetText(text)
		self.__RefreshOverlay()

	def SetUpdateEvent(self, event):
		self.eventUpdate = event

	def GetOverlayText(self):
		return self.overLay.GetText()

	def SetMax(self, max):
		self.max = max
		wndMgr.SetMax(self.hWnd, self.max)
		ime.SetMax(self.max)
		self.SetUserMax(self.max)
		
	def SetUserMax(self, max):
		self.userMax = max
		ime.SetUserMax(self.userMax)

	def SetNumberMode(self):
		self.numberMode = True

	def GetDisplayText(self):
		if self.GetText():
			return self.GetText()
		else:
			return self.overLay.GetText()

	def __RefreshOverlay(self, isFocus = -1):
		if isFocus == -1:
			isFocus = self.IsFocus()
		if self.GetText() or isFocus:
			self.overLay.Hide()
		else:
			self.overLay.Show()

	#def AddExceptKey(self, key):
	#	ime.AddExceptKey(key)

	#def ClearExceptKey(self):
	#	ime.ClearExceptKey()

	def SetIMEFlag(self, flag):
		self.useIME = flag

	def SetText(self, text):
		wndMgr.SetText(self.hWnd, text)
		self.__RefreshOverlay()

		if self.IsFocus():
			ime.SetText(text)

	def Enable(self):
		wndMgr.ShowCursor(self.hWnd)

	def Disable(self):
		wndMgr.HideCursor(self.hWnd)

	def IsShowCursor(self):
		return wndMgr.IsShowCursor(self.hWnd)

	def SetEndPosition(self):
		ime.MoveEnd()

	def OnSetFocus(self):
		Text = self.GetText()
		ime.SetText(Text)
		ime.SetMax(self.max)
		ime.SetUserMax(self.userMax)
		ime.SetCursorPosition(-1)
		if self.numberMode:
			ime.SetNumberMode()
		else:
			ime.SetStringMode()
		ime.EnableCaptureInput()
		if self.useIME:
			ime.EnableIME()
		else:
			ime.DisableIME()
		wndMgr.ShowCursor(self.hWnd, True)
		self.__RefreshOverlay()

	def OnKillFocus(self):
		self.SetText(ime.GetText(self.bCodePage))
		self.OnIMECloseReadingWnd()
		ime.DisableIME()
		ime.DisableCaptureInput()
		wndMgr.HideCursor(self.hWnd)
		self.__RefreshOverlay(False)

	def OnIMEOpenCandidateList(self):
		self.candidateWindow.Show()
		self.candidateWindow.Clear()
		self.candidateWindow.Refresh()

		gx, gy = self.GetGlobalPosition()
		self.candidateWindow.SetCandidatePosition(gx, gy, len(self.GetText()))

		return True

	def OnIMECloseCandidateList(self):
		self.candidateWindow.Hide()
		return True

	def OnIMEOpenReadingWnd(self):
		gx, gy = self.GetGlobalPosition()
		textlen = len(self.GetText())-2		
		reading = ime.GetReading()
		readinglen = len(reading)
		self.readingWnd.SetReadingPosition( gx + textlen*6-24-readinglen*6, gy )
		self.readingWnd.SetText(reading)
		if ime.GetReadingError() == 0:
			self.readingWnd.SetTextColor(0xffffffff)
		else:
			self.readingWnd.SetTextColor(0xffff0000)
		self.readingWnd.SetSize(readinglen * 6 + 4, 19)
		self.readingWnd.Show()
		return True

	def OnIMECloseReadingWnd(self):
		self.readingWnd.Hide()
		return True

	def OnIMEUpdate(self):
		snd.PlaySound("sound/ui/type.wav")
		TextLine.SetText(self, ime.GetText(self.bCodePage))
		self.__RefreshOverlay()

		if self.eventUpdate:
			self.eventUpdate()

	def OnIMETab(self):
		if self.eventTab:
			self.eventTab()
			return True

		return False

	def OnIMEReturn(self):
		snd.PlaySound("sound/ui/click.wav")
		self.eventReturn()

		return True

	def OnPressEscapeKey(self):
		if self.eventEscape:
			ret = apply(self.eventEscape, self.argsEscape)
			if ret:
				return True
		return True

	def OnKeyDown(self, key):
		if key in (app.DIK_F1, app.DIK_F2, app.DIK_F3, app.DIK_F4, app.DIK_F5, app.DIK_F6, app.DIK_F7, app.DIK_F8, app.DIK_F9, app.DIK_F10, app.DIK_F11, app.DIK_LALT, app.DIK_SYSRQ, app.DIK_LCONTROL):
			return False
		
		if app.DIK_V == key:
			if app.IsPressed(app.DIK_LCONTROL):
				self.SetText(self.GetText().replace("\x16", ""))
				ime.PasteTextFromClipBoard()

		return True

	def OnKeyUp(self, key):
		if key in (app.DIK_F1, app.DIK_F2, app.DIK_F3, app.DIK_F4, app.DIK_F5, app.DIK_F6, app.DIK_F7, app.DIK_F8, app.DIK_F9, app.DIK_F10, app.DIK_F11, app.DIK_LALT, app.DIK_SYSRQ, app.DIK_LCONTROL):
			return False

		return True

	def OnIMEKeyDown(self, key):		
		# Left
		if app.VK_LEFT == key:
			ime.MoveLeft()
			return True
		# Right
		if app.VK_RIGHT == key:
			ime.MoveRight()
			return True

		# Home
		if app.VK_HOME == key:
			ime.MoveHome()
			return True
		# End
		if app.VK_END == key:
			ime.MoveEnd()
			return True

		# Delete
		if app.VK_DELETE == key:
			ime.Delete()
			TextLine.SetText(self, ime.GetText(self.bCodePage))
			return True
			
		return True

	#def OnMouseLeftButtonDown(self):
	#	self.SetFocus()
	def OnMouseLeftButtonDown(self):
		if False == self.IsIn():
			return False

		self.SetFocus()
		PixelPosition = wndMgr.GetCursorPosition(self.hWnd)
		ime.SetCursorPosition(PixelPosition)

class MarkBox(Window):
	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)

	def __del__(self):
		Window.__del__(self)

	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.RegisterMarkBox(self, layer)

	def Load(self):
		wndMgr.MarkBox_Load(self.hWnd)

	def SetScale(self, scale):
		wndMgr.MarkBox_SetScale(self.hWnd, scale)

	def SetIndex(self, guildID):
		MarkID = guild.GuildIDToMarkID(guildID)
		wndMgr.MarkBox_SetImageFilename(self.hWnd, guild.GetMarkImageFilenameByMarkID(MarkID))
		wndMgr.MarkBox_SetIndex(self.hWnd, guild.GetMarkIndexByMarkID(MarkID))

	def SetAlpha(self, alpha):
		wndMgr.MarkBox_SetDiffuseColor(self.hWnd, 1.0, 1.0, 1.0, alpha)

class ImageBox(Window):
	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)

		self.eventDict={}
		self.argDict={}
		self.name=""
		self.eventFunc = {"mouse_click" : None, "mouse_over_in" : None, "mouse_over_out" : None}
		self.eventArgs = {"mouse_click" : None, "mouse_over_in" : None, "mouse_over_out" : None}

	def __del__(self):
		Window.__del__(self)
		self.eventFunc = None
		self.eventArgs = None

	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.RegisterImageBox(self, layer)

	def LoadImage(self, imageName):
		self.name=imageName
		wndMgr.LoadImage(self.hWnd, imageName)

		if len(self.eventDict)!=0:
			print "LOAD IMAGE", self, self.eventDict

	def SetScale(self, xScale, yScale):
		wndMgr.SetScale(self.hWnd, xScale, yScale)

	def LoadScaledImage(self, imageName, scaleFactor):
		imgPtr = app.GetImagePtr(imageName)
		return self.LoadScaledImageByPtr(imgPtr, scaleFactor)

	def LoadScaledImageByPtr(self, imagePtr, scaleFactor):
		if imagePtr == 0:
			return False

		(width, height) = app.GetImageSize(imagePtr)
		return wndMgr.LoadScaledImageByPtr(self.hWnd, imagePtr, int(width * scaleFactor), int(height * scaleFactor))

	def LoadScaledImageAbs(self, imageName, width, height):
		imgPtr = app.GetImagePtr(imageName)
		return self.LoadScaledImageAbsByPtr(imgPtr, width, height)

	def LoadScaledImageAbsByPtr(self, imagePtr, width, height):
		if imagePtr == 0:
			return False

		return wndMgr.LoadScaledImageByPtr(self.hWnd, imagePtr, width, height)

	def GetImageName(self):
		return self.name

	def SetAlpha(self, alpha):
		wndMgr.SetDiffuseColor(self.hWnd, 1.0, 1.0, 1.0, alpha)

	def GetAlpha(self):
		return wndMgr.GetAlpha(self.hWnd)

	def GetWidth(self):
		return wndMgr.GetWidth(self.hWnd)

	def GetHeight(self):
		return wndMgr.GetHeight(self.hWnd)

	def __OnMouseOverIn(self):
		try:
			apply(self.eventDict["MOUSE_OVER_IN"], self.argDict["MOUSE_OVER_IN"])
		except KeyError:
			pass

	def __OnMouseOverOut(self):
		try:
			apply(self.eventDict["MOUSE_OVER_OUT"], self.argDict["MOUSE_OVER_OUT"])
		except KeyError:
			pass

	def OnMouseLeftButtonDown(self):
		if self.eventDict.has_key("MOUSE_LEFT_DOWN"):
			apply(self.eventDict["MOUSE_LEFT_DOWN"], self.argDict["MOUSE_LEFT_DOWN"])

	def OnMouseLeftButtonUp(self):
		if self.eventDict.has_key("MOUSE_LEFT_UP"):
			apply(self.eventDict["MOUSE_LEFT_UP"], self.argDict["MOUSE_LEFT_UP"])
		if self.eventFunc["mouse_click"] :
			apply(self.eventFunc["mouse_click"], self.eventArgs["mouse_click"])

	def SetStringEvent(self, event, func, *args):
		self.eventDict[event]=func
		self.argDict[event]=args

	def SAFE_SetStringEvent(self, event, func, *args):
		self.eventDict[event]=__mem_func__(func)
		self.argDict[event]=args

	def SetEvent(self, func, *args) :
		result = self.eventFunc.has_key(args[0])		
		if result :
			self.eventFunc[args[0]] = func
			self.eventArgs[args[0]] = args
		else :
			print "[ERROR] ui.py SetEvent, Can`t Find has_key : %s" % args[0]

	def OnMouseOverIn(self) :
		if self.eventFunc["mouse_over_in"] :
			apply(self.eventFunc["mouse_over_in"], self.eventArgs["mouse_over_in"])
		else:
			self.__OnMouseOverIn()

	def OnMouseOverOut(self) :
		if self.eventFunc["mouse_over_out"] :
			apply(self.eventFunc["mouse_over_out"], self.eventArgs["mouse_over_out"])
		else :
			self.__OnMouseOverOut()

	def SetDiffuseColor(self, r, g, b, a):
		wndMgr.SetDiffuseColor(self.hWnd, r, g, b, a)

	def DisplayProcent(self, percent):
		wndMgr.DisplayImageProcent(self.hWnd, percent)

class ExpandedImageBox(ImageBox):
	def __init__(self, layer = "UI"):
		ImageBox.__init__(self, layer)

	def __del__(self):
		ImageBox.__del__(self)

	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.RegisterExpandedImageBox(self, layer)

	#def SetScale(self, xScale, yScale):
	#	wndMgr.SetScale(self.hWnd, xScale, yScale)

	def SetOrigin(self, x, y):
		wndMgr.SetOrigin(self.hWnd, x, y)

	def SetRotation(self, rotation):
		wndMgr.SetRotation(self.hWnd, rotation)

	def SetRenderingMode(self, mode):
		wndMgr.SetRenderingMode(self.hWnd, mode)

	def SetRenderingRect(self, left, top, right, bottom):
		wndMgr.SetRenderingRect(self.hWnd, left, top, right, bottom)

	def SetPercentage(self, curValue, maxValue):
		if maxValue:
			self.SetRenderingRect(0.0, 0.0, -1.0 + float(curValue) / float(maxValue), 0.0)
		else:
			self.SetRenderingRect(0.0, 0.0, 0.0, 0.0)
			
	def SetPercentageHorizontal(self, curValue, maxValue):
		wndMgr.SetRenderingRect(self.hWnd, 0.0,  -1.0 + float(curValue) / float(maxValue), 0.0,0.0)

	def GetPixelColor(self, x, y):
		if x < 0 or x >= self.GetWidth() or y < 0 or y >= self.GetHeight():
			return (0, 0, 0, 0)
		r, g, b, a = wndMgr.GetPixelColor(self.hWnd, x, y)
		return (r, g, b, a)

	def IsInRenderingPosition(self, xMouse = -1, yMouse = -1):
		if xMouse == -1 and yMouse == -1:
			xMouse, yMouse = self.GetMouseLocalPosition()
		color = self.GetPixelColor(xMouse, yMouse)

		if color[3] == 0.0:
			return False

		return self.IsInPosition()

class AniImageBox(Window):
	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)

		self.nextFrameEvent = None
		self.nextFrameArgs = None
		self.endFrameEvent = None
		self.endFrameArgs = None

		if app.AHMET_FISH_EVENT_SYSTEM:
			self.end_frame_event = None

		self.SetWindowName("NONAME_AniImageBox")

	def __del__(self):
		Window.__del__(self)

		if app.AHMET_FISH_EVENT_SYSTEM:
			self.end_frame_event = None

	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.RegisterAniImageBox(self, layer)

	def SetDelay(self, delay):
		wndMgr.SetDelay(self.hWnd, delay)

	def SetSkipCount(self, skip_count):
		wndMgr.SetSkipCount(self.hWnd, skip_count)

	def ResetFrame(self):
		wndMgr.ResetFrame(self.hWnd)

	def GetFrameIndex(self):
		return wndMgr.GetFrameIndex(self.hWnd)

	def AppendImage(self, filename):
		wndMgr.AppendImage(self.hWnd, filename)

	def ClearImages(self):
		wndMgr.ClearImages(self.hWnd)

	def SetPercentage(self, curValue, maxValue):
		if maxValue == 0:
			import dbg
			dbg.TraceError("AniImageBox.SetPercentage(%d, %d) -> invalid max value", curValue, maxValue)
			maxValue = 1
		wndMgr.SetRenderingRect(self.hWnd, 0.0, 0.0, -1.0 + float(curValue) / float(maxValue), 0.0)

	if app.AHMET_FISH_EVENT_SYSTEM:
		def ResetFrame(self):
			wndMgr.ResetFrame(self.hWnd)
			
		def SetEndFrameEvent(self, event):
			self.end_frame_event = event

		def SetScale(self, xScale, yScale):
			wndMgr.SetScale(self.hWnd, xScale, yScale)

	def SetVPercentage(self, curValue, maxValue):
		if maxValue == 0:
			import dbg
			dbg.TraceError("AniImageBox.SetVPercentage(%d, %d) -> invalid max value", curValue, maxValue)
			maxValue = 1
		wndMgr.SetRenderingRect(self.hWnd, 0.0, -1.0 + float(curValue) / float(maxValue), 0.0, 0.0)

	def SAFE_SetNextFrameEvent(self, event, *args):
		self.nextFrameEvent = __mem_func__(event)
		self.nextFrameArgs = args

	def SAFE_SetEndFrameEvent(self, event, *args):
		self.endFrameEvent = __mem_func__(event)
		self.endFrameArgs = args

	def OnNextFrame(self):
		if self.nextFrameEvent:
			apply(self.nextFrameEvent, self.nextFrameArgs)

	def SetOnEndFrame(self, event, *args):
		self.endFrameEvent = event
		self.endFrameArgs = args

	def OnEndFrame(self):
		if self.endFrameEvent:
			apply(self.endFrameEvent, self.endFrameArgs)

		if app.AHMET_FISH_EVENT_SYSTEM:
			if self.end_frame_event:
				self.end_frame_event( )

	def LoadGIFImage(self, filename):
		return wndMgr.LoadGIFImage(self.hWnd, filename)

	def LoadScaledGIFImage(self, filename, max_width, max_height):
		return wndMgr.LoadScaledGIFImage(self.hWnd, filename, max_width, max_height)

class LimitTextLine(TextLine):

	def __init__(self):
		TextLine.__init__(self)

		self.limitWidth = 0

		self.baseX = 0.0
		self.displayX = 1.0
		self.maxX = 0.0
		self.basePosChange = 0.001
		self.sleepTimer = 0

		self.realLeft = 0
		self.textWidth = 0

	def __del__(self):
		TextLine.__del__(self)

	def SetPosition(self, x, y):
		TextLine.SetPosition(self, x, y)
		self.realLeft = x
		self.__RefreshText()

	def SetSpeed(self, speed):
		if self.basePosChange < 0:
			speed = -speed
		self.basePosChange = 1.0 / float(speed)

	def SetText(self, text):
		self.baseX = 0
		self.sleepTimer = 0
		self.basePosChange = abs(self.basePosChange)
		TextLine.SetText(self, text)
		TextLine.UpdateRect(self)
		self.textWidth = self.GetTextWidth()
		self.__RefreshBasePos()

	def SetLimitWidth(self, width):
		self.limitWidth = int(width)
		self.__RefreshBasePos()

	def GetLimitWidth(self):
		return self.limitWidth

	def __CheckBasePos(self):
		self.baseX = min(self.baseX, self.maxX)
		self.__RefreshText()

	def IsSliding(self):
		return self.maxX > 0.0

	def __RefreshBasePos(self):
		self.displayX = 1.0
		self.maxX = 0.0

		if self.limitWidth <= 0:
			self.__CheckBasePos()
			return

		if self.GetTextWidth() == 0:
			return

		self.displayX = min(1.0, float(self.limitWidth) / float(self.GetTextWidth()))
		self.maxX = 1.0 - self.displayX

		self.__CheckBasePos()

	def __RefreshText(self):
		self.ShowPercentage(self.baseX, self.baseX + self.displayX)
		TextLine.SetPosition(self, self.realLeft - int(float(self.textWidth) * self.baseX), self.GetTop())

	def SetRightSide(self):
		self.baseX = self.maxX
		self.sleepTimer = app.GetTime() + 2.5
		self.basePosChange = -abs(self.basePosChange)
		self.__RefreshText()

	def OnUpdate(self):
		if self.maxX == 0:
			return

		if self.sleepTimer != 0:
			if app.GetTime() < self.sleepTimer:
				return
			self.sleepTimer = 0

		self.baseX += self.basePosChange
		self.baseX = max(0.0, min(self.baseX, self.maxX))
		self.__RefreshText()

		if self.baseX == 0.0 or self.baseX == self.maxX:
			self.sleepTimer = app.GetTime() + 2.5
			self.basePosChange = -self.basePosChange

class Button(Window):
	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)

		self.eventFunc = None
		self.eventArgs = None

		self.setUpVisualEvent = None
		self.setUpVisualArgs = None

		self.setOverVisualEvent = None
		self.setOverVisualArgs = None

		self.setDownVisualEvent = None
		self.setDownVisualArgs = None

		self.overInEvent = None
		self.overInArgs = None
		self.overOutEvent = None
		self.overOutArgs = None

		self.ButtonText = None
		self.ToolTipText = None

		self.TextChild = []

		self.showtooltipevent = None
		self.showtooltiparg = None
		self.hidetooltipevent = None
		self.hidetooltiparg = None

		self.underlayImageList = {
			"up" : None,
			"over" : None,
			"down" : None,
		}

		self.innerImageList = {
			"up" : None,
			"over" : None,
			"down" : None,
		}

		self.innerFlashStart = 0.0
		self.innerFlashTime = 0.0
		self.flashRGB = [1.0, 1.0, 1.0]

		self.underlayAlpha = 1.0

	def __del__(self):
		Window.__del__(self)

		self.eventFunc = None
		self.eventArgs = None

	def LeftRightReverse(self):
		return
		# self.SetText(self.GetText()[::-1])

	def SetDiffuseColor(self, r, g, b, a):
		wndMgr.SetDiffuseColor(self.hWnd, r, g, b, a)
		for key in self.underlayImageList:
			if self.underlayImageList[key]:
				self.underlayImageList[key].SetDiffuseColor(r, g, b, self.underlayAlpha)

	def __HideInnerImages(self):
		for key in self.innerImageList:
			if self.innerImageList[key]:
				self.innerImageList[key].Hide()

	def __ShowInnerImage(self, type):
		self.__HideInnerImages()

		if self.innerImageList[type]:
			self.innerImageList[type].Show()

	def __SetInnerAlpha(self, alpha, r=1.0, g=1.0, b=1.0):
		if self.innerImageList["up"]:
			self.innerImageList["up"].SetDiffuseColor(r, g, b, alpha)

	def SetInnerImage(self, type, fileName):
		if not self.innerImageList.has_key(type):
			import dbg
			dbg.TraceError("SetInnerImage(%s, %s) -> invalid type" % (str(type), str(fileName)))
			return

		if not self.innerImageList[type]:
			img = ImageBox()
			img.SetParent(self)
			img.SetWindowHorizontalAlignCenter()
			img.SetWindowVerticalAlignCenter()
			img.AddFlag("not_pick")
			if type == "up":
				img.Show()
			else:
				img.Hide()
			self.innerImageList[type] = img

		self.innerImageList[type].LoadImage(fileName)

	def SetUpInnerVisual(self, fileName):
		self.SetInnerImage("up", fileName)

	def SetOverInnerVisual(self, fileName):
		self.SetInnerImage("over", fileName)

	def SetDownInnerVisual(self, fileName):
		self.SetInnerImage("down", fileName)

	def SetInnerVisual(self, fileName):
		for key in self.innerImageList:
			self.SetInnerImage(key, fileName)

	def SetInnerColor(self, r, g, b, a):
		for key in self.innerImageList:
			if self.innerImageList[key]:
				self.innerImageList[key].SetDiffuseColor(r, g, b, a)

	def ClearInnerVisual(self):
		for key in self.innerImageList:
			if self.innerImageList[key]:
				self.innerImageList[key] = None

	def __HideUnderlayImages(self):
		for key in self.underlayImageList:
			if self.underlayImageList[key]:
				self.underlayImageList[key].Hide()

	def __ShowUnderlayImage(self, type):
		self.__HideUnderlayImages()

		if self.underlayImageList[type]:
			self.underlayImageList[type].Show()

	def SetUnderlayImage(self, type, fileName):
		if not self.underlayImageList.has_key(type):
			import dbg
			dbg.TraceError("SetUnderlayImage(%s, %s) -> invalid type" % (str(type), str(fileName)))
			return

		if not self.underlayImageList[type]:
			img = ImageBox()
			img.SetParent(self)
			img.SetWindowHorizontalAlignCenter()
			img.SetWindowVerticalAlignCenter()
			img.SetAlpha(self.underlayAlpha)
			img.AddFlag("not_pick")
			if type == "up":
				img.Show()
			else:
				img.Hide()
			self.underlayImageList[type] = img

		self.underlayImageList[type].LoadImage(fileName)

	def SetUpUnderlayVisual(self, fileName):
		self.SetUnderlayImage("up", fileName)

	def SetOverUnderlayVisual(self, fileName):
		self.SetUnderlayImage("over", fileName)

	def SetDownUnderlayVisual(self, fileName):
		self.SetUnderlayImage("down", fileName)

	def SetUnderlayAlpha(self, alpha):
		for key in self.underlayImageList:
			if self.underlayImageList[key]:
				self.underlayImageList[key].SetAlpha(alpha)
		self.underlayAlpha = alpha

	def StartFlashing(self, flashTime, r=1.0, g=1.0, b=1.0):
		self.innerFlashStart = app.GetTime()
		self.innerFlashTime = flashTime
		self.flashRGB = [1.0 - r, 1.0 - g, 1.0 - b]

	def StopFlashing(self):
		self.innerFlashStart = 0.0
		self.__SetInnerAlpha(1.0)
		if self.ButtonText:
			self.ButtonText.SetAlpha(1.0)

	def SetName(self, name):
		self.SetWindowName(name)
		
	def GetName(self):
		return self.GetWindowName()

	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.RegisterButton(self, layer)

	def SetUpVisual(self, filename):
		wndMgr.SetUpVisual(self.hWnd, filename)

	def GetText(self):
		if self.ButtonText:
			return self.ButtonText.GetText()
		return ""

	def SetUpVisualEvent(self, event, *args):
		self.setUpVisualEvent = __mem_func__(event)
		self.setUpVisualArgs = args

	def SetOverVisual(self, filename):
		wndMgr.SetOverVisual(self.hWnd, filename)

	def SetOverVisualEvent(self, event, *args):
		self.setOverVisualEvent = __mem_func__(event)
		self.setOverVisualArgs = args

	def SetDownVisual(self, filename):
		wndMgr.SetDownVisual(self.hWnd, filename)

	def SetDownVisualEvent(self, event, *args):
		self.setDownVisualEvent = __mem_func__(event)
		self.setDownVisualArgs = args

	def SAFE_SetOverInEvent(self, event, *args):
		self.overInEvent = __mem_func__(event)
		self.overInArgs = args

	def OnMouseOverIn(self):
		if self.overInEvent:
			apply(self.overInEvent, self.overInArgs)

	def SAFE_SetOverOutEvent(self, event, *args):
		self.overOutEvent = __mem_func__(event)
		self.overOutArgs = args

	def OnMouseOverOut(self):
		if self.overOutEvent:
			apply(self.overOutEvent, self.overOutArgs)

	def SetDisableVisual(self, filename):
		wndMgr.SetDisableVisual(self.hWnd, filename)

	def GetUpVisualFileName(self):
		return wndMgr.GetUpVisualFileName(self.hWnd)

	def GetOverVisualFileName(self):
		return wndMgr.GetOverVisualFileName(self.hWnd)

	def GetDownVisualFileName(self):
		return wndMgr.GetDownVisualFileName(self.hWnd)

	def OnSetUpVisual(self):
		if self.setUpVisualEvent:
			apply(self.setUpVisualEvent, self.setUpVisualArgs)

	def OnSetOverVisual(self):
		if self.setOverVisualEvent:
			apply(self.setOverVisualEvent, self.setOverVisualArgs)

	def OnSetDownVisual(self):
		if self.setDownVisualEvent:
			apply(self.setDownVisualEvent, self.setDownVisualArgs)

	def Flash(self):
		wndMgr.Flash(self.hWnd)

	def Enable(self):
		wndMgr.Enable(self.hWnd)

	def Disable(self):
		wndMgr.Disable(self.hWnd)
			
	def IsDown(self):
		return wndMgr.IsDown(self.hWnd)

	def ShowToolTip(self):
		if self.ToolTipText:
			self.ToolTipText.Show()

		if self.showtooltipevent:
			apply(self.showtooltipevent, self.showtooltiparg)

	def HideToolTip(self):
		if self.ToolTipText:
			self.ToolTipText.Hide()

		if self.hidetooltipevent:
			apply(self.hidetooltipevent, self.hidetooltiparg)

	def SetShowToolTipEvent(self, func, *args):
		self.showtooltipevent = func
		self.showtooltiparg = args
		
	def SetHideToolTipEvent(self, func, *args):
		self.hidetooltipevent = func
		self.hidetooltiparg = args

	def SetEnabled(self, isEnabled):
		if isEnabled:
			if not self.IsEnabled():
				self.Enable()
		else:
			if self.IsEnabled():
				self.Disable()

	def IsEnabled(self):
		return wndMgr.IsEnabled(self.hWnd)

	def IsDisabled(self):
		return not self.IsEnabled()
	
	def SetDown(self):
		wndMgr.Down(self.hWnd)

	def Down(self):
		wndMgr.Down(self.hWnd)

	def FlashEx(self):
		wndMgr.FlashEx(self.hWnd)

	def SetUp(self):
		wndMgr.SetUp(self.hWnd)

	def SAFE_SetEvent(self, func, *args):
		self.eventFunc = __mem_func__(func)
		self.eventArgs = args
		
	def SetEvent(self, func, *args):
		self.eventFunc = func
		self.eventArgs = args

	def Over(self):
		wndMgr.Over(self.hWnd)

	def SetFontColor(self, r, g, b):
		if not self.ButtonText:
			return
		self.ButtonText.SetFontColor(r, g, b)

	def SetTextColor(self, color):
		if not self.ButtonText:
			return
		self.ButtonText.SetPackedFontColor(color)

	def SetOutlineColor(self, red, green, blue):
		if not self.ButtonText:
			return
		self.ButtonText.SetOutlineColor(red, green, blue)

	def SetPackedOutlineColor(self, color):
		if not self.ButtonText:
			return
		self.ButtonText.SetPackedOutlineColor(color)

	def SetText(self, text, height = 4):

		if not self.ButtonText:
			textLine = TextLine()
			textLine.SetParent(self)
			textLine.SetPosition(self.GetWidth()/2, self.GetHeight()/2)
			textLine.SetVerticalAlignCenter()
			textLine.SetHorizontalAlignCenter()
			textLine.Show()
			self.ButtonText = textLine

		self.ButtonText.SetText(text)

	def SetFormToolTipText(self, type, text, x, y, isCenter = True):
		if not self.ToolTipText:		
			toolTip=createToolTipWindowDict[type]("TOP_MOST")
			if type == "TEXT":
				toolTip.SetFontName( constInfo.GetChoosenFontName( ) )
			toolTip.SetSize(0, 0)
			toolTip.AddFlag("float")
			if isCenter:
				toolTip.SetHorizontalAlignCenter()
			toolTip.SetOutline()
			toolTip.Hide()
			toolTip.x = x
			toolTip.y = y
			toolTip.SetPosition(x + self.GetWidth()/2, y)
			toolTip.SetAlpha(1.0)
			toolTip.isShow = False
			self.ToolTipText=toolTip
			self.UpdateToolTipPosition()

		self.ToolTipText.SetText(text)

	def ClearToolTip(self):
		if self.ToolTipText:
			self.ToolTipText.Hide()
			self.ToolTipText = None

	def UpdateToolTipPosition(self):
		obj = self.ToolTipText
		if obj and obj.x != -1 and obj.y != -1:
			x, y = self.GetGlobalPosition()
			obj.SetPosition(x + obj.x + self.GetWidth() / 2, y + obj.y)

	def SetToolTipWindow(self, toolTip):		
		self.ToolTipText=toolTip		
		self.ToolTipText.SetParentProxy(self)
		self.ToolTipText.x = -1
		self.ToolTipText.y = -1
		self.ToolTipText.isShow = False

	def SetToolTipText(self, text, x=0, y = -19, isCenter = True):
		self.SetFormToolTipText("TEXT", text, x, y, isCenter)

	def CallEvent(self):
		snd.PlaySound("sound/ui/click.wav")

		if self.eventFunc:
			apply(self.eventFunc, self.eventArgs)

	def ShowToolTip(self):
		if self.ToolTipText:
			self.ToolTipText.isShow = True
			if self.IsShow():
				self.ToolTipText.Show()
				self.ToolTipText.SetTop()

	def HideToolTip(self):
		if self.ToolTipText:
			self.ToolTipText.isShow = False
			self.ToolTipText.Hide()

	def IsToolTipShow(self):
		if not self.ToolTipText:
			return False
		return self.ToolTipText.IsShow()

	def Show(self):
		Window.Show(self)
		if self.ToolTipText and self.ToolTipText.isShow:
			self.ShowToolTip()

	def OnHide(self):
		try:
			if self.ToolTipText.IsShow():
				self.ToolTipText.Hide()
		except:
			pass

	def SetRenderingRect(self, left, top, right, bottom):
		wndMgr.SetRenderingRect(self.hWnd, left, top, right, bottom)

		if self.ButtonText and self.ButtonText.GetText():
			xShowStart = int((-left) * self.GetWidth())
			xShowEnd = int((1.0 + right) * self.GetWidth())

			xTextStart = (self.GetWidth() - self.ButtonText.GetTextWidth()) / 2
			xTextEnd = xTextStart + self.ButtonText.GetTextWidth()

			xLeftRect = 0.0
			xRightRect = 1.0

			if xShowStart > xTextStart:
				xLeftRect = float(min(xShowStart, xTextEnd) - xTextStart) / float(xTextEnd - xTextStart)
			if xShowEnd < xTextEnd:
				xRightRect = float(max(xShowEnd, xTextStart) - xTextStart) / float(xTextEnd - xTextStart)

		#	dbg.TraceError("xShowStart %d xShowEnd %d xTextStart %d xTextEnd %d xLeftRect %f xRightRect %f" % \
		#		(xShowStart, xShowEnd, xTextStart, xTextEnd, xLeftRect, xRightRect))

			self.ButtonText.ShowPercentage(xLeftRect, xRightRect, 1.0 + bottom, top)

	def OnUpdate(self):
		if self.ToolTipText:
			self.UpdateToolTipPosition()

		if self.innerFlashStart != 0.0:
			timeNeed = self.innerFlashTime * 2
			curPct = ((app.GetTime() - self.innerFlashStart) % timeNeed) / timeNeed

			if curPct < 0.5:
				alpha = self.INNER_FLASH_START_ALPHA - (self.INNER_FLASH_START_ALPHA - self.INNER_FLASH_END_ALPHA) * (curPct * 2)
				colorPct = curPct * 2
			else:
				curPct -= 0.5
				alpha = self.INNER_FLASH_END_ALPHA - (self.INNER_FLASH_END_ALPHA -  self.INNER_FLASH_START_ALPHA) * (curPct * 2)
				colorPct = (0.5 - curPct) * 2

			r = 1.0 - self.flashRGB[0] * colorPct
			g = 1.0 - self.flashRGB[1] * colorPct
			b = 1.0 - self.flashRGB[2] * colorPct

			self.__SetInnerAlpha(alpha, r, g, b)
			if self.ButtonText:
				self.ButtonText.SetAlpha(alpha)

	def AppendTextLineAllClear(self) : 
		self.TextChild = []

	def SetAppendTextChangeText(self, idx, text):
		if not len(self.TextChild) :
			return

		self.TextChild[idx].SetText(text)

	def SetAppendTextColor(self, idx, color) :
		if not len(self.TextChild) :
			return

		self.TextChild[idx].SetPackedFontColor(color)

	def AppendTextLine(self, text
		, font_size = localeInfo.UI_DEF_FONT
		, font_color = grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)
		, text_sort = "center"
		, pos_x = None
		, pos_y = None) :
		textLine = TextLine()
		textLine.SetParent(self)
		textLine.SetFontName(font_size)
		textLine.SetPackedFontColor(font_color)
		textLine.SetText(text)
		textLine.Show()

		if not pos_x and not pos_y :
			textLine.SetPosition(self.GetWidth()/2, self.GetHeight()/2)
		else :
			textLine.SetPosition(pos_x, pos_y)

		textLine.SetVerticalAlignCenter()
		if "center" == text_sort :
			textLine.SetHorizontalAlignCenter()
		elif "right" == text_sort :
			textLine.SetHorizontalAlignRight()
		elif "left" == 	text_sort :
			textLine.SetHorizontalAlignLeft()
			
		self.TextChild.append(textLine)

class StateButton(Button):

	STATE_CLOSED = 0
	STATE_OPEN = 1

	def __init__(self):
		Button.__init__(self)

		self.state = self.STATE_CLOSED

		self.fileNames = {}

	def __GetFileNames(self, state):
		if not self.fileNames.has_key(state):
			self.fileNames[state] = {}

		return self.fileNames[state]

	def SetUpVisual(self, state, filename):
		self.__GetFileNames(state)["UP"] = filename
		if state == self.state:
			self.__RefreshVisual("UP")

	def SetOverVisual(self, state, filename):
		self.__GetFileNames(state)["OVER"] = filename
		if state == self.state:
			self.__RefreshVisual("OVER")

	def SetDownVisual(self, state, filename):
		self.__GetFileNames(state)["DOWN"] = filename
		if state == self.state:
			self.__RefreshVisual("DOWN")

	def SetDisableVisual(self, state, filename):
		self.__GetFileNames(state)["DISABLE"] = filename
		if state == self.state:
			self.__RefreshVisual("DISABLE")

	def SetStateOpen(self):
		self.SetState(self.STATE_OPEN)

	def SetStateClosed(self):
		self.SetState(self.STATE_CLOSED)

	def SetState(self, state):
		if self.state == state:
			return

		self.state = state

		self.__RefreshVisual("UP")
		self.__RefreshVisual("OVER")
		self.__RefreshVisual("DOWN")
		self.__RefreshVisual("DISABLE")

	def GetState(self):
		return self.state

	def __RefreshVisual(self, name):
		if not self.fileNames.has_key(self.state):
			return
		if not self.fileNames[self.state].has_key(name):
			if name != "UP" and self.fileNames[self.state].has_key("UP"):
				self.fileNames[self.state][name] = self.fileNames[self.state]["UP"]

		if name == "UP":
			Button.SetUpVisual(self, self.fileNames[self.state][name])
		elif name == "OVER":
			Button.SetOverVisual(self, self.fileNames[self.state][name])
		elif name == "DOWN":
			Button.SetDownVisual(self, self.fileNames[self.state][name])
		elif name == "DISABLE":
			Button.SetDisableVisual(self, self.fileNames[self.state][name])

class RadioButton(Button):
	def __init__(self):
		Button.__init__(self)

	def __del__(self):
		Button.__del__(self)

	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.RegisterRadioButton(self, layer)

class ToggleButton(Button):
	def __init__(self):
		Button.__init__(self)

		self.eventUp = None
		self.argsUp = None
		self.eventDown = None
		self.argsDown = None
		self.state = 0

	def __del__(self):
		Button.__del__(self)

		self.eventUp = None
		self.eventDown = None

	def SetToggleUpEvent(self, event, *args):
		self.eventUp = event
		self.argsUp = args

	def SetToggleDownEvent(self, event, *args):
		self.eventDown = event
		self.argsDown = args

	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.RegisterToggleButton(self, layer)

	def GetState(self):
		return self.state

	def OnToggleUp(self):
		if self.eventUp:
			self.state = 1
			apply(self.eventUp, self.argsUp)

	def OnToggleDown(self):
		if self.eventDown:
			self.state = 0
			apply(self.eventDown, self.argsDown)

class DragButton(Button):
	def __init__(self):
		Button.__init__(self)
		self.AddFlag("movable")

		self.callbackEnable = True
		self.eventMove = lambda: None

	def __del__(self):
		Button.__del__(self)

		self.eventMove = lambda: None

	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.RegisterDragButton(self, layer)

	def SetMoveEvent(self, event):
		self.eventMove = event

	def SetRestrictMovementArea(self, x, y, width, height):
		wndMgr.SetRestrictMovementArea(self.hWnd, x, y, width, height)

	def TurnOnCallBack(self):
		self.callbackEnable = True

	def TurnOffCallBack(self):
		self.callbackEnable = False

	def OnMove(self):
		if self.callbackEnable:
			self.eventMove()

class NumberLine(Window):

	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)

	def __del__(self):
		Window.__del__(self)

	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.RegisterNumberLine(self, layer)

	def SetHorizontalAlignCenter(self):
		wndMgr.SetNumberHorizontalAlignCenter(self.hWnd)

	def SetHorizontalAlignRight(self):
		wndMgr.SetNumberHorizontalAlignRight(self.hWnd)

	def SetPath(self, path):
		wndMgr.SetPath(self.hWnd, path)

	def SetNumber(self, number):
		wndMgr.SetNumber(self.hWnd, number)

###################################################################################################
## PythonScript Element
###################################################################################################

class Box(Window):

	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.RegisterBox(self, layer)

	def SetColor(self, color):
		wndMgr.SetColor(self.hWnd, color)

class Bar(Window):

	def __init__(self, layer = "UI"):
		Window.__init__(self)
		self.eventFunc = None
		self.eventArgs = None
		self.eventDict={"MOUSE_OVER_IN":[0,0],"MOUSE_OVER_OUT":[0,0],}
		self.RegisterWindow(layer)

	def __del__(self):
		Window.__del__(self)
		self.eventFunc = None
		self.eventArgs = None
		self.eventDict={"MOUSE_OVER_IN":[0,0],"MOUSE_OVER_OUT":[0,0],}

	def OnMouseOverIn(self):
		try:
			if self.eventDict["MOUSE_OVER_IN"][0] != 0 and self.eventDict["MOUSE_OVER_IN"][1] != 0:
				apply(self.eventDict["MOUSE_OVER_IN"][0], self.eventDict["MOUSE_OVER_IN"][1])
		except KeyError:
			pass

	def OnMouseOverOut(self):
		try:
			if self.eventDict["MOUSE_OVER_OUT"][0] != 0 and self.eventDict["MOUSE_OVER_OUT"][1] != 0:
				apply(self.eventDict["MOUSE_OVER_OUT"][0], self.eventDict["MOUSE_OVER_OUT"][1])
		except KeyError:
			pass

	def SAFE_SetStringEvent(self, event, func, *args):
		self.eventDict[event][0]=__mem_func__(func)
		self.eventDict[event][1] = args

	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.RegisterBar(self, layer)

	def SAFE_SetEvent(self, func, *args):
		self.eventFunc = __mem_func__(func)
		self.eventArgs = args

	def SetEvent(self, func, *args):
		self.eventFunc = func
		self.eventArgs = args
	
	def CallEvent(self):
		snd.PlaySound("sound/ui/click.wav")

		if self.eventFunc:
			apply(self.eventFunc, self.eventArgs)

	def SetColor(self, color):
		wndMgr.SetColor(self.hWnd, color)

class Line(Window):

	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.RegisterLine(self, layer)

	def SetColor(self, color):
		wndMgr.SetColor(self.hWnd, color)

class SlotBar(Window):

	def __init__(self):
		Window.__init__(self)

	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.RegisterBar3D(self, layer)

## Same with SlotBar
class Bar3D(Window):

	def __init__(self):
		Window.__init__(self)

	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.RegisterBar3D(self, layer)

	def SetColor(self, left, right, center):
		wndMgr.SetColor(self.hWnd, left, right, center)

class SlotWindow(Window):

	def __init__(self):
		Window.__init__(self)

		self.StartIndex = 0

		self.eventSelectEmptySlot = None
		self.eventSelectItemSlot = None
		self.eventUnselectEmptySlot = None
		self.eventUnselectItemSlot = None
		self.eventUseSlot = None
		self.eventOverInItem = None
		self.eventOverOutItem = None
		self.eventPressedSlotButton = None

		if app.AHMET_FISH_EVENT_SYSTEM:
			self.eventSelectEmptySlotWindow = None
			self.eventSelectItemSlotWindow = None
			self.eventUnselectItemSlotWindow = None
			self.eventOverInItemWindow = None	

	def __del__(self):
		Window.__del__(self)

		self.eventSelectEmptySlot = None
		self.eventSelectItemSlot = None
		self.eventUnselectEmptySlot = None
		self.eventUnselectItemSlot = None
		self.eventUseSlot = None
		self.eventOverInItem = None
		self.eventOverOutItem = None
		self.eventPressedSlotButton = None

		if app.AHMET_FISH_EVENT_SYSTEM:
			self.eventSelectEmptySlotWindow = None
			self.eventSelectItemSlotWindow = None
			self.eventUnselectItemSlotWindow = None
			self.eventOverInItemWindow = None	

	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.RegisterSlotWindow(self, layer)

	def SetSlotStyle(self, style):
		wndMgr.SetSlotStyle(self.hWnd, style)

	def HasSlot(self, slotIndex):
		return wndMgr.HasSlot(self.hWnd, slotIndex)

	def SetSlotBaseImage(self, imageFileName, r = 1.0, g = 1.0, b = 1.0, a = 1.0):
		wndMgr.SetSlotBaseImage(self.hWnd, imageFileName, r, g, b, a)

	def SetCoverButton(self,\
						slotIndex,\
						upName="d:/ymir work/ui/public/slot_cover_button_01.sub",\
						overName="d:/ymir work/ui/public/slot_cover_button_02.sub",\
						downName="d:/ymir work/ui/public/slot_cover_button_03.sub",\
						disableName="d:/ymir work/ui/public/slot_cover_button_04.sub",\
						LeftButtonEnable = False,\
						RightButtonEnable = True):
		wndMgr.SetCoverButton(self.hWnd, slotIndex, upName, overName, downName, disableName, LeftButtonEnable, RightButtonEnable)

	def SetAlwaysRenderCoverButton(self, slotIndex, bAlwaysRender = True):
		wndMgr.SetAlwaysRenderCoverButton(self.hWnd, slotIndex, bAlwaysRender)

	def EnableCoverButton(self, slotIndex):
		wndMgr.EnableCoverButton(self.hWnd, slotIndex)

	def DisableCoverButton(self, slotIndex):
		wndMgr.DisableCoverButton(self.hWnd, slotIndex)

	if app.AHMET_FISH_EVENT_SYSTEM:
		def DeleteCoverButton(self, slotIndex):
			wndMgr.DeleteCoverButton(self.hWnd, slotIndex)		

	def AppendSlotButton(self, upName, overName, downName):
		wndMgr.AppendSlotButton(self.hWnd, upName, overName, downName)

	def ShowSlotButton(self, slotNumber):
		wndMgr.ShowSlotButton(self.hWnd, slotNumber)

	def HideAllSlotButton(self):
		wndMgr.HideAllSlotButton(self.hWnd)

	def AppendRequirementSignImage(self, filename):
		wndMgr.AppendRequirementSignImage(self.hWnd, filename)

	def ShowRequirementSign(self, slotNumber):
		wndMgr.ShowRequirementSign(self.hWnd, slotNumber)

	def HideRequirementSign(self, slotNumber):
		wndMgr.HideRequirementSign(self.hWnd, slotNumber)

	def ActivateSlot(self, slotNumber, colorType = -1):
		if colorType != -1:
			wndMgr.SetSlotDiffuseColor(self.hWnd, slotNumber, colorType)

		wndMgr.ActivateSlot(self.hWnd, slotNumber)

	def DeactivateSlot(self, slotNumber):
		wndMgr.DeactivateSlot(self.hWnd, slotNumber)

	def ShowSlotBaseImage(self, slotNumber):
		wndMgr.ShowSlotBaseImage(self.hWnd, slotNumber)

	def HideSlotBaseImage(self, slotNumber):
		wndMgr.HideSlotBaseImage(self.hWnd, slotNumber)

	def SAFE_SetButtonEvent(self, button, state, event):
		if "LEFT"==button:
			if "EMPTY"==state:
				self.eventSelectEmptySlot=__mem_func__(event)
			elif "EXIST"==state:
				self.eventSelectItemSlot=__mem_func__(event)
			elif "ALWAYS"==state:
				self.eventSelectEmptySlot=__mem_func__(event)
				self.eventSelectItemSlot=__mem_func__(event)
		elif "RIGHT"==button:
			if "EMPTY"==state:
				self.eventUnselectEmptySlot=__mem_func__(event)
			elif "EXIST"==state:
				self.eventUnselectItemSlot=__mem_func__(event)
			elif "ALWAYS"==state:
				self.eventUnselectEmptySlot=__mem_func__(event)
				self.eventUnselectItemSlot=__mem_func__(event)

	if app.AHMET_FISH_EVENT_SYSTEM:
		def SetSelectEmptySlotEvent(self, empty, window = None):
			self.eventSelectEmptySlot = empty
			self.eventSelectEmptySlotWindow = window
	
		def SetSelectItemSlotEvent(self, item, window = None):
			self.eventSelectItemSlot = item
			self.eventSelectItemSlotWindow = window
	else:
		def SetSelectEmptySlotEvent(self, empty):
			self.eventSelectEmptySlot = empty

		def SetSelectItemSlotEvent(self, item):
			self.eventSelectItemSlot = item

	def SetUnselectEmptySlotEvent(self, empty):
		self.eventUnselectEmptySlot = empty

	if app.AHMET_FISH_EVENT_SYSTEM:
		def SetUnselectItemSlotEvent(self, item, window = None):
			self.eventUnselectItemSlot = item
			self.eventUnselectItemSlotWindow = window
	else:
		def SetUnselectItemSlotEvent(self, item):
			self.eventUnselectItemSlot = item

	def IsEmptySlot(self, slot):
		return wndMgr.IsEmptySlot(self.hWnd, slot)

	def SetUseSlotEvent(self, use):
		self.eventUseSlot = use

	if app.AHMET_FISH_EVENT_SYSTEM:
		def SetOverInItemEvent(self, event, window = None):
			self.eventOverInItem = event
			self.eventOverInItemWindow = window
	else:
		def SetOverInItemEvent(self, event):
			self.eventOverInItem = event

	def SetOverOutItemEvent(self, event):
		self.eventOverOutItem = event

	def SetPressedSlotButtonEvent(self, event):
		self.eventPressedSlotButton = event

	def GetSlotCount(self):
		return wndMgr.GetSlotCount(self.hWnd)

	def SetUseMode(self, flag):
		wndMgr.SetUseMode(self.hWnd, flag)

	def SetUsableItem(self, flag): 
		wndMgr.SetUsableItem(self.hWnd, flag)

	# ENABLE_ITEM_SWAP_SYSTEM
	def SetUsableItem2(self, flag):
		wndMgr.SetUsableItem2(self.hWnd, flag)
	# ENABLE_ITEM_SWAP_SYSTEM

	## Slot
	def SetSlotCoolTime(self, slotIndex, coolTime, elapsedTime = 0.0):
		wndMgr.SetSlotCoolTime(self.hWnd, slotIndex, coolTime, elapsedTime)

	def DisableSlot(self, slotIndex):
		wndMgr.DisableSlot(self.hWnd, slotIndex)

	def EnableSlot(self, slotIndex):
		wndMgr.EnableSlot(self.hWnd, slotIndex)

	def SetUnusableSlot(self, slotIndex, flag = True):
		wndMgr.SetUnusableSlot(self.hWnd, slotIndex, flag)
		
	def SetUnusableSlotWorld(self, slotIndex, flag = True):
		wndMgr.SetUnusableSlotWorld(self.hWnd, slotIndex, flag)

	def LockSlot(self, slotIndex):
		wndMgr.LockSlot(self.hWnd, slotIndex)

	def UnlockSlot(self, slotIndex):
		wndMgr.UnlockSlot(self.hWnd, slotIndex)

	def RefreshSlot(self):
		wndMgr.RefreshSlot(self.hWnd)

	def ClearSlot(self, slotNumber):
		wndMgr.ClearSlot(self.hWnd, slotNumber)

	def ClearAllSlot(self):
		wndMgr.ClearAllSlot(self.hWnd)

	def GetSlotPosition(self, slotNumber):
		left, top = wndMgr.GetSlotPosition(self.hWnd, slotNumber)
		return (left, top)

	def AppendSlot(self, index, x, y, width, height):
		wndMgr.AppendSlot(self.hWnd, index, x, y, width, height)

	def SetSlot(self, slotIndex, itemIndex, width, height, icon, diffuseColor = (1.0, 1.0, 1.0, 1.0)):
		wndMgr.SetSlot(self.hWnd, slotIndex, itemIndex, width, height, icon, diffuseColor)

	def SetSlotCount(self, slotNumber, count):
		wndMgr.SetSlotCount(self.hWnd, slotNumber, count)

	def SetSlotCountNew(self, slotNumber, grade, count):
		wndMgr.SetSlotCountNew(self.hWnd, slotNumber, grade, count)

	def SetCardSlot(self, renderingSlotNumber, CardIndex, cardIcon, diffuseColor = (1.0, 1.0, 1.0, 1.0)):
		CardIndex = 1000
		if 0 == CardIndex or None == CardIndex:
			wndMgr.ClearSlot(self.hWnd, renderingSlotNumber)
			return

		item.SelectItem(1, 2, CardIndex)
		(width, height) = item.GetItemSize(1,2,3)
     
		wndMgr.SetCardSlot(self.hWnd, renderingSlotNumber, CardIndex, width, height, cardIcon, diffuseColor)

	def SetItemSlot(self, renderingSlotNumber, ItemIndex, ItemCount = 0, metinSlot = []):

		if 0 == ItemIndex or None == ItemIndex:
			wndMgr.ClearSlot(self.hWnd, renderingSlotNumber)
			return

		item.SelectItem(1, 2, ItemIndex)

		if ItemIndex == 95310:
			allSocketsEmpty = True
			if len(metinSlot) == player.METIN_SOCKET_MAX_NUM:
				for socket in metinSlot:
					if socket >= 95300 and socket <= 95309:
						allSocketsEmpty = False
						break
			if not allSocketsEmpty:
				item.SelectItem(1, 2, 95311) # select only for image pointer

		itemIcon = item.GetIconImage()
		(width, height) = item.GetItemSize()

		wndMgr.SetSlot(self.hWnd, renderingSlotNumber, ItemIndex, width, height, itemIcon)

		wndMgr.SetSlotCount(self.hWnd, renderingSlotNumber, ItemCount)

	def SetSkillSlot(self, renderingSlotNumber, skillIndex, skillLevel):

		skillIcon = skill.GetIconImage(skillIndex)

		if 0 == skillIcon:
			wndMgr.ClearSlot(self.hWnd, renderingSlotNumber)
			return

		wndMgr.SetSlot(self.hWnd, renderingSlotNumber, skillIndex, 1, 1, skillIcon)
		wndMgr.SetSlotCount(self.hWnd, renderingSlotNumber, skillLevel)

	def SetSkillSlotNew(self, renderingSlotNumber, skillIndex, skillGrade, skillLevel):
		
		skillIcon = skill.GetIconImageNew(skillIndex, skillGrade)
		# tchat("GetSkillIcon(%d, %d) : %d" % (skillIndex, skillGrade, skillIcon))

		if 0 == skillIcon:
			wndMgr.ClearSlot(self.hWnd, renderingSlotNumber)
			return

		wndMgr.SetSlot(self.hWnd, renderingSlotNumber, skillIndex, 1, 1, skillIcon)

	def SetEmotionSlot(self, renderingSlotNumber, emotionIndex):
		icon = player.GetEmotionIconImage(emotionIndex)

		if 0 == icon:
			wndMgr.ClearSlot(self.hWnd, renderingSlotNumber)
			return

		wndMgr.SetSlot(self.hWnd, renderingSlotNumber, emotionIndex, 1, 1, icon)

	## Event
	if app.AHMET_FISH_EVENT_SYSTEM:
		def OnSelectEmptySlot(self, slotNumber):
			if self.eventSelectEmptySlot:
				if self.eventSelectEmptySlotWindow:
					self.eventSelectEmptySlot(slotNumber, self.eventSelectEmptySlotWindow)
				else:
					self.eventSelectEmptySlot(slotNumber)

		def OnSelectItemSlot(self, slotNumber):
			if self.eventSelectItemSlot:
				if self.eventSelectItemSlotWindow:
					self.eventSelectItemSlot(slotNumber, self.eventSelectItemSlotWindow)
				else:
					self.eventSelectItemSlot(slotNumber)
	else:
		def OnSelectEmptySlot(self, slotNumber):
			if self.eventSelectEmptySlot:
				self.eventSelectEmptySlot(slotNumber)

		def OnSelectItemSlot(self, slotNumber):
			if self.eventSelectItemSlot:
				self.eventSelectItemSlot(slotNumber)

	def OnUnselectEmptySlot(self, slotNumber):
		if self.eventUnselectEmptySlot:
			self.eventUnselectEmptySlot(slotNumber)

	if app.AHMET_FISH_EVENT_SYSTEM:
		def OnUnselectItemSlot(self, slotNumber):
			if self.eventUnselectItemSlot:
				if self.eventUnselectItemSlotWindow:
					self.eventUnselectItemSlot(slotNumber, self.eventUnselectItemSlotWindow)
				else:
					self.eventUnselectItemSlot(slotNumber)
	else:
		def OnUnselectItemSlot(self, slotNumber):
			if self.eventUnselectItemSlot:
				self.eventUnselectItemSlot(slotNumber)

	def OnUseSlot(self, slotNumber):
		if self.eventUseSlot:
			self.eventUseSlot(slotNumber)

	if app.AHMET_FISH_EVENT_SYSTEM:
		def OnOverInItem(self, slotNumber):
			if self.eventOverInItem:
				if self.eventOverInItemWindow:
					self.eventOverInItem(slotNumber, self.eventOverInItemWindow)
				else:
					self.eventOverInItem(slotNumber)
	else:
		def OnOverInItem(self, slotNumber):
			if self.eventOverInItem:
				self.eventOverInItem(slotNumber)

	def OnOverOutItem(self):
		if self.eventOverOutItem:
			self.eventOverOutItem()

	def OnPressedSlotButton(self, slotNumber):
		if self.eventPressedSlotButton:
			self.eventPressedSlotButton(slotNumber)

	def GetStartIndex(self):
		return 0

class SlotBackground(Window):

	CORNER_WIDTH = 4
	CORNER_HEIGHT = 4
	LINE_WIDTH = 6
	LINE_HEIGHT = 6
	BASE_SIZE = 6

	LT = 0
	LB = 1
	RT = 2
	RB = 3
	L = 0
	R = 1
	T = 2
	B = 3

	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)

		self.isShowBottomCorner = True
		self.eventFunc = None
		self.eventArgs = None

		CornerFileNames = [ "d:/ymir work/ui/public/slot_bg_"+dir+".sub" for dir in ["LeftTop","LeftBottom","RightTop","RightBottom"] ]
		LineFileNames = [ "d:/ymir work/ui/pattern/slot_bg_"+dir+".tga" for dir in ["Left","Right","Top","Bottom"] ]

		self.Corners = []
		for fileName in CornerFileNames:
			Corner = ExpandedImageBox()
			Corner.AddFlag("attach")
			Corner.AddFlag("not_pick")
			Corner.LoadImage(fileName)
			Corner.SetParent(self)
			Corner.SetPosition(0, 0)
			Corner.Show()
			self.Corners.append(Corner)

		self.Lines = []
		for fileName in LineFileNames:
			Line = ExpandedImageBox()
			Line.AddFlag("attach")
			Line.AddFlag("not_pick")
			Line.LoadImage(fileName)
			Line.SetParent(self)
			Line.SetPosition(0, 0)
			Line.Show()
			self.Lines.append(Line)

		Base = ExpandedImageBox()
		Base.AddFlag("attach")
		Base.AddFlag("not_pick")
		Base.LoadImage("d:/ymir work/ui/pattern/slot_bg_base.tga")
		Base.SetParent(self)
		Base.SetPosition(self.CORNER_WIDTH, self.CORNER_HEIGHT)
		Base.Show()
		self.Base = Base

		self.Lines[self.L].SetPosition(0, self.CORNER_HEIGHT)
		self.Lines[self.T].SetPosition(self.CORNER_WIDTH, 0)

		self.isButtonStyle = False
		self.isDown = False
		self.renderData = {}

		self.SetWindowName("NONAME_SlotBackground")

	def __del__(self):
		Window.__del__(self)

	def ShowBottomCorner(self):
		self.Corners[self.LB].Show()
		self.Corners[self.RB].Show()
		self.Lines[self.B].Show()
		self.isShowBottomCorner = True
		self.SetSize(self.GetWidth(), self.GetHeight())

	def HideBottomCorner(self):
		self.Corners[self.LB].Hide()
		self.Corners[self.RB].Hide()
		self.Lines[self.B].Hide()
		self.isShowBottomCorner = False
		self.SetSize(self.GetWidth(), self.GetHeight())

	def SetSize(self, width, height):

		width = max(self.CORNER_WIDTH*2, width)
		height = max(self.CORNER_HEIGHT*2, height)
		Window.SetSize(self, width, height)

		self.Corners[self.LB].SetPosition(0, height - self.CORNER_HEIGHT)
		self.Corners[self.RT].SetPosition(width - self.CORNER_WIDTH, 0)
		self.Corners[self.RB].SetPosition(width - self.CORNER_WIDTH, height - self.CORNER_HEIGHT)
		self.Lines[self.R].SetPosition(width - self.CORNER_WIDTH, self.CORNER_HEIGHT)
		self.Lines[self.B].SetPosition(self.CORNER_WIDTH, height - self.CORNER_HEIGHT)

		if self.isShowBottomCorner:
			verticalShowingPercentage = float((height - self.CORNER_HEIGHT*2) - self.LINE_HEIGHT) / self.LINE_HEIGHT
		else:
			verticalShowingPercentage = float((height - self.CORNER_HEIGHT) - self.LINE_HEIGHT) / self.LINE_HEIGHT
		horizontalShowingPercentage = float((width - self.CORNER_WIDTH*2) - self.LINE_WIDTH) / self.LINE_WIDTH
		self.Lines[self.L].SetRenderingRect(0, 0, 0, verticalShowingPercentage)
		self.Lines[self.R].SetRenderingRect(0, 0, 0, verticalShowingPercentage)
		self.Lines[self.T].SetRenderingRect(0, 0, horizontalShowingPercentage, 0)
		self.Lines[self.B].SetRenderingRect(0, 0, horizontalShowingPercentage, 0)

		if self.isShowBottomCorner:
			verticalShowingPercentage = float((height - self.CORNER_HEIGHT*2) - self.BASE_SIZE) / self.BASE_SIZE
		else:
			verticalShowingPercentage = float((height - self.CORNER_HEIGHT) - self.BASE_SIZE) / self.BASE_SIZE
		horizontalShowingPercentage = float((width - self.CORNER_WIDTH*2) - self.BASE_SIZE) / self.BASE_SIZE
		self.Base.SetRenderingRect(0, 0, horizontalShowingPercentage, verticalShowingPercentage)

	def ShowInternal(self):
		self.Base.Show()
		for wnd in self.Lines:
			wnd.Show()
		for wnd in self.Corners:
			wnd.Show()

	def HideInternal(self):
		self.Base.Hide()
		for wnd in self.Lines:
			wnd.Hide()
		for wnd in self.Corners:
			wnd.Hide()

	def SAFE_SetEvent(self, event, *args):
		self.eventFunc = __mem_func__(event)
		self.eventArgs = args

	def OnMouseLeftButtonDown(self):
		self.isDown = True
		if self.isButtonStyle:
			self.__SetRenderData("color", SELECT_COLOR)

	def OnMouseLeftButtonUp(self):
		self.isDown = False
		self.__ResetRenderData()

		if self.IsIn():
			if self.isButtonStyle:
				self.__SetRenderData("color", HALF_WHITE_COLOR)
			if self.eventFunc:
				apply(self.eventFunc, self.eventArgs)

	def OnMouseOverIn(self):
		if self.isButtonStyle:
			if self.isDown == False:
				self.__SetRenderData("color", HALF_WHITE_COLOR)
			else:
				self.__SetRenderData("color", SELECT_COLOR)

	def OnMouseOverOut(self):
		if self.isButtonStyle:
			if self.isDown == False:
				self.__ResetRenderData()

	def SetButtonStyle(self, isButtonStyle):
		self.isButtonStyle = isButtonStyle

		if self.isButtonStyle == False:
			self.__ResetRenderData()

	def __ResetRenderData(self):
		self.renderData = {"render" : False}

	def __SetRenderData(self, key, val):
		self.renderData["render"] = True
		self.renderData[key] = val

	def __GetRenderData(self, key):
		return self.renderData.get(key, False)

	def OnRenderFinish(self):
		if not self.__GetRenderData("render"):
			return

		x, y, width, height = self.GetRect()
		grp.SetColor(self.__GetRenderData("color"))
		grp.RenderBar(x, y, width, height)

class GridSlotWindow(SlotWindow):

	def __init__(self):
		SlotWindow.__init__(self)

		self.startIndex = 0

	def __del__(self):
		SlotWindow.__del__(self)

	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.RegisterGridSlotWindow(self, layer)

	def ArrangeSlot(self, StartIndex, xCount, yCount, xSize, ySize, xBlank, yBlank):

		self.startIndex = StartIndex

		wndMgr.ArrangeSlot(self.hWnd, StartIndex, xCount, yCount, xSize, ySize, xBlank, yBlank)
		self.startIndex = StartIndex

	if app.AHMET_FISH_EVENT_SYSTEM:
		def SetPickedAreaRender(self, flag):
			wndMgr.SetPickedAreaRender(self.hWnd, flag)

	def GetStartIndex(self):
		return self.startIndex

class TitleBar(Window):

	BLOCK_WIDTH = 32
	if app.GetSelectedDesignName() != "illumina":
		BLOCK_HEIGHT = 23
	else:
		BLOCK_HEIGHT = 32

	def __init__(self):
		Window.__init__(self)
		self.AddFlag("attach")

	def __del__(self):
		Window.__del__(self)

	def MakeTitleBar(self, width, color):
		width = max(64, width)

		imgDeco = ImageBox()
		imgLeft = ImageBox()
		imgCenter = ExpandedImageBox()
		imgRight = ImageBox()
		imgDeco.AddFlag("not_pick")
		imgLeft.AddFlag("not_pick")
		imgCenter.AddFlag("not_pick")
		imgRight.AddFlag("not_pick")
		imgLeft.SetParent(self)
		imgCenter.SetParent(self)
		imgRight.SetParent(self)
		imgDeco.SetParent(imgRight)

		if app.GetSelectedDesignName() != "illumina":
			imgLeft.LoadImage("d:/ymir work/ui/pattern/titlebar_left.tga")
			imgCenter.LoadImage("d:/ymir work/ui/pattern/titlebar_center.tga")
			imgRight.LoadImage("d:/ymir work/ui/pattern/titlebar_right.tga")
		else:
			imgDeco.LoadImage("d:/ymir work/ui/controls/titlebar/decoration_right.tga")
			imgLeft.LoadImage("d:/ymir work/ui/controls/titlebar/left.tga")
			imgCenter.LoadImage("d:/ymir work/ui/controls/titlebar/center.tga")
			imgRight.LoadImage("d:/ymir work/ui/controls/titlebar/right.tga")

			imgDeco.Show()

		imgLeft.Show()
		imgCenter.Show()
		imgRight.Show()

		btnClose = Button()
		if app.GetSelectedDesignName() != "illumina":
			btnClose.SetParent(self)
			btnClose.SetUpVisual("d:/ymir work/ui/public/close_button_01.sub")
			btnClose.SetOverVisual("d:/ymir work/ui/public/close_button_02.sub")
			btnClose.SetDownVisual("d:/ymir work/ui/public/close_button_03.sub")
		else:
			btnClose.SetParent(imgDeco)
			btnClose.SetUpVisual("d:/ymir work/ui/controls/titlebar/board_close_01_normal.tga")
			btnClose.SetOverVisual("d:/ymir work/ui/controls/titlebar/board_close_02_hover.tga")
			btnClose.SetDownVisual("d:/ymir work/ui/controls/titlebar/board_close_03_active.tga")
		btnClose.SetToolTipText(localeInfo.UI_CLOSE, 0, -23)
		btnClose.Show()

		self.imgDeco = imgDeco
		self.imgLeft = imgLeft
		self.imgCenter = imgCenter
		self.imgRight = imgRight
		self.btnClose = btnClose

		self.SetWidth(width)

	def SetWidth(self, width):
		self.imgCenter.SetRenderingRect(0.0, 0.0, float((width - self.BLOCK_WIDTH*2) - self.BLOCK_WIDTH) / self.BLOCK_WIDTH, 0.0)
		self.imgCenter.SetPosition(self.BLOCK_WIDTH, 0)
		self.imgRight.SetPosition(width - self.BLOCK_WIDTH, 0)
		self.imgDeco.SetPosition(-18,-19)
		if app.GetSelectedDesignName() != "illumina":
			self.btnClose.SetPosition(width - self.btnClose.GetWidth() - 3, 3)
		else:
			self.btnClose.SetPosition(21,18)
		self.SetSize(width, self.BLOCK_HEIGHT)

	def SetCloseEvent(self, event):
		self.btnClose.SetEvent(event)

class HorizontalBar(Window):

	BLOCK_WIDTH = 32
	BLOCK_HEIGHT = 17

	def __init__(self):
		Window.__init__(self)
		self.AddFlag("attach")

	def __del__(self):
		Window.__del__(self)

	def Create(self, width):

		width = max(96, width)

		imgLeft = ImageBox()
		imgLeft.SetParent(self)
		imgLeft.AddFlag("not_pick")
		imgLeft.LoadImage("d:/ymir work/ui/pattern/horizontalbar_left.tga")
		imgLeft.Show()

		imgCenter = ExpandedImageBox()
		imgCenter.SetParent(self)
		imgCenter.AddFlag("not_pick")
		imgCenter.LoadImage("d:/ymir work/ui/pattern/horizontalbar_center.tga")
		imgCenter.Show()

		imgRight = ImageBox()
		imgRight.SetParent(self)
		imgRight.AddFlag("not_pick")
		imgRight.LoadImage("d:/ymir work/ui/pattern/horizontalbar_right.tga")
		imgRight.Show()

		self.imgLeft = imgLeft
		self.imgCenter = imgCenter
		self.imgRight = imgRight
		self.SetWidth(width)

	def SetWidth(self, width):
		self.imgCenter.SetRenderingRect(0.0, 0.0, float((width - self.BLOCK_WIDTH*2) - self.BLOCK_WIDTH) / self.BLOCK_WIDTH, 0.0)
		self.imgCenter.SetPosition(self.BLOCK_WIDTH, 0)
		self.imgRight.SetPosition(width - self.BLOCK_WIDTH, 0)
		self.SetSize(width, self.BLOCK_HEIGHT)

class Gauge(Window):

	SLOT_WIDTH = 16
	SLOT_HEIGHT = 7

	GAUGE_TEMPORARY_PLACE = 12
	GAUGE_WIDTH = 16

	def __init__(self):
		Window.__init__(self)
		self.width = 0
	def __del__(self):
		Window.__del__(self)

	def MakeGauge(self, width, color):

		self.width = max(48, width)

		imgSlotLeft = ImageBox()
		imgSlotLeft.SetParent(self)
		imgSlotLeft.LoadImage("d:/ymir work/ui/pattern/gauge_slot_left.tga")
		imgSlotLeft.Show()

		imgSlotRight = ImageBox()
		imgSlotRight.SetParent(self)
		imgSlotRight.LoadImage("d:/ymir work/ui/pattern/gauge_slot_right.tga")
		imgSlotRight.Show()
		imgSlotRight.SetPosition(width - self.SLOT_WIDTH, 0)

		imgSlotCenter = ExpandedImageBox()
		imgSlotCenter.SetParent(self)
		imgSlotCenter.LoadImage("d:/ymir work/ui/pattern/gauge_slot_center.tga")
		imgSlotCenter.Show()
		imgSlotCenter.SetRenderingRect(0.0, 0.0, float((width - self.SLOT_WIDTH*2) - self.SLOT_WIDTH) / self.SLOT_WIDTH, 0.0)
		imgSlotCenter.SetPosition(self.SLOT_WIDTH, 0)

		imgGauge = ExpandedImageBox()
		imgGauge.SetParent(self)
		imgGauge.LoadImage("d:/ymir work/ui/pattern/gauge_" + color + ".tga")
		imgGauge.Show()
		imgGauge.SetRenderingRect(0.0, 0.0, 0.0, 0.0)
		imgGauge.SetPosition(self.GAUGE_TEMPORARY_PLACE, 0)

		imgSlotLeft.AddFlag("attach")
		imgSlotCenter.AddFlag("attach")
		imgSlotRight.AddFlag("attach")

		self.imgLeft = imgSlotLeft
		self.imgCenter = imgSlotCenter
		self.imgRight = imgSlotRight
		self.imgGauge = imgGauge
		self.currValue = 100
		self.maxValue = 100

		self.SetSize(width, self.SLOT_HEIGHT)

	def SetPercentage(self, curValue, maxValue):
		self.currValue = curValue
		self.maxValue = maxValue
		# PERCENTAGE_MAX_VALUE_ZERO_DIVISION_ERROR
		if maxValue > 0.0:
			percentage = min(1.0, float(curValue)/float(maxValue))
		else:
			percentage = 0.0
		# END_OF_PERCENTAGE_MAX_VALUE_ZERO_DIVISION_ERROR

		gaugeSize = -1.0 + float(self.width - self.GAUGE_TEMPORARY_PLACE*2) * percentage / self.GAUGE_WIDTH
		self.imgGauge.SetRenderingRect(0.0, 0.0, gaugeSize, 0.0)

	def GetPercentage(self):
		return (self.currValue, self.maxValue,)

class BoardBase(Window):

		def __init__(self, padding = 0, onChangeSizeFunc = None):
			if padding == 0:
				self.PADDING = { self.L : 0, self.R : 0, self.T : 0, self.B : 0 }
			else:
				self.PADDING = padding

			self.parentWnd = Window()

			Window.__init__(self)
			Window.SetParent(self, self.parentWnd)
			Window.SetPosition(self, self.PADDING[self.L], self.PADDING[self.T])
			Window.AddFlag(self, "float")
			Window.Show(self)

			self.onChangeSizeFunc = onChangeSizeFunc

		def Destroy(self):
			self.parentWnd.Hide()
			self.parentWnd = None
			Window.Destroy(self)

		# parentWnd handler
		def SetParent(self, parent):
			self.parentWnd.SetParent(parent)

		def Show(self):
			self.parentWnd.Show()

		def Hide(self):
			self.parentWnd.Hide()

		def IsShow(self):
			return self.parentWnd.IsShow()

		def GetLeft(self):
			return self.parentWnd.GetLeft()

		def GetTop(self):
			return self.parentWnd.GetTop()

		def SetPosition(self, x, y):
			self.parentWnd.SetPosition(x, y)

		def GetLocalPosition(self):
			return self.parentWnd.GetLocalPosition()

		def GetGlobalPosition(self):
			return self.parentWnd.GetGlobalPosition()

		def AddFlag(self, style):
			self.parentWnd.AddFlag(style)

			if style == "movable" or style == "attach":
				Window.AddFlag(self, "attach")

		def SetAllAlpha(self, alpha):
			self.parentWnd.SetAllAlpha(alpha)

		def SetCenterPosition(self):
			self.parentWnd.SetCenterPosition()

		def IsIn(self, checkChilds = True):
			return self.parentWnd.IsIn(checkChilds)

		def SetTop(self):
			self.parentWnd.SetTop()
			Window.SetTop(self)
		# end of parentWnd handler

		def __del__(self):
			Window.__del__(self)

		def SetSize(self, width, height):
			width = max(self.CORNER_WIDTH*2 - self.PADDING[self.L] - self.PADDING[self.R], width)
			height = max(self.CORNER_HEIGHT*2 - self.PADDING[self.T] - self.PADDING[self.B], height)

			self.parentWnd.SetSize(width + self.PADDING[self.L] + self.PADDING[self.R], height + self.PADDING[self.T] + self.PADDING[self.B])
			Window.SetSize(self, width, height)

			if self.onChangeSizeFunc:
				self.onChangeSizeFunc(self.parentWnd.GetWidth(), self.parentWnd.GetHeight())

		def GetRealWidth(self):
			return self.parentWnd.GetWidth()

		def GetRealHeight(self):
			return self.parentWnd.GetHeight()

		def GetHeightPadding(self):
			return self.PADDING[self.T] + self.PADDING[self.B]

		def GetWidthPadding(self):
			return self.PADDING[self.T] + self.PADDING[self.B]

if app.GetSelectedDesignName() != "illumina":
	class Board(BoardBase):

		CORNER_WIDTH = 32
		CORNER_HEIGHT = 32
		LINE_WIDTH = 128
		LINE_HEIGHT = 128

		LT = 0
		LB = 1
		RT = 2
		RB = 3
		L = 0
		R = 1
		T = 2
		B = 3

		PADDING = {
			L : 8,
			R : 8,
			T : 7,
			B : 7,
		}

		MARGIN = {
			L : 3,
			R : 3,
			T : 3,
			B : 3,
		}

		def __init__(self, padding = PADDING):
			BoardBase.__init__(self, padding, __mem_func__(self.__OnChangeSize))

			self.MakeBoard("d:/ymir work/ui/pattern/Board_Corner_", "d:/ymir work/ui/pattern/Board_Line_")
			self.MakeBase()
			self.SetTop()

		def MakeBoard(self, cornerPath, linePath):

			CornerFileNames = [ cornerPath+dir+".tga" for dir in ("LeftTop", "LeftBottom", "RightTop", "RightBottom", ) ]
			LineFileNames = [ linePath+dir+".tga" for dir in ("Left", "Right", "Top", "Bottom", ) ]
			"""
			CornerFileNames = (
								"d:/ymir work/ui/pattern/Board_Corner_LeftTop.tga",
								"d:/ymir work/ui/pattern/Board_Corner_LeftBottom.tga",
								"d:/ymir work/ui/pattern/Board_Corner_RightTop.tga",
								"d:/ymir work/ui/pattern/Board_Corner_RightBottom.tga",
								)
			LineFileNames = (
								"d:/ymir work/ui/pattern/Board_Line_Left.tga",
								"d:/ymir work/ui/pattern/Board_Line_Right.tga",
								"d:/ymir work/ui/pattern/Board_Line_Top.tga",
								"d:/ymir work/ui/pattern/Board_Line_Bottom.tga",
								)
			"""

			self.Corners = []
			for fileName in CornerFileNames:
				Corner = ExpandedImageBox()
				Corner.AddFlag("not_pick")
				Corner.LoadImage(fileName)
				Corner.SetParent(self.parentWnd)
				Corner.SetPosition(0, 0)
				Corner.Show()
				self.Corners.append(Corner)

			self.Lines = []
			for fileName in LineFileNames:
				Line = ExpandedImageBox()
				Line.AddFlag("not_pick")
				Line.LoadImage(fileName)
				Line.SetParent(self.parentWnd)
				Line.SetPosition(0, 0)
				Line.Show()
				self.Lines.append(Line)

			self.Lines[self.L].SetPosition(0, self.CORNER_HEIGHT)
			self.Lines[self.T].SetPosition(self.CORNER_WIDTH, 0)

		def MakeBase(self):
			self.Base = ExpandedImageBox()
			self.Base.AddFlag("not_pick")
			self.Base.LoadImage("d:/ymir work/ui/pattern/Board_Base.tga")
			self.Base.SetParent(self.parentWnd)
			self.Base.SetPosition(self.CORNER_WIDTH, self.CORNER_HEIGHT)
			self.Base.Show()

		def __OnChangeSize(self, width, height):
			self.Corners[self.LB].SetPosition(0, height - self.CORNER_HEIGHT)
			self.Corners[self.RT].SetPosition(width - self.CORNER_WIDTH, 0)
			self.Corners[self.RB].SetPosition(width - self.CORNER_WIDTH, height - self.CORNER_HEIGHT)
			self.Lines[self.R].SetPosition(width - self.CORNER_WIDTH, self.CORNER_HEIGHT)
			self.Lines[self.B].SetPosition(self.CORNER_HEIGHT, height - self.CORNER_HEIGHT)

			verticalShowingPercentage = float((height - self.CORNER_HEIGHT*2) - self.LINE_HEIGHT) / self.LINE_HEIGHT
			horizontalShowingPercentage = float((width - self.CORNER_WIDTH*2) - self.LINE_WIDTH) / self.LINE_WIDTH
			self.Lines[self.L].SetRenderingRect(0, 0, 0, verticalShowingPercentage)
			self.Lines[self.R].SetRenderingRect(0, 0, 0, verticalShowingPercentage)
			self.Lines[self.T].SetRenderingRect(0, 0, horizontalShowingPercentage, 0)
			self.Lines[self.B].SetRenderingRect(0, 0, horizontalShowingPercentage, 0)

			if self.Base:
				self.Base.SetRenderingRect(0, 0, horizontalShowingPercentage, verticalShowingPercentage)

else:
	class Board(BoardBase):

		CORNER_WIDTH = 55
		CORNER_HEIGHT = 55
		LINE_WIDTH = 128
		LINE_HEIGHT = 128

		LT = 0
		LB = 1
		RT = 2
		RB = 3
		L = 0
		R = 1
		T = 2
		B = 3

		PADDING = {
			L : 14,
			R : 14,
			T : 14,
			B : 14,
		}

		MARGIN = {
			L : 8,
			R : 8,
			T : 8,
			B : 8,
		}

		def __init__(self, padding = PADDING):
			BoardBase.__init__(self, padding, __mem_func__(self.__OnChangeSize))

			self.MakeBoard("d:/ymir work/ui/controls/board/corner_", "d:/ymir work/ui/controls/board/bar_")
			self.MakeBase()
			self.SetTop()

		def MakeBoard(self, cornerPath, linePath):

			CornerFileNames = [ cornerPath+dir+".tga" for dir in ("LeftTop", "LeftBottom", "RightTop", "RightBottom", ) ]
			LineFileNames = [ linePath+dir+".tga" for dir in ("Left", "Right", "Top", "Bottom", ) ]
			"""
			CornerFileNames = (
								"d:/ymir work/ui/pattern/Board_Corner_LeftTop.tga",
								"d:/ymir work/ui/pattern/Board_Corner_LeftBottom.tga",
								"d:/ymir work/ui/pattern/Board_Corner_RightTop.tga",
								"d:/ymir work/ui/pattern/Board_Corner_RightBottom.tga",
								)
			LineFileNames = (
								"d:/ymir work/ui/pattern/Board_Line_Left.tga",
								"d:/ymir work/ui/pattern/Board_Line_Right.tga",
								"d:/ymir work/ui/pattern/Board_Line_Top.tga",
								"d:/ymir work/ui/pattern/Board_Line_Bottom.tga",
								)
			"""
			#############
			DecoCorner = ExpandedImageBox()
			DecoCorner.AddFlag("not_pick")
			DecoCorner.LoadImage("d:/ymir work/ui/controls/board/decoration_leftbottom.tga")
			DecoCorner.SetParent(self.parentWnd)
			DecoCorner.SetPosition(0, self.CORNER_HEIGHT)
			DecoCorner.Show()	
			self.DecoCorner = DecoCorner
				
			#############

			self.Corners = []
			for fileName in CornerFileNames:
				Corner = ExpandedImageBox()
				Corner.AddFlag("not_pick")
				Corner.LoadImage(fileName)
				Corner.SetParent(self.parentWnd)
				Corner.SetPosition(0, 0)
				Corner.Show()
				self.Corners.append(Corner)

			self.Lines = []
			for fileName in LineFileNames:
				Line = ExpandedImageBox()
				Line.AddFlag("not_pick")
				Line.LoadImage(fileName)
				Line.SetParent(self.parentWnd)
				Line.SetPosition(0, 0)
				Line.Show()
				self.Lines.append(Line)
				
			self.Lines[self.L].SetPosition(0, self.CORNER_HEIGHT)
			self.Lines[self.T].SetPosition(self.CORNER_WIDTH, 0)

		def MakeBase(self):
			self.Base = ExpandedImageBox()
			self.Base.AddFlag("not_pick")
			self.Base.LoadImage("d:/ymir work/ui/controls/board/fill.tga")
			self.Base.SetParent(self.parentWnd)
			self.Base.SetPosition(self.CORNER_WIDTH, self.CORNER_HEIGHT)
			self.Base.Show()

		def __OnChangeSize(self, width, height):
			self.Corners[self.LB].SetPosition(0, height - self.CORNER_HEIGHT)
			self.Corners[self.RT].SetPosition(width - self.CORNER_WIDTH, 0)
			self.Corners[self.RB].SetPosition(width - self.CORNER_WIDTH, height - self.CORNER_HEIGHT)
			self.Lines[self.R].SetPosition(width - self.CORNER_WIDTH, self.CORNER_HEIGHT)
			self.Lines[self.B].SetPosition(self.CORNER_HEIGHT, height - self.CORNER_HEIGHT)

			##########
			self.DecoCorner.SetPosition(-5, height - self.CORNER_HEIGHT)
			##########
			
			verticalShowingPercentage = float((height - self.CORNER_HEIGHT*2) - self.LINE_HEIGHT) / self.LINE_HEIGHT
			horizontalShowingPercentage = float((width - self.CORNER_WIDTH*2) - self.LINE_WIDTH) / self.LINE_WIDTH
			self.Lines[self.L].SetRenderingRect(0, 0, 0, verticalShowingPercentage)
			self.Lines[self.R].SetRenderingRect(0, 0, 0, verticalShowingPercentage)
			self.Lines[self.T].SetRenderingRect(0, 0, horizontalShowingPercentage, 0)
			self.Lines[self.B].SetRenderingRect(0, 0, horizontalShowingPercentage, 0)
			

			if self.Base:
				self.Base.SetRenderingRect(0, 0, horizontalShowingPercentage, verticalShowingPercentage)

class BoardWithTitleBar(Board):

	PADDING = {
		Board.L : Board.PADDING[Board.L],
		Board.R : Board.PADDING[Board.R],
		Board.T : Board.PADDING[Board.T] + TitleBar.BLOCK_HEIGHT,
		Board.B : Board.PADDING[Board.B],
	}

	def __init__(self, padding = PADDING):
		Board.__init__(self, padding)

		titleBar = TitleBar()
		titleBar.SetParent(self.parentWnd)
		titleBar.MakeTitleBar(0, "red")
		if app.GetSelectedDesignName() != "illumina":
			titleBar.SetPosition(8, 7)
		else:
			titleBar.SetPosition(8, 11)
		titleBar.Show()

		titleName = TextLine()
		titleName.SetParent(titleBar)
		titleName.SetPosition(0, 4)
		if app.GetSelectedDesignName() != "illumina":
			titleName.SetPosition(0, 4)
		else:
			titleName.SetPosition(0, 7)
		titleName.SetWindowHorizontalAlignCenter()
		titleName.SetHorizontalAlignCenter()
		titleName.Show()

		self.titleBar = titleBar
		self.titleName = titleName

		self.SetCloseEvent(self.Hide)

	def __del__(self):
		Board.__del__(self)
		self.titleBar = None
		self.titleName = None

	def SetSize(self, width, height):
		self.titleBar.SetWidth(width - 15 + self.PADDING[self.L] + self.PADDING[self.R])
		#self.pickRestrictWindow.SetSize(width, height - 30)
		Board.SetSize(self, width, height)
		self.titleName.UpdateRect()

	def SetTitleColor(self, color):
		self.titleName.SetPackedFontColor(color)

	def SetTitleName(self, name):
		self.titleName.SetText(name)

	def GetTitleName(self):
		return self.titleName.GetText()

	def SetCloseEvent(self, event):
		self.titleBar.SetCloseEvent(event)

if app.GetSelectedDesignName() != "illumina":
	class ThinBoard(Window):

		CORNER_WIDTH = 16
		CORNER_HEIGHT = 16
		LINE_WIDTH = 16
		LINE_HEIGHT = 16
		BOARD_COLOR = grp.GenerateColor(0.0, 0.0, 0.0, 0.51)

		LT = 0
		LB = 1
		RT = 2
		RB = 3
		L = 0
		R = 1
		T = 2
		B = 3

		def __init__(self, layer = "UI"):
			Window.__init__(self, layer)

			CornerFileNames = [ "d:/ymir work/ui/pattern/ThinBoard_Corner_"+dir+".tga" for dir in ["LeftTop","LeftBottom","RightTop","RightBottom"] ]
			LineFileNames = [ "d:/ymir work/ui/pattern/ThinBoard_Line_"+dir+".tga" for dir in ["Left","Right","Top","Bottom"] ]

			self.Corners = []
			for fileName in CornerFileNames:
				Corner = ExpandedImageBox()
				Corner.AddFlag("attach")
				Corner.AddFlag("not_pick")
				Corner.LoadImage(fileName)
				Corner.SetParent(self)
				Corner.SetPosition(0, 0)
				Corner.Show()
				self.Corners.append(Corner)

			self.Lines = []
			for fileName in LineFileNames:
				Line = ExpandedImageBox()
				Line.AddFlag("attach")
				Line.AddFlag("not_pick")
				Line.LoadImage(fileName)
				Line.SetParent(self)
				Line.SetPosition(0, 0)
				Line.Show()
				self.Lines.append(Line)

			Base = Bar()
			Base.SetParent(self)
			Base.AddFlag("attach")
			Base.AddFlag("not_pick")
			Base.SetPosition(self.CORNER_WIDTH, self.CORNER_HEIGHT)
			Base.SetColor(self.BOARD_COLOR)
			Base.Show()
			self.Base = Base

			self.Lines[self.L].SetPosition(0, self.CORNER_HEIGHT)
			self.Lines[self.T].SetPosition(self.CORNER_WIDTH, 0)

		def __del__(self):
			Window.__del__(self)

		def ShowCorner(self, corner):
			self.Corners[corner].Show()
			self.SetSize(self.GetWidth(), self.GetHeight())

		def HideCorners(self, corner):
			self.Corners[corner].Hide()
			self.SetSize(self.GetWidth(), self.GetHeight())

		def ShowLine(self, line):
			self.Lines[line].Show()
			self.SetSize(self.GetWidth(), self.GetHeight())

		def HideLine(self, line):
			self.Lines[line].Hide()
			self.SetSize(self.GetWidth(), self.GetHeight())

		def SetSize(self, width, height):

			width = max(self.CORNER_WIDTH*2, width)
			height = max(self.CORNER_HEIGHT*2, height)
			Window.SetSize(self, width, height)

			if self.Corners[self.LT].IsShow():
				self.Lines[self.L].SetPosition(0, self.CORNER_HEIGHT)
				self.Lines[self.T].SetPosition(self.CORNER_WIDTH, 0)
			else:
				self.Lines[self.L].SetPosition(0, 0)
				self.Lines[self.T].SetPosition(0, 0)

			self.Corners[self.LB].SetPosition(0, height - self.CORNER_HEIGHT)
			self.Corners[self.RT].SetPosition(width - self.CORNER_WIDTH, 0)
			self.Corners[self.RB].SetPosition(width - self.CORNER_WIDTH, height - self.CORNER_HEIGHT)

			if self.Corners[self.RT].IsShow():
				self.Lines[self.R].SetPosition(width - self.CORNER_WIDTH, self.CORNER_HEIGHT)
			else:
				self.Lines[self.R].SetPosition(width - self.CORNER_WIDTH, 0)
			if self.Corners[self.LB].IsShow():
				self.Lines[self.B].SetPosition(self.CORNER_HEIGHT, height - self.CORNER_HEIGHT)
			else:
				self.Lines[self.B].SetPosition(0, height - self.CORNER_HEIGHT)

			cornerCount = {}
			cornerCount[self.L] = self.Corners[self.LB].IsShow() + self.Corners[self.LT].IsShow()
			cornerCount[self.R] = self.Corners[self.RB].IsShow() + self.Corners[self.RT].IsShow()
			cornerCount[self.T] = self.Corners[self.LT].IsShow() + self.Corners[self.RT].IsShow()
			cornerCount[self.B] = self.Corners[self.LB].IsShow() + self.Corners[self.RB].IsShow()

			self.Lines[self.L].SetRenderingRect(0, 0, 0, float(height - self.LINE_HEIGHT - self.CORNER_HEIGHT * cornerCount[self.L]) / self.LINE_HEIGHT)
			self.Lines[self.R].SetRenderingRect(0, 0, 0, float(height - self.LINE_HEIGHT - self.CORNER_HEIGHT * cornerCount[self.R]) / self.LINE_HEIGHT)
			self.Lines[self.T].SetRenderingRect(0, 0, float(width - self.LINE_WIDTH - self.CORNER_WIDTH * cornerCount[self.T]) / self.LINE_WIDTH, 0)
			self.Lines[self.B].SetRenderingRect(0, 0, float(width - self.LINE_WIDTH - self.CORNER_WIDTH * cornerCount[self.B]) / self.LINE_WIDTH, 0)

			lineCount = []
			lineCount.append(self.Lines[self.T].IsShow() + self.Lines[self.B].IsShow())
			lineCount.append(self.Lines[self.L].IsShow() + self.Lines[self.R].IsShow())

			if self.Lines[self.L].IsShow():
				self.Base.SetPosition(self.CORNER_WIDTH, self.Base.GetTop())
			else:
				self.Base.SetPosition(0, self.Base.GetTop())
			if self.Lines[self.T].IsShow():
				self.Base.SetPosition(self.Base.GetLeft(), self.CORNER_HEIGHT)
			else:
				self.Base.SetPosition(self.Base.GetLeft(), 0)

			self.Base.SetSize(width - self.CORNER_WIDTH*lineCount[1], height - self.CORNER_HEIGHT*lineCount[0])

		def ShowInternal(self):
			self.Base.Show()
			for wnd in self.Lines:
				wnd.Show()
			for wnd in self.Corners:
				wnd.Show()

		def HideInternal(self):
			self.Base.Hide()
			for wnd in self.Lines:
				wnd.Hide()
			for wnd in self.Corners:
				wnd.Hide()

else:
	class ThinBoard(Window):

		CORNER_WIDTH = 21
		CORNER_HEIGHT = 21
		LINE_WIDTH = 21
		LINE_W_HEIGHT = 21
		LINE_HEIGHT = 21
		LINE_H_WIDTH = 21
		BOARD_COLOR = grp.GenerateColor(0.0, 0.0, 0.0, 0.6117647058823529) #TROLOLOLOLOL

		LT = 0
		LB = 1
		RT = 2
		RB = 3
		L = 0
		R = 1
		T = 2
		B = 3

		def __init__(self, layer = "UI", CornerFileNames = None, LineFileNames = None):
			Window.__init__(self, layer)

			if CornerFileNames == None:
				CornerFileNames = [ "d:/ymir work/ui/controls/thinboard/corner_"+dir+".tga" for dir in ["LeftTop","LeftBottom","RightTop","RightBottom"] ]
			if LineFileNames == None:
				LineFileNames = [ "d:/ymir work/ui/controls/thinboard/bar_"+dir+".tga" for dir in ["Left","Right","Top","Bottom"] ]

			self.Corners = []
			for fileName in CornerFileNames:
				Corner = ExpandedImageBox()
				Corner.AddFlag("attach")
				Corner.AddFlag("not_pick")
				Corner.LoadImage(fileName)
				Corner.SetParent(self)
				Corner.SetPosition(0, 0)
				Corner.Show()
				self.Corners.append(Corner)

			self.Lines = []
			for fileName in LineFileNames:
				Line = ExpandedImageBox()
				Line.AddFlag("attach")
				Line.AddFlag("not_pick")
				Line.LoadImage(fileName)
				Line.SetParent(self)
				Line.SetPosition(0, 0)
				Line.Show()
				self.Lines.append(Line)

			Base = Bar()
			Base.SetParent(self)
			Base.AddFlag("attach")
			Base.AddFlag("not_pick")
			Base.SetPosition(self.CORNER_WIDTH, self.CORNER_HEIGHT)
			Base.SetColor(self.BOARD_COLOR)
			Base.Show()
			self.Base = Base

			self.Lines[self.L].SetPosition(0, self.CORNER_HEIGHT)
			self.Lines[self.T].SetPosition(self.CORNER_WIDTH, 0)

		def __del__(self):
			Window.__del__(self)

		def ShowCorner(self, corner):
			self.Corners[corner].Show()
			self.SetSize(self.GetWidth(), self.GetHeight())

		def HideCorners(self, corner):
			self.Corners[corner].Hide()
			self.SetSize(self.GetWidth(), self.GetHeight())

		def ShowLine(self, line):
			self.Lines[line].Show()
			self.SetSize(self.GetWidth(), self.GetHeight())

		def HideLine(self, line):
			self.Lines[line].Hide()
			self.SetSize(self.GetWidth(), self.GetHeight())

		def SetSize(self, width, height):

			width = max(self.CORNER_WIDTH*2, width)
			height = max(self.CORNER_HEIGHT*2, height)
			Window.SetSize(self, width, height)

			if self.Corners[self.LT].IsShow():
				self.Lines[self.L].SetPosition(0, self.CORNER_HEIGHT)
				self.Lines[self.T].SetPosition(self.CORNER_WIDTH, 0)
			else:
				self.Lines[self.L].SetPosition(0, 0)
				self.Lines[self.T].SetPosition(0, 0)

			self.Corners[self.LB].SetPosition(0, height - self.CORNER_HEIGHT)
			self.Corners[self.RT].SetPosition(width - self.CORNER_WIDTH, 0)
			self.Corners[self.RB].SetPosition(width - self.CORNER_WIDTH, height - self.CORNER_HEIGHT)

			if self.Corners[self.RT].IsShow():
				self.Lines[self.R].SetPosition(width - self.LINE_H_WIDTH, self.CORNER_HEIGHT)
			else:
				self.Lines[self.R].SetPosition(width - self.LINE_H_WIDTH, 0)
			if self.Corners[self.LB].IsShow():
				self.Lines[self.B].SetPosition(self.CORNER_WIDTH, height - self.LINE_W_HEIGHT)
			else:
				self.Lines[self.B].SetPosition(0, height - self.LINE_W_HEIGHT)

			cornerCount = {}
			cornerCount[self.L] = self.Corners[self.LB].IsShow() + self.Corners[self.LT].IsShow()
			cornerCount[self.R] = self.Corners[self.RB].IsShow() + self.Corners[self.RT].IsShow()
			cornerCount[self.T] = self.Corners[self.LT].IsShow() + self.Corners[self.RT].IsShow()
			cornerCount[self.B] = self.Corners[self.LB].IsShow() + self.Corners[self.RB].IsShow()

			self.Lines[self.L].SetRenderingRect(0, 0, 0, float(height - self.LINE_HEIGHT - self.CORNER_HEIGHT * cornerCount[self.L]) / self.LINE_HEIGHT)
			self.Lines[self.R].SetRenderingRect(0, 0, 0, float(height - self.LINE_HEIGHT - self.CORNER_HEIGHT * cornerCount[self.R]) / self.LINE_HEIGHT)
			self.Lines[self.T].SetRenderingRect(0, 0, float(width - self.LINE_WIDTH - self.CORNER_WIDTH * cornerCount[self.T]) / self.LINE_WIDTH, 0)
			self.Lines[self.B].SetRenderingRect(0, 0, float(width - self.LINE_WIDTH - self.CORNER_WIDTH * cornerCount[self.B]) / self.LINE_WIDTH, 0)

			lineCount = []
			lineCount.append(self.Lines[self.T].IsShow() + self.Lines[self.B].IsShow())
			lineCount.append(self.Lines[self.L].IsShow() + self.Lines[self.R].IsShow())

			if self.Lines[self.L].IsShow():
				self.Base.SetPosition(self.CORNER_WIDTH, self.Base.GetTop())
			else:
				self.Base.SetPosition(0, self.Base.GetTop())
			if self.Lines[self.T].IsShow():
				self.Base.SetPosition(self.Base.GetLeft(), self.CORNER_HEIGHT)
			else:
				self.Base.SetPosition(self.Base.GetLeft(), 0)

			verticalShowingPercentage = height - self.CORNER_HEIGHT*lineCount[0]
			horizontalShowingPercentage = width - self.CORNER_WIDTH*lineCount[1]
			self.Base.SetSize(horizontalShowingPercentage, verticalShowingPercentage)

		def ShowInternal(self):
			self.Base.Show()
			for wnd in self.Lines:
				wnd.Show()
			for wnd in self.Corners:
				wnd.Show()

		def HideInternal(self):
			self.Base.Hide()
			for wnd in self.Lines:
				wnd.Hide()
			for wnd in self.Corners:
				wnd.Hide()

class ThinBoardGold(Window):
	CORNER_WIDTH = 16
	CORNER_HEIGHT = 16
	LINE_WIDTH = 16
	LINE_HEIGHT = 16

	LT = 0
	LB = 1
	RT = 2
	RB = 3
	L = 0
	R = 1
	T = 2
	B = 3

	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)

		CornerFileNames = [ "d:/ymir work/ui/pattern/thinboardgold/ThinBoard_Corner_"+dir+"_Gold.tga" for dir in ["LeftTop","LeftBottom","RightTop","RightBottom"] ]
		LineFileNames = [ "d:/ymir work/ui/pattern/thinboardgold/ThinBoard_Line_"+dir+"_Gold.tga" for dir in ["Left","Right","Top","Bottom"] ]

		self.MakeBase()

		self.Corners = []
		for fileName in CornerFileNames:
			Corner = ExpandedImageBox()
			Corner.AddFlag("attach")
			Corner.AddFlag("not_pick")
			Corner.LoadImage(fileName)
			Corner.SetParent(self)
			Corner.SetPosition(0, 0)
			Corner.Show()
			self.Corners.append(Corner)

		self.Lines = []
		for fileName in LineFileNames:
			Line = ExpandedImageBox()
			Line.AddFlag("attach")
			Line.AddFlag("not_pick")
			Line.LoadImage(fileName)
			Line.SetParent(self)
			Line.SetPosition(0, 0)
			Line.Show()
			self.Lines.append(Line)

		self.Lines[self.L].SetPosition(0, self.CORNER_HEIGHT)
		self.Lines[self.T].SetPosition(self.CORNER_WIDTH, 0)

	def __del__(self):
		Window.__del__(self)

	def SetSize(self, width, height):

		width = max(self.CORNER_WIDTH*2, width)
		height = max(self.CORNER_HEIGHT*2, height)
		Window.SetSize(self, width, height)

		self.Corners[self.LB].SetPosition(0, height - self.CORNER_HEIGHT)
		self.Corners[self.RT].SetPosition(width - self.CORNER_WIDTH, 0)
		self.Corners[self.RB].SetPosition(width - self.CORNER_WIDTH, height - self.CORNER_HEIGHT)
		self.Lines[self.R].SetPosition(width - self.CORNER_WIDTH, self.CORNER_HEIGHT)
		self.Lines[self.B].SetPosition(self.CORNER_HEIGHT, height - self.CORNER_HEIGHT)

		verticalShowingPercentage = float((height - self.CORNER_HEIGHT*2) - self.LINE_HEIGHT) / self.LINE_HEIGHT
		horizontalShowingPercentage = float((width - self.CORNER_WIDTH*2) - self.LINE_WIDTH) / self.LINE_WIDTH

		self.Lines[self.L].SetRenderingRect(0, 0, 0, verticalShowingPercentage)
		self.Lines[self.R].SetRenderingRect(0, 0, 0, verticalShowingPercentage)
		self.Lines[self.T].SetRenderingRect(0, 0, horizontalShowingPercentage, 0)
		self.Lines[self.B].SetRenderingRect(0, 0, horizontalShowingPercentage, 0)

		#self.Base.GetWidth()
		#self.Base.GetHeight()
		"""
			Defalt Width : 128, Height : 128 
			0.0 > 128, 1.0 > 256 
		"""
		if self.Base:
			self.Base.SetRenderingRect(0, 0, (float(width)-32)/float(self.Base.GetWidth()) - 1.0, (float(height)-32)/float(self.Base.GetHeight()) - 1.0)

	def MakeBase(self):
		self.Base = ExpandedImageBox()
		self.Base.AddFlag("not_pick")
		self.Base.LoadImage("d:/ymir work/ui/pattern/Board_Base.tga")
		self.Base.SetParent(self)
		self.Base.SetPosition(16, 16)
		self.Base.SetAlpha(0.8)
		self.Base.Show()

	def ShowInternal(self):
		self.Base.Show()
		for wnd in self.Lines:
			wnd.Show()
		for wnd in self.Corners:
			wnd.Show()

	def HideInternal(self):
		self.Base.Hide()
		for wnd in self.Lines:
			wnd.Hide()
		for wnd in self.Corners:
			wnd.Hide()

class ThinBoardCircle(Window):
	CORNER_WIDTH = 4
	CORNER_HEIGHT = 4
	LINE_WIDTH = 4
	LINE_HEIGHT = 4
	BOARD_COLOR = grp.GenerateColor(0.0, 0.0, 0.0, 1.0)

	LT = 0
	LB = 1
	RT = 2
	RB = 3
	L = 0
	R = 1
	T = 2
	B = 3

	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)

		CornerFileNames = [ "d:/ymir work/ui/pattern/thinboardcircle/ThinBoard_Corner_"+dir+"_Circle.tga" for dir in ["LeftTop","LeftBottom","RightTop","RightBottom"] ]
		LineFileNames = [ "d:/ymir work/ui/pattern/thinboardcircle/ThinBoard_Line_"+dir+"_Circle.tga" for dir in ["Left","Right","Top","Bottom"] ]

		self.Corners = []
		for fileName in CornerFileNames:
			Corner = ExpandedImageBox()
			Corner.AddFlag("attach")
			Corner.AddFlag("not_pick")
			Corner.LoadImage(fileName)
			Corner.SetParent(self)
			Corner.SetPosition(0, 0)
			Corner.Show()
			self.Corners.append(Corner)

		self.Lines = []
		for fileName in LineFileNames:
			Line = ExpandedImageBox()
			Line.AddFlag("attach")
			Line.AddFlag("not_pick")
			Line.LoadImage(fileName)
			Line.SetParent(self)
			Line.SetPosition(0, 0)
			Line.Show()
			self.Lines.append(Line)

		Base = Bar()
		Base.SetParent(self)
		Base.AddFlag("attach")
		Base.AddFlag("not_pick")
		Base.SetPosition(self.CORNER_WIDTH, self.CORNER_HEIGHT)
		Base.SetColor(self.BOARD_COLOR)
		Base.Show()
		self.Base = Base

		self.Lines[self.L].SetPosition(0, self.CORNER_HEIGHT)
		self.Lines[self.T].SetPosition(self.CORNER_WIDTH, 0)

	def __del__(self):
		Window.__del__(self)

	def SetSize(self, width, height):

		width = max(self.CORNER_WIDTH*2, width)
		height = max(self.CORNER_HEIGHT*2, height)
		Window.SetSize(self, width, height)

		self.Corners[self.LB].SetPosition(0, height - self.CORNER_HEIGHT)
		self.Corners[self.RT].SetPosition(width - self.CORNER_WIDTH, 0)
		self.Corners[self.RB].SetPosition(width - self.CORNER_WIDTH, height - self.CORNER_HEIGHT)
		self.Lines[self.R].SetPosition(width - self.CORNER_WIDTH, self.CORNER_HEIGHT)
		self.Lines[self.B].SetPosition(self.CORNER_HEIGHT, height - self.CORNER_HEIGHT)

		verticalShowingPercentage = float((height - self.CORNER_HEIGHT*2) - self.LINE_HEIGHT) / self.LINE_HEIGHT
		horizontalShowingPercentage = float((width - self.CORNER_WIDTH*2) - self.LINE_WIDTH) / self.LINE_WIDTH
		self.Lines[self.L].SetRenderingRect(0, 0, 0, verticalShowingPercentage)
		self.Lines[self.R].SetRenderingRect(0, 0, 0, verticalShowingPercentage)
		self.Lines[self.T].SetRenderingRect(0, 0, horizontalShowingPercentage, 0)
		self.Lines[self.B].SetRenderingRect(0, 0, horizontalShowingPercentage, 0)
		self.Base.SetSize(width - self.CORNER_WIDTH*2, height - self.CORNER_HEIGHT*2)

	def ShowInternal(self):
		self.Base.Show()
		for wnd in self.Lines:
			wnd.Show()
		for wnd in self.Corners:
			wnd.Show()

	def HideInternal(self):
		self.Base.Hide()
		for wnd in self.Lines:
			wnd.Hide()
		for wnd in self.Corners:
			wnd.Hide()
if constInfo.NEW_TARGET_UI:
	class ThinBoardTarget(Window):
		CORNER_WIDTH = 16
		CORNER_HEIGHT = 16
		LINE_WIDTH = 16
		LINE_HEIGHT = 16
		BOARD_COLOR = grp.GenerateColor(0.0, 0.0, 0.0, 0.45)
		LT = 0
		LB = 1
		RT = 2
		RB = 3
		L = 0
		R = 1
		T = 2
		B = 3
		def __init__(self, layer = "UI"):
			Window.__init__(self, layer)
			CornerFileNames = [ "d:/ymir work/ui/pattern/thinboardnew/ThinBoard_Corner_"+dir+".tga" for dir in ["LeftTop","LeftBottom","RightTop","RightBottom"] ]
			LineFileNames = [ "d:/ymir work/ui/pattern/thinboardnew/ThinBoard_Line_"+dir+".tga" for dir in ["Left","Right","Top","Bottom"] ]
			self.Corners = []
			for fileName in CornerFileNames:
				Corner = ExpandedImageBox()
				Corner.AddFlag("attach")
				Corner.AddFlag("not_pick")
				Corner.LoadImage(fileName)
				Corner.SetParent(self)
				Corner.SetPosition(0, 0)
				Corner.Show()
				self.Corners.append(Corner)
			self.Lines = []
			for fileName in LineFileNames:
				Line = ExpandedImageBox()
				Line.AddFlag("attach")
				Line.AddFlag("not_pick")
				Line.LoadImage(fileName)
				Line.SetParent(self)
				Line.SetPosition(0, 0)
				Line.Show()
				self.Lines.append(Line)
			Base = Bar()
			Base.SetParent(self)
			Base.AddFlag("attach")
			Base.AddFlag("not_pick")
			Base.SetPosition(self.CORNER_WIDTH, self.CORNER_HEIGHT)
			Base.SetColor(self.BOARD_COLOR)
			Base.Show()
			self.Base = Base

			self.Lines[self.L].SetPosition(0, self.CORNER_HEIGHT)
			self.Lines[self.T].SetPosition(self.CORNER_WIDTH, 0)

		def __del__(self):
			Window.__del__(self)

		def ShowCorner(self, corner):
			self.Corners[corner].Show()
			self.SetSize(self.GetWidth(), self.GetHeight())

		def HideCorners(self, corner):
			self.Corners[corner].Hide()
			self.SetSize(self.GetWidth(), self.GetHeight())

		def ShowLine(self, line):
			self.Lines[line].Show()
			self.SetSize(self.GetWidth(), self.GetHeight())

		def HideLine(self, line):
			self.Lines[line].Hide()
			self.SetSize(self.GetWidth(), self.GetHeight())

		def SetSize(self, width, height):

			width = max(self.CORNER_WIDTH*2, width)
			height = max(self.CORNER_HEIGHT*2, height)
			Window.SetSize(self, width, height)

			if self.Corners[self.LT].IsShow():
				self.Lines[self.L].SetPosition(0, self.CORNER_HEIGHT)
				self.Lines[self.T].SetPosition(self.CORNER_WIDTH, 0)
			else:
				self.Lines[self.L].SetPosition(0, 0)
				self.Lines[self.T].SetPosition(0, 0)

			self.Corners[self.LB].SetPosition(0, height - self.CORNER_HEIGHT)
			self.Corners[self.RT].SetPosition(width - self.CORNER_WIDTH, 0)
			self.Corners[self.RB].SetPosition(width - self.CORNER_WIDTH, height - self.CORNER_HEIGHT)

			if self.Corners[self.RT].IsShow():
				self.Lines[self.R].SetPosition(width - self.CORNER_WIDTH, self.CORNER_HEIGHT)
			else:
				self.Lines[self.R].SetPosition(width - self.CORNER_WIDTH, 0)
			if self.Corners[self.LB].IsShow():
				self.Lines[self.B].SetPosition(self.CORNER_HEIGHT, height - self.CORNER_HEIGHT)
			else:
				self.Lines[self.B].SetPosition(0, height - self.CORNER_HEIGHT)

			cornerCount = {}
			cornerCount[self.L] = self.Corners[self.LB].IsShow() + self.Corners[self.LT].IsShow()
			cornerCount[self.R] = self.Corners[self.RB].IsShow() + self.Corners[self.RT].IsShow()
			cornerCount[self.T] = self.Corners[self.LT].IsShow() + self.Corners[self.RT].IsShow()
			cornerCount[self.B] = self.Corners[self.LB].IsShow() + self.Corners[self.RB].IsShow()

			self.Lines[self.L].SetRenderingRect(0, 0, 0, float(height - self.LINE_HEIGHT - self.CORNER_HEIGHT * cornerCount[self.L]) / self.LINE_HEIGHT)
			self.Lines[self.R].SetRenderingRect(0, 0, 0, float(height - self.LINE_HEIGHT - self.CORNER_HEIGHT * cornerCount[self.R]) / self.LINE_HEIGHT)
			self.Lines[self.T].SetRenderingRect(0, 0, float(width - self.LINE_WIDTH - self.CORNER_WIDTH * cornerCount[self.T]) / self.LINE_WIDTH, 0)
			self.Lines[self.B].SetRenderingRect(0, 0, float(width - self.LINE_WIDTH - self.CORNER_WIDTH * cornerCount[self.B]) / self.LINE_WIDTH, 0)

			lineCount = []
			lineCount.append(self.Lines[self.T].IsShow() + self.Lines[self.B].IsShow())
			lineCount.append(self.Lines[self.L].IsShow() + self.Lines[self.R].IsShow())

			if self.Lines[self.L].IsShow():
				self.Base.SetPosition(self.CORNER_WIDTH, self.Base.GetTop())
			else:
				self.Base.SetPosition(0, self.Base.GetTop())
			if self.Lines[self.T].IsShow():
				self.Base.SetPosition(self.Base.GetLeft(), self.CORNER_HEIGHT)
			else:
				self.Base.SetPosition(self.Base.GetLeft(), 0)

			self.Base.SetSize(width - self.CORNER_WIDTH*lineCount[1], height - self.CORNER_HEIGHT*lineCount[0])

		def ShowInternal(self):
			self.Base.Show()
			for wnd in self.Lines:
				wnd.Show()
			for wnd in self.Corners:
				wnd.Show()

		def HideInternal(self):
			self.Base.Hide()
			for wnd in self.Lines:
				wnd.Hide()
			for wnd in self.Corners:
				wnd.Hide()

class ScrollBarTemplate(Window):

	MIDDLE_BAR_POS = 5
	MIDDLE_BAR_UPPER_PLACE = 2
	MIDDLE_BAR_DOWNER_PLACE = 2
	TEMP_SPACE = MIDDLE_BAR_UPPER_PLACE + MIDDLE_BAR_DOWNER_PLACE

	class MiddleBar(DragButton):
		def __init__(self):
			self.middle = None
			DragButton.__init__(self)
			self.AddFlag("movable")

		def MakeImage(self, img):
			middle = ExpandedImageBox()
			middle.SetParent(self)
			middle.LoadImage(img)
			middle.SetPosition(0, 0)
			middle.AddFlag("not_pick")
			middle.Show()
			self.middle = middle
			self.SetSize(self.GetHeight())

		def SetSize(self, height):
			height = max(12, height)
			if self.middle:
				DragButton.SetSize(self, self.middle.GetWidth(), height)
				val = 0
				if self.middle.GetHeight() != 0:
					val = float(height)/self.middle.GetHeight()
				self.middle.SetRenderingRect(0, 0, 0, -1.0 + val)
			else:
				DragButton.SetSize(self, self.GetWidth(), height)

	def __init__(self):
		Window.__init__(self)

		self.pageSize = 1
		self.curPos = 0.0
		self.eventScroll = None
		self.eventArgs = None
		self.lockFlag = False

		self.SCROLLBAR_WIDTH = 0
		self.SCROLLBAR_BUTTON_WIDTH = 0
		self.SCROLLBAR_BUTTON_HEIGHT = 0
		self.SCROLLBAR_MIDDLE_HEIGHT = 0

		self.CreateScrollBar()

		self.scrollStep = 0.20

	def SetUpButton(self, upVisual, overVisual, downVisual):
		self.upButton.SetUpVisual(upVisual)
		self.upButton.SetOverVisual(overVisual)
		self.upButton.SetDownVisual(downVisual)
		self.upButton.Show()
		self.SCROLLBAR_BUTTON_WIDTH = self.upButton.GetWidth()
		self.SCROLLBAR_BUTTON_HEIGHT = self.upButton.GetHeight() + 3

	def SetDownButton(self, upVisual, overVisual, downVisual):
		self.downButton.SetUpVisual(upVisual)
		self.downButton.SetOverVisual(overVisual)
		self.downButton.SetDownVisual(downVisual)
		self.downButton.Show()

	def SetMiddleImage(self, img):
		self.middleBar.MakeImage(img)
		self.SCROLLBAR_MIDDLE_HEIGHT = self.middleBar.GetHeight()
		self.MIDDLE_BAR_POS = (self.SCROLLBAR_WIDTH - self.middleBar.GetWidth()) / 2

	def SetBarPartImages(self, topImg, centerImg, bottomImg):
		self.barTopImage.LoadImage(topImg)
		self.barTopImage.Show()
		self.barCenterImage.LoadImage(centerImg)
		self.barCenterImage.SetPosition(0, self.barTopImage.GetHeight())
		self.barCenterImage.Show()
		self.barBottomImage.LoadImage(bottomImg)
		self.barBottomImage.Show()
		self.SCROLLBAR_WIDTH = max(self.barTopImage.GetWidth(), self.SCROLLBAR_WIDTH)
		self.MIDDLE_BAR_POS = (self.SCROLLBAR_WIDTH - self.middleBar.GetWidth()) / 2

	def SetBarImage(self, img):
		self.barImage.LoadImage(img)
		self.barImage.Show()
		self.SCROLLBAR_WIDTH = max(self.barImage.GetWidth(), self.SCROLLBAR_WIDTH)
		self.MIDDLE_BAR_POS = (self.SCROLLBAR_WIDTH - self.middleBar.GetWidth()) / 2

	def CreateScrollBar(self):
		barImage = ExpandedImageBox()
		barImage.SetParent(self)
		barImage.AddFlag("not_pick")
		barImage.Hide()

		barTopImage = ImageBox()
		barTopImage.SetParent(self)
		barTopImage.AddFlag("not_pick")
		barTopImage.Hide()

		barCenterImage = ExpandedImageBox()
		barCenterImage.SetParent(self)
		barCenterImage.AddFlag("not_pick")
		barCenterImage.Hide()

		barBottomImage = ImageBox()
		barBottomImage.SetParent(self)
		barBottomImage.AddFlag("not_pick")
		barBottomImage.Hide()

		middleBar = self.MiddleBar()
		middleBar.SetParent(self)
		middleBar.SetMoveEvent(__mem_func__(self.OnMove))
		middleBar.Show()
		middleBar.SetSize(12)

		upButton = Button()
		upButton.SetParent(self)
		upButton.SetEvent(__mem_func__(self.OnUp))
		upButton.SetWindowHorizontalAlignCenter()
		upButton.Hide()

		downButton = Button()
		downButton.SetParent(self)
		downButton.SetEvent(__mem_func__(self.OnDown))
		downButton.SetWindowHorizontalAlignCenter()
		downButton.Hide()

		self.upButton = upButton
		self.downButton = downButton
		self.middleBar = middleBar
		self.barImage = barImage
		self.barTopImage = barTopImage
		self.barCenterImage = barCenterImage
		self.barBottomImage = barBottomImage

	def Destroy(self):
		self.middleBar = None
		self.upButton = None
		self.downButton = None
		self.barImage = None
		self.barTopImage = None
		self.barCenterImage = None
		self.barBottomImage = None
		self.eventScroll = None
		self.eventArgs = None

	def SetScrollEvent(self, event, *args):
		self.eventScroll = event
		self.eventArgs = args

	# ------------------------------------------------------------------------------------------

	# Important: pageScale must be float! so parse the values to float before you use them.
	# Otherwise it simply won't work or the bar is gonna be very small

	# ------------------------------------------------------------------------------------------

	def SetMiddleBarSize(self, pageScale):
		realHeight = self.GetHeight() - self.SCROLLBAR_BUTTON_HEIGHT*2
		self.SCROLLBAR_MIDDLE_HEIGHT = max(12, int(pageScale * float(realHeight)))
		self.middleBar.SetSize(self.SCROLLBAR_MIDDLE_HEIGHT)
		self.pageSize = (self.GetHeight() - self.SCROLLBAR_BUTTON_HEIGHT*2) - self.SCROLLBAR_MIDDLE_HEIGHT - (self.TEMP_SPACE)

	def SetScrollBarSize(self, height):
		self.pageSize = (height - self.SCROLLBAR_BUTTON_HEIGHT*2) - self.SCROLLBAR_MIDDLE_HEIGHT - (self.TEMP_SPACE)
		self.SetSize(self.SCROLLBAR_WIDTH, height)
		self.upButton.SetPosition(0, 3)
		self.downButton.SetPosition(0, height - self.SCROLLBAR_BUTTON_HEIGHT)
		self.middleBar.SetRestrictMovementArea(self.MIDDLE_BAR_POS, self.SCROLLBAR_BUTTON_HEIGHT + self.MIDDLE_BAR_UPPER_PLACE, self.middleBar.GetWidth(), height - self.SCROLLBAR_BUTTON_HEIGHT*2 - self.TEMP_SPACE)
		self.middleBar.SetPosition(self.MIDDLE_BAR_POS, 0)

		self.UpdateBarImage()
		self.upButton.UpdateRect()
		self.downButton.UpdateRect()
		
	def SetScrollStep(self, step):
		self.scrollStep = step
	
	def GetScrollStep(self):
		return self.scrollStep

	def UpdateBarImage(self):
		if self.barImage.IsShow():
			val = 0
			if self.barImage.GetHeight() != 0:
				val = self.GetHeight() / float(self.barImage.GetHeight())
			self.barImage.SetRenderingRect(0.0, 0.0, 0.0, -1.0 + val)
		if self.barCenterImage.IsShow():
			centerHeight = self.GetHeight() - (self.barTopImage.GetHeight() + self.barBottomImage.GetHeight())
			val = 0
			if self.barCenterImage.GetHeight() != 0:
				val = (centerHeight / float(self.barCenterImage.GetHeight()))
			self.barCenterImage.SetRenderingRect(0.0, 0.0, 0.0, -1.0 + val)
		if self.barBottomImage.IsShow():
			self.barBottomImage.SetPosition(0, self.GetHeight() - self.barBottomImage.GetHeight())

	def GetPos(self):
		return self.curPos

	def SetPos(self, pos):
		pos = max(0.0, pos)
		pos = min(1.0, pos)

		newPos = float(self.pageSize) * pos
		self.middleBar.SetPosition(self.MIDDLE_BAR_POS, int(newPos) + self.SCROLLBAR_BUTTON_HEIGHT + self.MIDDLE_BAR_UPPER_PLACE)
		self.OnMove()

	def OnUp(self):
		self.SetPos(self.curPos-self.scrollStep)

	def OnDown(self):
		self.SetPos(self.curPos+self.scrollStep)

	def OnMove(self):

		if self.lockFlag:
			return

		if 0 == self.pageSize:
			return

		(xLocal, yLocal) = self.middleBar.GetLocalPosition()
		self.curPos = float(yLocal - self.SCROLLBAR_BUTTON_HEIGHT - self.MIDDLE_BAR_UPPER_PLACE) / float(self.pageSize)

		if self.eventScroll:
			apply(self.eventScroll, self.eventArgs)

	def OnMouseLeftButtonDown(self):
		(xMouseLocalPosition, yMouseLocalPosition) = self.GetMouseLocalPosition()
		pickedPos = yMouseLocalPosition - self.SCROLLBAR_BUTTON_HEIGHT - self.SCROLLBAR_MIDDLE_HEIGHT/2
		newPos = float(pickedPos) / float(self.pageSize)
		self.SetPos(newPos)

	def LockScroll(self):
		self.lockFlag = True

	def UnlockScroll(self):
		self.lockFlag = False

class ScrollBar(Window):

	SCROLLBAR_WIDTH = 17
	SCROLLBAR_MIDDLE_HEIGHT = 9
	SCROLLBAR_BUTTON_WIDTH = 17
	SCROLLBAR_BUTTON_HEIGHT = 17
	MIDDLE_BAR_POS = 5
	MIDDLE_BAR_UPPER_PLACE = 3
	MIDDLE_BAR_DOWNER_PLACE = 4
	TEMP_SPACE = MIDDLE_BAR_UPPER_PLACE + MIDDLE_BAR_DOWNER_PLACE

	class MiddleBar(DragButton):
		def __init__(self):
			DragButton.__init__(self)
			self.AddFlag("movable")
			#self.AddFlag("restrict_x")

		def MakeImage(self):
			top = ImageBox()
			top.SetParent(self)
			top.LoadImage("d:/ymir work/ui/pattern/ScrollBar_Top.tga")
			top.SetPosition(0, 0)
			top.AddFlag("not_pick")
			top.Show()
			bottom = ImageBox()
			bottom.SetParent(self)
			bottom.LoadImage("d:/ymir work/ui/pattern/ScrollBar_Bottom.tga")
			bottom.AddFlag("not_pick")
			bottom.Show()

			middle = ExpandedImageBox()
			middle.SetParent(self)
			middle.LoadImage("d:/ymir work/ui/pattern/ScrollBar_Middle.tga")
			middle.SetPosition(0, 4)
			middle.AddFlag("not_pick")
			middle.Show()

			self.top = top
			self.bottom = bottom
			self.middle = middle

		def SetSize(self, height):
			height = max(12, height)
			DragButton.SetSize(self, 10, height)
			self.bottom.SetPosition(0, height-4)

			height -= 4*3
			self.middle.SetRenderingRect(0, 0, 0, float(height)/4.0)

	def __init__(self):
		Window.__init__(self)

		self.pageSize = 1
		self.curPos = 0.0
		self.eventScroll = None
		self.eventArgs = None
		self.lockFlag = False

		self.CreateScrollBar()

		self.scrollStep = 0.20

	def __del__(self):
		Window.__del__(self)

	def CreateScrollBar(self):
		barSlot = Bar3D()
		barSlot.SetParent(self)
		barSlot.AddFlag("not_pick")
		barSlot.Show()

		middleBar = self.MiddleBar()
		middleBar.SetParent(self)
		middleBar.SetMoveEvent(__mem_func__(self.OnMove))
		middleBar.Show()
		middleBar.MakeImage()
		middleBar.SetSize(12)

		upButton = Button()
		upButton.SetParent(self)
		upButton.SetEvent(__mem_func__(self.OnUp))
		upButton.SetUpVisual("d:/ymir work/ui/public/scrollbar_up_button_01.sub")
		upButton.SetOverVisual("d:/ymir work/ui/public/scrollbar_up_button_02.sub")
		upButton.SetDownVisual("d:/ymir work/ui/public/scrollbar_up_button_03.sub")
		upButton.Show()

		downButton = Button()
		downButton.SetParent(self)
		downButton.SetEvent(__mem_func__(self.OnDown))
		downButton.SetUpVisual("d:/ymir work/ui/public/scrollbar_down_button_01.sub")
		downButton.SetOverVisual("d:/ymir work/ui/public/scrollbar_down_button_02.sub")
		downButton.SetDownVisual("d:/ymir work/ui/public/scrollbar_down_button_03.sub")
		downButton.Show()

		self.upButton = upButton
		self.downButton = downButton
		self.middleBar = middleBar
		self.barSlot = barSlot

		self.SCROLLBAR_WIDTH = self.upButton.GetWidth()
		self.SCROLLBAR_MIDDLE_HEIGHT = self.middleBar.GetHeight()
		self.SCROLLBAR_BUTTON_WIDTH = self.upButton.GetWidth()
		self.SCROLLBAR_BUTTON_HEIGHT = self.upButton.GetHeight()

	def Destroy(self):
		self.middleBar = None
		self.upButton = None
		self.downButton = None
		self.eventScroll = None
		self.eventArgs = None

	def SetScrollEvent(self, event, *args):
		self.eventScroll = event
		self.eventArgs = args

	def SetMiddleBarSize(self, pageScale):
		realHeight = self.GetHeight() - self.SCROLLBAR_BUTTON_HEIGHT*2
		self.SCROLLBAR_MIDDLE_HEIGHT = int(pageScale * float(realHeight))
		self.middleBar.SetSize(self.SCROLLBAR_MIDDLE_HEIGHT)
		self.pageSize = (self.GetHeight() - self.SCROLLBAR_BUTTON_HEIGHT*2) - self.SCROLLBAR_MIDDLE_HEIGHT - (self.TEMP_SPACE)

	def SetScrollBarSize(self, height):
		self.pageSize = (height - self.SCROLLBAR_BUTTON_HEIGHT*2) - self.SCROLLBAR_MIDDLE_HEIGHT - (self.TEMP_SPACE)
		self.SetSize(self.SCROLLBAR_WIDTH, height)
		self.upButton.SetPosition(0, 0)
		self.downButton.SetPosition(0, height - self.SCROLLBAR_BUTTON_HEIGHT)
		self.middleBar.SetRestrictMovementArea(self.MIDDLE_BAR_POS, self.SCROLLBAR_BUTTON_HEIGHT + self.MIDDLE_BAR_UPPER_PLACE, self.MIDDLE_BAR_POS+2, height - self.SCROLLBAR_BUTTON_HEIGHT*2 - self.TEMP_SPACE)
		self.middleBar.SetPosition(self.MIDDLE_BAR_POS, 0)

		self.UpdateBarSlot()
		
	def SetScrollStep(self, step):
		self.scrollStep = step
	
	def GetScrollStep(self):
		return self.scrollStep

	def UpdateBarSlot(self):
		self.barSlot.SetPosition(0, self.SCROLLBAR_BUTTON_HEIGHT)
		self.barSlot.SetSize(self.GetWidth() - 2, self.GetHeight() - self.SCROLLBAR_BUTTON_HEIGHT*2 - 2)

	def GetPos(self):
		return self.curPos

	def SetPos(self, pos):
		pos = max(0.0, pos)
		pos = min(1.0, pos)

		newPos = float(self.pageSize) * pos
		self.middleBar.SetPosition(self.MIDDLE_BAR_POS, int(newPos) + self.SCROLLBAR_BUTTON_HEIGHT + self.MIDDLE_BAR_UPPER_PLACE)
		self.OnMove()

	def OnUp(self):
		self.SetPos(self.curPos-self.scrollStep)

	def OnDown(self):
		self.SetPos(self.curPos+self.scrollStep)

	def OnMove(self):

		if self.lockFlag:
			return

		if 0 == self.pageSize:
			return

		(xLocal, yLocal) = self.middleBar.GetLocalPosition()
		self.curPos = float(yLocal - self.SCROLLBAR_BUTTON_HEIGHT - self.MIDDLE_BAR_UPPER_PLACE) / float(self.pageSize)

		if self.eventScroll:
			apply(self.eventScroll, self.eventArgs)

	def OnMouseLeftButtonDown(self):
		(xMouseLocalPosition, yMouseLocalPosition) = self.GetMouseLocalPosition()
		pickedPos = yMouseLocalPosition - self.SCROLLBAR_BUTTON_HEIGHT - self.SCROLLBAR_MIDDLE_HEIGHT/2
		newPos = float(pickedPos) / float(self.pageSize)
		self.SetPos(newPos)

	def LockScroll(self):
		self.lockFlag = True

	def UnlockScroll(self):
		self.lockFlag = False

class ThinScrollBar(ScrollBar):

	def CreateScrollBar(self):
		middleBar = self.MiddleBar()
		middleBar.SetParent(self)
		middleBar.SetMoveEvent(__mem_func__(self.OnMove))
		middleBar.Show()
		middleBar.SetUpVisual("d:/ymir work/ui/public/scrollbar_thin_middle_button_01.sub")
		middleBar.SetOverVisual("d:/ymir work/ui/public/scrollbar_thin_middle_button_02.sub")
		middleBar.SetDownVisual("d:/ymir work/ui/public/scrollbar_thin_middle_button_03.sub")

		upButton = Button()
		upButton.SetParent(self)
		upButton.SetUpVisual("d:/ymir work/ui/public/scrollbar_thin_up_button_01.sub")
		upButton.SetOverVisual("d:/ymir work/ui/public/scrollbar_thin_up_button_02.sub")
		upButton.SetDownVisual("d:/ymir work/ui/public/scrollbar_thin_up_button_03.sub")
		upButton.SetEvent(__mem_func__(self.OnUp))
		upButton.Show()

		downButton = Button()
		downButton.SetParent(self)
		downButton.SetUpVisual("d:/ymir work/ui/public/scrollbar_thin_down_button_01.sub")
		downButton.SetOverVisual("d:/ymir work/ui/public/scrollbar_thin_down_button_02.sub")
		downButton.SetDownVisual("d:/ymir work/ui/public/scrollbar_thin_down_button_03.sub")
		downButton.SetEvent(__mem_func__(self.OnDown))
		downButton.Show()

		self.middleBar = middleBar
		self.upButton = upButton
		self.downButton = downButton

		self.SCROLLBAR_WIDTH = self.upButton.GetWidth()
		self.SCROLLBAR_MIDDLE_HEIGHT = self.middleBar.GetHeight()
		self.SCROLLBAR_BUTTON_WIDTH = self.upButton.GetWidth()
		self.SCROLLBAR_BUTTON_HEIGHT = self.upButton.GetHeight()
		self.MIDDLE_BAR_POS = 0
		self.MIDDLE_BAR_UPPER_PLACE = 0
		self.MIDDLE_BAR_DOWNER_PLACE = 0
		self.TEMP_SPACE = 0

	def UpdateBarSlot(self):
		pass

class SmallThinScrollBar(ScrollBar):

	def CreateScrollBar(self):
		middleBar = self.MiddleBar()
		middleBar.SetParent(self)
		middleBar.SetMoveEvent(__mem_func__(self.OnMove))
		middleBar.Show()
		middleBar.SetUpVisual("d:/ymir work/ui/public/scrollbar_small_thin_middle_button_01.sub")
		middleBar.SetOverVisual("d:/ymir work/ui/public/scrollbar_small_thin_middle_button_01.sub")
		middleBar.SetDownVisual("d:/ymir work/ui/public/scrollbar_small_thin_middle_button_01.sub")

		upButton = Button()
		upButton.SetParent(self)
		upButton.SetUpVisual("d:/ymir work/ui/public/scrollbar_small_thin_up_button_01.sub")
		upButton.SetOverVisual("d:/ymir work/ui/public/scrollbar_small_thin_up_button_02.sub")
		upButton.SetDownVisual("d:/ymir work/ui/public/scrollbar_small_thin_up_button_03.sub")
		upButton.SetEvent(__mem_func__(self.OnUp))
		upButton.Show()

		downButton = Button()
		downButton.SetParent(self)
		downButton.SetUpVisual("d:/ymir work/ui/public/scrollbar_small_thin_down_button_01.sub")
		downButton.SetOverVisual("d:/ymir work/ui/public/scrollbar_small_thin_down_button_02.sub")
		downButton.SetDownVisual("d:/ymir work/ui/public/scrollbar_small_thin_down_button_03.sub")
		downButton.SetEvent(__mem_func__(self.OnDown))
		downButton.Show()

		self.middleBar = middleBar
		self.upButton = upButton
		self.downButton = downButton

		self.SCROLLBAR_WIDTH = self.upButton.GetWidth()
		self.SCROLLBAR_MIDDLE_HEIGHT = self.middleBar.GetHeight()
		self.SCROLLBAR_BUTTON_WIDTH = self.upButton.GetWidth()
		self.SCROLLBAR_BUTTON_HEIGHT = self.upButton.GetHeight()
		self.MIDDLE_BAR_POS = 0
		self.MIDDLE_BAR_UPPER_PLACE = 0
		self.MIDDLE_BAR_DOWNER_PLACE = 0
		self.TEMP_SPACE = 0

	def UpdateBarSlot(self):
		pass

class SliderBar(Window):

	def __init__(self):
		Window.__init__(self)

		self.curPos = 1.0
		self.pageSize = 1.0
		self.eventChange = None

		self.__CreateBackGroundImage()
		self.__CreateCursor()

	def __del__(self):
		Window.__del__(self)

	def __CreateBackGroundImage(self):
		img = ImageBox()
		img.SetParent(self)
		img.LoadImage("d:/ymir work/ui/game/windows/sliderbar.sub")
		img.Show()
		self.backGroundImage = img

		##
		self.SetSize(self.backGroundImage.GetWidth(), self.backGroundImage.GetHeight())

	def __CreateCursor(self):
		cursor = DragButton()
		cursor.AddFlag("movable")
		cursor.AddFlag("restrict_y")
		cursor.SetParent(self)
		cursor.SetMoveEvent(__mem_func__(self.__OnMove))
		cursor.SetUpVisual("d:/ymir work/ui/game/windows/sliderbar_cursor.sub")
		cursor.SetOverVisual("d:/ymir work/ui/game/windows/sliderbar_cursor.sub")
		cursor.SetDownVisual("d:/ymir work/ui/game/windows/sliderbar_cursor.sub")
		cursor.Show()
		self.cursor = cursor

		##
		self.cursor.SetRestrictMovementArea(0, 0, self.backGroundImage.GetWidth(), 0)
		self.pageSize = self.backGroundImage.GetWidth() - self.cursor.GetWidth()

	def __OnMove(self):
		(xLocal, yLocal) = self.cursor.GetLocalPosition()
		self.curPos = float(xLocal) / float(self.pageSize)

		if self.eventChange:
			self.eventChange()

	def SetSliderPos(self, pos):
		self.curPos = pos
		self.cursor.SetPosition(int(self.pageSize * pos), 0)

	def GetSliderPos(self):
		return self.curPos

	def SetEvent(self, event):
		self.eventChange = event

	def Enable(self):
		self.cursor.Show()

	def Disable(self):
		self.cursor.Hide()

class ListBox(Window):

	TEMPORARY_PLACE = 3

	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)
		self.overLine = -1
		self.selectedLine = -1
		self.width = 0
		self.height = 0
		self.stepSize = 17
		self.basePos = 0
		self.showLineCount = 0
		self.itemCenterAlign = True
		self.itemList = []
		self.keyDict = {}
		self.textDict = {}
		self.event = None
		self.args = None
		self.xPadding = 0
	def __del__(self):
		Window.__del__(self)

	def SetWidth(self, width):
		self.SetSize(width, self.height)

	def SetSize(self, width, height):
		Window.SetSize(self, width, height)
		self.width = width
		self.height = height

	def GetStepSize(self):
		return self.stepSize

	def SetTextCenterAlign(self, flag):
		self.itemCenterAlign = flag

	def SetBasePos(self, pos):
		self.basePos = pos
		self._LocateItem()

	def ClearItem(self):
		self.keyDict = {}
		self.textDict = {}
		self.itemList = []
		self.overLine = -1
		self.selectedLine = -1

	def InsertItem(self, number, text):
		self.keyDict[len(self.itemList)] = number
		self.textDict[len(self.itemList)] = text

		textLine = TextLine()
		textLine.SetParent(self)
		textLine.SetText(text)
		textLine.Show()

		if self.itemCenterAlign:
			textLine.SetWindowHorizontalAlignCenter()
			textLine.SetHorizontalAlignCenter()

		self.itemList.append(textLine)

		self._LocateItem()

	def ChangeItem(self, number, text):
		for key, value in self.keyDict.items():
			if value == number:
				self.textDict[key] = text

				if number < len(self.itemList):
					self.itemList[key].SetText(text)

				return

	def LocateItem(self):
		self._LocateItem()

	def _LocateItem(self):

		skipCount = self.basePos
		yPos = 0
		self.showLineCount = 0

		for textLine in self.itemList:
			textLine.Hide()

			if skipCount > 0:
				skipCount -= 1
				continue

			textLine.SetPosition(self.xPadding, yPos + 3)
			yPos += self.stepSize

			if yPos <= self.GetHeight():
				self.showLineCount += 1
				textLine.Show()

	def ArrangeItem(self):
		self.SetSize(self.width, len(self.itemList) * self.stepSize)
		self._LocateItem()

	def GetViewItemCount(self):
		return int(self.GetHeight() / self.stepSize)

	def GetItemCount(self):
		return len(self.itemList)

	def SetEvent(self, event, *args):
		self.event = event
		self.args = args

	def SelectItem(self, line):

		if not self.keyDict.has_key(line):
			return

		if line == self.selectedLine:
			return

		self.selectedLine = line
		if self.event:
			apply(self.event, self.args + (self.keyDict.get(line, 0), self.textDict.get(line, "None"),))

	def GetSelectedItem(self):
		return self.keyDict.get(self.selectedLine, 0)

	def OnMouseLeftButtonDown(self):
		if self.overLine < 0:
			return

	def OnMouseLeftButtonUp(self):
		if self.overLine >= 0:
			self.SelectItem(self.overLine+self.basePos)

	def OnUpdate(self):

		self.overLine = -1

		if self.IsIn():
			x, y = self.GetGlobalPosition()
			height = self.GetHeight()
			xMouse, yMouse = wndMgr.GetMousePosition()

			if yMouse - y < height - 1:
				self.overLine = (yMouse - y) / self.stepSize

				if self.overLine < 0:
					self.overLine = -1
				if self.overLine >= len(self.itemList):
					self.overLine = -1

	def OnRender(self):
		xRender, yRender = self.GetGlobalPosition()
		yRender -= self.TEMPORARY_PLACE
		widthRender = self.width
		heightRender = self.height + self.TEMPORARY_PLACE*2

		if -1 != self.overLine:
			(rLeft, rTop, rRight, rBottom) = self.itemList[self.overLine].GetRenderBox()
			grp.SetColor(HALF_WHITE_COLOR)
			grp.RenderBar(xRender + 2 + rLeft, yRender + self.overLine*self.stepSize + 4 + rTop, self.width - 3 - rRight - rLeft, self.stepSize - rBottom - rTop)

		if -1 != self.selectedLine:
			if self.selectedLine >= self.basePos:
				if self.selectedLine - self.basePos < self.showLineCount:
					(rLeft, rTop, rRight, rBottom) = self.itemList[self.selectedLine].GetRenderBox()
					grp.SetColor(SELECT_COLOR)
					grp.RenderBar(xRender + 2 + rLeft, yRender + (self.selectedLine-self.basePos)*self.stepSize + 4 + rTop, self.width - 3 - rRight - rLeft, self.stepSize - rBottom - rTop)



class ListBox2(ListBox):
	def __init__(self, *args, **kwargs):
		ListBox.__init__(self, *args, **kwargs)
		self.rowCount = 10
		self.barWidth = 0
		self.colCount = 0

	def SetRowCount(self, rowCount):
		self.rowCount = rowCount

	def SetSize(self, width, height):
		ListBox.SetSize(self, width, height)
		self._RefreshForm()

	def ClearItem(self):
		ListBox.ClearItem(self)
		self._RefreshForm()

	def InsertItem(self, *args, **kwargs):
		ListBox.InsertItem(self, *args, **kwargs)
		self._RefreshForm()

	def OnUpdate(self):
		mpos = wndMgr.GetMousePosition()
		self.overLine = self._CalcPointIndex(mpos)

	def OnRender(self):
		x, y = self.GetGlobalPosition()
		pos = (x + 2, y)

		if -1 != self.overLine:
			grp.SetColor(HALF_WHITE_COLOR)
			self._RenderBar(pos, self.overLine)

		if -1 != self.selectedLine:
			if self.selectedLine >= self.basePos:
				if self.selectedLine - self.basePos < self.showLineCount:
					grp.SetColor(SELECT_COLOR)
					self._RenderBar(pos, self.selectedLine-self.basePos)

	

	def _CalcPointIndex(self, mpos):
		if self.IsIn():
			px, py = mpos
			gx, gy = self.GetGlobalPosition()
			lx, ly = px - gx, py - gy

			col = lx / self.barWidth
			row = ly / self.stepSize
			idx = col * self.rowCount + row
			if col >= 0 and col < self.colCount:
				if row >= 0 and row < self.rowCount:
					if idx >= 0 and idx < len(self.itemList):
						return idx
		
		return -1

	def _CalcRenderPos(self, pos, idx):
		x, y = pos
		row = idx % self.rowCount
		col = idx / self.rowCount
		return (x + col * self.barWidth, y + row * self.stepSize)

	def _RenderBar(self, basePos, idx):
		x, y = self._CalcRenderPos(basePos, idx)
		grp.RenderBar(x, y, self.barWidth - 3, self.stepSize)

	def _LocateItem(self):
		pos = (0, self.TEMPORARY_PLACE)

		self.showLineCount = 0
		for textLine in self.itemList:
			x, y = self._CalcRenderPos(pos, self.showLineCount)
			textLine.SetPosition(x, y)
			textLine.Show()

			self.showLineCount += 1

	def _RefreshForm(self):
		if len(self.itemList) % self.rowCount:
			self.colCount = len(self.itemList) / self.rowCount + 1
		else:
			self.colCount = len(self.itemList) / self.rowCount

		if self.colCount:
			self.barWidth = self.width / self.colCount
		else:
			self.barWidth = self.width


class ComboBox(Window):

	class ListBoxWithBoard(ListBox):

		def __init__(self, layer = "UI"):
			ListBox.__init__(self, layer)

		def OnRender(self):
			xRender, yRender = self.GetGlobalPosition()
			yRender -= self.TEMPORARY_PLACE
			widthRender = self.width
			heightRender = self.height + self.TEMPORARY_PLACE*2
			grp.SetColor(BACKGROUND_COLOR)
			grp.RenderBar(xRender, yRender, widthRender, heightRender)
			grp.SetColor(DARK_COLOR)
			grp.RenderLine(xRender, yRender, widthRender, 0)
			grp.RenderLine(xRender, yRender, 0, heightRender)
			grp.SetColor(BRIGHT_COLOR)
			grp.RenderLine(xRender, yRender+heightRender, widthRender, 0)
			grp.RenderLine(xRender+widthRender, yRender, 0, heightRender)

			ListBox.OnRender(self)

	def __init__(self):
		Window.__init__(self)
		self.x = 0
		self.y = 0
		self.width = 0
		self.height = 0
		self.isSelected = False
		self.isOver = False
		self.isListOpened = False
		self.event = lambda *arg: None
		self.enable = True

		self.AddFlag("float")

		self.textLine = MakeTextLine(self)
		self.textLine.SetText(localeInfo.UI_ITEM)

		self.listBox = self.ListBoxWithBoard()
		self.listBox.SetPickAlways()
		self.listBox.SetParent(self)
		self.listBox.SetEvent(__mem_func__(self.OnSelectItem))
		self.listBox.Hide()

	def __del__(self):
		Window.__del__(self)

	def Destroy(self):
		self.textLine = None
		self.listBox = None

	def SetPosition(self, x, y):
		Window.SetPosition(self, x, y)
		self.x = x
		self.y = y
		self.__ArrangeListBox()

	def SetTextAlign(self, align):
		if align == "center":
			self.textLine.SetWindowHorizontalAlignCenter()
			self.textLine.SetHorizontalAlignCenter()
		elif align == "left":
			self.textLine.SetWindowHorizontalAlignLeft()
			self.textLine.SetHorizontalAlignLeft()

	def SetTextPos(self, xpos):
		self.textLine.SetPosition(xpos, 0)

	def SetSize(self, width, height):
		Window.SetSize(self, width, height)
		self.width = width
		self.height = height
		self.textLine.UpdateRect()
		self.__ArrangeListBox()

	def __ArrangeListBox(self):
		self.listBox.SetPosition(0, self.height + 5)
		self.listBox.SetWidth(self.width)

	def Enable(self):
		self.enable = True

	def Disable(self):
		self.enable = False
		self.textLine.SetText("")
		self.CloseListBox()

	def SetEvent(self, event):
		self.event = event


	def ClearItem(self):
		self.CloseListBox()
		self.listBox.ClearItem()

	def InsertItem(self, index, name):
		self.listBox.InsertItem(index, name)
		self.listBox.ArrangeItem()

	def SetCurrentItem(self, text):
		self.textLine.SetText(text)

	def SelectItem(self, key):
		self.listBox.SelectItem(key)

	def OnSelectItem(self, index, name):

		self.CloseListBox()
		self.SetCurrentItem(name)
		self.event(index)

	def CloseListBox(self):
		self.isListOpened = False
		self.listBox.Hide()

	def OnMouseLeftButtonDown(self):

		if not self.enable:
			return

		self.isSelected = True

	def OnMouseLeftButtonUp(self):

		if not self.enable:
			return

		self.isSelected = False

		if self.isListOpened:
			self.CloseListBox()
		else:
			if self.listBox.GetItemCount() > 0:
				self.isListOpened = True
				self.listBox.Show()
				self.__ArrangeListBox()
				self.SetTop()

	def OnUpdate(self):

		if not self.enable:
			return

		if self.IsIn():
			self.isOver = True
		else:
			self.isOver = False

	def OnRender(self):
		self.x, self.y = self.GetGlobalPosition()
		xRender = self.x
		yRender = self.y
		widthRender = self.width
		heightRender = self.height
		grp.SetColor(BACKGROUND_COLOR)
		grp.RenderBar(xRender, yRender, widthRender, heightRender)
		grp.SetColor(DARK_COLOR)
		grp.RenderLine(xRender, yRender, widthRender, 0)
		grp.RenderLine(xRender, yRender, 0, heightRender)
		grp.SetColor(BRIGHT_COLOR)
		grp.RenderLine(xRender, yRender+heightRender, widthRender, 0)
		grp.RenderLine(xRender+widthRender, yRender, 0, heightRender)

		if self.isOver:
			grp.SetColor(HALF_WHITE_COLOR)
			grp.RenderBar(xRender + 2, yRender + 3, self.width - 3, heightRender - 5)

			if self.isSelected:
				grp.SetColor(WHITE_COLOR)
				grp.RenderBar(xRender + 2, yRender + 3, self.width - 3, heightRender - 5)

class TextDropdown(Window):
	class Item(ListBoxEx.Item):
		def __init__(self, text):
			ListBoxEx.Item.__init__(self)

			textline = TextLine()
			textline.SetParent(self)
			textline.SetText(text)
			textline.Show()
			self.text = textline
		
		def __del__(self):
			ListBoxEx.Item.__del__(self)
		
		def SetArgs(self, argv):
			self.argv = argv

		def GetArgs(self):
			return self.argv

		def GetText(self):
			return self.text.GetText()

	def __init__(self, layer="UI"):
		Window.__init__(self, layer)
		self.select_event = None
		self.open_event = None
		self.close_event = None
		self.index = 0
		self.is_enabled = True

	def Create(self, width, height, item_height):
		self.SetSize(width, height)

		self.default_width = width
		self.default_height = height

		button = Bar()
		button.SetParent(self)
		button.SetSize(width, height)
		button.SetColor(TRANSPARENT)
		button.Show()
		button.OnMouseLeftButtonUp = self.Toggle
		self.button = button

		text = TextLine()
		text.SetParent(self.button)
		text.SetHorizontalAlignCenter()
		text.SetVerticalAlignCenter()
		text.SetText("---")
		text.SetPosition(width/2, height/2)
		text.Show()
		self.text = text

		dw = Bar()
		dw.SetParent(self)
		dw.SetSize(width, height)
		dw.SetPosition(0, height - 1)
		dw.Hide()
		self.drop_window = dw

		sb = ThinScrollBar()
		sb.SetParent(self.drop_window)
		sb.SetPosition(self.drop_window.GetWidth() - ScrollBar.SCROLLBAR_WIDTH, 1)
		sb.SetScrollBarSize(10)
		sb.Hide()
		self.scrollbar = sb

		dl = ListBoxEx()
		dl.SetParent(self.drop_window)
		dl.SetItemSize(width - ScrollBar.SCROLLBAR_WIDTH, item_height)
		dl.SetItemStep(item_height + 2)
		dl.SetScrollBar(self.scrollbar)
		dl.SetSelectEvent(self.Select)
		dl.Hide()
		self.drop_list = dl
	
	def __del__(self):
		del self.drop_window
		del self.drop_list
		del self.scrollbar
		del self.select_event
		del self.open_event
		del self.close_event
		Window.__del__(self)

	def SetIndex(self, index):
		self.index = index

	def GetIndex(self):
		return self.index

	def Append(self, text, *argv):
		item = self.Item(text)
		item.SetArgs(argv)
		self.drop_list.AppendItem(item)

		count = min(self.drop_list.GetItemCount(), self.drop_list.GetViewItemCount())
		self.drop_window.SetSize(self.GetWidth(), count * self.drop_list.GetItemStep())
		self.scrollbar.SetScrollBarSize(self.drop_window.GetHeight() - 2)

	def Select(self, item):
		if self.select_event is not None:
			self.select_event(self, item)

	def SetViewItemCount(self, count):
		self.drop_list.SetViewItemCount(count)

	def SetDefaultText(self, text):
		self.text.SetText(text)

	def OnRender(self):
		if not self.is_enabled:
			return

		if self.button.IsInPosition():
			self.button.SetColor(HALF_WHITE_COLOR)
		else:
			self.button.SetColor(TRANSPARENT)

	def Resize(self, expand=True):
		if expand is False:
			self.SetSize(self.GetWidth(), self.default_height)
		else:
			self.SetSize(self.GetWidth(), self.default_height + self.drop_window.GetHeight())

	def Toggle(self):
		if not self.is_enabled:
			return

		if self.drop_window.IsShow():
			self.drop_list.Hide()
			self.drop_window.Hide()
			self.Resize(False)

			if self.close_event is not None:
				self.close_event()
		else:
			self.drop_list.Show()
			self.drop_window.Show()

			if self.drop_list.GetItemCount() > self.drop_list.GetViewItemCount():
				self.scrollbar.Show()
			else:
				self.scrollbar.Hide()
			self.Resize()

			if self.open_event is not None:
				self.open_event()

	def SetSelectEvent(self, event):
		self.select_event = event

	def SetOpenEvent(self, event):
		self.open_event = event

	def SetCloseEvent(self, event):
		self.close_event = event

	def Disable(self):
		self.is_enabled = False

	def Enable(self):
		self.is_enabled = True

	def IsOpen(self):
		return self.drop_window.IsShow()

	def SelectItemByArg(self, index, value):
		for i in xrange(self.drop_list.GetItemCount()):
			item = self.drop_list.GetItemAtIndex(i)
			if item.GetArgs()[index] == value:
				self.drop_list.SelectItem(item)
				return


class InputField(Window):

	PATH = "d:/ymir work/ui/pattern/input_%s.tga"

	BORDER_SIZE = 1
	BASE_SIZE = 1

	L = 0
	R = 1
	T = 2
	B = 3

	def __init__(self, basePath = PATH):
		Window.__init__(self)

		self.isButtonStyle = False
		self.isButtonStyleOverOnly = False
		self.isDown = False
		self.renderData = {}

		self.onClickEvent = None
		self.onClickArgs = None

		self.MakeField(basePath)
		self.SetSize(0, 0)

		self.SetWindowName("NONAME_InputField")

	def __del__(self):
		Window.__del__(self)

	def MakeField(self, basePath):
		self.Lines = []
		for i in xrange(4):
			line = ExpandedImageBox()
			line.AddFlag("not_pick")
			line.SetParent(self)
			line.LoadImage(basePath % "border")
			line.Show()
			self.Lines.append(line)

		self.Lines[self.T].SetPosition(self.BORDER_SIZE, 0)
		self.Lines[self.B].SetPosition(self.BORDER_SIZE, 0)

		self.Base = ExpandedImageBox()
		self.Base.AddFlag("not_pick")
		self.Base.SetParent(self)
		self.Base.SetPosition(self.BORDER_SIZE, self.BORDER_SIZE)
		self.Base.LoadImage(basePath % "base")
		self.Base.Show()

	def SetSize(self, width, height):
		minSize = self.BORDER_SIZE * 2 + self.BASE_SIZE
		width = max(minSize, width)
		height = max(minSize, height)
		Window.SetSize(self, width, height)

		scaleH = float(width - self.BORDER_SIZE * 2 - self.BORDER_SIZE) / float(self.BORDER_SIZE)
		scaleV = float(height - self.BORDER_SIZE) / float(self.BORDER_SIZE)
		self.Lines[self.L].SetRenderingRect(0, 0, 0, scaleV)
		self.Lines[self.R].SetRenderingRect(0, 0, 0, scaleV)
		self.Lines[self.T].SetRenderingRect(0, 0, scaleH, 0)
		self.Lines[self.B].SetRenderingRect(0, 0, scaleH, 0)
		self.Lines[self.R].SetPosition(width - self.BORDER_SIZE, self.Lines[self.R].GetTop())
		self.Lines[self.B].SetPosition(self.Lines[self.B].GetLeft(), height - self.BORDER_SIZE)

		scaleH = float(width - self.BORDER_SIZE * 2 - self.BASE_SIZE) / float(self.BASE_SIZE)
		scaleV = float(height - self.BORDER_SIZE * 2 - self.BASE_SIZE) / float(self.BASE_SIZE)
		self.Base.SetRenderingRect(0, 0, scaleH, scaleV)

	def SetAlpha(self, alpha):
		for line in self.Lines:
			line.SetAlpha(alpha)
		self.Base.SetAlpha(alpha)

	def SetEvent(self, event, *args):
		self.onClickEvent = event
		self.onClickArgs = args

	def ClearEvent(self):
		self.onClickEvent = None

	def SetButtonStyle(self, isButtonStyle):
		self.isButtonStyle = isButtonStyle

		if self.isButtonStyle == False and (self.isButtonStyleOverOnly == False or not self.IsIn()):
			self.__ResetRenderData()

	def SetButtonStyleOverOnly(self, isButtonStyleOverOnly):
		self.isButtonStyleOverOnly = isButtonStyleOverOnly

		if self.isButtonStyleOverOnly == False:
			if self.isButtonStyle == False:
				self.__ResetRenderData()

	def __ResetRenderData(self):
		self.renderData = {"render" : False}

	def __SetRenderData(self, key, val):
		self.renderData["render"] = True
		self.renderData[key] = val

	def __GetRenderData(self, key):
		return self.renderData.get(key, False)

	def OnMouseOverIn(self):
		if self.isButtonStyle or self.isButtonStyleOverOnly:
			if self.isButtonStyle == False or self.isDown == False:
				self.__SetRenderData("color", HALF_WHITE_COLOR)
			elif self.isButtonStyle:
				self.__SetRenderData("color", SELECT_COLOR)

	def OnMouseOverOut(self):
		if self.isButtonStyle or self.isButtonStyleOverOnly:
			if self.isButtonStyle == False or self.isDown == False:
				self.__ResetRenderData()

	def OnMouseLeftButtonDown(self):
		Window.OnMouseLeftButtonDown(self)

		self.isDown = True
		if self.isButtonStyle:
			self.__SetRenderData("color", SELECT_COLOR)

	def OnMouseLeftButtonUp(self):
		Window.OnMouseLeftButtonUp(self)

		self.isDown = False
		self.__ResetRenderData()

		if self.IsIn():
			if self.isButtonStyle or self.isButtonStyleOverOnly:
				self.__SetRenderData("color", HALF_WHITE_COLOR)
			if self.onClickEvent:
				apply(self.onClickEvent, self.onClickArgs)

	def OnAfterRender(self):
		if not self.__GetRenderData("render"):
			return

		x, y, width, height = self.GetRect()
		grp.SetColor(self.__GetRenderData("color"))
		grp.RenderBar(x, y, width, height)

class VerticalBoard(Window):

	VB_TOP = 0
	VB_MID = 1
	VB_BOT = 2
	VB_COUNT = 3

	def __init__(self):
		Window.__init__(self)

		self.vboard_imageList = []

		for i in xrange(self.VB_COUNT):
			img = ExpandedImageBox()
			img.SetParent(self)
			img.Show()
			self.vboard_imageList.append(img)

	def __SetImage(self, pos, imgPath):
		self.__GetImage(pos).LoadImage(imgPath)

	def __GetImage(self, pos):
		return self.vboard_imageList[pos]

	def SetTopImage(self, imgPath):
		self.__SetImage(self.VB_TOP, imgPath)

	def SetMiddleImage(self, imgPath):
		self.__SetImage(self.VB_MID, imgPath)

	def SetBottomImage(self, imgPath):
		self.__SetImage(self.VB_BOT, imgPath)

	def SetHeight(self, height):
		self.SetSize(0, height)

	def SetSize(self, width, height):
		width = self.__GetImage(0).GetWidth()
		minHeight = -self.__GetImage(self.VB_MID).GetHeight()
		for i in xrange(self.VB_COUNT):
			minHeight += self.__GetImage(i).GetHeight()
		height = max(minHeight, height)

		Window.SetSize(self, width, height)
		self.__Resize()

	def __Resize(self):
		height = self.GetHeight()
		botImage = self.__GetImage(self.VB_BOT)
		botImage.SetPosition(0, height - botImage.GetHeight())
		midImage = self.__GetImage(self.VB_MID)
		midImage.SetPosition(0, self.__GetImage(self.VB_TOP).GetHeight())
		midHeight = height - self.__GetImage(self.VB_TOP).GetHeight() - botImage.GetHeight()
		midImage.SetRenderingRect(0.0, 0.0, 0.0, -1.0 + midHeight / float(midImage.GetHeight()))

class VerticalBoardWithTitleBar(VerticalBoard):

	TITLE_LEFT = 0
	TITLE_MID = 1
	TITLE_RIGHT = 2
	TITLE_COUNT = 3

	def __init__(self):
		VerticalBoard.__init__(self)

		self.titlePosY = 0
		self.titleBorderLeft = 0
		self.titleBorderRight = 0

		self.title_imageList = []
		for i in xrange(self.VB_COUNT):
			img = ExpandedImageBox()
			img.SetParent(self)
			img.AddFlag("attach")
			img.Show()
			self.title_imageList.append(img)

		textLine = TextLine()
		textLine.SetParent(self)
		textLine.SetHorizontalAlignCenter()
		textLine.SetVerticalAlignCenter()
		textLine.Show()
		self.title_TextLine = textLine

	def __SetImage(self, pos, imgPath):
		self.__GetImage(pos).LoadImage(imgPath)

	def __GetImage(self, pos):
		return self.title_imageList[pos]

	def SetTitleLeftImage(self, imgPath):
		self.__SetImage(self.TITLE_LEFT, imgPath)

	def SetTitleMiddleImage(self, imgPath):
		self.__SetImage(self.TITLE_MID, imgPath)

	def SetTitleRightImage(self, imgPath):
		self.__SetImage(self.TITLE_RIGHT, imgPath)

	def SetTitlePosY(self, posY):
		self.titlePosY = int(posY)

	def SetTitleBorderLeft(self, borderLeft):
		self.titleBorderLeft = int(borderLeft)

	def SetTitleBorderRight(self, borderRight):
		self.titleBorderRight = int(borderRight)

	def SetTitleText(self, text):
		self.title_TextLine.SetText(text)

	def SetSize(self, width, height):
		VerticalBoard.SetSize(self, width, height)
		self.__ResizeTitle()

	def __ResizeTitle(self):
		titleWidth = self.GetWidth() - self.titleBorderLeft - self.titleBorderRight
		leftImg = self.__GetImage(self.TITLE_LEFT)
		leftImg.SetPosition(self.titleBorderLeft, self.titlePosY)
		rightImg = self.__GetImage(self.TITLE_RIGHT)
		rightImg.SetPosition(self.GetWidth() - self.titleBorderRight - rightImg.GetWidth(), self.titlePosY)
		midImg = self.__GetImage(self.TITLE_MID)
		midImg.SetPosition(self.titleBorderLeft + leftImg.GetWidth(), self.titlePosY)
		midWidth = titleWidth - leftImg.GetWidth() - rightImg.GetWidth()
		midImg.SetRenderingRect(0.0, 0.0, -1.0 + midWidth / float(midImg.GetWidth()), 0.0)

		self.title_TextLine.SetPosition(self.titleBorderLeft + titleWidth / 2, self.titlePosY + self.__GetImage(0).GetHeight() / 2)

###################################################################################################
## Python Script Loader
###################################################################################################

class ScriptWindow(Window):
	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)
		self.Children = []
		self.ElementDictionary = {}

	def __del__(self):
		Window.__del__(self)

	def ClearDictionary(self):
		self.Children = []
		self.ElementDictionary = {}

	def InsertChild(self, name, child):
		self.ElementDictionary[name] = child

	def IsChild(self, name):
		return self.ElementDictionary.has_key(name)

	def GetChild(self, name):
		return self.ElementDictionary[name]

	def GetChild2(self, name):
		return self.ElementDictionary.get(name, None)

class BaseScriptWindow(ScriptWindow):
	def __init__(self, scriptFileName, initFunc=None, layer="UI"):
		ScriptWindow.__init__(self, layer)
		self.SetWindowName(scriptFileName)

		self.initObjectDict = {}
		self.main = {}
		self.onCloseEvent = None

		if initFunc:
			initFunc()

		self.__LoadScript(scriptFileName)
		self.__LoadBaseWindow()

	def __del__(self):
		ScriptWindow.__del__(self)

	def _AddLoadObject(self, name, scriptKey):
		self.initObjectDict[name] = scriptKey

	def __LoadScript(self, scriptFileName):
		try:
			pyScrLoader = PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/%s.py" % scriptFileName)
		except:
			import exception
			exception.Abort("BaseScriptWindow.LoadDialog.LoadScript")

	def __LoadBaseWindow_LoadInDict(self, resultDict, readDict):
		for key in readDict:
			if type(readDict[key]) == dict:
				resultDict[key] = {}
				self.__LoadBaseWindow_LoadInDict(resultDict[key], readDict[key])
			elif type(readDict[key]) == list:
				newDict = {}
				i = 0
				for val in readDict[key]:
					newDict[i] = val
					i += 1

				resultDict[key] = {}
				self.__LoadBaseWindow_LoadInDict(resultDict[key], newDict)
			else:
				resultDict[key] = self.GetChild(readDict[key])

	def __LoadBaseWindow(self):
		try:
			GetObject=self.GetChild
			self.__LoadBaseWindow_LoadInDict(self.main, self.initObjectDict)

		except:
			import exception
			exception.Abort("BaseScriptWindow.LoadDialog.BindObject")

		try:
			self.board = GetObject("board")
			self.board.SetCloseEvent(self.Close)
		except:
			pass

	def Destroy(self):
		self.Close()
		Window.Destroy(self)

	def Open(self):
		if self.onCloseEvent != None:
			self.onCloseEvent()
		self.SetCenterPosition()
		self.Show()
		self.SetTop()

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True

class PythonScriptLoader(object):

	BODY_KEY_LIST = ( "x", "y", "width", "height" )

	#####

	DEFAULT_KEY_LIST = ( "type", "x", "y", )
	WINDOW_KEY_LIST = ( "width", "height", )
	IMAGE_KEY_LIST = ( "image", )
	EXPANDED_IMAGE_KEY_LIST = ( "image", )
	ANI_IMAGE_KEY_LIST = ( "images", )
	SLOT_KEY_LIST = ( "width", "height", "slot", )
	CANDIDATE_LIST_KEY_LIST = ( "item_step", "item_xsize", "item_ysize", )
	GRID_TABLE_KEY_LIST = ( "start_index", "x_count", "y_count", "x_step", "y_step", )
	EDIT_LINE_KEY_LIST = ( "width", "height", "input_limit", )
	COMBO_BOX_KEY_LIST = ( "width", "height", )
	TITLE_BAR_KEY_LIST = ( "width", )
	HORIZONTAL_BAR_KEY_LIST = ( "width", )
	BOARD_KEY_LIST = ( "width", "height", )
	BOARD_WITH_TITLEBAR_KEY_LIST = ( "width", "height", )
	VERTICAL_BOARD_KEY_LIST = ( "height", "top_image", "mid_image", "bot_image", )
	VERTICAL_BOARD_WITH_TITLEBAR_KEY_LIST = VERTICAL_BOARD_KEY_LIST + ( "title_left_image", "title_mid_image", "title_right_image", "title", )
	BOX_KEY_LIST = ( "width", "height", )
	BAR_KEY_LIST = ( "width", "height", )
	LINE_KEY_LIST = ( "width", "height", )
	SLOTBAR_KEY_LIST = ( "width", "height", )
	GAUGE_KEY_LIST = ( "width", "color", )
	SCROLLBAR_KEY_LIST = ( "size", )
	SCROLLBAR_TEMPLATE_KEY_LIST = SCROLLBAR_KEY_LIST + ( "middle_image", )
	LIST_BOX_KEY_LIST = ( "width", "height", )
	INPUT_FIELD_KEY_LIST = ("width", "height", )
	TEXT_DROPDOWN_KEY_LIST = ("width", "height", "item_height")

	def __init__(self):
		self.Clear()

	def Clear(self):
		self.ScriptDictionary = {
			"SCREEN_WIDTH" : wndMgr.GetScreenWidth(),
			"SCREEN_HEIGHT" : wndMgr.GetScreenHeight(),
			# BOARD
			"BOARD_PADDING_TOP" : Board.PADDING[Board.T],
			"BOARD_PADDING_LEFT" : Board.PADDING[Board.L],
			"BOARD_PADDING_BOTTOM" : Board.PADDING[Board.B],
			"BOARD_PADDING_RIGHT" : Board.PADDING[Board.R],
		}
		self.InsertFunction = 0

	def LoadScriptFile(self, window, FileName):

		self.Clear()

		print "===== Load Script File : %s" % (FileName)

		DesignFileName = FileName[:FileName.rfind(".py")] + "_" + app.GetSelectedDesignName() + ".py"
		if timer.Exists(DesignFileName):
			FileName = DesignFileName

		if __USE_CYTHON__:
			# sub functions
			from os.path import splitext as op_splitext, basename as op_basename
			def GetModName(filename):
				return op_splitext(op_basename(filename))[0]

			# module name to import
			modname = GetModName(FileName.lower())
			# lazy loading of uiscriptlib
			import uiscriptlib
			# copy scriptdictionary stuff to builtin scope (otherwise, import will fail)
			tpl2Main = (
				"SCREEN_WIDTH","SCREEN_HEIGHT",
				"BOARD_PADDING_TOP", "BOARD_PADDING_LEFT","BOARD_PADDING_BOTTOM","BOARD_PADDING_RIGHT"
			)
			import __builtin__ as bt
			for idx in tpl2Main:
				tmpVal = self.ScriptDictionary[idx]
				exec "bt.%s = tmpVal"%idx in globals(), locals()

		try:
			if __USE_CYTHON__ and uiscriptlib.isExist(modname):
				m1 = uiscriptlib.moduleImport(modname)
				self.ScriptDictionary["window"] = m1.window.copy()
				del m1
			else:
				execfile(FileName, self.ScriptDictionary)
		except:
			import exception
			dbg.TraceError("Failed to load script file : %s" % (FileName))
			exception.Abort("LoadScriptFile")
		
		#####

		Body = self.ScriptDictionary["window"]
		self.CheckKeyList("window", Body, self.BODY_KEY_LIST)

		dbg.TraceError("LoadWindow [%s]" % Body.get("name", "<file:%s>" % FileName), dbg.IsEnabled())

		window.ClearDictionary()
		self.InsertFunction = window.InsertChild

		window.SetPosition(int(Body["x"]), int(Body["y"]))
		window.SetSize(int(Body["width"]), int(Body["height"]))
		if True == Body.has_key("style"):
			for StyleList in Body["style"]:
				window.AddFlag(StyleList)

		self.LoadChildren(window, Body, window)

	def LoadChildren(self, parent, dicChildren, mainParent):

		if False == dicChildren.has_key("children"):
			return False

		Index = 0

		ChildrenList = dicChildren["children"]
		parent.Children = range(len(ChildrenList))
		for ElementValue in ChildrenList:
			try:
				Name = ElementValue["name"]				
			except KeyError:
				Name = ElementValue["name"] = "NONAME"
				
			try:
				Type = ElementValue["type"]
			except KeyError:								
				Type = ElementValue["type"] = "window"				

			if False == self.CheckKeyList(Name, ElementValue, self.DEFAULT_KEY_LIST):
				del parent.Children[Index]
				continue

			if Type == "window":
				parent.Children[Index] = ScriptWindow()
				parent.Children[Index].SetParent(parent)
				self.LoadElementWindow(parent.Children[Index], ElementValue, parent)

			elif Type == "button":
				parent.Children[Index] = Button()
				parent.Children[Index].SetParent(parent)
				self.LoadElementButton(parent.Children[Index], ElementValue, parent)

			elif Type == "state_button":
				parent.Children[Index] = StateButton()
				parent.Children[Index].SetParent(parent)
				self.LoadElementStateButton(parent.Children[Index], ElementValue, parent)

			elif Type == "radio_button":
				parent.Children[Index] = RadioButton()
				parent.Children[Index].SetParent(parent)
				self.LoadElementButton(parent.Children[Index], ElementValue, parent)

			elif Type == "toggle_button":
				parent.Children[Index] = ToggleButton()
				parent.Children[Index].SetParent(parent)
				self.LoadElementButton(parent.Children[Index], ElementValue, parent)

			elif Type == "mark":
				parent.Children[Index] = MarkBox()
				parent.Children[Index].SetParent(parent)
				self.LoadElementMark(parent.Children[Index], ElementValue, parent)

			elif Type == "image":
				parent.Children[Index] = ImageBox()
				parent.Children[Index].SetParent(parent)
				self.LoadElementImage(parent.Children[Index], ElementValue, parent)

			elif Type == "expanded_image":
				parent.Children[Index] = ExpandedImageBox()
				parent.Children[Index].SetParent(parent)
				self.LoadElementExpandedImage(parent.Children[Index], ElementValue, parent)

			elif Type == "ani_image":
				parent.Children[Index] = AniImageBox()
				parent.Children[Index].SetParent(parent)
				self.LoadElementAniImage(parent.Children[Index], ElementValue, parent)

			elif Type == "limit_text":
				parent.Children[Index] = LimitTextLine()
				parent.Children[Index].SetParent(parent)
				self.LoadElementLimitText(parent.Children[Index], ElementValue, parent)

			elif Type == "slot":
				parent.Children[Index] = SlotWindow()
				parent.Children[Index].SetParent(parent)
				self.LoadElementSlot(parent.Children[Index], ElementValue, parent)

			elif Type == "slot_background":
				parent.Children[Index] = SlotBackground()
				parent.Children[Index].SetParent(parent)
				self.LoadElementSlotBackground(parent.Children[Index], ElementValue, parent)

			elif Type == "candidate_list":
				parent.Children[Index] = CandidateListBox()
				parent.Children[Index].SetParent(parent)
				self.LoadElementCandidateList(parent.Children[Index], ElementValue, parent)

			elif Type == "grid_table":
				parent.Children[Index] = GridSlotWindow()
				parent.Children[Index].SetParent(parent)
				self.LoadElementGridTable(parent.Children[Index], ElementValue, parent)

			elif Type == "text":
				parent.Children[Index] = TextLine()
				parent.Children[Index].SetParent(parent)
				self.LoadElementText(parent.Children[Index], ElementValue, parent)

			elif Type == "extended_text":
				parent.Children[Index] = ExtendedTextLine()
				parent.Children[Index].SetParent(parent)
				self.LoadElementExtendedText(parent.Children[Index], ElementValue, parent)

			elif Type == "multi_text":
				parent.Children[Index] = MultiTextLine()
				parent.Children[Index].SetParent(parent)
				self.LoadElementMultiText(parent.Children[Index], ElementValue, parent)

			elif Type == "checkbox":
				parent.Children[Index] = CheckBox()
				parent.Children[Index].SetParent(parent)
				self.LoadElementCheckBox(parent.Children[Index], ElementValue, parent)

			elif Type == "editline":
				parent.Children[Index] = EditLine()
				parent.Children[Index].SetParent(parent)
				self.LoadElementEditLine(parent.Children[Index], ElementValue, parent)

			elif Type == "titlebar":
				parent.Children[Index] = TitleBar()
				parent.Children[Index].SetParent(parent)
				self.LoadElementTitleBar(parent.Children[Index], ElementValue, parent)

			elif Type == "horizontalbar":
				parent.Children[Index] = HorizontalBar()
				parent.Children[Index].SetParent(parent)
				self.LoadElementHorizontalBar(parent.Children[Index], ElementValue, parent)

			elif Type == "board":
				padding = Board.PADDING
				if ElementValue.has_key("padding"):
					padding = ElementValue["padding"]

				parent.Children[Index] = Board(padding)
				parent.Children[Index].SetParent(parent)
				self.LoadElementBoard(parent.Children[Index], ElementValue, parent)

				child = parent.Children[Index]
				mainParent.SetSize(mainParent.GetWidth() + child.PADDING[Board.L] + child.PADDING[Board.R], mainParent.GetHeight() + child.PADDING[Board.T] + child.PADDING[Board.B])

			elif Type == "board_with_titlebar":
				padding = BoardWithTitleBar.PADDING
				if ElementValue.has_key("padding"):
					padding = ElementValue["padding"]

				parent.Children[Index] = BoardWithTitleBar(padding)
				parent.Children[Index].SetParent(parent)
				self.LoadElementBoardWithTitleBar(parent.Children[Index], ElementValue, parent)

				child = parent.Children[Index]
				mainParent.SetSize(mainParent.GetWidth() + child.PADDING[Board.L] + child.PADDING[Board.R], mainParent.GetHeight() + child.PADDING[Board.T] + child.PADDING[Board.B])

			elif Type == "thinboard":
				parent.Children[Index] = ThinBoard()
				parent.Children[Index].SetParent(parent)
				self.LoadElementThinBoard(parent.Children[Index], ElementValue, parent)

			elif Type == "thinboard_gold":
				parent.Children[Index] = ThinBoardGold()
				parent.Children[Index].SetParent(parent)
				self.LoadElementThinBoard(parent.Children[Index], ElementValue, parent)

			elif Type == "thinboard_circle":
				parent.Children[Index] = ThinBoardCircle()
				parent.Children[Index].SetParent(parent)
				self.LoadElementThinBoard(parent.Children[Index], ElementValue, parent)

			elif Type == "vboard":
				parent.Children[Index] = VerticalBoard()
				parent.Children[Index].SetParent(parent)
				self.LoadElementVerticalBoard(parent.Children[Index], ElementValue, parent)

			elif Type == "vboard_with_titlebar":
				parent.Children[Index] = VerticalBoardWithTitleBar()
				parent.Children[Index].SetParent(parent)
				self.LoadElementVerticalBoardWithTitleBar(parent.Children[Index], ElementValue, parent)

			elif Type == "box":
				parent.Children[Index] = Box()
				parent.Children[Index].SetParent(parent)
				self.LoadElementBox(parent.Children[Index], ElementValue, parent)

			elif Type == "bar":
				parent.Children[Index] = Bar()
				parent.Children[Index].SetParent(parent)
				self.LoadElementBar(parent.Children[Index], ElementValue, parent)

			elif Type == "line":
				parent.Children[Index] = Line()
				parent.Children[Index].SetParent(parent)
				self.LoadElementLine(parent.Children[Index], ElementValue, parent)

			elif Type == "slotbar":
				parent.Children[Index] = SlotBar()
				parent.Children[Index].SetParent(parent)
				self.LoadElementSlotBar(parent.Children[Index], ElementValue, parent)

			elif Type == "gauge":
				parent.Children[Index] = Gauge()
				parent.Children[Index].SetParent(parent)
				self.LoadElementGauge(parent.Children[Index], ElementValue, parent)

			elif Type == "scrollbar_template":
				parent.Children[Index] = ScrollBarTemplate()
				parent.Children[Index].SetParent(parent)
				self.LoadElementScrollBarTemplate(parent.Children[Index], ElementValue, parent)

			elif Type == "scrollbar":
				parent.Children[Index] = ScrollBar()
				parent.Children[Index].SetParent(parent)
				self.LoadElementScrollBar(parent.Children[Index], ElementValue, parent)

			elif Type == "thin_scrollbar":
				parent.Children[Index] = ThinScrollBar()
				parent.Children[Index].SetParent(parent)
				self.LoadElementScrollBar(parent.Children[Index], ElementValue, parent)

			elif Type == "small_thin_scrollbar":
				parent.Children[Index] = SmallThinScrollBar()
				parent.Children[Index].SetParent(parent)
				self.LoadElementScrollBar(parent.Children[Index], ElementValue, parent)

			elif Type == "sliderbar":
				parent.Children[Index] = SliderBar()
				parent.Children[Index].SetParent(parent)
				self.LoadElementSliderBar(parent.Children[Index], ElementValue, parent)

			elif Type == "listbox":
				parent.Children[Index] = ListBox()
				parent.Children[Index].SetParent(parent)
				self.LoadElementListBox(parent.Children[Index], ElementValue, parent)

			elif Type == "listbox2":
				parent.Children[Index] = ListBox2()
				parent.Children[Index].SetParent(parent)
				self.LoadElementListBox2(parent.Children[Index], ElementValue, parent)
			elif Type == "listboxex":
				parent.Children[Index] = ListBoxEx()
				parent.Children[Index].SetParent(parent)
				self.LoadElementListBoxEx(parent.Children[Index], ElementValue, parent)

			elif Type == "field":
				if ElementValue.has_key("path"):
					parent.Children[Index] = InputField(ElementValue["path"])
				else:
					parent.Children[Index] = InputField()
					
				parent.Children[Index].SetParent(parent)
				self.LoadElementInputField(parent.Children[Index], ElementValue, parent)

			elif Type == "combobox":
				parent.Children[Index] = ComboBox()
				parent.Children[Index].SetParent(parent)
				self.LoadElementComboBox(parent.Children[Index], ElementValue, parent)

			elif Type == "render_target":
				parent.Children[Index] = RenderTarget()
				parent.Children[Index].SetParent(parent)
				self.LoadElementRenderTarget(parent.Children[Index], ElementValue, parent)

			elif Type == "text_dropdown":
				parent.Children[Index] = TextDropdown()
				parent.Children[Index].SetParent(parent)
				self.LoadElementTextDropdown(parent.Children[Index], ElementValue, parent)
			else:
				Index += 1
				continue

			parent.Children[Index].SetWindowName(Name)
			if 0 != self.InsertFunction:
				self.InsertFunction(Name, parent.Children[Index])

			if True == ElementValue.has_key("style"):
				for StyleList in ElementValue["style"]:
					parent.Children[Index].AddFlag(StyleList)

			self.LoadChildren(parent.Children[Index], ElementValue, mainParent)
			Index += 1

	def CheckKeyList(self, name, value, key_list):

		for DataKey in key_list:
			if False == value.has_key(DataKey):
				print "Failed to find data key", "[" + name + "/" + DataKey + "]"
				return False

		return True

	def LoadDefaultData(self, window, value, parentWindow):
		loc_x = int(value["x"])
		loc_y = int(value["y"])
		if value.has_key("vertical_align"):
			if "center" == value["vertical_align"]:
				window.SetWindowVerticalAlignCenter()
			elif "bottom" == value["vertical_align"]:
				window.SetWindowVerticalAlignBottom()

		if parentWindow.IsRTL():
			loc_x = int(value["x"]) + window.GetWidth()
			if value.has_key("horizontal_align"):
				if "center" == value["horizontal_align"]:
					window.SetWindowHorizontalAlignCenter()
					loc_x = - int(value["x"])
				elif "right" == value["horizontal_align"]:
					window.SetWindowHorizontalAlignLeft()
					loc_x = int(value["x"]) - window.GetWidth()
					## loc_x = parentWindow.GetWidth() - int(value["x"]) + window.GetWidth()
			else:
				window.SetWindowHorizontalAlignRight()

			if value.has_key("all_align"):
				window.SetWindowVerticalAlignCenter()
				window.SetWindowHorizontalAlignCenter()
				loc_x = - int(value["x"])
		else:
			if value.has_key("horizontal_align"):
				if "center" == value["horizontal_align"]:
					window.SetWindowHorizontalAlignCenter()
				elif "right" == value["horizontal_align"]:
					window.SetWindowHorizontalAlignRight()

		window.SetPosition(loc_x, loc_y)
		window.Show()

	## Window
	def LoadElementWindow(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.WINDOW_KEY_LIST):
			return False

		self.LoadDefaultData(window, value, parentWindow)
		window.SetSize(int(value["width"]), int(value["height"]))

		return True

	## Button
	def LoadElementButton(self, window, value, parentWindow):

		if value.has_key("width") and value.has_key("height"):
			window.SetSize(int(value["width"]), int(value["height"]))

		if True == value.has_key("default_image"):
			window.SetUpVisual(value["default_image"])
		if True == value.has_key("over_image"):
			window.SetOverVisual(value["over_image"])
		if True == value.has_key("down_image"):
			window.SetDownVisual(value["down_image"])
		if True == value.has_key("disable_image"):
			window.SetDisableVisual(value["disable_image"])

		if True == value.has_key("default_inner_image"):
			window.SetUpInnerVisual(value["default_inner_image"])
		if True == value.has_key("default_over_image"):
			window.SetOverInnerVisual(value["default_over_image"])
		if True == value.has_key("default_down_image"):
			window.SetDownInnerVisual(value["default_down_image"])

		if True == value.has_key("up_underlay"):
			window.SetUpUnderlayVisual(value["up_underlay"])
		if True == value.has_key("over_underlay"):
			window.SetOverUnderlayVisual(value["over_underlay"])
		if True == value.has_key("down_underlay"):
			window.SetDownUnderlayVisual(value["down_underlay"])
		if True == value.has_key("underlay_alpha"):
			window.SetUnderlayAlpha(value["underlay_alpha"])

		if True == value.has_key("text"):
			if True == value.has_key("text_height"):
				window.SetText(value["text"], value["text_height"])
			else:
				window.SetText(value["text"])

			if value.has_key("text_color"):
				window.SetTextColor(value["text_color"])

		if True == value.has_key("tooltip_text"):
			if True == value.has_key("tooltip_x") and True == value.has_key("tooltip_y"):
				window.SetToolTipText(value["tooltip_text"], int(value["tooltip_x"]), int(value["tooltip_y"]))
			else:
				window.SetToolTipText(value["tooltip_text"])

		self.LoadDefaultData(window, value, parentWindow)

		return True

	## StateButton
	def LoadElementStateButton(self, window, value, parentWindow):

		i = 0
		while True == value.has_key("default_image_%d" % (i + 1)):
			# tchat("SetUpVisual(%d, %s)" % (i, value["default_image_%d" % (i + 1)]))
			window.SetUpVisual(i, value["default_image_%d" % (i + 1)])
			if True == value.has_key("over_image_%d" % (i + 1)):
				window.SetOverVisual(i, value["over_image_%d" % (i + 1)])
			if True == value.has_key("down_image_%d" % (i + 1)):
				window.SetDownVisual(i, value["down_image_%d" % (i + 1)])
			if True == value.has_key("disable_image_%d" % (i + 1)):
				window.SetDisableVisual(i, value["disable_image_%d" % (i + 1)])

			i += 1

		if i == 0:
			if True == value.has_key("closed_default_image"):
				window.SetUpVisual(window.STATE_CLOSED, value["closed_default_image"])
			if True == value.has_key("open_default_image"):
				window.SetUpVisual(window.STATE_OPEN, value["open_default_image"])
			if True == value.has_key("closed_over_image"):
				window.SetOverVisual(window.STATE_CLOSED, value["closed_over_image"])
			if True == value.has_key("open_over_image"):
				window.SetOverVisual(window.STATE_OPEN, value["open_over_image"])
			if True == value.has_key("closed_down_image"):
				window.SetDownVisual(window.STATE_CLOSED, value["closed_down_image"])
			if True == value.has_key("open_down_image"):
				window.SetDownVisual(window.STATE_OPEN, value["open_down_image"])
			if True == value.has_key("closed_disable_image"):
				window.SetDisableVisual(window.STATE_CLOSED, value["closed_disable_image"])
			if True == value.has_key("open_disable_image"):
				window.SetDisableVisual(window.STATE_OPEN, value["open_disable_image"])

		if value.has_key("width") and value.has_key("height"):
			window.SetSize(int(value["width"]), int(value["height"]))

		if True == value.has_key("text"):
			if True == value.has_key("text_height"):
				window.SetText(value["text"], value["text_height"])
			else:
				window.SetText(value["text"])
			if value.has_key("outline"):
				if value["outline"]:
					window.SetTextOutline()

			if value.has_key("text_color"):
				window.SetTextColor(value["text_color"])

		if True == value.has_key("tooltip_text"):
			if True == value.has_key("tooltip_x") and True == value.has_key("tooltip_y"):
				window.SetToolTipText(value["tooltip_text"], int(value["tooltip_x"]), int(value["tooltip_y"]))
			else:
				window.SetToolTipText(value["tooltip_text"])

		self.LoadDefaultData(window, value, parentWindow)

		return True

	## Mark
	def LoadElementMark(self, window, value, parentWindow):

		#if False == self.CheckKeyList(value["name"], value, self.MARK_KEY_LIST):
		#	return False

		self.LoadDefaultData(window, value, parentWindow)

		return True

	## Image
	def LoadElementImage(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.IMAGE_KEY_LIST):
			return False

		if value.has_key("scaled_load"):
			window.LoadScaledImage(value["image"], value["scaled_load"])
		elif value.has_key("scaled_width") and value.has_key("scaled_height"):
			window.LoadScaledImageAbs(value["image"], value["scaled_width"], value["scaled_height"])
		else:
			window.LoadImage(value["image"])
		self.LoadDefaultData(window, value, parentWindow)

		return True

	## AniImage
	def LoadElementAniImage(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.ANI_IMAGE_KEY_LIST):
			return False

		if True == value.has_key("delay"):
			window.SetDelay(value["delay"])

		for image in value["images"]:
			window.AppendImage(image)

		if value.has_key("width") and value.has_key("height"):
			window.SetSize(value["width"], value["height"])

		self.LoadDefaultData(window, value, parentWindow)

		return True

	## LimitTextLine
	def LoadElementLimitText(self, window, value, parentWindow):

		if value.has_key("limit_width"):
			window.SetLimitWidth(value["limit_width"])

		if value.has_key("speed"):
			window.SetSpeed(value["speed"])

		return self.LoadElementText(window, value, parentWindow)

	## Expanded Image
	def LoadElementExpandedImage(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.EXPANDED_IMAGE_KEY_LIST):
			return False

		window.LoadImage(value["image"])
		self.LoadDefaultData(window, value, parentWindow)

		if True == value.has_key("x_origin") and True == value.has_key("y_origin"):
			window.SetOrigin(float(value["x_origin"]), float(value["y_origin"]))

		if True == value.has_key("x_scale") and True == value.has_key("y_scale"):
			window.SetScale(float(value["x_scale"]), float(value["y_scale"]))

		if True == value.has_key("rect"):
			RenderingRect = value["rect"]
			window.SetRenderingRect(RenderingRect[0], RenderingRect[1], RenderingRect[2], RenderingRect[3])

		if True == value.has_key("mode"):
			mode = value["mode"]
			if "MODULATE" == mode:
				window.SetRenderingMode(wndMgr.RENDERING_MODE_MODULATE)

		return True

	## Slot
	def LoadElementSlot(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.SLOT_KEY_LIST):
			return False

		global_x = int(value["x"])
		global_y = int(value["y"])
		global_width = int(value["width"])
		global_height = int(value["height"])

		window.SetPosition(global_x, global_y)
		window.SetSize(global_width, global_height)
		window.Show()

		r = 1.0
		g = 1.0
		b = 1.0
		a = 1.0

		if True == value.has_key("image_r") and \
			True == value.has_key("image_g") and \
			True == value.has_key("image_b") and \
			True == value.has_key("image_a"):
			r = float(value["image_r"])
			g = float(value["image_g"])
			b = float(value["image_b"])
			a = float(value["image_a"])

		SLOT_ONE_KEY_LIST = ("index", "x", "y", "width", "height")

		for slot in value["slot"]:
			if True == self.CheckKeyList(value["name"] + " - one", slot, SLOT_ONE_KEY_LIST):
				wndMgr.AppendSlot(window.hWnd,
									int(slot["index"]),
									int(slot["x"]),
									int(slot["y"]),
									int(slot["width"]),
									int(slot["height"]))

		if True == value.has_key("image"):
			wndMgr.SetSlotBaseImage(window.hWnd,
									value["image"],
									r, g, b, a)

		return True

	## SlotBackground
	def LoadElementSlotBackground(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.BOARD_KEY_LIST):
			return False

		window.SetSize(int(value["width"]), int(value["height"]))
		self.LoadDefaultData(window, value, parentWindow)

		return True

	def LoadElementCandidateList(self, window, value, parentWindow):
		if False == self.CheckKeyList(value["name"], value, self.CANDIDATE_LIST_KEY_LIST):
			return False

		window.SetPosition(int(value["x"]), int(value["y"]))
		window.SetItemSize(int(value["item_xsize"]), int(value["item_ysize"]))
		window.SetItemStep(int(value["item_step"]))		
		window.Show()

		return True
				
	## Table
	def LoadElementGridTable(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.GRID_TABLE_KEY_LIST):
			return False

		xBlank = 0
		yBlank = 0
		if True == value.has_key("x_blank"):
			xBlank = int(value["x_blank"])
		if True == value.has_key("y_blank"):
			yBlank = int(value["y_blank"])

		window.SetPosition(int(value["x"]), int(value["y"]))
		window.ArrangeSlot(	int(value["start_index"]),
							int(value["x_count"]),
							int(value["y_count"]),
							int(value["x_step"]),
							int(value["y_step"]),
							xBlank,
							yBlank)
		if True == value.has_key("image"):
			r = 1.0
			g = 1.0
			b = 1.0
			a = 1.0
			if True == value.has_key("image_r") and \
				True == value.has_key("image_g") and \
				True == value.has_key("image_b") and \
				True == value.has_key("image_a"):
				r = float(value["image_r"])
				g = float(value["image_g"])
				b = float(value["image_b"])
				a = float(value["image_a"])
			wndMgr.SetSlotBaseImage(window.hWnd, value["image"], r, g, b, a)

		if True == value.has_key("style"):
			if "select" == value["style"]:
				wndMgr.SetSlotStyle(window.hWnd, wndMgr.SLOT_STYLE_SELECT)
		window.Show()

		return True

	## Text
	def LoadElementText(self, window, value, parentWindow):

		if value.has_key("fontsize"):
			fontSize = value["fontsize"]

			if "LARGE" == fontSize:
				window.SetFontName(localeInfo.UI_DEF_FONT_LARGE)

		elif value.has_key("fontname"):
			fontName = value["fontname"]
			window.SetFontName(fontName)

		if value.has_key("text_horizontal_align"):
			if "left" == value["text_horizontal_align"]:
				window.SetHorizontalAlignLeft()
			elif "center" == value["text_horizontal_align"]:
				window.SetHorizontalAlignCenter()
			elif "right" == value["text_horizontal_align"]:
				window.SetHorizontalAlignRight()
			elif "arabic" == value["text_horizontal_align"]:
				window.SetHorizontalAlignArabic()

		if value.has_key("text_vertical_align"):
			if "top" == value["text_vertical_align"]:
				window.SetVerticalAlignTop()
			elif "center" == value["text_vertical_align"]:
				window.SetVerticalAlignCenter()
			elif "bottom" == value["text_vertical_align"]:
				window.SetVerticalAlignBottom()

		if value.has_key("all_align"):
			window.SetHorizontalAlignCenter()
			window.SetVerticalAlignCenter()
			window.SetWindowHorizontalAlignCenter()
			window.SetWindowVerticalAlignCenter()

		if value.has_key("r") and value.has_key("g") and value.has_key("b"):
			window.SetFontColor(float(value["r"]), float(value["g"]), float(value["b"]))
		elif value.has_key("color"):
			window.SetPackedFontColor(value["color"])
		else:
			window.SetFontColor(0.8549, 0.8549, 0.8549)

		if value.has_key("outline"):
			if value["outline"]:
				window.SetOutline()
		if True == value.has_key("text"):
			window.SetText(value["text"])

		# FOR_ARABIC_ALIGN
		window.SetSize(int(value.get("width", 0)), int(value.get("height", 0)))

		self.LoadDefaultData(window, value, parentWindow)

		return True

	## ExtendedTextLine
	def LoadElementExtendedText(self, window, value, parentWindow):

		if True == value.has_key("text"):
			window.SetText(value["text"])

		self.LoadDefaultData(window, value, parentWindow)

		return True

	## MultiTextLine
	def LoadElementMultiText(self, window, value, parentWindow):

		if value.has_key("width") and value.has_key("height"):
			window.SetSize(value["width"], value["height"])
		elif value.has_key("width"):
			window.SetWidth(value["width"])

		if value.has_key("text_horizontal_align"):
			if "center" == value["text_horizontal_align"]:
				window.SetTextHorizontalAlignCenter()

		if value.has_key("text_vertical_align"):
			if "center" == value["text_vertical_align"]:
				window.SetTextVerticalAlignCenter()

		if value.has_key("r") and value.has_key("g") and value.has_key("b"):
			window.SetFontColor(float(value["r"]), float(value["g"]), float(value["b"]))

		if value.has_key("text"):
			window.SetText(value["text"])

		if value.has_key("line_height"):
			window.SetLineHeight(value["line_height"])

		self.LoadDefaultData(window, value, parentWindow)

		return True

	def LoadElementCheckBox(self, window, value, parentWindow):

		if value.has_key("text"):
			window.SetText(value["text"])

		if value.has_key("checked") and value["checked"] == True:
			window.SetChecked(window.STATE_SELECTED)

		if value.has_key("disabled") and value["disabled"] == True:
			window.Disable()

		self.LoadDefaultData(window, value, parentWindow)

		return True

	## EditLine
	def LoadElementEditLine(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.EDIT_LINE_KEY_LIST):
			return False

		self.LoadElementText(window, value, parentWindow)

		if value.has_key("secret_flag"):
			window.SetSecret(value["secret_flag"])
		if value.has_key("with_codepage"):
			if value["with_codepage"]:
				window.bCodePage = True
		if value.has_key("only_number"):
			if value["only_number"]:
				window.SetNumberMode()
		if value.has_key("enable_codepage"):
			window.SetIMEFlag(value["enable_codepage"])
		if value.has_key("enable_ime"):
			window.SetIMEFlag(value["enable_ime"])
		if value.has_key("limit_width"):
			window.SetLimitWidth(value["limit_width"])
		if value.has_key("multi_line"):
			if value["multi_line"]:
				window.SetMultiLine()
		if value.has_key("overlay"):
			window.SetOverlayText(value["overlay"])

		window.SetMax(int(value["input_limit"]))
		window.SetSize(int(value["width"]), int(value["height"]))

		return True

	## TitleBar
	def LoadElementTitleBar(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.TITLE_BAR_KEY_LIST):
			return False

		window.MakeTitleBar(int(value["width"]), value.get("color", "red"))
		self.LoadDefaultData(window, value, parentWindow)

		return True

	## HorizontalBar
	def LoadElementHorizontalBar(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.HORIZONTAL_BAR_KEY_LIST):
			return False

		window.Create(int(value["width"]))
		self.LoadDefaultData(window, value, parentWindow)

		return True

	## Board
	def LoadElementBoard(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.BOARD_KEY_LIST):
			return False

		window.SetSize(int(value["width"]), int(value["height"]))
		self.LoadDefaultData(window, value, parentWindow)

		return True

	## Board With TitleBar
	def LoadElementBoardWithTitleBar(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.BOARD_WITH_TITLEBAR_KEY_LIST):
			return False

		self.LoadDefaultData(window, value, parentWindow)
		window.SetSize(int(value["width"]), int(value["height"]))
		if value.has_key("title"):
			window.SetTitleName(value["title"])

		return True

	## ThinBoard
	def LoadElementThinBoard(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.BOARD_KEY_LIST):
			return False

		window.SetSize(int(value["width"]), int(value["height"]))
		self.LoadDefaultData(window, value, parentWindow)

		return True

	## VerticalBoard
	def LoadElementVerticalBoard(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.VERTICAL_BOARD_KEY_LIST):
			return False

		window.SetTopImage(value["top_image"])
		window.SetMiddleImage(value["mid_image"])
		window.SetBottomImage(value["bot_image"])

		window.SetHeight(int(value["height"]))
		self.LoadDefaultData(window, value, parentWindow)

		return True

	## VerticalBoardWithTitleBar
	def LoadElementVerticalBoardWithTitleBar(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.VERTICAL_BOARD_WITH_TITLEBAR_KEY_LIST):
			return False

		window.SetTopImage(value["top_image"])
		window.SetMiddleImage(value["mid_image"])
		window.SetBottomImage(value["bot_image"])

		window.SetTitleLeftImage(value["title_left_image"])
		window.SetTitleMiddleImage(value["title_mid_image"])
		window.SetTitleRightImage(value["title_right_image"])
		window.SetTitleText(value["title"])

		if value.has_key("title_border_left"):
			window.SetTitleBorderLeft(value["title_border_left"])
		if value.has_key("title_border_right"):
			window.SetTitleBorderRight(value["title_border_right"])
		if value.has_key("title_pos_y"):
			window.SetTitlePosY(value["title_pos_y"])

		window.SetHeight(int(value["height"]))
		self.LoadDefaultData(window, value, parentWindow)

		return True

	## Box
	def LoadElementBox(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.BOX_KEY_LIST):
			return False

		self.LoadDefaultData(window, value, parentWindow)
		window.SetSize(int(value["width"]), int(value["height"]))

		if True == value.has_key("color"):
			window.SetColor(value["color"])

		return True

	## Bar
	def LoadElementBar(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.BAR_KEY_LIST):
			return False

		self.LoadDefaultData(window, value, parentWindow)
		window.SetSize(int(value["width"]), int(value["height"]))

		if True == value.has_key("color"):
			window.SetColor(value["color"])

		return True

	## Line
	def LoadElementLine(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.LINE_KEY_LIST):
			return False

		self.LoadDefaultData(window, value, parentWindow)
		window.SetSize(int(value["width"]), int(value["height"]))

		if True == value.has_key("color"):
			window.SetColor(value["color"])

		return True

	## Slot
	def LoadElementSlotBar(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.SLOTBAR_KEY_LIST):
			return False

		self.LoadDefaultData(window, value, parentWindow)
		window.SetSize(int(value["width"]), int(value["height"]))

		return True

	## Gauge
	def LoadElementGauge(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.GAUGE_KEY_LIST):
			return False

		self.LoadDefaultData(window, value, parentWindow)
		window.MakeGauge(value["width"], value["color"])

		return True

	def LoadElementScrollBarTemplate(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.SCROLLBAR_TEMPLATE_KEY_LIST):
			return False

		if value.has_key("bg_image"):
			window.SetBarImage(value["bg_image"])
		if value.has_key("bg_top_image") and value.has_key("bg_center_image") and value.has_key("bg_bottom_image"):
			window.SetBarPartImages(value["bg_top_image"], value["bg_center_image"], value["bg_bottom_image"])
		if value.has_key("top_btn_up_visual") and value.has_key("top_btn_over_visual") and value.has_key("top_btn_down_visual"):
			window.SetUpButton(value["top_btn_up_visual"], value["top_btn_over_visual"], value["top_btn_down_visual"])
		if value.has_key("bot_btn_up_visual") and value.has_key("bot_btn_over_visual") and value.has_key("bot_btn_down_visual"):
			window.SetDownButton(value["bot_btn_up_visual"], value["bot_btn_over_visual"], value["bot_btn_down_visual"])
		window.SetMiddleImage(value["middle_image"])

		self.LoadDefaultData(window, value, parentWindow)
		window.SetScrollBarSize(value["size"])

		return True

	## ScrollBar
	def LoadElementScrollBar(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.SCROLLBAR_KEY_LIST):
			return False

		self.LoadDefaultData(window, value, parentWindow)
		window.SetScrollBarSize(value["size"])

		return True

	## SliderBar
	def LoadElementSliderBar(self, window, value, parentWindow):

		self.LoadDefaultData(window, value, parentWindow)

		return True

	## ListBox
	def LoadElementListBox(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.LIST_BOX_KEY_LIST):
			return False

		window.SetSize(value["width"], value["height"])
		self.LoadDefaultData(window, value, parentWindow)

		if value.has_key("item_align"):
			window.SetTextCenterAlign(value["item_align"])

		return True

	## ListBox2
	def LoadElementListBox2(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.LIST_BOX_KEY_LIST):
			return False

		window.SetRowCount(value.get("row_count", 10))
		window.SetSize(value["width"], value["height"])
		self.LoadDefaultData(window, value, parentWindow)

		if value.has_key("item_align"):
			window.SetTextCenterAlign(value["item_align"])

		return True
	def LoadElementListBoxEx(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.LIST_BOX_KEY_LIST):
			return False

		window.SetSize(value["width"], value["height"])
		self.LoadDefaultData(window, value, parentWindow)

		if value.has_key("itemsize_x") and value.has_key("itemsize_y"):
			itemsize_x = int(value["itemsize_x"])
			if itemsize_x == 0:
				itemsize_x = int(value["width"])
			window.SetItemSize(itemsize_x, int(value["itemsize_y"]))

		if value.has_key("itemstep"):
			window.SetItemStep(int(value["itemstep"]))

		if value.has_key("viewcount"):
			window.SetViewItemCount(int(value["viewcount"]))

		return True

	def LoadElementInputField(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.INPUT_FIELD_KEY_LIST):
			return False

		if True == value.has_key("alpha"):
			window.SetAlpha(value["alpha"])

		if True == value.has_key("button_style"):
			window.SetButtonStyle(value["button_style"])
		if True == value.has_key("button_style_overonly"):
			window.SetButtonStyleOverOnly(value["button_style_overonly"])

		window.SetSize(int(value["width"]), int(value["height"]))

		self.LoadDefaultData(window, value, parentWindow)

		return True

	def LoadElementComboBox(self, window, value, parentWindow):

		if False == self.CheckKeyList(value["name"], value, self.COMBO_BOX_KEY_LIST):
			return False

		window.SetSize(value["width"], value["height"])

		if value.has_key("text_align"):
			window.SetTextAlign(value["text_align"])
		if value.has_key("text_pos"):
			window.SetTextPos(value["text_pos"])

		if value.has_key("items"):
			for item in value["items"]:
				window.InsertItem(item[0], item[1])

		if value.has_key("select_item"):
			window.SelectItem(value["select_item"])

		self.LoadDefaultData(window, value, parentWindow)

		return True

	def LoadElementRenderTarget(self, window, value, parentWindow):
		if False == self.CheckKeyList(value["name"], value, self.RENDER_TARGET_KEY_LIST):
			return False

		window.SetSize(value["width"], value["height"])
		if True == value.has_key("style"):
			for style in value["style"]:
				window.AddFlag(style)

		self.LoadDefaultData(window, value, parentWindow)

		if value.has_key("index"):
			window.SetRenderTarget(int(value["index"]))

		return True

	def LoadElementTextDropdown(self, window, value, parentWindow):
		if False == self.CheckKeyList(value["name"], value, self.TEXT_DROPDOWN_KEY_LIST):
			return False

		window.Create(value["width"], value["height"], value["item_height"])

		if True == value.has_key("viewcount"):
			window.SetViewItemCount(value["viewcount"])

		if True == value.has_key("default"):
			window.SetDefaultText(value["default"])

		self.LoadDefaultData(window, value, parentWindow)

		return True

class ReadingWnd(Bar):

	def __init__(self):
		Bar.__init__(self,"TOP_MOST")

		self.__BuildText()
		self.SetSize(80, 19)
		self.Show()

	def __del__(self):
		Bar.__del__(self)

	def __BuildText(self):
		self.text = TextLine()
		self.text.SetParent(self)
		self.text.SetPosition(4, 3)
		self.text.Show()

	def SetText(self, text):
		self.text.SetText(text)

	def SetReadingPosition(self, x, y):
		xPos = x + 2
		yPos = y  - self.GetHeight() - 2
		self.SetPosition(xPos, yPos)

	def SetTextColor(self, color):
		self.text.SetPackedFontColor(color)

class RenderTarget(Window):
	def __init__(self):
		Window.__init__(self)
		self.number = -1

	def __del__(self):
		Window.__del__(self)

	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.RegisterRenderTarget(self, layer)

	def SetRenderTarget(self, number):
		self.number = number
		wndMgr.SetRenderTarget(self.hWnd, self.number)

class ShopDecoTitle(Window):
	DEFAULT_VALUE = 16
	CORNER_WIDTH = 48
	CORNER_HEIGHT = 32
	LINE_WIDTH = 16
	LINE_HEIGHT = 32

	LT = 0
	LB = 1
	RT = 2
	RB = 3
	L = 0
	R = 1
	T = 2
	B = 3

	DECO_SHOP_TITLE_LIST = [
		"d:/ymir work/ui/pattern/myshop/fire/p_fire",
		"d:/ymir work/ui/pattern/myshop/ice/p_ice",
		"d:/ymir work/ui/pattern/myshop/paper/p_paper",
		"d:/ymir work/ui/pattern/myshop/ribon/p_ribon",
		"d:/ymir work/ui/pattern/myshop/wing/p_wing",
		#duplicated in order to be 6 and + normal total is 7
		"d:/ymir work/ui/pattern/myshop/ribon/p_wing",
	]

	def __init__(self, type, layer = "UI"):
		Window.__init__(self, layer)

		CornerFileNames, LineFileNames = self.__GetFilePath(type)

		if CornerFileNames == None or LineFileNames == None :
			return

		self.Corners = []
		for fileName in CornerFileNames:
			Corner = ExpandedImageBox()
			Corner.AddFlag("attach")
			Corner.AddFlag("not_pick")
			Corner.LoadImage(fileName)
			Corner.SetParent(self)
			Corner.SetPosition(0, 0)
			Corner.Show()
			self.Corners.append(Corner)

		self.Lines = []
		for fileName in LineFileNames:
			Line = ExpandedImageBox()
			Line.AddFlag("attach")
			Line.AddFlag("not_pick")
			Line.LoadImage(fileName)
			Line.SetParent(self)
			Line.SetPosition(0, 0)
			Line.Show()
			self.Lines.append(Line)

	def __del__(self):
		Window.__del__(self)

	def __GetFilePath(self, type):
		CornerFileNames = [ self.DECO_SHOP_TITLE_LIST[type]+"_"+dir+".tga" for dir in ["left_top","left_bottom","right_top","right_bottom"] ]
		LineFileNames = [ self.DECO_SHOP_TITLE_LIST[type]+"_"+dir+".tga" for dir in ["left","right","top","bottom"] ]

		return CornerFileNames, LineFileNames

	def SetSize(self, width, height):
		width = max(self.DEFAULT_VALUE*2, width)
		height = max(self.DEFAULT_VALUE*2, height)
		Window.SetSize(self, width, height)

		self.Corners[self.LT].SetPosition(-self.CORNER_WIDTH + self.DEFAULT_VALUE, -self.CORNER_HEIGHT + self.DEFAULT_VALUE)
		self.Corners[self.LB].SetPosition(-self.CORNER_WIDTH + self.DEFAULT_VALUE, height - self.CORNER_HEIGHT + self.DEFAULT_VALUE)

		self.Corners[self.RT].SetPosition(width - self.DEFAULT_VALUE, -self.CORNER_HEIGHT + self.DEFAULT_VALUE)
		self.Corners[self.RB].SetPosition(width - self.DEFAULT_VALUE, height - self.CORNER_HEIGHT + self.DEFAULT_VALUE)

		self.Lines[self.L].SetPosition(0, self.DEFAULT_VALUE)
		self.Lines[self.R].SetPosition(width - self.DEFAULT_VALUE, self.DEFAULT_VALUE)
		self.Lines[self.B].SetPosition(self.DEFAULT_VALUE, height - self.LINE_HEIGHT + self.DEFAULT_VALUE)
		self.Lines[self.T].SetPosition(self.DEFAULT_VALUE, -self.LINE_HEIGHT + self.DEFAULT_VALUE)

		verticalShowingPercentage = float((height - self.DEFAULT_VALUE*2) - self.DEFAULT_VALUE) / self.DEFAULT_VALUE
		horizontalShowingPercentage = float((width - self.DEFAULT_VALUE*2) - self.DEFAULT_VALUE) / self.DEFAULT_VALUE

		self.Lines[self.L].SetRenderingRect(0, 0, 0, verticalShowingPercentage)
		self.Lines[self.R].SetRenderingRect(0, 0, 0, verticalShowingPercentage)
		self.Lines[self.T].SetRenderingRect(0, 0, horizontalShowingPercentage, 0)
		self.Lines[self.B].SetRenderingRect(0, 0, horizontalShowingPercentage, 0)

	def ShowInternal(self):
		for wnd in self.Lines:
			wnd.Show()
		for wnd in self.Corners:
			wnd.Show()

	def HideInternal(self):
		for wnd in self.Lines:
			wnd.Hide()
		for wnd in self.Corners:
			wnd.Hide()

def MakeSlotBar(parent, x, y, width, height):
	slotBar = SlotBar()
	slotBar.SetParent(parent)
	slotBar.SetSize(width, height)
	slotBar.SetPosition(x, y)
	slotBar.Show()
	return slotBar

def MakeWindow(parent, x, y, width, height):
	wind = Window()
	wind.SetParent(parent)
	wind.SetSize(width, height)
	wind.SetPosition(x, y)
	wind.Show()
	return wind

def MakeBar(parent, x, y, width, height):
	bar = Bar()
	bar.SetParent(parent)
	bar.SetSize(width, height)
	bar.SetPosition(x, y)
	bar.Show()
	return bar

def MakeImageBox(parent, name, x, y):
	image = ImageBox()
	image.SetParent(parent)
	image.LoadImage(name)
	image.SetPosition(x, y)
	image.Show()
	return image

def MakeTextLine(parent):
	textLine = TextLine()
	textLine.SetParent(parent)
	textLine.SetWindowHorizontalAlignCenter()
	textLine.SetWindowVerticalAlignCenter()
	textLine.SetHorizontalAlignCenter()
	textLine.SetVerticalAlignCenter()
	textLine.Show()
	return textLine

def MakeButton(parent, x, y, tooltipText, path, up, over, down, disable=False):
	button = Button()
	button.SetParent(parent)
	button.SetPosition(x, y)
	button.SetUpVisual(path + up)
	button.SetOverVisual(path + over)
	button.SetDownVisual(path + down)
	if disable:
		button.SetDisableVisual(path + disable)
	button.SetToolTipText(tooltipText)
	button.Show()
	return button

def RenderRoundBox(x, y, width, height, color):
	grp.SetColor(color)
	grp.RenderLine(x+2, y, width-3, 0)
	grp.RenderLine(x+2, y+height, width-3, 0)
	grp.RenderLine(x, y+2, 0, height-4)
	grp.RenderLine(x+width, y+1, 0, height-3)
	grp.RenderLine(x, y+2, 2, -2)
	grp.RenderLine(x, y+height-2, 2, 2)
	grp.RenderLine(x+width-2, y, 2, 2)
	grp.RenderLine(x+width-2, y+height, 2, -2)

def GenerateColor(r, g, b, a = 255):
	r = float(r) / 255.0
	g = float(g) / 255.0
	b = float(b) / 255.0
	a = float(a) / 255.0
	return grp.GenerateColor(r, g, b, a)

def EnablePaste(flag):
	ime.EnablePaste(flag)

def GetHyperlink():
	return wndMgr.GetHyperlink()

RegisterToolTipWindow("TEXT", TextLine)
