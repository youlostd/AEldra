import app
import ui
import grp
import net
import guild
import messenger
import localeInfo
import constInfo
import uiToolTip
import uiGameOption
import player
import cfg
import time

import uiCommon
from _weakref import proxy

FRIEND = 0
GUILD = 1
TEAM = 2
BLOCK = 3

class MessengerItem(ui.Window):

	def __init__(self, getParentEvent):
		ui.Window.__init__(self)

		self.SetParent(getParentEvent())
		self.AddFlag("float")

		self.name = ""
		self.image = ui.ImageBox()
		self.image.AddFlag("not_pick")
		self.image.SetParent(self)
		self.image.Show()
		self.text = ui.TextLine()
		self.text.SetParent(self)
		self.text.SetPosition(20, 2)
		self.text.Show()

		self.lovePoint = -1
		self.lovePointToolTip = None

		self.isSelected = False

		self.getParentEvent = getParentEvent

	def SetName(self, name):
		self.name = name
		if name:
			self.text.SetText(name)
			self.SetSize(20 + 6*len(name) + 4, 16)

			if localeInfo.IsARABIC():
				self.text.SetPosition(20 + 6*len(name) + 4, 2)

	def SetLovePoint(self, lovePoint):
		self.lovePoint = lovePoint

	def Select(self):
		self.isSelected = True

	def UnSelect(self):
		self.isSelected = False

	def GetName(self):
		return self.name

	def GetStepWidth(self):
		return 0

	# Whisper
	def CanWhisper(self):
		return False

	def IsOnline(self):
		return False

	def IsMobile(self):
		return False

	def OnWhisper(self):
		pass

	def OnMobileMessage(self):
		pass

	# Remove
	def CanRemove(self):
		return False

	def OnRemove(self):
		return False

	# Warp
	def CanWarp(self):
		return False

	def OnWarp(self):
		pass

	def OnMouseOverIn(self):
		if -1 != self.lovePoint:
			if not self.lovePointToolTip:
				self.lovePointToolTip = uiToolTip.ToolTip(100)
				self.lovePointToolTip.SetTitle(self.name)
				self.lovePointToolTip.AppendTextLine(localeInfo.AFF_LOVE_POINT % (self.lovePoint))
				self.lovePointToolTip.ResizeToolTip()
			self.lovePointToolTip.ShowToolTip()

	def OnMouseOverOut(self):
		if self.lovePointToolTip:
			self.lovePointToolTip.HideToolTip()

	def OnMouseLeftButtonDown(self):
		self.getParentEvent().OnSelectItem(self)

	def OnMouseLeftButtonDoubleClick(self):
		self.getParentEvent().OnDoubleClickItem(self)

	def OnRender(self):
		if self.isSelected:
			x, y = self.GetGlobalPosition()
			grp.SetColor(grp.GenerateColor(0.0, 0.0, 0.7, 0.7))
			grp.RenderBar(x+16, y, self.GetWidth()-16, self.GetHeight())

class MessengerMemberItem(MessengerItem):

	STATE_OFFLINE = 0
	STATE_ONLINE = 1
	STATE_MOBILE = 2

	IMAGE_FILE_NAME = {	"ONLINE" : "d:/ymir work/ui/game/windows/messenger_list_online.sub",
						"OFFLINE" : "d:/ymir work/ui/game/windows/messenger_list_offline.sub",
						"MOBILE" : "d:/ymir work/ui/game/windows/messenger_list_mobile.sub", }

	def __init__(self, getParentEvent):
		MessengerItem.__init__(self, getParentEvent)
		self.key = None
		self.state = self.STATE_OFFLINE
		self.mobileFlag = False
		self.Offline()

	def GetStepWidth(self):
		return 15

	def SetKey(self, key):
		self.key = key
		if app.ENABLE_MESSENGER_BLOCK:
			constInfo.ME_KEY = key
			

	def IsSameKey(self, key):
		return self.key == key

	def IsOnline(self):
		if self.STATE_ONLINE == self.state:
			return True

		return False

	def IsMobile(self):
		if self.STATE_MOBILE == self.state:
			return True

		return False

	def Online(self):
		self.image.LoadImage(self.IMAGE_FILE_NAME["ONLINE"])
		self.state = self.STATE_ONLINE

	def Offline(self):
		if self.mobileFlag:
			self.image.LoadImage(self.IMAGE_FILE_NAME["MOBILE"])
			self.state = self.STATE_MOBILE

		else:
			self.image.LoadImage(self.IMAGE_FILE_NAME["OFFLINE"])
			self.state = self.STATE_OFFLINE

	def SetMobile(self, flag):
		self.mobileFlag = flag

		if not self.IsOnline():
			self.Offline()

	def CanWhisper(self):
		if self.IsOnline():
			return True

		return False

	def OnWhisper(self):
		if self.IsOnline():
			self.getParentEvent().whisperButtonEvent(self.GetName())

	def OnMobileMessage(self):
		if not uiGameOption.MOBILE:
			return

		if not self.IsMobile():
			return

		self.getParentEvent().SendMobileMessage(self.GetName())

	def Select(self):
		MessengerItem.Select(self)

class MessengerGroupItem(MessengerItem):

	IMAGE_FILE_NAME = {	"OPEN" : "d:/ymir work/ui/game/windows/messenger_list_open.sub",
						"CLOSE" : "d:/ymir work/ui/game/windows/messenger_list_close.sub", }

	def __init__(self, getParentEvent):
		self.isOpen = False
		self.memberList = []

		MessengerItem.__init__(self, getParentEvent)

	def AppendMember(self, member, key, name):
		member.SetKey(key)
		member.SetName(name)
		self.memberList.append(member)
		return member

	def RemoveMember(self, item):
		for i in xrange(len(self.memberList)):
			if item == self.memberList[i]:
				del self.memberList[i]
				return

	def ClearMember(self):
		self.memberList = []

	def FindMember(self, key):
		list = filter(lambda argMember, argKey=key: argMember.IsSameKey(argKey), self.memberList)
		if list:
			return list[0]

		return None

	def GetLoginMemberList(self):
		return filter(MessengerMemberItem.IsOnline, self.memberList)

	def GetLogoutMemberList(self):
		return filter(lambda arg: not arg.IsOnline(), self.memberList)

	def IsOpen(self):
		return self.isOpen

	def Open(self):
		self.image.LoadImage(self.IMAGE_FILE_NAME["OPEN"])
		self.isOpen = True

	def Close(self):
		self.image.LoadImage(self.IMAGE_FILE_NAME["CLOSE"])
		self.isOpen = False

		map(ui.Window.Hide, self.memberList)

	def Select(self):

		if self.IsOpen():
			self.Close()
		else:
			self.Open()

		MessengerItem.Select(self)
		self.getParentEvent().OnRefreshList()

class MessengerFriendItem(MessengerMemberItem):

	def __init__(self, getParentEvent):
		MessengerMemberItem.__init__(self, getParentEvent)

	def CanRemove(self):
		return True

	def OnRemove(self):
		messenger.RemoveFriend(self.key)
		net.SendMessengerRemovePacket(self.key, self.name)
		return True

if app.ENABLE_MESSENGER_BLOCK:
	class MessengerBlockItem(MessengerMemberItem):

		def __init__(self, getParentEvent):
			MessengerMemberItem.__init__(self, getParentEvent)

		def CanRemove(self):
			return True

		def OnRemove(self):
			messenger.RemoveBlock(self.key)
			net.SendMessengerRemoveBlockPacket(self.key, self.name)
			return True
			

class MessengerGuildItem(MessengerMemberItem):

	def __init__(self, getParentEvent):
		MessengerMemberItem.__init__(self, getParentEvent)

	def CanWarp(self):
		if not self.IsOnline():
			return False
		return True

	def OnWarp(self):
		net.SendGuildUseSkillPacket(155, self.key)

	def CanRemove(self):
		for i in xrange(guild.ENEMY_GUILD_SLOT_MAX_COUNT):
			if guild.GetEnemyGuildName(i) != "":
				return False

		if guild.MainPlayerHasAuthority(guild.AUTH_REMOVE_MEMBER):
			if guild.IsMemberByName(self.name):
				return True

		return False

	def OnRemove(self):
		net.SendGuildRemoveMemberPacket(self.key)
		return True

class MessengerFriendGroup(MessengerGroupItem):

	def __init__(self, getParentEvent):
		MessengerGroupItem.__init__(self, getParentEvent)
		self.SetName(localeInfo.MESSENGER_FRIEND)

	def AppendMember(self, key, name):
		item = MessengerFriendItem(self.getParentEvent)
		return MessengerGroupItem.AppendMember(self, item, key, name)

if app.ENABLE_MESSENGER_BLOCK:
	class MessengerBlockGroup(MessengerGroupItem):

		def __init__(self, getParentEvent):
			MessengerGroupItem.__init__(self, getParentEvent)
			self.SetName(localeInfo.MESSENGER_BLOCK)

		def AppendMember(self, key, name):
			item = MessengerBlockItem(self.getParentEvent)
			return MessengerGroupItem.AppendMember(self, item, key, name)
			
class MessengerGuildGroup(MessengerGroupItem):

	def __init__(self, getParentEvent):
		MessengerGroupItem.__init__(self, getParentEvent)
		self.SetName(localeInfo.MESSENGER_GUILD)
		self.AddFlag("float")

	def AppendMember(self, key, name):
		item = MessengerGuildItem(self.getParentEvent)
		return MessengerGroupItem.AppendMember(self, item, key, name)

class MessengerTeamGroup(MessengerGroupItem):

	STATE_IMAGE_FILE_NAME = {	"ON" : "d:/ymir work/ui/pattern/on.tga",
								"OFF" : "d:/ymir work/ui/pattern/off.tga", }

	def __init__(self, getParentEvent):
		MessengerGroupItem.__init__(self, getParentEvent)
		self.SetName(localeInfo.MESSENGER_TEAM)
		self.AddFlag("float")

		stateImage = ui.ImageBox()
		stateImage.SetParent(self)
		stateImage.SAFE_SetStringEvent("MOUSE_LEFT_DOWN", self.OnClickStateImage)
		stateImage.Show()
		self.stateImage = stateImage
		self.RefreshStateImage()

	def SetSize(self, width, height):
		MessengerGroupItem.SetSize(self, width + 15, height)

	def AppendMember(self, key, name):
		item = MessengerMemberItem(self.getParentEvent)
		return MessengerGroupItem.AppendMember(self, item, key, name)

	def OnClickStateImage(self):
		if "[GM]" not in player.GetName() and not "[TGM]" in player.GetName():
			net.SendChatPacket("/set_is_show_teamler %d" % (0 if player.IsShowTeamler() else 1))

	def RefreshStateImage(self):
		if player.IsGameMaster():
			self.stateImage.LoadImage(self.STATE_IMAGE_FILE_NAME["ON" if player.IsShowTeamler() else "OFF"])
			self.stateImage.SetPosition(self.GetRight() - (self.stateImage.GetWidth() + 25), (self.GetHeight() - self.stateImage.GetHeight()) / 2)
			self.stateImage.Show()
		else:
			self.stateImage.Hide()

	def OnRender(self):
		if self.isSelected:
			x, y = self.GetGlobalPosition()
			grp.SetColor(grp.GenerateColor(0.0, 0.0, 0.7, 0.7))
			grp.RenderBar(x+16, y, self.GetWidth()-16-15, self.GetHeight())

class MessengerFamilyGroup(MessengerGroupItem):

	def __init__(self, getParentEvent):
		MessengerGroupItem.__init__(self, getParentEvent)
		self.SetName(localeInfo.MESSENGER_FAMILY)
		self.AddFlag("float")

		self.lover = None

	def AppendMember(self, key, name):
		item = MessengerGuildItem(self.getParentEvent)
		self.lover = item
		return MessengerGroupItem.AppendMember(self, item, key, name)

	def GetLover(self):
		return self.lover

###################################################################################################
###################################################################################################
###################################################################################################

class MessengerWindow(ui.ScriptWindow):

	START_POSITION = 40

	class ResizeButton(ui.DragButton):

		def OnMouseOverIn(self):
			app.SetCursor(app.VSIZE)

		def OnMouseOverOut(self):
			app.SetCursor(app.NORMAL)

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		messenger.SetMessengerHandler(self)

		self.board = None
		self.groupList = []
		self.showingItemList = []
		self.selectedItem = None
		self.whisperButtonEvent = lambda *arg: None
		self.familyGroup = None

		self.guildButtonEvent = None

		self.showingPageSize = 0
		self.startLine = 0
		self.hasMobilePhoneNumber = True

		self.isLoaded = 0
		self.OnlinePopupQueue = []

		self.__AddGroup()
		messenger.RefreshGuildMember()

		self.onlinePopup = []

	def Show(self):
		if self.isLoaded==0:
			self.isLoaded=1

			self.__LoadWindow()
			self.OnRefreshList()
			self.OnResizeDialog()
			self.RefreshTeamState()

		if constInfo.SAVE_WINDOW_POSITION:
			if int(cfg.Get(cfg.SAVE_GENERAL, "save_wnd_pos", "0")):
				x, y = map(int, cfg.Get(cfg.SAVE_GENERAL, "wnd_pos_msg", "0 0").split(" "))
				if x and y:
					self.SetPosition(x, y)

		ui.ScriptWindow.Show(self)

	def HideAllOnlinePopups(self):
		for obj in self.onlinePopup:
			obj.Hide()

	if constInfo.SAVE_WINDOW_POSITION:
		def OnMoveWindow(self, x, y):
			cfg.Set(cfg.SAVE_GENERAL, "wnd_pos_msg", ("%d %d") % (x, y))

	def __LoadWindow(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "UIScript/MessengerWindow.py")		

		try:
			self.board = self.GetChild("board")
			self.scrollBar = self.GetChild("ScrollBar")
			self.whisperButton = self.GetChild("WhisperButton")
			self.mobileButton = self.GetChild("MobileButton")
			self.removeButton = self.GetChild("RemoveButton")
			self.addFriendButton = self.GetChild("AddFriendButton")
			self.guildButton = self.GetChild("GuildButton")
			self.addBlockButton = self.GetChild("BlockFriendButton")
			
		except:
			import exception
			exception.Abort("MessengerWindow.__LoadWindow.__Bind")

		self.board.SetCloseEvent(ui.__mem_func__(self.Close))
		self.scrollBar.SetScrollEvent(ui.__mem_func__(self.OnScroll))
		self.whisperButton.SetEvent(ui.__mem_func__(self.OnPressWhisperButton))
		self.mobileButton.SetEvent(ui.__mem_func__(self.OnPressMobileButton))
		self.removeButton.SetEvent(ui.__mem_func__(self.OnPressRemoveButton))
		self.addFriendButton.SetEvent(ui.__mem_func__(self.OnPressAddFriendButton))
		self.guildButton.SetEvent(ui.__mem_func__(self.OnPressGuildButton))
		if app.ENABLE_MESSENGER_BLOCK:
			self.addBlockButton.SetEvent(ui.__mem_func__(self.OnPressAddBlockButton))
		else:
			self.addBlockButton.Hide()

		if not uiGameOption.MOBILE:
			self.mobileButton.Hide()
			width = self.GetWidth()
			height = self.GetHeight()

		self.whisperButton.Disable()
		self.mobileButton.Disable()
		self.removeButton.Disable()

		resizeButton = self.ResizeButton()
		resizeButton.AddFlag("restrict_x")
		resizeButton.SetParent(self)
		resizeButton.SetSize(self.GetWidth(), 10)
		resizeButton.SetWindowVerticalAlignBottom()
		resizeButton.SetPosition(0, 0)
		resizeButton.Show()
		self.resizeButton = resizeButton
		self.resizeButton.SetMoveEvent(ui.__mem_func__(self.OnResizeDialog))
		self.resizeButton.SetPosition(0, 300)

		for listItem in self.groupList:
			listItem.SetTop()

	def __del__(self):
		messenger.SetMessengerHandler(None)
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.board = None
		self.scrollBar = None
		self.resizeButton = None
		self.friendNameBoard = None
		self.questionDialog = None
		self.popupDialog = None
		self.inputDialog = None
		self.familyGroup = None

		self.whisperButton = None
		self.mobileButton = None
		self.removeButton = None

		self.onlinePopup = []

	def OnCloseQuestionDialog(self):
		self.questionDialog.Close()
		self.questionDialog = None
		return True

	def Close(self):
		self.questionDialog = None
		self.Hide()

	def SetSize(self, width, height):
		if self.board:
			self.board.SetSize(width - self.board.GetWidthPadding(), height - self.board.GetHeightPadding())
			ui.ScriptWindow.SetSize(self, width, height)
		else:
			ui.ScriptWindow.SetSize(self, width, height)

	def OnResizeDialog(self):
		x, y = self.resizeButton.GetLocalPosition()
		if y < 140:
			self.resizeButton.SetPosition(x, 140)
			return
		self.SetSize(self.GetWidth(), y + self.resizeButton.GetHeight())

		self.showingPageSize = y - (self.START_POSITION + 26)
		self.scrollBar.SetScrollBarSize(self.showingPageSize)

		self.__LocateMember()

		self.resizeButton.TurnOffCallBack()
		self.UpdateRect()
		self.resizeButton.TurnOnCallBack()

	def OnMouseWheel(self, length):
		lineCount = len(self.showingItemList)
		if self.IsInPosition() and self.scrollBar.IsShow() and lineCount > 0:
			dir = constInfo.WHEEL_TO_SCROLL(length)
			new_pos = self.scrollBar.GetPos() + ((1.0 / lineCount) * dir)
			new_pos = max(0.0, new_pos)
			new_pos = min(1.0, new_pos)
			self.scrollBar.SetPos(new_pos)
			return True
		return False

	def __LocateMember(self):
		if self.isLoaded==0:
			return

		if self.showingPageSize/20 >= len(self.showingItemList):
			self.scrollBar.Hide()
			self.startLine = 0
		else:
			if self.showingItemList:
				self.scrollBar.SetMiddleBarSize(float(self.showingPageSize/20) / float(len(self.showingItemList)))
			self.scrollBar.Show()

		#####

		yPos = self.START_POSITION
		heightLimit = self.GetHeight() - (self.START_POSITION + 13)

		map(ui.Window.Hide, self.showingItemList)

		for item in self.showingItemList[self.startLine:]:
			item.SetPosition(20 + item.GetStepWidth(), yPos)
			item.SetTop()
			item.Show()

			yPos += 20
			if yPos > heightLimit:
				break

	def __AddGroup(self):
		member = MessengerFriendGroup(ui.__mem_func__(self.GetSelf))
		member.Open()
		member.Show()
		self.groupList.append(member)

		member = MessengerGuildGroup(ui.__mem_func__(self.GetSelf))
		member.Open()
		member.Show()
		self.groupList.append(member)

		member = MessengerTeamGroup(ui.__mem_func__(self.GetSelf))
		member.Open()
		member.Show()
		self.groupList.append(member)

		if app.ENABLE_MESSENGER_BLOCK:
			member = MessengerBlockGroup(ui.__mem_func__(self.GetSelf))
			member.Open()
			member.Show()
			self.groupList.append(member)

	def __AddFamilyGroup(self):
		member = MessengerFamilyGroup(ui.__mem_func__(self.GetSelf))
		member.Open()
		member.Show()

		self.familyGroup = member

	def ClearGuildMember(self):
		self.groupList[GUILD].ClearMember()

	def SetWhisperButtonEvent(self, event):
		self.whisperButtonEvent=event

	def SetGuildButtonEvent(self, event):
		self.guildButtonEvent=event

	def SendMobileMessage(self, name):
		if not uiGameOption.MOBILE:
			return

		if not self.hasMobilePhoneNumber:
			questionDialog = uiCommon.QuestionDialog2()
			questionDialog.SetText1(localeInfo.MESSENGER_INPUT_MOBILE_PHONE_NUMBER_1)
			questionDialog.SetText2(localeInfo.MESSENGER_INPUT_MOBILE_PHONE_NUMBER_2)
			questionDialog.SetAcceptEvent(ui.__mem_func__(self.OnAcceptInputMobilePhoneNumber))
			questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCancelInputMobilePhoneNumber))
			questionDialog.SetWidth(400)
			questionDialog.Open()
			self.questionDialog = questionDialog
			return

		## Input Sending Mobile Message
		inputDialog = uiCommon.InputDialog()
		inputDialog.SetTitle(localeInfo.MESSENGER_SEND_MOBILE_MESSAGE_TITLE)
		inputDialog.SetMaxLength(50)
		inputDialog.SetAcceptEvent(ui.__mem_func__(self.OnInputMobileMessage))
		inputDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseInputDialog))
		inputDialog.name = name
		inputDialog.Open()
		self.inputDialog = inputDialog

	def OnAcceptInputMobilePhoneNumber(self):
		if not uiGameOption.MOBILE:
			return

		## Input Mobile Phone Number
		inputDialog = uiCommon.InputDialog()
		inputDialog.SetTitle(localeInfo.MESSENGER_INPUT_MOBILE_PHONE_NUMBER_TITLE)
		inputDialog.SetMaxLength(13)
		inputDialog.SetAcceptEvent(ui.__mem_func__(self.OnInputMobilePhoneNumber))
		inputDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseInputDialog))
		inputDialog.Open()
		self.inputDialog = inputDialog
		self.OnCancelInputMobilePhoneNumber()

	def OnCancelInputMobilePhoneNumber(self):
		if not uiGameOption.MOBILE:
			return
		self.questionDialog.Close()
		self.questionDialog = None
		return True

	def OnInputMobilePhoneNumber(self):
		if not uiGameOption.MOBILE:
			return

		text = self.inputDialog.GetText()
		if not text:
			return

		text.replace('-', '')
		net.SendChatPacket("/mobile " + text)
		self.OnCloseInputDialog()
		return True

	def OnInputMobileMessage(self):
		if not uiGameOption.MOBILE:
			return

		text = self.inputDialog.GetText()

		if not text:
			return

		net.SendMobileMessagePacket(self.inputDialog.name, text)
		self.OnCloseInputDialog()
		return True

	def OnCloseInputDialog(self):
		self.inputDialog.Close()
		self.inputDialog = None
		return True

	def OnPressGuildButton(self):
		self.guildButtonEvent()

	def OnPressAddFriendButton(self):
		friendNameBoard = uiCommon.InputDialog()
		friendNameBoard.SetTitle(localeInfo.MESSENGER_ADD_FRIEND)
		friendNameBoard.SetAcceptEvent(ui.__mem_func__(self.OnAddFriend))
		friendNameBoard.SetCancelEvent(ui.__mem_func__(self.OnCancelAddFriend))
		friendNameBoard.Open()
		self.friendNameBoard = friendNameBoard

	def OnAddFriend(self):
		text = self.friendNameBoard.GetText()
		if text:
			net.SendMessengerAddByNamePacket(text)
		self.friendNameBoard.Close()
		self.friendNameBoard = None
		return True

	def OnCancelAddFriend(self):
		self.friendNameBoard.Close()
		self.friendNameBoard = None
		return True

	if app.ENABLE_MESSENGER_BLOCK:
		def OnPressAddBlockButton(self):
			blockNameBoard = uiCommon.InputDialog()
			blockNameBoard.SetTitle(localeInfo.MESSENGER_ADD_BLOCK_FRIEND)
			blockNameBoard.SetAcceptEvent(ui.__mem_func__(self.OnAddBlock))
			blockNameBoard.SetCancelEvent(ui.__mem_func__(self.OnCancelAddBlock))
			blockNameBoard.Open()
			self.blockNameBoard = blockNameBoard

		def OnAddBlock(self):
			text2 = self.blockNameBoard.GetText()
			if text2:
				net.SendMessengerAddBlockByNamePacket(text2)
			self.blockNameBoard.Close()
			self.blockNameBoard = None
			return True

		def OnCancelAddBlock(self):
			self.blockNameBoard.Close()
			self.blockNameBoard = None
			return True

	def OnPressWhisperButton(self):
		if self.selectedItem:
			self.selectedItem.OnWhisper()

	def OnPressMobileButton(self):
		if self.selectedItem:
			self.selectedItem.OnMobileMessage()

	def OnPressRemoveButton(self):
		if self.selectedItem:
			if self.selectedItem.CanRemove():
				self.questionDialog = uiCommon.QuestionDialog()
				self.questionDialog.SetText(localeInfo.MESSENGER_DO_YOU_DELETE)
				self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.OnRemove))
				self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
				self.questionDialog.Open()

	def OnRemove(self):
		if self.selectedItem:
			if self.selectedItem.CanRemove():
				map(lambda arg, argDeletingItem=self.selectedItem: arg.RemoveMember(argDeletingItem), self.groupList)
				self.selectedItem.OnRemove()
				self.selectedItem.UnSelect()
				self.selectedItem = None
				self.OnRefreshList()

		self.OnCloseQuestionDialog()

	def OnScroll(self):
		scrollLineCount = len(self.showingItemList) - (self.showingPageSize/20)
		startLine = int(scrollLineCount * self.scrollBar.GetPos())

		if startLine != self.startLine:
			self.startLine = startLine
			self.__LocateMember()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	## CallBack
	def OnSelectItem(self, item):

		if self.selectedItem:
			if item != self.selectedItem:
				self.selectedItem.UnSelect()

		self.selectedItem = item

		if self.selectedItem:
			self.selectedItem.Select()

			if self.selectedItem.CanWhisper():
				self.whisperButton.Enable()
			else:
				self.whisperButton.Disable()

			if self.selectedItem.IsMobile():
				self.mobileButton.Enable()
			else:
				self.mobileButton.Disable()

			if self.selectedItem.CanRemove():
				self.removeButton.Enable()
			else:
				self.removeButton.Disable()

	def OnDoubleClickItem(self, item):

		if not self.selectedItem:
			return

		if self.selectedItem.IsOnline():
			self.OnPressWhisperButton()

		elif self.selectedItem.IsMobile():
			self.OnPressMobileButton()

	def GetSelf(self):
		return self

	def OnRefreshList(self):
		self.showingItemList = []

		if self.familyGroup:
			self.showingItemList.append(self.familyGroup)
			if self.familyGroup.GetLover():
				self.showingItemList.append(self.familyGroup.GetLover())

		for group in self.groupList:

			self.showingItemList.append(group)

			if group.IsOpen():

				loginMemberList = group.GetLoginMemberList()
				logoutMemberList = group.GetLogoutMemberList()

				if loginMemberList or logoutMemberList:
					for member in loginMemberList:
						self.showingItemList.append(member)
					for member in logoutMemberList:
						self.showingItemList.append(member)

				else:
					item = MessengerItem(ui.__mem_func__(self.GetSelf))
					item.SetName(localeInfo.MESSENGER_EMPTY_LIST)
					self.showingItemList.append(item)

		self.__LocateMember()

	def RefreshMessenger(self):
		self.OnRefreshList()

	## EventHandler
	def __AddList(self, groupIndex, key, name):
		group = self.groupList[groupIndex]
		member = group.FindMember(key)
		if not member:
			member = group.AppendMember(key, name)
			self.OnSelectItem(None)
		return member

	def OnRemoveList(self, groupIndex, key):
		group = self.groupList[groupIndex]
		group.RemoveMember(group.FindMember(key))
		self.OnRefreshList()

	def OnRemoveAllList(self, groupIndex):
		group = self.groupList[groupIndex]
		group.ClearMember()
		self.OnRefreshList()

	def OnLogin(self, groupIndex, key, name=None):
		if not name:
			name = key
		group = self.groupList[groupIndex]
		member = self.__AddList(groupIndex, key, name)
		member.SetName(name)
		member.Online()
		self.OnRefreshList()

		if groupIndex in (FRIEND, TEAM) and constInfo.SHOW_MESSENGER_NOTIFICATION:
			tchat("onLogin name %s" % str(name))

			if not constInfo.PM_ONLINE_POPUP_DICT.has_key(name):
				constInfo.PM_ONLINE_POPUP_DICT[name] = "init"
				return

			if time.clock() > constInfo.PM_ONLINE_POPUP_LOADED:
				state = "online"
				if not self.ClearOnlinePopup(name,state):
					return

				self.OnlinePopupAddQueue(name, state)

	def OnLogout(self, groupIndex, key, name=None):
		group = self.groupList[groupIndex]
		member = self.__AddList(groupIndex, key, name)
		if not name:
			name = key

		member.SetName(name)
		member.Offline()
		self.OnRefreshList()

		if groupIndex in (FRIEND, TEAM) and constInfo.SHOW_MESSENGER_NOTIFICATION:

			if not constInfo.PM_ONLINE_POPUP_DICT.has_key(name):
				constInfo.PM_ONLINE_POPUP_DICT[name] = "init"
				return

			if time.clock() > constInfo.PM_ONLINE_POPUP_LOADED:
				state = "offline"

				if not self.ClearOnlinePopup(name,state):
					return

				self.OnlinePopupAddQueue(name, state)

	if constInfo.SHOW_MESSENGER_NOTIFICATION:

		def ClearOnlinePopup(self, name, state):
			retValue = True
			for obj in self.onlinePopup:
				if obj.IsShow():
					if obj.GetUserName() == name and obj.GetUserState() == state:
						retValue = False
				else:
					self.onlinePopup.remove(obj)
			return retValue

		def OnlinePopupAddQueue(self, name, state):
			names = []
			for item in self.OnlinePopupQueue:
				names.append(item[0])

			if name in names:
				for item in self.OnlinePopupQueue:
					self.OnlinePopupQueue.remove(item)
					return

			self.OnlinePopupQueue.append([name, state, app.GetTime()])
		

		def OnlinePopupProcessQueue(self):
			for item in self.OnlinePopupQueue:
				name, state, time = item

				if state == "online":
					onlinePopup = uiCommon.OnlinePopup()
					onlinePopup.SetStep(len(self.onlinePopup)*30)
					onlinePopup.SetUserName(name,state)
					onlinePopup.SAFE_SetEvent(self.OpenWhisper, name)
					onlinePopup.SlideIn()
					self.onlinePopup.append(onlinePopup)
					constInfo.PM_ONLINE_POPUP_DICT[name] = state
					self.OnlinePopupQueue.remove(item)

				elif state == "offline":
					if time + 2 < app.GetTime():
						onlinePopup = uiCommon.OnlinePopup()
						onlinePopup.SetStep(len(self.onlinePopup)*30)
						onlinePopup.SetUserName(name,state)
						onlinePopup.SlideIn()
						self.onlinePopup.append(onlinePopup)
						constInfo.PM_ONLINE_POPUP_DICT[name] = state
						self.OnlinePopupQueue.remove(item)

		def OnUpdate(self):
			if len(self.OnlinePopupQueue):
				self.OnlinePopupProcessQueue()


	def OpenWhisper(self, userName):
		self.whisperButtonEvent(userName)

	def OnMobile(self, groupIndex, key, mobileFlag):
		group = self.groupList[groupIndex]
		member = group.FindMember(key)
		if not member:
			return
		member.SetMobile(mobileFlag)
		self.OnRefreshList()

	def OnAddLover(self, name, lovePoint):
		if not self.familyGroup:
			self.__AddFamilyGroup()

		member = self.familyGroup.AppendMember(0, name)
		member.SetName(name)
		member.SetLovePoint(lovePoint)
		member.Offline()
		self.OnRefreshList()

	def OnUpdateLovePoint(self, lovePoint):
		if not self.familyGroup:
			return

		lover = self.familyGroup.GetLover()
		if not lover:
			return

		lover.SetLovePoint(lovePoint)

	def OnLoginLover(self):
		if not self.familyGroup:
			return

		lover = self.familyGroup.GetLover()
		if not lover:
			return

		lover.Online()

	def OnLogoutLover(self):
		if not self.familyGroup:
			return

		lover = self.familyGroup.GetLover()
		if not lover:
			return

		lover.Offline()

	def ClearLoverInfo(self):
		if not self.familyGroup:
			return

		self.familyGroup.ClearMember()
		self.familyGroup = None
		self.OnRefreshList()

	def RefreshTeamState(self):
		group = self.groupList[TEAM]
		group.RefreshStateImage()
