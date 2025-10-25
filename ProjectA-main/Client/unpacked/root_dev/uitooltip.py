import dbg
import player
import item
import grp
import wndMgr
import skill
import shop
import exchange
import grpText
import safebox
import localeInfo
import app
import background
import nonplayer
import chr
import auction

import ui
import mouseModule
import constInfo

WARP_SCROLLS = [22011, 22000, 22010]

DESC_DEFAULT_MAX_COLS = 26 
DESC_WESTERN_MAX_COLS = 35
DESC_WESTERN_MAX_WIDTH = 220

def chop(n):
	return int(n)

def SplitDescription(desc, limit):
	total_tokens = desc.split()
	line_tokens = []
	line_len = 0
	lines = []
	for token in total_tokens:
		if "|" in token:
			sep_pos = token.find("|")
			line_tokens.append(token[:sep_pos])

			lines.append(" ".join(line_tokens))
			line_len = len(token) - (sep_pos + 1)
			line_tokens = [token[sep_pos+1:]]
		else:
			line_len += len(token)
			if len(line_tokens) + line_len > limit:
				lines.append(" ".join(line_tokens))
				line_len = len(token)
				line_tokens = [token]
			else:
				line_tokens.append(token)
	
	if line_tokens:
		lines.append(" ".join(line_tokens))

	return lines

def GET_AFFECT_STRING(affType, affValue):
	if 0 == affType:
		return None

	try:
		if player.GetName().startswith('['):
			affectString = ItemToolTip.AFFECT_DICT[affType]
			if type(affectString) != str:
				return affectString(affValue) + " " + str(affType)

			if affectString.find("%d") != -1:
				return str(affectString % affValue) + " " + str(affType)
			else:
				return affectString + " " + str(affType)

		affectString = ItemToolTip.AFFECT_DICT[affType]
		if type(affectString) != str:
			return affectString(affValue)

		if affectString.find("%d") != -1:
			return affectString % affValue
		else:
			return affectString
	except TypeError:
		return "TypeError[%s] %s x %s" % (affType, affValue, affectString)
	except KeyError:
		return "UNKNOWN_TYPE[%s] %s" % (affType, affValue)

def GET_ACCE_AFFECT_STRINGF(affType, affValueCur, affValueMax):
	if 0 == affType:
		return None

	try:
		affectString = ItemToolTip.AFFECT_DICT[affType]
		if type(ItemToolTip.AFFECT_DICT[affType]) != str:
			text = affectString(None).replace("%d", "%s")
		else:
			text = affectString.replace("%d", "%s")
		pos = text.find("%s")
		if pos != -1:
			startPos = pos
			endPos = pos + 2

			if pos > 0:
				if text[pos-1] == "+":
					startPos -= 1
			if pos < len(text) - 2:
				if text[pos+1:pos+2+1]:
					endPos += 2

			copyData = text[startPos:endPos]
			text = text[:endPos] + " " + (localeInfo.TOOLTIP_ACCE_ATTR_MAX_INFO % copyData) + text[endPos:]

			if affValueCur < 1.0:
				affValueCur = 1
			else:
				affValueCur = int(affValueCur)

			# max 25%
			affValueMax = affValueMax * 0.25
			if affValueMax < 1.0:
				affValueMax = 1
			else:
				affValueMax = int(affValueMax)

			return text % (localeInfo.FloatAsString(affValueCur), localeInfo.FloatAsString(affValueMax))
		else:
			return text
	except TypeError as e:
		return "UNKNOWN_VALUE[%s] %s %s: %s" % (affType, affValueCur, affValueMax, str(e))
	except KeyError as e:
		return "UNKNOWN_TYPE[%s] %s %s: %s" % (affType, affValueCur, affValueMax, str(e))

###################################################################################################
## ToolTip
##
##   NOTE : ����� Item�� Skill�� ������� Ưȭ ���ѵξ���
##          ������ �״��� �ǹ̰� ���� ����
##
class ToolTip(ui.ThinBoard):

	TOOL_TIP_WIDTH = 190
	TOOL_TIP_HEIGHT = 10

	TEXT_LINE_HEIGHT = 17

	TITLE_COLOR = grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)
	SPECIAL_TITLE_COLOR = grp.GenerateColor(1.0, 0.7843, 0.0, 1.0)
	NORMAL_COLOR = grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)
	FONT_COLOR = grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)
	PRICE_COLOR = 0xffFFB96D

	HIGH_PRICE_COLOR = SPECIAL_TITLE_COLOR
	MIDDLE_PRICE_COLOR = grp.GenerateColor(0.85, 0.85, 0.85, 1.0)
	LOW_PRICE_COLOR = grp.GenerateColor(0.7, 0.7, 0.7, 1.0)

	ENABLE_COLOR = grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)
	DISABLE_COLOR = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)

	NEGATIVE_COLOR = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)

	POSITIVE_COLOR = grp.GenerateColor(0.5411, 0.7254, 0.5568, 1.0)
	POSITIVE_COLOR_HEX = "b0dfb4"

	SPECIAL_POSITIVE_COLOR = grp.GenerateColor(0.6911, 0.8754, 0.7068, 1.0)
	SPECIAL_POSITIVE_COLOR_LOW = grp.GenerateColor(0.6911, 0.8754, 0.7068, 0.5)
	SPECIAL_POSITIVE_COLOR2 = grp.GenerateColor(0.8824, 0.9804, 0.8824, 1.0)
	SPECIAL_COSTUME_45_COLOR = grp.GenerateColor(0.0, 0.6, 0.6, 1.0)
	SOCKET_CHANGED_COLOR = grp.GenerateColor(0.8784, 0.47, 0.3137, 1.0)
	APPLY_CHANGED_COLOR = grp.GenerateColor(0.8784, 0.47, 0.3137, 1.0)
	ATTR_CHANGED_COLOR = grp.GenerateColor(0.8784, 0.47, 0.3137, 1.0)

	CONDITION_COLOR = 0xffBEB47D
	CAN_LEVEL_UP_COLOR = 0xff8EC292
	CANNOT_LEVEL_UP_COLOR = DISABLE_COLOR
	NEED_SKILL_POINT_COLOR = 0xff9A9CDB
	
	def __init__(self, width = TOOL_TIP_WIDTH, isPickable=False):
		ui.ThinBoard.__init__(self, "TOP_MOST")

		if isPickable:
			pass
		else:
			self.AddFlag("not_pick")

		self.AddFlag("float")

		self.followFlag = True
		self.toolTipWidth = width
		if app.ENABLE_ZODIAC:
			self.alwaysUp = False
		self.xPos = -1
		self.yPos = -1

		self.defFontName = constInfo.GetChoosenFontName( )
		self.ClearToolTip()

	def __del__(self):
		ui.ThinBoard.__del__(self)
	if app.ENABLE_ZODIAC:
		def SetAlwaysUp(self, flag):
			self.alwaysUp = flag
	def ClearToolTip(self):
		self.toolTipHeight = 12
		self.childrenList = []

	def SetFollow(self, flag):
		self.followFlag = flag

	def SetDefaultFontName(self, fontName):
		self.defFontName = fontName

	def AppendSpace(self, size):
		self.toolTipHeight += size
		self.ResizeToolTip()

	def AppendHorizontalLine(self):

		for i in xrange(2):
			horizontalLine = ui.Line()
			horizontalLine.SetParent(self)
			horizontalLine.SetPosition(0, self.toolTipHeight + 3 + i)
			horizontalLine.SetWindowHorizontalAlignCenter()
			horizontalLine.SetSize(150, 0)
			horizontalLine.Show()

			if 0 == i:
				horizontalLine.SetColor(0xff555555)
			else:
				horizontalLine.SetColor(0xff000000)

			self.childrenList.append(horizontalLine)

		self.toolTipHeight += 11
		self.ResizeToolTip()

	def AlignHorizonalCenter(self):
		for child in self.childrenList:
			(x, y)=child.GetLocalPosition()
			child.SetPosition(self.toolTipWidth/2, y)

		self.ResizeToolTip()

	def SetThinBoardSize(self, width, height = 12) :
		self.toolTipWidth = width 
		self.toolTipHeight = height

	def AutoAppendTextLine(self, text, color = FONT_COLOR, centerAlign = True):
		textLine = ui.TextLine()
		textLine.SetParent(self)
		textLine.SetFontName(self.defFontName)
		textLine.SetPackedFontColor(color)
		textLine.SetText(text)
		textLine.SetOutline()
		textLine.SetFeather(False)
		textLine.Show()

		if centerAlign:
			textLine.SetPosition(self.toolTipWidth/2, self.toolTipHeight)
			textLine.SetHorizontalAlignCenter()

		else:
			textLine.SetPosition(10, self.toolTipHeight)

		self.childrenList.append(textLine)

		(textWidth, textHeight)=textLine.GetTextSize()

		textWidth += 40
		textHeight += 5

		if self.toolTipWidth < textWidth:
			self.toolTipWidth = textWidth

		self.toolTipHeight += textHeight

		return textLine

	def AutoAppendTextLine2(self, text, color = FONT_COLOR, centerAlign = True):
		textLine = ui.TextLine()
		textLine.SetParent(self)
		textLine.SetFontName(self.defFontName)
		textLine.SetPackedFontColor(color)
		textLine.SetText(text)
		textLine.SetOutline()
		textLine.SetFeather(False)
		textLine.Show()

		if centerAlign:
			textLine.SetWindowHorizontalAlignCenter()
			textLine.SetHorizontalAlignCenter()
			textLine.SetPosition(0, self.toolTipHeight)
		else:
			textLine.SetPosition(10, self.toolTipHeight)

		self.childrenList.append(textLine)

		(textWidth, textHeight)=textLine.GetTextSize()

		textWidth += 40
		textHeight += 5

		if self.toolTipWidth < textWidth:
			self.toolTipWidth = textWidth

		self.toolTipHeight += textHeight

		return textLine

	def AppendTextLine(self, text, color = FONT_COLOR, centerAlign = True):
		textLine = ui.TextLine()
		textLine.SetParent(self)
		textLine.SetFontName(self.defFontName)
		textLine.SetPackedFontColor(color)
		textLine.SetText(text)
		textLine.SetOutline()
		textLine.SetFeather(False)
		textLine.Show()

		if centerAlign:
			textLine.SetPosition(self.toolTipWidth/2, self.toolTipHeight)
			textLine.SetHorizontalAlignCenter()

		else:
			textLine.SetPosition(10, self.toolTipHeight)

		self.childrenList.append(textLine)

		self.toolTipHeight += self.TEXT_LINE_HEIGHT
		self.ResizeToolTip()

		return textLine

	def AppendImage(self, imageName):
		image = ui.MakeImageBox(self, imageName, 0, self.toolTipHeight)

		self.toolTipHeight += image.GetHeight()
		self.childrenList.append(image)
		self.AlignHorizonalCenter()
		self.ShowToolTip()

	def AppendDescription(self, desc, limit, color = FONT_COLOR):
		if localeInfo.IsEUROPE():
			self.__AppendDescription_WesternLanguage(desc, color)
		else:
			self.__AppendDescription_EasternLanguage(desc, limit, color)

	def __AppendDescription_EasternLanguage(self, description, characterLimitation, color=FONT_COLOR):
		length = len(description)
		if 0 == length:
			return

		lineCount = grpText.GetSplitingTextLineCount(description, characterLimitation)
		for i in xrange(lineCount):
			if 0 == i:
				self.AppendSpace(5)
			self.AppendTextLine(grpText.GetSplitingTextLine(description, characterLimitation, i), color)

	def __AppendDescription_WesternLanguage(self, desc, color=FONT_COLOR):
		lines = SplitDescription(desc, DESC_WESTERN_MAX_COLS)
		if not lines:
			return

		self.AppendSpace(5)
		for line in lines:
			self.AppendTextLine(line, color)

	def ResizeToolTip(self):
		self.SetSize(self.toolTipWidth, self.TOOL_TIP_HEIGHT + self.toolTipHeight)

	def SetTitle(self, name):
		self.AppendTextLine(name, self.TITLE_COLOR)

	def GetLimitTextLineColor(self, curValue, limitValue):
		if curValue < limitValue:
			return self.DISABLE_COLOR

		return self.ENABLE_COLOR

	def GetChangeTextLineColor(self, value, isSpecial=False):
		if value > 0:
			if isSpecial:
				return self.SPECIAL_POSITIVE_COLOR
			else:
				return self.POSITIVE_COLOR

		if 0 == value:
			return self.NORMAL_COLOR

		return self.NEGATIVE_COLOR

	def SetToolTipPosition(self, x = -1, y = -1):
		self.xPos = x
		self.yPos = y

	def ShowToolTip(self):
		self.SetTop()
		self.Show()

		self.OnUpdate()

	def HideToolTip(self):
		self.Hide()

	def OnUpdate(self):

		if not self.followFlag:
			return

		x = 0
		y = 0
		width = self.GetWidth()
		height = self.toolTipHeight

		if -1 == self.xPos and -1 == self.yPos:
			(mouseX, mouseY) = wndMgr.GetMousePosition()

			#ENABLE_ZODIAC_TEMPLE
			if app.ENABLE_ZODIAC and mouseY < wndMgr.GetScreenHeight() - 300 and not self.alwaysUp:
				y = mouseY + 40
			else:
				y = mouseY - height - 30

			if app.ENABLE_ZODIAC and constInfo.ZODIAC_WINDOW_FIX == 1:
				if mouseX < wndMgr.GetScreenWidth() - 150 and not self.alwaysUp:
					x = mouseX - width/2 - 10
				else:
					x = mouseX - width/2 - 85
			else:
				x = mouseX - width/2
			#ENABLE_ZODIAC_TEMPLE
		else:
			x = self.xPos - width/2
			y = self.yPos - height

		x = max(x, 0)
		y = max(y, 0)
		x = min(x + width/2, wndMgr.GetScreenWidth() - width/2) - width/2
		y = min(y + self.GetHeight(), wndMgr.GetScreenHeight()) - self.GetHeight()

		parentWindow = self.GetParentProxy()
		if parentWindow:
			(gx, gy) = parentWindow.GetGlobalPosition()
			x -= gx
			y -= gy

		self.SetPosition(x, y)

class ItemToolTip(ToolTip):

	CHARACTER_NAMES = ( 
		localeInfo.TOOLTIP_WARRIOR,
		localeInfo.TOOLTIP_ASSASSIN,
		localeInfo.TOOLTIP_SURA,
		localeInfo.TOOLTIP_SHAMAN,
		# localeInfo.TOOLTIP_WOLFMAN,
	)		

	CHARACTER_COUNT = len(CHARACTER_NAMES)
	WEAR_NAMES = ( 
		localeInfo.TOOLTIP_ARMOR, 
		localeInfo.TOOLTIP_HELMET, 
		localeInfo.TOOLTIP_SHOES, 
		localeInfo.TOOLTIP_WRISTLET, 
		localeInfo.TOOLTIP_WEAPON, 
		localeInfo.TOOLTIP_NECK,
		localeInfo.TOOLTIP_EAR,
		localeInfo.TOOLTIP_UNIQUE,
		localeInfo.TOOLTIP_SHIELD,
		localeInfo.TOOLTIP_ARROW,
	)
	WEAR_COUNT = len(WEAR_NAMES)

	AFFECT_DICT = {
		item.APPLY_MAX_HP : localeInfo.TOOLTIP_MAX_HP,
		item.APPLY_MAX_SP : localeInfo.TOOLTIP_MAX_SP,
		item.APPLY_CON : localeInfo.TOOLTIP_CON,
		item.APPLY_INT : localeInfo.TOOLTIP_INT,
		item.APPLY_STR : localeInfo.TOOLTIP_STR,
		item.APPLY_DEX : localeInfo.TOOLTIP_DEX,
		item.APPLY_ATT_SPEED : localeInfo.TOOLTIP_ATT_SPEED,
		item.APPLY_MOV_SPEED : localeInfo.TOOLTIP_MOV_SPEED,
		item.APPLY_CAST_SPEED : localeInfo.TOOLTIP_CAST_SPEED,
		item.APPLY_HP_REGEN : localeInfo.TOOLTIP_HP_REGEN,
		item.APPLY_SP_REGEN : localeInfo.TOOLTIP_SP_REGEN,
		item.APPLY_POISON_PCT : localeInfo.TOOLTIP_APPLY_POISON_PCT,
		item.APPLY_STUN_PCT : localeInfo.TOOLTIP_APPLY_STUN_PCT,
		item.APPLY_SLOW_PCT : localeInfo.TOOLTIP_APPLY_SLOW_PCT,
		item.APPLY_CRITICAL_PCT : localeInfo.TOOLTIP_APPLY_CRITICAL_PCT,
		item.APPLY_PENETRATE_PCT : localeInfo.TOOLTIP_APPLY_PENETRATE_PCT,

		item.APPLY_ATTBONUS_WARRIOR : localeInfo.TOOLTIP_APPLY_ATTBONUS_WARRIOR,
		item.APPLY_ATTBONUS_ASSASSIN : localeInfo.TOOLTIP_APPLY_ATTBONUS_ASSASSIN,
		item.APPLY_ATTBONUS_SURA : localeInfo.TOOLTIP_APPLY_ATTBONUS_SURA,
		item.APPLY_ATTBONUS_SHAMAN : localeInfo.TOOLTIP_APPLY_ATTBONUS_SHAMAN,
		item.APPLY_ATTBONUS_MONSTER : localeInfo.TOOLTIP_APPLY_ATTBONUS_MONSTER,
		item.APPLY_ATTBONUS_ZODIAC : localeInfo.TOOLTIP_APPLY_ATTBONUS_ZODIAC,

		item.APPLY_ATTBONUS_HUMAN : localeInfo.TOOLTIP_APPLY_ATTBONUS_HUMAN,
		item.APPLY_ATTBONUS_ANIMAL : localeInfo.TOOLTIP_APPLY_ATTBONUS_ANIMAL,
		item.APPLY_ATTBONUS_ORC : localeInfo.TOOLTIP_APPLY_ATTBONUS_ORC,
		item.APPLY_ATTBONUS_MILGYO : localeInfo.TOOLTIP_APPLY_ATTBONUS_MILGYO,
		item.APPLY_ATTBONUS_UNDEAD : localeInfo.TOOLTIP_APPLY_ATTBONUS_UNDEAD,
		item.APPLY_ATTBONUS_DEVIL : localeInfo.TOOLTIP_APPLY_ATTBONUS_DEVIL,
		item.APPLY_STEAL_HP : localeInfo.TOOLTIP_APPLY_STEAL_HP,
		item.APPLY_STEAL_SP : localeInfo.TOOLTIP_APPLY_STEAL_SP,
		item.APPLY_MANA_BURN_PCT : localeInfo.TOOLTIP_APPLY_MANA_BURN_PCT,
		item.APPLY_DAMAGE_SP_RECOVER : localeInfo.TOOLTIP_APPLY_DAMAGE_SP_RECOVER,
		item.APPLY_BLOCK : localeInfo.TOOLTIP_APPLY_BLOCK,
		item.APPLY_DODGE : localeInfo.TOOLTIP_APPLY_DODGE,
		item.APPLY_RESIST_SWORD : localeInfo.TOOLTIP_APPLY_RESIST_SWORD,
		item.APPLY_RESIST_TWOHAND : localeInfo.TOOLTIP_APPLY_RESIST_TWOHAND,
		item.APPLY_RESIST_DAGGER : localeInfo.TOOLTIP_APPLY_RESIST_DAGGER,
		item.APPLY_RESIST_BELL : localeInfo.TOOLTIP_APPLY_RESIST_BELL,
		item.APPLY_RESIST_FAN : localeInfo.TOOLTIP_APPLY_RESIST_FAN,
		item.APPLY_RESIST_BOW : localeInfo.TOOLTIP_RESIST_BOW,
		item.APPLY_RESIST_FIRE : localeInfo.TOOLTIP_RESIST_FIRE,
		item.APPLY_RESIST_ELEC : localeInfo.TOOLTIP_RESIST_ELEC,
		item.APPLY_RESIST_MAGIC : localeInfo.TOOLTIP_RESIST_MAGIC,
		item.APPLY_RESIST_WIND : localeInfo.TOOLTIP_APPLY_RESIST_WIND,
		item.APPLY_REFLECT_MELEE : localeInfo.TOOLTIP_APPLY_REFLECT_MELEE,
		item.APPLY_REFLECT_CURSE : localeInfo.TOOLTIP_APPLY_REFLECT_CURSE,
		item.APPLY_POISON_REDUCE : localeInfo.TOOLTIP_APPLY_POISON_REDUCE,
		item.APPLY_KILL_SP_RECOVER : localeInfo.TOOLTIP_APPLY_KILL_SP_RECOVER,
		item.APPLY_EXP_DOUBLE_BONUS : localeInfo.TOOLTIP_APPLY_EXP_DOUBLE_BONUS,
		item.APPLY_GOLD_DOUBLE_BONUS : localeInfo.TOOLTIP_APPLY_GOLD_DOUBLE_BONUS,
		item.APPLY_ITEM_DROP_BONUS : localeInfo.TOOLTIP_APPLY_ITEM_DROP_BONUS,
		item.APPLY_POTION_BONUS : localeInfo.TOOLTIP_APPLY_POTION_BONUS,
		item.APPLY_KILL_HP_RECOVER : localeInfo.TOOLTIP_APPLY_KILL_HP_RECOVER,
		item.APPLY_IMMUNE_STUN : localeInfo.TOOLTIP_APPLY_IMMUNE_STUN,
		item.APPLY_IMMUNE_SLOW : localeInfo.TOOLTIP_APPLY_IMMUNE_SLOW,
		item.APPLY_IMMUNE_FALL : localeInfo.TOOLTIP_APPLY_IMMUNE_FALL,
		item.APPLY_BOW_DISTANCE : localeInfo.TOOLTIP_BOW_DISTANCE,
		item.APPLY_DEF_GRADE_BONUS : localeInfo.TOOLTIP_DEF_GRADE,
		item.APPLY_ATT_GRADE_BONUS : localeInfo.TOOLTIP_ATT_GRADE,
		item.APPLY_MAGIC_ATT_GRADE : localeInfo.TOOLTIP_MAGIC_ATT_GRADE,
		item.APPLY_MAGIC_DEF_GRADE : localeInfo.TOOLTIP_MAGIC_DEF_GRADE,
		item.APPLY_MAX_STAMINA : localeInfo.TOOLTIP_MAX_STAMINA,
		item.APPLY_MALL_ATTBONUS : localeInfo.TOOLTIP_MALL_ATTBONUS,
		item.APPLY_MALL_DEFBONUS : localeInfo.TOOLTIP_MALL_DEFBONUS,
		item.APPLY_MALL_EXPBONUS : localeInfo.TOOLTIP_MALL_EXPBONUS,
		item.APPLY_MALL_ITEMBONUS : localeInfo.TOOLTIP_MALL_ITEMBONUS,
		item.APPLY_MALL_GOLDBONUS : localeInfo.TOOLTIP_MALL_GOLDBONUS,
		item.APPLY_SKILL_DAMAGE_BONUS : localeInfo.TOOLTIP_SKILL_DAMAGE_BONUS,
		item.APPLY_NORMAL_HIT_DAMAGE_BONUS : localeInfo.TOOLTIP_NORMAL_HIT_DAMAGE_BONUS,
		item.APPLY_SKILL_DEFEND_BONUS : localeInfo.TOOLTIP_SKILL_DEFEND_BONUS,
		item.APPLY_NORMAL_HIT_DEFEND_BONUS : localeInfo.TOOLTIP_NORMAL_HIT_DEFEND_BONUS,
		item.APPLY_RESIST_WARRIOR : localeInfo.TOOLTIP_APPLY_RESIST_WARRIOR,
		item.APPLY_RESIST_ASSASSIN : localeInfo.TOOLTIP_APPLY_RESIST_ASSASSIN,
		item.APPLY_RESIST_SURA : localeInfo.TOOLTIP_APPLY_RESIST_SURA,
		item.APPLY_RESIST_SHAMAN : localeInfo.TOOLTIP_APPLY_RESIST_SHAMAN,
		
		# item.APPLY_BLEEDING_PCT : localeInfo.TOOLTIP_APPLY_BLEEDING_PCT,
		# item.APPLY_BLEEDING_REDUCE : localeInfo.TOOLTIP_APPLY_BLEEDING_REDUCE,
		# item.APPLY_ATTBONUS_WOLFMAN : localeInfo.TOOLTIP_APPLY_ATTBONUS_WOLFMAN,
		# item.APPLY_RESIST_WOLFMAN : localeInfo.TOOLTIP_APPLY_RESIST_WOLFMAN,
		# item.APPLY_RESIST_CLAW : localeInfo.TOOLTIP_APPLY_RESIST_CLAW,

		item.APPLY_ACCEDRAIN_RATE : localeInfo.TOOLTIP_APPLY_ACCEDRAIN_RATE,

		# item.APPLY_PET_EXP_BONUS : localeInfo.TOOLTIP_APPLY_PET_EXP_BONUS,

		item.APPLY_RESIST_MONSTER : localeInfo.TOOLTIP_APPLY_RESIST_MONSTER,
		item.APPLY_RESIST_BOSS : localeInfo.TOOLTIP_APPLY_RESIST_BOSS,
		item.APPLY_ATTBONUS_METIN : localeInfo.TOOLTIP_APPLY_ATTBONUS_METIN,
		item.APPLY_ATTBONUS_BOSS : localeInfo.TOOLTIP_APPLY_ATTBONUS_BOSS,
		
		item.APPLY_RESIST_SWORD_PEN : localeInfo.TOOLTIP_APPLY_RESIST_SWORD_PEN,
		item.APPLY_RESIST_TWOHAND_PEN : localeInfo.TOOLTIP_APPLY_RESIST_TWOHAND_PEN,
		item.APPLY_RESIST_DAGGER_PEN : localeInfo.TOOLTIP_APPLY_RESIST_DAGGER_PEN,
		item.APPLY_RESIST_BELL_PEN : localeInfo.TOOLTIP_APPLY_RESIST_BELL_PEN,
		item.APPLY_RESIST_FAN_PEN : localeInfo.TOOLTIP_APPLY_RESIST_FAN_PEN,
		item.APPLY_RESIST_BOW_PEN : localeInfo.TOOLTIP_APPLY_RESIST_BOW_PEN,
		item.APPLY_RESIST_ATTBONUS_HUMAN : localeInfo.TOOLTIP_APPLY_RESIST_ATTBONUS_HUMAN,
		
		item.APPLY_ATTBONUS_ALL_ELEMENTS : localeInfo.TOOLTIP_APPLY_ATTBONUS_ALL_ELEMENTS,
		
		item.APPLY_ATTBONUS_ELEC : localeInfo.TOOLTIP_APPLY_ATTBONUS_ELEC,
		item.APPLY_ATTBONUS_FIRE : localeInfo.TOOLTIP_APPLY_ATTBONUS_FIRE,
		item.APPLY_ATTBONUS_ICE : localeInfo.TOOLTIP_APPLY_ATTBONUS_ICE,
		item.APPLY_ATTBONUS_WIND : localeInfo.TOOLTIP_APPLY_ATTBONUS_WIND,
		item.APPLY_ATTBONUS_EARTH : localeInfo.TOOLTIP_APPLY_ATTBONUS_EARTH,
		item.APPLY_ATTBONUS_DARK : localeInfo.TOOLTIP_APPLY_ATTBONUS_DARK,
		
		item.APPLY_DEFENSE_BONUS : localeInfo.TOOLTIP_APPLY_DEFENSE_BONUS,

		item.APPLY_ANTI_RESIST_MAGIC : localeInfo.TOOLTIP_APPLY_ANTI_RESIST_MAGIC,
		item.APPLY_BLOCK_IGNORE_BONUS : localeInfo.TOOLTIP_APPLY_BLOCK_IGNORE_BONUS,
		
		# new
		item.APPLY_MAX_HP_PCT : localeInfo.TOOLTIP_APPLY_MAX_HP_PCT,
		item.APPLY_MAX_SP_PCT : localeInfo.TOOLTIP_APPLY_MAX_SP_PCT,
		item.APPLY_MAGIC_ATTBONUS_PER : localeInfo.TOOLTIP_APPLY_MAGIC_ATTBONUS_PER,
		item.APPLY_MELEE_MAGIC_ATTBONUS_PER : localeInfo.TOOLTIP_APPLY_MELEE_MAGIC_ATTBONUS_PER,
		item.APPLY_RESIST_ICE : localeInfo.TOOLTIP_APPLY_RESIST_ICE,
		item.APPLY_RESIST_EARTH : localeInfo.TOOLTIP_APPLY_RESIST_EARTH,
		item.APPLY_RESIST_DARK : localeInfo.TOOLTIP_APPLY_RESIST_DARK,
		item.APPLY_ANTI_CRITICAL_PCT : localeInfo.TOOLTIP_APPLY_ANTI_CRITICAL_PCT,
		item.APPLY_ANTI_PENETRATE_PCT : localeInfo.TOOLTIP_APPLY_ANTI_PENETRATE_PCT,
		item.APPLY_EXP_REAL_BONUS : localeInfo.TOOLTIP_APPLY_EXP_REAL_BONUS,

		item.APPLY_RESIST_HUMAN : localeInfo.TOOLTIP_APPLY_RESIST_HUMAN,

		item.APPLY_HEAL_EFFECT_BONUS : localeInfo.TOOLTTIP_APPLY_HEAL_EFFECT_BONUS,
		item.APPLY_CRITICAL_DAMAGE_BONUS : localeInfo.TOOLTTIP_APPLY_CRITICAL_DAMAGE_BONUS,
		item.APPLY_DOUBLE_ITEM_DROP_BONUS : localeInfo.TOOLTTIP_APPLY_DOUBLE_ITEM_DROP_BONUS,
		item.APPLY_DAMAGE_BY_SP_BONUS : localeInfo.TOOLTTIP_APPLY_DAMAGE_BY_SP_BONUS,
		item.APPLY_SINGLETARGET_SKILL_DAMAGE_BONUS : localeInfo.TOOLTTIP_APPLY_SINGLETARGET_SKILL_DAMAGE_BONUS,
		item.APPLY_MULTITARGET_SKILL_DAMAGE_BONUS : localeInfo.TOOLTTIP_APPLY_MULTITARGET_SKILL_DAMAGE_BONUS,
		item.APPLY_MIXED_DEFEND_BONUS : localeInfo.TOOLTTIP_APPLY_MIXED_DEFEND_BONUS,
		item.APPLY_EQUIP_SKILL_BONUS : localeInfo.TOOLTTIP_APPLY_EQUIP_SKILL_BONUS,
		item.APPLY_AURA_HEAL_EFFECT_BONUS : localeInfo.TOOLTTIP_APPLY_AURA_HEAL_EFFECT_BONUS,
		item.APPLY_AURA_EQUIP_SKILL_BONUS : localeInfo.TOOLTTIP_APPLY_AURA_EQUIP_SKILL_BONUS,
		item.APPLY_MOUNT_BUFF_BONUS : localeInfo.TOOLTTIP_APPLY_MOUNT_BUFF_BONUS,
		item.APPLY_SKILL_DURATION : localeInfo.TOOLTIP_APPLY_SKILL_DURATION,
		item.APPLY_RUNE_MOUNT_PARALYZE : localeInfo.TOOLTIP_APPLY_RUNE_MOUNT_PARALYZE,
	}

	AFFECT_RANGE_DICT = {
		item.APPLY_CRITICAL_PCT : localeInfo.TOOLTIP_RANGE_APPLY_CRITICAL_PCT,
		item.APPLY_PENETRATE_PCT : localeInfo.TOOLTIP_RANGE_APPLY_PENETRATE_PCT,
		item.APPLY_ATT_SPEED : localeInfo.TOOLTIP_RANGE_ATT_SPEED,
		item.APPLY_ATT_GRADE_BONUS : localeInfo.TOOLTIP_RANGE_ATT_GRADE,
		item.APPLY_DEF_GRADE_BONUS : localeInfo.TOOLTIP_RANGE_DEF_GRADE,
		item.APPLY_RESIST_MAGIC : localeInfo.TOOLTIP_RANGE_RESIST_MAGIC,
		item.APPLY_POTION_BONUS : localeInfo.TOOLTIP_RANGE_POTION_BONUS,
		item.APPLY_ATTBONUS_ELEC : localeInfo.TOOLTIP_APPLY_ATTBONUS_ELEC,
		item.APPLY_ATTBONUS_FIRE : localeInfo.TOOLTIP_APPLY_ATTBONUS_FIRE,
		item.APPLY_ATTBONUS_ICE : localeInfo.TOOLTIP_APPLY_ATTBONUS_ICE,
		item.APPLY_ATTBONUS_WIND : localeInfo.TOOLTIP_APPLY_ATTBONUS_WIND,
		item.APPLY_ATTBONUS_EARTH : localeInfo.TOOLTIP_APPLY_ATTBONUS_EARTH,
		item.APPLY_ATTBONUS_DARK : localeInfo.TOOLTIP_APPLY_ATTBONUS_DARK,
		item.APPLY_MAGIC_ATT_GRADE : localeInfo.TOOLTIP_RANGE_MAGIC_ATT_GRADE,
	}

	ATTRIBUTE_NEED_WIDTH = {
		23 : 230,
		24 : 230,
		25 : 230,
		26 : 220,
		27 : 210,

		35 : 210,
		36 : 210,
		37 : 210,
		38 : 210,
		39 : 210,
		40 : 210,
		41 : 210,

		42 : 220,
		43 : 230,
		45 : 230,
	}

	ANTI_FLAG_DICT = {
		0 : item.ITEM_ANTIFLAG_WARRIOR,
		1 : item.ITEM_ANTIFLAG_ASSASSIN,
		2 : item.ITEM_ANTIFLAG_SURA,
		3 : item.ITEM_ANTIFLAG_SHAMAN,
		# 4 : item.ITEM_ANTIFLAG_WOLFMAN,
	}

	FONT_COLOR = grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)

	def __init__(self, *args, **kwargs):
		ToolTip.__init__(self, *args, **kwargs)
		self.itemVnum = 0
		self.isShopItem = False
		self.bCannotUseItemForceSetDisableColor = True 

		self.canShowSearchItemHotkey = False

	def __del__(self):
		ToolTip.__del__(self)

	def SetShowSearchItemHotkey(self,booleanVal):
		self.canShowSearchItemHotkey = booleanVal

	def SetCannotUseItemForceSetDisableColor(self, enable):
		self.bCannotUseItemForceSetDisableColor = enable

	def CanEquip(self):
		if not item.IsEquipmentVID(self.itemVnum):
			return True

		race = player.GetRace()
		job = chr.RaceToJob(race)
		if not self.ANTI_FLAG_DICT.has_key(job):
			return False

		if item.IsAntiFlag(self.ANTI_FLAG_DICT[job]):
			return False

		sex = chr.RaceToSex(race)
		
		MALE = 1
		FEMALE = 0

		if item.IsAntiFlag(item.ITEM_ANTIFLAG_MALE) and sex == MALE:
			return False

		if item.IsAntiFlag(item.ITEM_ANTIFLAG_FEMALE) and sex == FEMALE:
			return False

		for i in xrange(item.LIMIT_MAX_NUM):
			(limitType, limitValue) = item.GetLimit(i)

			if item.LIMIT_LEVEL == limitType:
				if player.GetStatus(player.LEVEL) < limitValue:
					return False

			if constInfo.ENABLE_LEVEL_LIMIT_MAX:
				if limitType == item.LIMIT_LEVEL_MAX:
					if player.GetStatus(player.LEVEL) >= limitValue:
						return False

			"""
			elif item.LIMIT_STR == limitType:
				if player.GetStatus(player.ST) < limitValue:
					return False
			elif item.LIMIT_DEX == limitType:
				if player.GetStatus(player.DX) < limitValue:
					return False
			elif item.LIMIT_INT == limitType:
				if player.GetStatus(player.IQ) < limitValue:
					return False
			elif item.LIMIT_CON == limitType:
				if player.GetStatus(player.HT) < limitValue:
					return False
			"""

		return True

	def AppendTextLine(self, text, color = FONT_COLOR, centerAlign = True):

		if not self.CanEquip() and self.bCannotUseItemForceSetDisableColor:
			color = self.DISABLE_COLOR

		return ToolTip.AppendTextLine(self, text, color, centerAlign)

	def ClearToolTip(self):
		self.isShopItem = False
		self.toolTipWidth = self.TOOL_TIP_WIDTH
		ToolTip.ClearToolTip(self)

	def IsShowingItemPrice(self, item_vnum, price):
		if shop.IsOpen():
			if not shop.IsPrivateShop():
				return True

		item.SelectItem(1, 2, item_vnum)
		item_type = item.GetItemType()
		if item_type == item.ITEM_TYPE_WEAPON or item_type == item.ITEM_TYPE_ARMOR or item_type == item.ITEM_TYPE_BELT:
			return False

		if item_type == item.ITEM_TYPE_COSTUME:
			if price < 50000:
				return False

		return True

	def SetInventoryItem(self, slotIndex, window = player.INVENTORY):
		itemVnum = player.GetItemIndex(window, slotIndex)
		if 0 == itemVnum:
			return

		self.ClearToolTip()

		metinSlot = [player.GetItemMetinSocket(window, slotIndex, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
		attrSlot = [player.GetItemAttribute(window, slotIndex, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]

		self.AddItemData(itemVnum, metinSlot, attrSlot, slotIndex)
		self.AddGMOwnerInfo(player.IsGMOwner(window, slotIndex))

		price = player.GetIBuyItemPrice(window, slotIndex) / 5
		if self.IsShowingItemPrice(itemVnum, price):
			item.SelectItem(1, 2, itemVnum)
			self.AppendSellingPrice(int(price))

	def SetAuctionItem(self, container_type, index):
		auction.SetContainerType(container_type)

		itemVnum, itemCount, itemPrice = auction.GetItemInfo(index)
		if 0 == itemVnum:
			return

		self.ClearToolTip()
		self.isShopItem = True

		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(auction.GetItemSocket(index, i))
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append(auction.GetItemAttribute(index, i))

		self.AddItemData(itemVnum, metinSlot, attrSlot)
		self.AppendPrice(itemPrice)

	def SetAuctionItemByID(self, container_type, itemID):
		index = auction.GetItemDataByID(container_type, itemID)
		if index == -1:
			return

		self.SetAuctionItem(container_type, index)

	def SetAuctionShopBuilderItem(self, invenType, invenPos, auctionShopSlotIndex):
		itemVnum = player.GetItemIndex(invenType, invenPos)
		if 0 == itemVnum:
			return

		item.SelectItem(1, 2, itemVnum)
		self.ClearToolTip()
		self.AppendSellingPrice(auction.GetShopCreatingItemPrice(invenType, invenPos))

		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(player.GetItemMetinSocket(invenPos, i))
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append(player.GetItemAttribute(invenPos, i))

		self.AddItemData(itemVnum, metinSlot, attrSlot)

	if (app.COMBAT_ZONE):
		def SetShopItemByCombatZoneCoin(self, slotIndex):
			itemVnum = shop.GetItemID(slotIndex)
			if 0 == itemVnum:
				return

			price = shop.GetItemPrice(slotIndex)
			self.ClearToolTip()
			self.isShopItem = True

			metinSlot = []
			for i in xrange(player.METIN_SOCKET_MAX_NUM):
				metinSlot.append(shop.GetItemMetinSocket(slotIndex, i))
			attrSlot = []
			for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
				attrSlot.append(shop.GetItemAttribute(slotIndex, i))

			self.AddItemData(itemVnum, metinSlot, attrSlot)
			self.AppendSpace(5)
			self.AppendTextLine(localeInfo.TOOLTIP_BUYPRICE  % (localeInfo.NumberToCombatZoneCoinString(price)), self.HIGH_PRICE_COLOR)

	def SetShopItem(self, slotIndex):
		itemVnum = shop.GetItemID(slotIndex)
		if 0 == itemVnum:
			return

		price = shop.GetItemPrice(slotIndex)
		self.ClearToolTip()
		self.isShopItem = True

		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(shop.GetItemMetinSocket(slotIndex, i))
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append(shop.GetItemAttribute(slotIndex, i))

		self.AddItemData(itemVnum, metinSlot, attrSlot)

		priceVnum = shop.GetItemPriceItem(slotIndex)
		# tchat("PriceVnum %d count %d" % (priceVnum, price))

		if constInfo.SECOND_ITEM_PRICE:
			priceVnum = shop.GetItemPriceItem(slotIndex)
			priceVnum2 = shop.GetItemPriceItem(slotIndex, 2)
			price2 = shop.GetItemPrice(slotIndex, 2)
			if priceVnum != 0:
				self.AppendItemPrice(priceVnum, price)
				if priceVnum2 and price2:
					self.AppendItemPrice(priceVnum2, price2)
			else:
				self.AppendPrice(price)
		else:
			if priceVnum != 0:
				self.AppendItemPrice(priceVnum, price)
			else:
				self.AppendPrice(price)
		
		item.SelectItem(1, 2, itemVnum)
		itemType = item.GetItemType()
		if constInfo.ENABLE_EMOJI and item.ITEM_TYPE_COSTUME == itemType:
			self.AppendSpace(5)
			self.AppendTextLine("|E%s|e %s" % ('alt', localeInfo.TOOLTIP_EMOJI_PREVIEW_WEAR))

	def SetExchangeOwnerItem(self, slotIndex):
		itemVnum = exchange.GetItemVnumFromSelf(slotIndex)
		if 0 == itemVnum:
			return

		self.ClearToolTip()

		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(exchange.GetItemMetinSocketFromSelf(slotIndex, i))
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append(exchange.GetItemAttributeFromSelf(slotIndex, i))

		self.AddItemData(itemVnum, metinSlot, attrSlot)

	def SetExchangeTargetItem(self, slotIndex):
		itemVnum = exchange.GetItemVnumFromTarget(slotIndex)
		if 0 == itemVnum:
			return

		self.ClearToolTip()

		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(exchange.GetItemMetinSocketFromTarget(slotIndex, i))
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append(exchange.GetItemAttributeFromTarget(slotIndex, i))

		self.AddItemData(itemVnum, metinSlot, attrSlot)

	def SetPrivateShopBuilderItem(self, invenType, invenPos, privateShopSlotIndex):
		itemVnum = player.GetItemIndex(invenType, invenPos)
		if 0 == itemVnum:
			return

		item.SelectItem(1, 2, itemVnum)
		self.ClearToolTip()
		self.AppendSellingPrice(shop.GetPrivateShopItemPrice(invenType, invenPos))

		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(player.GetItemMetinSocket(invenPos, i))
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append(player.GetItemAttribute(invenPos, i))

		self.AddItemData(itemVnum, metinSlot, attrSlot)

	def SetSafeBoxItem(self, slotIndex):
		itemVnum = safebox.GetItemID(slotIndex)
		if 0 == itemVnum:
			return

		self.ClearToolTip()
		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(safebox.GetItemMetinSocket(slotIndex, i))
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append(safebox.GetItemAttribute(slotIndex, i))

		self.AddItemData(itemVnum, metinSlot, attrSlot)

	def SetAcceWindowItem(self, slotIndex):
		itemVnum = player.GetAcceItemID(slotIndex)

		if 0 == itemVnum:
			return

		self.ClearToolTip()

		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(player.GetAcceItemMetinSocket(slotIndex, i))

		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append(player.GetAcceItemAttribute(slotIndex, i))

		self.AddItemData(itemVnum, metinSlot, attrSlot)#, player.GetAcceItemFlags(slotIndex))

	def SetGuildSafeBoxItem(self, slotIndex):
		itemVnum = safebox.GetGuildItemID(slotIndex)
		if 0 == itemVnum:
			return

		self.ClearToolTip()
		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(safebox.GetGuildItemMetinSocket(slotIndex, i))
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append(safebox.GetGuildItemAttribute(slotIndex, i))

		self.AddItemData(itemVnum, metinSlot, attrSlot)

	def SetMallItem(self, slotIndex):
		itemVnum = safebox.GetMallItemID(slotIndex)
		if 0 == itemVnum:
			return

		self.ClearToolTip()
		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(safebox.GetMallItemMetinSocket(slotIndex, i))
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append(safebox.GetMallItemAttribute(slotIndex, i))

		self.AddItemData(itemVnum, metinSlot, attrSlot)

	if app.ENABLE_COSTUME_BONUS_TRANSFER:
		def SetCostumeBonusTransferWindowItem(self, selectedSlotPos):
			itemVnum = player.GetCostumeBonusTransferItemID(selectedSlotPos)
			if 0 == itemVnum:
				return

			self.ClearToolTip()
			if shop.IsOpen() and not shop.IsPrivateShop():
				self.AppendSellingPrice(item.GetISellItemPrice(item.SelectItem(1, 2, itemVnum)))

			metinSlot = [player.GetCostumeBonusTransferItemMetinSocket(selectedSlotPos, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
			attrSlot = [player.GetCostumeBonusTransferItemAttribute(selectedSlotPos, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]

			self.AddItemData(itemVnum, metinSlot, attrSlot)

	def SetItemToolTip(self, itemVnum):
		self.ClearToolTip()
		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(0)
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append((0, 0))

		self.AddItemData(itemVnum, metinSlot, attrSlot)

	def __AppendAttackSpeedInfo(self, item):
		atkSpd = item.GetValue(0)

		if atkSpd < 80:
			stSpd = localeInfo.TOOLTIP_ITEM_VERY_FAST
		elif atkSpd <= 95:
			stSpd = localeInfo.TOOLTIP_ITEM_FAST
		elif atkSpd <= 105:
			stSpd = localeInfo.TOOLTIP_ITEM_NORMAL
		elif atkSpd <= 120:
			stSpd = localeInfo.TOOLTIP_ITEM_SLOW
		else:
			stSpd = localeInfo.TOOLTIP_ITEM_VERY_SLOW

		self.AppendTextLine(localeInfo.TOOLTIP_ITEM_ATT_SPEED % stSpd, self.NORMAL_COLOR)

	def __AppendAttackGradeInfo(self):
		atkGrade = item.GetValue(1)
		self.AppendTextLine(localeInfo.TOOLTIP_ITEM_ATT_GRADE % atkGrade, self.GetChangeTextLineColor(atkGrade))

	def __AppendAttackPowerInfo(self):
		minPower = item.GetValue(3)
		maxPower = item.GetValue(4)
		addPower = item.GetValue(5)
		if maxPower > minPower:
			self.AppendTextLine(localeInfo.TOOLTIP_ITEM_ATT_POWER % (minPower+addPower, maxPower+addPower), self.POSITIVE_COLOR)
		else:
			self.AppendTextLine(localeInfo.TOOLTIP_ITEM_ATT_POWER_ONE_ARG % (minPower+addPower), self.POSITIVE_COLOR)

	def __AppendMagicAttackInfo(self):
		minMagicAttackPower = item.GetValue(1)
		maxMagicAttackPower = item.GetValue(2)
		addPower = item.GetValue(5)

		if minMagicAttackPower > 0 or maxMagicAttackPower > 0:
			if maxMagicAttackPower > minMagicAttackPower:
				self.AppendTextLine(localeInfo.TOOLTIP_ITEM_MAGIC_ATT_POWER % (minMagicAttackPower+addPower, maxMagicAttackPower+addPower), self.POSITIVE_COLOR)
			else:
				self.AppendTextLine(localeInfo.TOOLTIP_ITEM_MAGIC_ATT_POWER_ONE_ARG % (minMagicAttackPower+addPower), self.POSITIVE_COLOR)

	def drainedPercent(self, value, percent):
		return int(float(value) / float(100) * float(percent))

	def __AppendAttackPowerInfoAcce(self, inDrainPct, itemInDrainVnum):
		item.SelectItem(1, 2, itemInDrainVnum)
		minPower = self.drainedPercent(item.GetValue(3), inDrainPct)
		maxPower = self.drainedPercent(item.GetValue(4), inDrainPct)
		addPower = self.drainedPercent(item.GetValue(5), inDrainPct)

		if maxPower > minPower:
			self.AppendTextLine(localeInfo.TOOLTIP_ITEM_ATT_POWER % (minPower+addPower, maxPower+addPower), self.POSITIVE_COLOR)
		else:
			self.AppendTextLine(localeInfo.TOOLTIP_ITEM_ATT_POWER_ONE_ARG % (minPower+addPower), self.POSITIVE_COLOR)

	def __AppendMagicAttackInfoAcce(self, inDrainPct, itemInDrainVnum):
		item.SelectItem(1, 2, itemInDrainVnum)
		minMagicAttackPower = self.drainedPercent(item.GetValue(1), inDrainPct)
		maxMagicAttackPower = self.drainedPercent(item.GetValue(2), inDrainPct)
		addPower = self.drainedPercent(item.GetValue(5), inDrainPct)

		if minMagicAttackPower > 0 or maxMagicAttackPower > 0:
			if maxMagicAttackPower > minMagicAttackPower:
				self.AppendTextLine(localeInfo.TOOLTIP_ITEM_MAGIC_ATT_POWER % (minMagicAttackPower+addPower, maxMagicAttackPower+addPower), self.POSITIVE_COLOR)
			else:
				self.AppendTextLine(localeInfo.TOOLTIP_ITEM_MAGIC_ATT_POWER_ONE_ARG % (minMagicAttackPower+addPower), self.POSITIVE_COLOR)
			
	def __AppendMagicDefenceInfoAcce(self, drainInPercent, itemInDrainVnum):
		item.SelectItem(1, 2, itemInDrainVnum)
		magicDefencePower = self.drainedPercent(item.GetValue(0), drainInPercent)

		if magicDefencePower > 0:
			self.AppendTextLine(localeInfo.TOOLTIP_ITEM_MAGIC_DEF_POWER % magicDefencePower, self.GetChangeTextLineColor(magicDefencePower))

	def __AppendAttributeInformationAcce(self, percent, attrSlot):
		if 0 != attrSlot:

			emptyBonusCount = 0
			for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
				type, value = attrSlot[i][0], attrSlot[i][1]
				if 0 == value:
					emptyBonusCount += 1
			# canAppendNoBonus = (item.GetItemType() != item.ITEM_TYPE_USE) and emptyBonusCount != player.ATTRIBUTE_SLOT_MAX_NUM # ignoring bonus adders
			for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
				type, value = attrSlot[i][0], attrSlot[i][1]
				curValue = float(value) * float(percent) / 100.0

				if 0 == value:
					# if i <= 4 and canAppendNoBonus:
					# 	self.AutoAppendTextLine(localeInfo.TOOLTIP_NO_BONUS)
					continue

				if float(value) == curValue:
					affectString = GET_AFFECT_STRING(type, value)
				else:
					affectString = GET_ACCE_AFFECT_STRINGF(type, curValue, value)

				if affectString:
					affectColor = self.GetAttributeColor(i, value)
					self.AutoAppendTextLine(affectString, affectColor)

	def __AppendMagicDefenceInfo(self):
		magicDefencePower = item.GetValue(0)

		if magicDefencePower > 0:
			self.AppendTextLine(localeInfo.TOOLTIP_ITEM_MAGIC_DEF_POWER % magicDefencePower, self.GetChangeTextLineColor(magicDefencePower))

	def __AppendAttributeInformation(self, attrSlot, isCostume = False):
		if 0 != attrSlot:

			#tchat("attrSlot %s" % str(attrSlot))
			emptyBonusCount = 0
			for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
				type, value = attrSlot[i][0], attrSlot[i][1]
				if 0 == value:
					emptyBonusCount += 1
			canAppendNoBonus = (item.GetItemType() == item.ITEM_TYPE_COSTUME) and emptyBonusCount != player.ATTRIBUTE_SLOT_MAX_NUM # ignoring bonus adders
			for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
				type, value = attrSlot[i][0], attrSlot[i][1]

				if 0 == value:
					if i <= 4 and canAppendNoBonus:
						self.AutoAppendTextLine(localeInfo.TOOLTIP_NO_BONUS)
					continue

				real_value = value

				affectString = self.__GetAffectString(type, real_value)
				if affectString:
					if real_value != value:
						affectColor = self.ATTR_CHANGED_COLOR
					else:
						affectColor = self.GetAttributeColor(i, value, isCostume)
					self.AppendTextLine(affectString, affectColor)

	def GetAttributeColor(self, index, value, isCostume = False):
		if isCostume and index >= 3: # 4/5 bonuses for costume
			return self.SPECIAL_COSTUME_45_COLOR
		elif value > 0:
			if index >= 5: # 6/7 bonuses
				return self.SPECIAL_POSITIVE_COLOR2
			else:
				return self.SPECIAL_POSITIVE_COLOR
		elif value == 0:
			return self.NORMAL_COLOR
		else:
			return self.NEGATIVE_COLOR

	def __IsPolymorphItem(self, itemVnum):
		if itemVnum >= 70103 and itemVnum <= 70106:
			return 1
		return 0

	def __SetPolymorphItemTitle(self, monsterVnum, itemVnum):
		if localeInfo.IsVIETNAM():
			itemName =item.GetItemName()
			itemName+=" "
			itemName+=nonplayer.GetMonsterName(monsterVnum)
		else:
			itemName =nonplayer.GetMonsterName(monsterVnum)
			itemName+=" "
			itemName+=item.GetItemName()
		if app.IsEnableTestServerFlag():
			itemName += " (" + str(itemVnum) + ")"
		self.SetTitle(itemName)

	def __SetNormalItemTitle(self, itemVnum):
		if app.IsEnableTestServerFlag():
			self.SetTitle(item.GetItemName() + " (" + str(itemVnum) + ")")
		else:
			self.SetTitle(item.GetItemName())

	def __SetSpecialItemTitle(self, itemVnum):
		if app.IsEnableTestServerFlag():
			self.AppendTextLine(item.GetItemName() + " (" + str(itemVnum) + ")", self.SPECIAL_TITLE_COLOR)
		else:
			self.AppendTextLine(item.GetItemName(), self.SPECIAL_TITLE_COLOR)

	def __SetItemTitle(self, itemVnum, metinSlot, attrSlot):
		if self.__IsPolymorphItem(itemVnum):
			self.__SetPolymorphItemTitle(metinSlot[0], itemVnum)
		else:
			if constInfo.ENABLE_CRYSTAL_SYSTEM:
				if item.IsActiveCrystal(itemVnum):
					self.SetTitle(item.GetItemName() + " (" + localeInfo.GetCrystalClarityName(metinSlot[1]) + ")")
					return

			if self.__IsAttr(attrSlot):
				self.__SetSpecialItemTitle(itemVnum)
				return

			self.__SetNormalItemTitle(itemVnum)

	def __IsAttr(self, attrSlot):
		if not attrSlot:
			return False

		# if item.GetItemType() == item.ITEM_TYPE_PET:
			# return False

		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			type = attrSlot[i][0]
			if 0 != type:
				return True

		return False
	
	def AddRefineItemData(self, itemVnum, metinSlot, attrSlot = 0):
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlotData=metinSlot[i]
			if self.GetMetinItemIndex(metinSlotData) == constInfo.ERROR_METIN_STONE:
				metinSlot[i]=player.METIN_SOCKET_TYPE_SILVER

		self.AddItemData(itemVnum, metinSlot, attrSlot)

	def AddItemData_Offline(self, itemVnum, itemDesc, itemSummary, metinSlot, attrSlot):
		self.__AdjustMaxWidth(attrSlot, itemDesc)
		self.__SetItemTitle(itemVnum, metinSlot, attrSlot)
		
		if self.__IsHair(itemVnum):	
			self.__AppendHairIcon(itemVnum)

		### Description ###
		self.AppendDescription(itemDesc, 26)
		self.AppendDescription(itemSummary, 26, self.CONDITION_COLOR)

	def AddGMOwnerInfo(self, isGMOwner=True):
		if not isGMOwner:
			return

		self.AppendSpace(5)
		self.AppendTextLine(localeInfo.TOOLTIP_ITEM_NO_TRADE, self.NEGATIVE_COLOR) # TOOLTIP_GM_OWNER_INFO (to make it less obvious)

	def AppendIceCreamBonusInfo(self, itemVnum, metinSlot):
		#try:
		if not (itemVnum >= 95300 and itemVnum <= 95310):
			return

		self.AppendSpace(5)

		spaceBetween = 16
		slotSize = 32

		accWnd = None
		if itemVnum == 95310:
			accWnd = ui.MakeWindow(self,0,self.toolTipHeight,((slotSize-4) + spaceBetween)*player.METIN_SOCKET_MAX_NUM,slotSize)
			accWnd.SetWindowHorizontalAlignCenter()
			accWnd.Show()

			self.toolTipHeight += slotSize

		socketCount = 0
		nameText = ""
		affList = [[0,0] for i in xrange(player.METIN_SOCKET_MAX_NUM)]

		affType = 0
		affValue = 0

		if itemVnum >= 95300 and itemVnum <= 95309:
			if constInfo.SUNDAE_EVENT_BONUS_DATA.has_key(itemVnum):
				affType = constInfo.SUNDAE_EVENT_BONUS_DATA[itemVnum][0]
				affValue = constInfo.SUNDAE_EVENT_BONUS_DATA[itemVnum][1]
			affList[0] = [affType,affValue]
			socketCount += 1

		if itemVnum == 95310:
			for i in xrange(player.METIN_SOCKET_MAX_NUM):
				slotImage = ui.ImageBox()
				slotImage.SetParent(accWnd)
				slotImage.LoadImage("d:/ymir work/ui/game/windows/metin_slot_silver.sub")
				slotImage.SetPosition(i*(slotSize+spaceBetween),0)
				slotImage.Show()
				self.childrenList.append(slotImage)

				itemVnum = metinSlot[i]
				if itemVnum >= 95300 and itemVnum <= 95309:
					socketCount += 1
					metinImage = ui.ImageBox()
					metinImage.SetParent(slotImage)
					metinImage.SetPosition(2,2)
					metinImage.LoadImage(item.GetIconImageFileName(itemVnum))
					metinImage.Show()
					self.childrenList.append(metinImage)
					if constInfo.SUNDAE_EVENT_BONUS_DATA.has_key(itemVnum):
						affType = constInfo.SUNDAE_EVENT_BONUS_DATA[itemVnum][0]
						affValue = constInfo.SUNDAE_EVENT_BONUS_DATA[itemVnum][1]
					affList[i] = [affType,affValue]

					commaTxt = ""
					if i != socketCount-1:
						commaTxt = ", "
					nameText = "%s%s%s" % (nameText,item.GetItemName(itemVnum),commaTxt)

			self.childrenList.append(accWnd)
			self.AppendSpace(5)

		## Name
		if socketCount:
			#self.AppendTextLine(nameText)
			self.AppendSpace(5)
			for i in xrange(socketCount):
				affType = affList[i][0]
				affValue = affList[i][1]
				affString = GET_AFFECT_STRING(affType, affValue)
				if affString:
					self.AppendTextLine(affString,self.POSITIVE_COLOR)
				#else:
				#	self.AppendTextLine("UNKNOWN Bonus(%d,%d)" % (affType,affValue),self.POSITIVE_COLOR)
		else:
			self.AppendTextLine("[ No flavours ]")
		self.AppendSpace(5)

		#except:
		#	import exception
		#	exception.Abort("abracadasrtdfy")

	def AddItemData(self, itemVnum, metinSlot, attrSlot = 0, slotIndex = 0):
		self.itemVnum = itemVnum
		item.SelectItem(1, 2, itemVnum)
		itemType = item.GetItemType()
		itemSubType = item.GetItemSubType()

		if 50026 == itemVnum:
			if 0 != metinSlot:
				name = item.GetItemName()
				if metinSlot[0] > 0:
					name += " "
					name += localeInfo.NumberToMoneyString(metinSlot[0])
				self.SetTitle(name)
				self.ShowToolTip()
			return

		### Skill Book ###
		elif 50300 == itemVnum:
			if 0 != metinSlot:
				self.__SetSkillBookToolTip(metinSlot[0], localeInfo.TOOLTIP_SKILLBOOK_NAME, 1)
				self.ShowToolTip()
			return 
		elif 70037 == itemVnum:
			if 0 != metinSlot:
				self.__SetSkillBookToolTip(metinSlot[0], localeInfo.TOOLTIP_SKILL_FORGET_BOOK_NAME, 0)
				self.AppendDescription(item.GetItemDescription(), 26)
				self.AppendDescription(item.GetItemSummary(), 26, self.CONDITION_COLOR)
				self.ShowToolTip()
			return
		elif 70055 == itemVnum:
			if 0 != metinSlot:
				self.__SetSkillBookToolTip(metinSlot[0], localeInfo.TOOLTIP_SKILL_FORGET_BOOK_NAME, 0)
				self.AppendDescription(item.GetItemDescription(), 26)
				self.AppendDescription(item.GetItemSummary(), 26, self.CONDITION_COLOR)
				self.ShowToolTip()
			return
		###########################################################################################

		limitTimeType = item.LIMIT_NONE
		limitTimeValue = 0
		for i in xrange(item.LIMIT_MAX_NUM):

			(limitType, limitValue) = item.GetLimit(i)

			if limitType == item.LIMIT_REAL_TIME or limitType == item.LIMIT_REAL_TIME_START_FIRST_USE or limitType == item.LIMIT_TIMER_BASED_ON_WEAR:
				limitTimeType = limitType
				limitTimeValue = limitValue
				break

		itemDesc = item.GetItemDescription()
		itemSummary = item.GetItemSummary()
	
		self.__AdjustMaxWidth(attrSlot, itemDesc)
		self.__SetItemTitle(itemVnum, metinSlot, attrSlot)
		
		if self.__IsHair(itemVnum):	
			self.__AppendHairIcon(itemVnum)

		### Description ###
		self.AppendDescription(itemDesc, 26)
		self.AppendDescription(itemSummary, 26, self.CONDITION_COLOR)

		# sundae
		self.AppendIceCreamBonusInfo(itemVnum,metinSlot)

		### Weapon ###
		if item.ITEM_TYPE_WEAPON == itemType:

			self.__AppendLimitInformation()

			self.AppendSpace(5)

			## ��ä�� ��� ������ ���� ǥ���Ѵ�.
			if item.WEAPON_QUIVER == itemSubType:
				self.__AppendQuiverItemInformation(metinSlot)

			elif item.WEAPON_FAN == itemSubType:
				self.__AppendMagicAttackInfo()
				self.__AppendAttackPowerInfo()

			else:
				self.__AppendAttackPowerInfo()
				self.__AppendMagicAttackInfo()

			self.__AppendAffectInformation()
			self.__AppendAttributeInformation(attrSlot)

			self.AppendWearableInformation()

			if item.WEAPON_QUIVER != itemSubType:
				self.__AppendMetinSlotInfo(metinSlot)

		### Armor ###
		elif item.ITEM_TYPE_ARMOR == itemType:

			self.__AppendLimitInformation()

			## ����
			defGrade = item.GetValue(1)
			defBonus = item.GetValue(5)*2 ## ���� ǥ�� �߸� �Ǵ� ������ ����
			if defGrade > 0:
				self.AppendSpace(5)
				self.AppendTextLine(localeInfo.TOOLTIP_ITEM_DEF_GRADE % (defGrade+defBonus), self.GetChangeTextLineColor(defGrade))

			self.__AppendMagicDefenceInfo()
			self.__AppendAffectInformation()
			self.__AppendAttributeInformation(attrSlot)

			self.AppendWearableInformation()

			if itemSubType in (item.ARMOR_WRIST, item.ARMOR_NECK, item.ARMOR_EAR):				
				self.__AppendAccessoryMetinSlotInfo(metinSlot, constInfo.GET_ACCESSORY_MATERIAL_VNUM(itemVnum, itemSubType))
			else:
				self.__AppendMetinSlotInfo(metinSlot)
			
		elif item.ITEM_TYPE_COSTUME == itemType and itemSubType in (item.COSTUME_TYPE_BODY, item.COSTUME_TYPE_HAIR, item.COSTUME_TYPE_WEAPON, item.COSTUME_TYPE_ACCE_COSTUME, item.COSTUME_TYPE_PET, item.COSTUME_TYPE_MOUNT):
			self.__AppendLimitInformation()

			self.__AppendAffectInformation()
			if itemSubType != item.COSTUME_TYPE_ACCE_COSTUME:
				self.__AppendAttributeInformation(attrSlot, True)
			else:
				self.__AppendAttributeInformation(attrSlot, False)

			self.__AppendLimitTimeLeft(metinSlot)

			self.AppendWearableInformation()

		elif item.ITEM_TYPE_COSTUME == itemType and item.COSTUME_TYPE_ACCE == itemSubType:
			self.__AppendLimitInformation()

			itemInDrainPct = float(metinSlot[0])
			itemInDrainVnum = metinSlot[1]

			if itemInDrainPct == 0:
				itemInDrainPct = 25
				if __SERVER__ == 2:
					itemInDrainPct = item.GetAffect(0)[1]

			acceInDrain = self.__GetAffectString(item.APPLY_ACCEDRAIN_RATE, itemInDrainPct)
			if acceInDrain:
				self.AppendDescription(acceInDrain, 26, self.CONDITION_COLOR)

			if(itemInDrainVnum != 0):
				item.SelectItem(1, 2, itemInDrainVnum)
	
				if item.GetItemType() == item.ITEM_TYPE_WEAPON:
					item.SelectItem(1, 2, itemInDrainVnum)
					self.__AppendAttackPowerInfoAcce(itemInDrainPct, itemInDrainVnum)
					self.__AppendMagicAttackInfoAcce(itemInDrainPct, itemInDrainVnum)
				elif item.GetItemType() == item.ITEM_TYPE_ARMOR:
					item.SelectItem(1, 2, itemInDrainVnum)
					defGrade = self.drainedPercent(item.GetValue(1), itemInDrainPct)
					defBonus = self.drainedPercent(item.GetValue(5) * 2, itemInDrainPct)

					if defGrade > 0:
						self.AppendTextLine(localeInfo.TOOLTIP_ITEM_DEF_GRADE % (defGrade+defBonus), self.GetChangeTextLineColor(defGrade))

					self.__AppendMagicDefenceInfoAcce(itemInDrainPct, itemInDrainVnum)

				self.__AppendAffectInformationAcce(itemInDrainPct, itemInDrainVnum)			
				self.__AppendAttributeInformationAcce(itemInDrainPct, attrSlot)
	
			self.AppendWearableInformation()
			
			item.SelectItem(1, 2, itemVnum)

		elif item.ITEM_TYPE_DS == itemType:
			self.AppendTextLine(self.__DragonSoulInfoString(itemVnum))
			self.__AppendAttributeInformation(attrSlot)

			if 0 != metinSlot:

				if limitTimeType != item.LIMIT_NONE:
					time = metinSlot[0]

					if limitTimeType == item.LIMIT_REAL_TIME:
						self.AppendMallItemLastTime(time)
					elif limitTimeType == item.LIMIT_TIMER_BASED_ON_WEAR:
						self.AppendItemLastTime(time)

		elif item.ITEM_TYPE_BELT == itemType:
			self.__AppendLimitInformation()

			self.__AppendAffectInformation()
			self.__AppendAttributeInformation(attrSlot)

			self.AppendWearableInformation()

			materialVnum = 18900
			self.__AppendAccessoryMetinSlotInfo(metinSlot, (materialVnum, 0))#constInfo.GET_ACCESSORY_MATERIAL_VNUM(itemVnum, itemSubType))

		## Rod ##
		elif item.ITEM_TYPE_ROD == itemType:

			if 0 != metinSlot:
				curLevel = item.GetValue(0) / 10
				curEXP = metinSlot[0]
				maxEXP = item.GetValue(2)
				self.__AppendLimitInformation()
				self.__AppendRodInformation(curLevel, curEXP, maxEXP)

		## Pick ##
		elif item.ITEM_TYPE_PICK == itemType:

			if 0 != metinSlot:
				curLevel = item.GetValue(0) / 10
				curEXP = metinSlot[0]
				maxEXP = item.GetValue(2)
				self.__AppendLimitInformation()
				self.__AppendPickInformation(curLevel, curEXP, maxEXP)

		## Lottery ##
		elif item.ITEM_TYPE_LOTTERY == itemType:
			if 0 != metinSlot:

				ticketNumber = int(metinSlot[0])
				stepNumber = int(metinSlot[1])

				self.AppendSpace(5)
				self.AppendTextLine(localeInfo.TOOLTIP_LOTTERY_STEP_NUMBER % (stepNumber), self.NORMAL_COLOR)
				self.AppendTextLine(localeInfo.TOOLTIP_LOTTO_NUMBER % (ticketNumber), self.NORMAL_COLOR);

		### Metin ###
		elif item.ITEM_TYPE_METIN == itemType:
			self.AppendMetinInformation()
			self.AppendMetinWearInformation()

		### Fish ###
		elif item.ITEM_TYPE_FISH == itemType:
			if 0 != metinSlot:
				self.__AppendFishInfo(metinSlot[0])
		
		## item.ITEM_TYPE_BLEND
		elif item.ITEM_TYPE_BLEND == itemType:
			self.__AppendLimitInformation()

			if metinSlot and metinSlot[0] != 0:
				affectType = metinSlot[0]
				affectValue = metinSlot[1]
				time = metinSlot[2]
				self.AppendSpace(5)
				affectText = self.__GetAffectString(affectType, affectValue)

				self.AppendTextLine(affectText, self.NORMAL_COLOR)

				if constInfo.INFINITY_ITEMS and constInfo.IS_INFINITY_ITEMS(itemVnum):
					pass
				else:
					if time > 0:
						minute = (time / 60)
						second = (time % 60)
						timeString = localeInfo.TOOLTIP_POTION_TIME

						if minute > 0:
							timeString += str(minute) + localeInfo.TOOLTIP_POTION_MIN
						if second > 0:
							timeString += " " + str(second) + localeInfo.TOOLTIP_POTION_SEC

						self.AppendTextLine(timeString)
					else:
						self.AppendTextLine(localeInfo.BLEND_POTION_NO_TIME)
			elif item.IsBlend(itemVnum):
				affectType = item.GetBlendApplyType(itemVnum)
				affectValueMin = 0
				affectValueMax = 0
				affectDurMin = 0
				affectDurMax = 0

				for i in xrange(item.GetBlendDataCount(itemVnum)):
					data = item.GetBlendData(itemVnum, i)
					if affectValueMin == 0 or affectValueMin > data[0]:
						affectValueMin = data[0]
					if affectValueMax == 0 or affectValueMax < data[0]:
						affectValueMax = data[0]
					if affectDurMin == 0 or affectDurMin > data[1]:
						affectDurMin = data[1]
					if affectDurMax == 0 or affectDurMax < data[1]:
						affectDurMax = data[1]

				if affectValueMin == affectValueMax:
					affectText = GET_AFFECT_STRING(affectType, affectValueMin)
				else:
					affectText = self.__GetAffectRangeString(affectType, affectValueMin, affectValueMax)

				self.AutoAppendTextLine(affectText, self.NORMAL_COLOR)

				
				if affectDurMin == affectDurMax:
					timeString = localeInfo.TOOLTIP_TIME % localeInfo.SecondToDHMS(affectDurMin)
				else:
					timeString = localeInfo.TOOLTIP_TIME_RANGE % (localeInfo.SecondToDHMS(affectDurMin), localeInfo.SecondToDHMS(affectDurMax))
				if constInfo.INFINITY_ITEMS and constInfo.IS_INFINITY_ITEMS(itemVnum):
					pass
				else:
					self.AppendTextLine(timeString)

				self.ResizeToolTip()
				self.AlignHorizonalCenter()
			else:
				self.AppendTextLine("BLEND_POTION_NO_INFO")

		elif item.ITEM_TYPE_UNIQUE == itemType:
			self.__AppendLimitInformation()

			if 0 != metinSlot:

				time = metinSlot[2]

				if time:
					if 1 == item.GetValue(2): ## �ǽð� �̿� Flag / ���� ���ص� �ش�
						self.AppendMallItemLastTime(time)
					else:
						self.AppendUniqueItemLastTime(time)

				else:
					self.__AppendLimitTimeLeft(metinSlot)

		### Use ###
		elif item.ITEM_TYPE_USE == itemType:
			self.__AppendLimitInformation()

			if item.USE_POTION == itemSubType or item.USE_POTION_NODELAY == itemSubType:
				self.__AppendPotionInformation()

			elif item.USE_ABILITY_UP == itemSubType:
				self.__AppendAbilityPotionInformation()

			elif item.USE_ADD_SPECIFIC_ATTRIBUTE == itemSubType:
				self.__AppendAttributeInformation(attrSlot)


			if (app.COMBAT_ZONE):
				if itemVnum in [50287, 50288, 50290]:
					if 0 != metinSlot:
						useCount = int(metinSlot[0])

						self.AppendSpace(5)
						self.AppendTextLine(localeInfo.TOOLTIP_REST_USABLE_COUNT % ((3 - useCount)), self.CONDITION_COLOR)

			## ���� ������
			if 27989 == itemVnum:
				if 0 != metinSlot:
					useCount = int(metinSlot[0])

					self.AppendSpace(5)
					self.AppendTextLine(localeInfo.TOOLTIP_REST_USABLE_COUNT % (6 - useCount), self.NORMAL_COLOR)

			## �̺�Ʈ ������
			elif 50004 == itemVnum:
				if 0 != metinSlot:
					useCount = int(metinSlot[0])

					self.AppendSpace(5)
					self.AppendTextLine(localeInfo.TOOLTIP_REST_USABLE_COUNT % (10 - useCount), self.NORMAL_COLOR)

			## �ڵ�����
			elif constInfo.IS_AUTO_POTION(itemVnum):#72723 == itemVnum or 72724 == itemVnum:
				if 0 != metinSlot:
					## 0: Ȱ��ȭ, 1: ��뷮, 2: �ѷ�
					isActivated = int(metinSlot[0])
					usedAmount = float(metinSlot[1])
					totalAmount = float(metinSlot[2])
					
					if 0 == totalAmount:
						totalAmount = 1
					
					self.AppendSpace(5)

					if 0 != isActivated:
						self.AppendTextLine("(%s)" % (localeInfo.TOOLTIP_AUTO_POTION_USING), self.SPECIAL_POSITIVE_COLOR)
						self.AppendSpace(5)
						
					self.AppendTextLine(localeInfo.TOOLTIP_AUTO_POTION_REST % (100.0 - ((usedAmount / totalAmount) * 100.0)), self.POSITIVE_COLOR)
								
			## ��ȯ ����
			elif itemVnum in WARP_SCROLLS:
				if 0 != metinSlot:
					xPos = int(metinSlot[0])
					yPos = int(metinSlot[1])

					if xPos != 0 and yPos != 0:
						(mapName, xBase, yBase) = background.GlobalPositionToMapInfo(xPos, yPos)
						
						localeMapName=localeInfo.MINIMAP_ZONE_NAME_DICT.get(mapName, "")

						self.AppendSpace(5)

						if localeMapName!="":						
							self.AppendTextLine(localeInfo.TOOLTIP_MEMORIZED_POSITION % (localeMapName, int(xPos-xBase)/100, int(yPos-yBase)/100), self.NORMAL_COLOR)
						else:
							self.AppendTextLine(localeInfo.TOOLTIP_MEMORIZED_POSITION_ERROR % (int(xPos)/100, int(yPos)/100), self.NORMAL_COLOR)
							dbg.TraceError("NOT_EXIST_IN_MINIMAP_ZONE_NAME_DICT: %s" % mapName)

			#####
			if item.USE_SPECIAL == itemSubType:
				if 0 != metinSlot:

					if limitTimeType != item.LIMIT_NONE:
						time = metinSlot[0]

						if limitTimeType == item.LIMIT_REAL_TIME:
							self.AppendMallItemLastTime(time)
						elif limitTimeType == item.LIMIT_TIMER_BASED_ON_WEAR:
							self.AppendItemLastTime(time)

					if 1 == item.GetValue(2):
						time = metinSlot[player.METIN_SOCKET_MAX_NUM-1]
						self.AppendMallItemLastTime(time)
			
			elif item.USE_TIME_CHARGE_PER == itemSubType:
				bHasRealtimeFlag = 0
				for i in xrange(item.LIMIT_MAX_NUM):
					(limitType, limitValue) = item.GetLimit(i)

					if item.LIMIT_REAL_TIME == limitType:
						bHasRealtimeFlag = 1
				if metinSlot[2]:
					self.AppendTextLine(localeInfo.TOOLTIP_TIME_CHARGER_PER(metinSlot[2]))
				else:
					self.AppendTextLine(localeInfo.TOOLTIP_TIME_CHARGER_PER(item.GetValue(0)))
 		
				if 1 == bHasRealtimeFlag:
					self.AppendMallItemLastTime(metinSlot[0])

			elif item.USE_TIME_CHARGE_FIX == itemSubType:
				bHasRealtimeFlag = 0
				for i in xrange(item.LIMIT_MAX_NUM):
					(limitType, limitValue) = item.GetLimit(i)

					if item.LIMIT_REAL_TIME == limitType:
						bHasRealtimeFlag = 1
				if metinSlot[2]:
					self.AppendTextLine(localeInfo.TOOLTIP_TIME_CHARGER_FIX(metinSlot[2]))
				else:
					self.AppendTextLine(localeInfo.TOOLTIP_TIME_CHARGER_FIX(item.GetValue(0)))
		
				if 1 == bHasRealtimeFlag:
					self.AppendMallItemLastTime(metinSlot[0])
			if constInfo.BRAVERY_CAPE_STORE:
				if itemVnum == 93359:
					self.AppendTextLine(localeInfo.STORED_CAPE_COUNT(metinSlot[0]))

		elif item.ITEM_TYPE_TOTEM == itemType:
			self.__AppendLimitInformation()
			self.__AppendAffectInformation(True)
			self.__AppendAttributeInformation(attrSlot)

		elif item.ITEM_TYPE_SOUL == itemType:
			self.__AppendAttributeInformation(attrSlot)
			
		elif itemVnum == 30304: # Zin-Bonin Key
			self.__AppendLimitTimeLeft(metinSlot)

		elif item.ITEM_TYPE_PET == itemType:
			self.__AppendAffectInformation(True)
			self.__AppendLimitTimeLeft(metinSlot)

		elif constInfo.ENABLE_CRYSTAL_SYSTEM and item.IsActiveCrystal(itemVnum):
			level = metinSlot[2]
			if metinSlot[1] == 4:
				level = localeInfo.CRYSTAL_TOOLTIP_LEVEL_MAX
			self.AppendTextLine(localeInfo.CRYSTAL_TOOLTIP_LEVEL % str(level))
			self.__AppendAttributeInformation(attrSlot)
			self.AppendSpace(5)
			self.AppendItemLastTime(metinSlot[0])

		elif item.ITEM_TYPE_MOUNT == itemType:
			if item.MOUNT_SUB_SUMMON == itemSubType:
				self.__AppendLimitInformation()
				self.__AppendAffectInformation(True)
				self.__AppendLimitTimeLeft(metinSlot)

				# if item.GetValue(1) == constInfo.HORSE_GRADE_MAX:
				# 	if attrSlot != 0:
				# 		self.AppendSpace(5)
				# 		self.AppendTextLine(localeInfo.TOOLTIP_KING_HORSE_BONUS, self.CONDITION_COLOR)
				# 		for i in xrange(player.HORSE_BONUS_COUNT):
				# 			bonusLevel = attrSlot[i][0]
				# 			applyType, applyValue, itemCount = player.GetHorseBonusProto(i, max(0, bonusLevel - 1))
				# 			_temp1, _temp2, itemCount = player.GetHorseBonusProto(i, bonusLevel)
				# 			itemCountGiven = attrSlot[i][1]
				# 			itemCountNeed = itemCount - itemCountGiven

				# 			if bonusLevel == 0:
				# 				applyValue = 0

				# 			if bonusLevel < player.HORSE_MAX_BONUS_LEVEL:
				# 				self.AutoAppendTextLine(localeInfo.PET_TEXT_TOOLTIP_BONUS2 % (bonusLevel, itemCountNeed, GET_AFFECT_STRING(applyType, applyValue)))
				# 			else:
				# 				self.AutoAppendTextLine(localeInfo.PET_TEXT_TOOLTIP_BONUS % (bonusLevel, GET_AFFECT_STRING(applyType, applyValue)))
				# 			img = self.AppendFillAniImage("d:/ymir work/ui/game/pet/bar/empty.tga", "d:/ymir work/ui/game/pet/bar/green.tga", 3, 2, 5)
				# 			if bonusLevel < player.HORSE_MAX_BONUS_LEVEL:
				# 				img.SetPercentage(itemCountGiven * 100.0 / float(max(1, itemCount)))
				# 			else:
				# 				img.SetPercentage(100.0)

				# 		self.AlignHorizonalCenter()

				# 	if metinSlot != 0 and metinSlot[1] != 0 and (metinSlot[2] == 0 or metinSlot[2] > app.GetGlobalTimeStamp()):
				# 		self.AppendSpace(5)
				# 		self.AppendTextLine(localeInfo.TOOLTIP_KING_HORSE_MELTED, self.CONDITION_COLOR)
						
				# 		item.SelectItem(1, 2, metinSlot[1])
				# 		self.AppendTextLine(item.GetItemName())
				# 		self.__AppendAffectInformation()

				# 		if metinSlot[2] > 0:
				# 			self.AppendMallItemLastTime(metinSlot[2], False)

				# item.SelectItem(1, 2, itemVnum)

		elif constInfo.ENABLE_EMOJI and item.ITEM_TYPE_GIFTBOX == itemType:
			self.AppendTextLine("|E%s|e + |E%s|e %s" % ('ctrl', 'mouse_right', localeInfo.TOOLTIP_EMOJI_MULTIOPEN_GIFTBOX % min(player.GetItemCount(slotIndex), 200)))

		elif constInfo.ENABLE_EMOJI and item.ITEM_TYPE_MATERIAL == itemType:
			self.AppendTextLine("|E%s|e + |E%s|e %s" % ('shift', 'mouse_left', localeInfo.TOOLTIP_EMOJI_UNSTACK))

		elif item.ITEM_TYPE_QUEST == itemType:
			if 0 != metinSlot:

				if limitTimeType != item.LIMIT_NONE:
					time = metinSlot[0]

					if limitTimeType == item.LIMIT_REAL_TIME:
						self.AppendMallItemLastTime(time)
					elif limitTimeType == item.LIMIT_TIMER_BASED_ON_WEAR:
						self.AppendItemLastTime(time)
			if constInfo.ENABLE_EMOJI:
				self.AppendTextLine("|E%s|e %s" % ('mouse_right', localeInfo.TOOLTIP_EMOJI_USE))

		else:
			self.__AppendLimitInformation()

		if constInfo.ENABLE_WARP_BIND_RING:
			if itemVnum == 93266:
				if metinSlot != 0:
					import cfg
					player_name = cfg.Get(cfg.SAVE_PLAYER, "warp_ring_%d" % metinSlot[0], "")
					if player_name and player_name != player.GetName():
						self.AppendDescription(localeInfo.WARP_RING_BIND_NAME(player_name), 26, self.CONDITION_COLOR)
					else:
						import net
						net.SendChatPacket("/request_warp_bind")

		appendedSpace = False
		if item.IsAntiFlag(item.ITEM_ANTIFLAG_GIVE):
			if not appendedSpace:
				appendedSpace = True
				self.AppendSpace(5)
			self.AppendTextLine(localeInfo.TOOLTIP_ITEM_NO_TRADE, self.NEGATIVE_COLOR)
		if item.IsAntiFlag(item.ITEM_ANTIFLAG_DESTROY):
			if not appendedSpace:
				appendedSpace = True
				self.AppendSpace(5)
			self.AppendTextLine(localeInfo.TOOLTIP_ITEM_NO_DESTROY, self.NEGATIVE_COLOR)

		if self.canShowSearchItemHotkey:
			self.AppendSpace(5)
			self.AppendTextLine(localeInfo.TOOLTIP_HOTKEY_SEARCH)
			self.AppendTextLine("|E%s|e + |E%s|e + |E%s|e" % ('ctrl', 'shift', 'mouse_right'))
			
		if __SERVER__ == 2 and constInfo.BRAVERY_CAPE_STORE and itemVnum == 93359:
			self.AppendSpace(5)
			self.AppendTextLine("Unstack capes")
			self.AppendTextLine("|E%s|e + |E%s|e" % ('shift', 'mouse_left'))

		self.ShowToolTip()

	def __DragonSoulInfoString (self, dwVnum):
		step = (dwVnum / 100) % 10
		refine = (dwVnum / 10) % 10
		# tchat(str(localeInfo.DRAGON_SOUL_STRENGTH))
		# tchat(localeInfo.DRAGON_SOUL_STRENGTH(4))
		if type(localeInfo.DRAGON_SOUL_STRENGTH) == str:
			if 0 == step:
				return localeInfo.DRAGON_SOUL_STEP_LEVEL1 + " " + (localeInfo.DRAGON_SOUL_STRENGTH % refine)
			elif 1 == step:
				return localeInfo.DRAGON_SOUL_STEP_LEVEL2 + " " + (localeInfo.DRAGON_SOUL_STRENGTH % refine)
			elif 2 == step:
				return localeInfo.DRAGON_SOUL_STEP_LEVEL3 + " " + (localeInfo.DRAGON_SOUL_STRENGTH % refine)
			elif 3 == step:
				return localeInfo.DRAGON_SOUL_STEP_LEVEL4 + " " + (localeInfo.DRAGON_SOUL_STRENGTH % refine)
			elif 4 == step:
				return localeInfo.DRAGON_SOUL_STEP_LEVEL5 + " " + (localeInfo.DRAGON_SOUL_STRENGTH % refine)
			else:
				return ""
		else:
			if 0 == step:
				return localeInfo.DRAGON_SOUL_STEP_LEVEL1 + " " + localeInfo.DRAGON_SOUL_STRENGTH(refine)
			elif 1 == step:
				return localeInfo.DRAGON_SOUL_STEP_LEVEL2 + " " + localeInfo.DRAGON_SOUL_STRENGTH(refine)
			elif 2 == step:
				return localeInfo.DRAGON_SOUL_STEP_LEVEL3 + " " + localeInfo.DRAGON_SOUL_STRENGTH(refine)
			elif 3 == step:
				return localeInfo.DRAGON_SOUL_STEP_LEVEL4 + " " + localeInfo.DRAGON_SOUL_STRENGTH(refine)
			elif 4 == step:
				return localeInfo.DRAGON_SOUL_STEP_LEVEL5 + " " + localeInfo.DRAGON_SOUL_STRENGTH(refine)
			else:
				return ""

	## ����ΰ�?
	def __IsHair(self, itemVnum):
		return (self.__IsOldHair(itemVnum) or 
			self.__IsNewHair(itemVnum) or
			self.__IsNewHair2(itemVnum))	

	def __IsOldHair(self, itemVnum):
		return itemVnum > 73000 and itemVnum < 74000	

	def __IsNewHair(self, itemVnum):
		return itemVnum > 74000 and itemVnum < 75000	

	def __IsNewHair2(self, itemVnum):
		return itemVnum > 75000 and itemVnum < 77000	

	def __AppendHairIcon(self, itemVnum):
		itemImage = ui.ImageBox()
		itemImage.SetParent(self)
		itemImage.Show()			

		if self.__IsOldHair(itemVnum):
			itemImage.LoadImage("d:/ymir work/item/quest/"+str(itemVnum)+".tga")
		elif self.__IsNewHair(itemVnum): # ���� ��� ��ȣ�� ������Ѽ� ����Ѵ�. ���ο� �������� 1000��ŭ ��ȣ�� �þ���.
			itemImage.LoadImage("d:/ymir work/item/quest/"+str(itemVnum-1000)+".tga")
		elif self.__IsNewHair2(itemVnum): # ���� ��� ��ȣ�� ������Ѽ� ����Ѵ�. ���ο� �������� 1000��ŭ ��ȣ�� �þ���.
			itemImage.LoadImage("icon/hair/%d.sub" % (itemVnum))

		itemImage.SetPosition(itemImage.GetWidth()/2, self.toolTipHeight)
		self.toolTipHeight += itemImage.GetHeight()
		#self.toolTipWidth += itemImage.GetWidth()/2
		self.childrenList.append(itemImage)
		self.ResizeToolTip()

	## ����� ū Description �� ��� ���� ����� �����Ѵ�
	def __AdjustMaxWidth(self, attrSlot, desc):
		newToolTipWidth = self.toolTipWidth
		newToolTipWidth = max(self.__AdjustAttrMaxWidth(attrSlot), newToolTipWidth)
		newToolTipWidth = max(self.__AdjustDescMaxWidth(desc), newToolTipWidth)
		if newToolTipWidth > self.toolTipWidth:
			self.toolTipWidth = newToolTipWidth
			self.ResizeToolTip()

	def __AdjustAttrMaxWidth(self, attrSlot):
		if 0 == attrSlot:
			return self.toolTipWidth

		maxWidth = self.toolTipWidth
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			type = attrSlot[i][0]
			value = attrSlot[i][1]
			if self.ATTRIBUTE_NEED_WIDTH.has_key(type):
				if value > 0:
					maxWidth = max(self.ATTRIBUTE_NEED_WIDTH[type], maxWidth)

					# ATTR_CHANGE_TOOLTIP_WIDTH
					#self.toolTipWidth = max(self.ATTRIBUTE_NEED_WIDTH[type], self.toolTipWidth)
					#self.ResizeToolTip()
					# END_OF_ATTR_CHANGE_TOOLTIP_WIDTH

		return maxWidth

	def __AdjustDescMaxWidth(self, desc):
		if len(desc) < DESC_DEFAULT_MAX_COLS:
			return self.toolTipWidth
	
		return DESC_WESTERN_MAX_WIDTH

	def __SetSkillBookToolTip(self, skillIndex, bookName, skillGrade):
		skillName = skill.GetSkillName(skillIndex)

		if not skillName:
			return

		if localeInfo.IsVIETNAM():
			itemName = bookName + " " + skillName
		else:
			itemName = skillName + " " + bookName
		self.SetTitle(itemName)

	def __AppendPickInformation(self, curLevel, curEXP, maxEXP):
		self.AppendSpace(5)
		self.AppendTextLine(localeInfo.TOOLTIP_PICK_LEVEL % (curLevel), self.NORMAL_COLOR)
		self.AppendTextLine(localeInfo.TOOLTIP_PICK_EXP % (curEXP, maxEXP), self.NORMAL_COLOR)

		if curEXP == maxEXP:
			self.AppendSpace(5)
			self.AppendTextLine(localeInfo.TOOLTIP_PICK_UPGRADE1, self.NORMAL_COLOR)
			self.AppendTextLine(localeInfo.TOOLTIP_PICK_UPGRADE2, self.NORMAL_COLOR)
			self.AppendTextLine(localeInfo.TOOLTIP_PICK_UPGRADE3, self.NORMAL_COLOR)


	def __AppendRodInformation(self, curLevel, curEXP, maxEXP):
		self.AppendSpace(5)
		self.AppendTextLine(localeInfo.TOOLTIP_FISHINGROD_LEVEL % (curLevel), self.NORMAL_COLOR)
		self.AppendTextLine(localeInfo.TOOLTIP_FISHINGROD_EXP % (curEXP, maxEXP), self.NORMAL_COLOR)

		if curEXP == maxEXP:
			self.AppendSpace(5)
			self.AppendTextLine(localeInfo.TOOLTIP_FISHINGROD_UPGRADE1, self.NORMAL_COLOR)
			self.AppendTextLine(localeInfo.TOOLTIP_FISHINGROD_UPGRADE2, self.NORMAL_COLOR)
			self.AppendTextLine(localeInfo.TOOLTIP_FISHINGROD_UPGRADE3, self.NORMAL_COLOR)

	def __AppendLimitInformation(self):

		appendSpace = False

		for i in xrange(item.LIMIT_MAX_NUM):

			(limitType, limitValue) = item.GetLimit(i)

			if limitValue > 0:
				if False == appendSpace:
					self.AppendSpace(5)
					appendSpace = True

			else:
				continue

			if item.LIMIT_LEVEL == limitType:
				color = self.GetLimitTextLineColor(player.GetStatus(player.LEVEL), limitValue)
				self.AppendTextLine(localeInfo.TOOLTIP_ITEM_LIMIT_LEVEL % (limitValue), color)

			if constInfo.ENABLE_LEVEL_LIMIT_MAX:
				if limitType == item.LIMIT_LEVEL_MAX:
					color = self.DISABLE_COLOR if player.GetStatus(player.LEVEL) >= limitValue else self.ENABLE_COLOR
					self.AppendTextLine(localeInfo.TOOLTIP_ITEM_LIMIT_LEVEL_MAX % (limitValue), color)

			"""
			elif item.LIMIT_STR == limitType:
				color = self.GetLimitTextLineColor(player.GetStatus(player.ST), limitValue)
				self.AppendTextLine(localeInfo.TOOLTIP_ITEM_LIMIT_STR % (limitValue), color)
			elif item.LIMIT_DEX == limitType:
				color = self.GetLimitTextLineColor(player.GetStatus(player.DX), limitValue)
				self.AppendTextLine(localeInfo.TOOLTIP_ITEM_LIMIT_DEX % (limitValue), color)
			elif item.LIMIT_INT == limitType:
				color = self.GetLimitTextLineColor(player.GetStatus(player.IQ), limitValue)
				self.AppendTextLine(localeInfo.TOOLTIP_ITEM_LIMIT_INT % (limitValue), color)
			elif item.LIMIT_CON == limitType:
				color = self.GetLimitTextLineColor(player.GetStatus(player.HT), limitValue)
				self.AppendTextLine(localeInfo.TOOLTIP_ITEM_LIMIT_CON % (limitValue), color)
			"""

	def __GetAffectString(self, affectType, affectValue):
		return GET_AFFECT_STRING(affectType, affectValue)

	def __GetAffectRangeString(self, affectType, affectMinValue, affectMaxValue):
		if 0 == affectType:
			return None

		try:
			return self.AFFECT_RANGE_DICT[affectType] % (affectMinValue, affectMaxValue)
		except TypeError:
			return "UNKNOWN_VALUE[%s] %s - %s" % (affectType, affectMinValue, affectMaxValue)
		except KeyError:
			return "UNKNOWN_TYPE[%s] %s - %s" % (affectType, affectMinValue, affectMaxValue)

	def __AppendAffectInformation(self, appendSpace = False):
		isAppendSpace = False

		isMount = (item.GetItemType() == item.ITEM_TYPE_COSTUME and item.GetItemSubType() == item.COSTUME_TYPE_MOUNT)

		mountBuffBonus = 0
		if isMount:
			mountBuffBonus = item.GetApplyPoint(item.APPLY_MOUNT_BUFF_BONUS)

		for i in xrange(item.ITEM_APPLY_MAX_NUM):

			(affectType, affectValue) = item.GetAffect(i)

			if isMount:
				affectValue = affectValue + mountBuffBonus

			if affectType != item.APPLY_NONE and affectValue != 0:
				affectString = GET_AFFECT_STRING(affectType, affectValue)
				if affectString:
					if appendSpace and not isAppendSpace:
						isAppendSpace = True
						self.AppendSpace(5)

					color = self.GetChangeTextLineColor(affectValue)
					self.AppendTextLine(affectString, color)

	def __AppendLimitTimeLeft(self, metinSlot):
		if metinSlot != 0:
			for i in xrange(item.LIMIT_MAX_NUM):

				(limitType, limitValue) = item.GetLimit(i)

				if limitType == item.LIMIT_REAL_TIME or limitType == item.LIMIT_REAL_TIME_START_FIRST_USE:
					if metinSlot != 0 and metinSlot[0] != 0 and metinSlot[0] != limitValue:
						timeEnd = metinSlot[0]
					else:
						timeEnd = app.GetGlobalTimeStamp() + limitValue

					self.AppendMallItemLastTime(timeEnd)
					return True

		return False

	def __AppendQuiverItemInformation(self, metinSlot):
		if metinSlot == 0 or metinSlot[1] == 0:
			self.AppendTextLine(localeInfo.QUIVER_NO_ARROWS)
		else:
			itemVnum = item.GetItemVnum()
			item.SelectItem(1, 2, metinSlot[0])
			self.AppendTextLine(localeInfo.QUIVER_ARROW_TYPE % item.GetItemName())
			item.SelectItem(1, 2, itemVnum)

			self.AppendTextLine(localeInfo.QUIVER_ARROW_COUNT % (localeInfo.NumberToString(metinSlot[1]), localeInfo.NumberToString(item.GetValue(0))))

	def __AppendAffectInformationAcce(self, drainInPercent, itemInDrainVnum):
		for i in xrange(item.ITEM_APPLY_MAX_NUM):
			item.SelectItem(1, 2, itemInDrainVnum)
			(affectType, affectValue) = item.GetAffect(i)
			
			if affectValue < 1:
				affectValue = 1
			
			affectValue = self.drainedPercent(affectValue, drainInPercent)

			affectString = self.__GetAffectString(affectType, affectValue)
			if affectString:
				self.AppendTextLine(affectString, self.GetChangeTextLineColor(affectValue))

	def AppendWearableInformation(self):

		self.AppendSpace(5)
		self.AppendTextLine(localeInfo.TOOLTIP_ITEM_WEARABLE_JOB, self.NORMAL_COLOR)

		flagList = (
			not item.IsAntiFlag(item.ITEM_ANTIFLAG_WARRIOR),
			not item.IsAntiFlag(item.ITEM_ANTIFLAG_ASSASSIN),
			not item.IsAntiFlag(item.ITEM_ANTIFLAG_SURA),
			not item.IsAntiFlag(item.ITEM_ANTIFLAG_SHAMAN),
			# not item.IsAntiFlag(item.ITEM_ANTIFLAG_WOLFMAN)
			)

		characterNames = ""
		for i in xrange(self.CHARACTER_COUNT):

			name = self.CHARACTER_NAMES[i]
			flag = flagList[i]

			if flag:
				characterNames += " "
				characterNames += name

		textLine = self.AppendTextLine(characterNames, self.NORMAL_COLOR, True)
		textLine.SetFeather()

		if item.IsAntiFlag(item.ITEM_ANTIFLAG_MALE):
			textLine = self.AppendTextLine(localeInfo.FOR_FEMALE, self.NORMAL_COLOR, True)
			textLine.SetFeather()

		if item.IsAntiFlag(item.ITEM_ANTIFLAG_FEMALE):
			textLine = self.AppendTextLine(localeInfo.FOR_MALE, self.NORMAL_COLOR, True)
			textLine.SetFeather()

	def __AppendPotionInformation(self):
		self.AppendSpace(5)

		healHP = item.GetValue(0)
		healSP = item.GetValue(1)
		healStatus = item.GetValue(2)
		healPercentageHP = item.GetValue(3)
		healPercentageSP = item.GetValue(4)

		if healHP > 0:
			self.AppendTextLine(localeInfo.TOOLTIP_POTION_PLUS_HP_POINT % healHP, self.GetChangeTextLineColor(healHP))
		if healSP > 0:
			self.AppendTextLine(localeInfo.TOOLTIP_POTION_PLUS_SP_POINT % healSP, self.GetChangeTextLineColor(healSP))
		if healStatus != 0:
			self.AppendTextLine(localeInfo.TOOLTIP_POTION_CURE)
		if healPercentageHP > 0:
			self.AppendTextLine(localeInfo.TOOLTIP_POTION_PLUS_HP_PERCENT % healPercentageHP, self.GetChangeTextLineColor(healPercentageHP))
		if healPercentageSP > 0:
			self.AppendTextLine(localeInfo.TOOLTIP_POTION_PLUS_SP_PERCENT % healPercentageSP, self.GetChangeTextLineColor(healPercentageSP))

	def __AppendAbilityPotionInformation(self):

		self.AppendSpace(5)

		abilityType = item.GetValue(0)
		time = item.GetValue(1)
		point = item.GetValue(2)

		if abilityType == item.APPLY_ATT_SPEED:
			self.AppendTextLine(localeInfo.TOOLTIP_POTION_PLUS_ATTACK_SPEED % point, self.GetChangeTextLineColor(point))
		elif abilityType == item.APPLY_MOV_SPEED:
			self.AppendTextLine(localeInfo.TOOLTIP_POTION_PLUS_MOVING_SPEED % point, self.GetChangeTextLineColor(point))

		if time > 0:
			minute = (time / 60)
			second = (time % 60)
			timeString = localeInfo.TOOLTIP_POTION_TIME

			if minute > 0:
				timeString += str(minute) + localeInfo.TOOLTIP_POTION_MIN
			if second > 0:
				timeString += " " + str(second) + localeInfo.TOOLTIP_POTION_SEC

			self.AppendTextLine(timeString)

	def GetPriceColor(self, price):
		if price>=constInfo.HIGH_PRICE:
			return self.HIGH_PRICE_COLOR
		elif price>=constInfo.MIDDLE_PRICE:
			return self.MIDDLE_PRICE_COLOR
		else:
			return self.LOW_PRICE_COLOR

	def GetGayaPriceColor(self, price):
		if price>=constInfo.GAYA_HIGH_PRICE:
			return self.HIGH_PRICE_COLOR
		elif price>=constInfo.GAYA_MIDDLE_PRICE:
			return self.MIDDLE_PRICE_COLOR
		else:
			return self.LOW_PRICE_COLOR
						
	def AppendPrice(self, price):	
		self.AppendSpace(5)
		self.AppendTextLine(localeInfo.TOOLTIP_BUYPRICE  % (localeInfo.NumberToMoneyString(price)), self.GetPriceColor(price))

	def AppendItemPrice(self, vnum, count):
		item.SelectItem(1, 2, vnum)

		self.AppendSpace(5)

		baseText = localeInfo.TOOLTIP_BUYPRICE
		textSplitPos = baseText.find("%s")
		textFront = baseText[:textSplitPos]
		textEnd = baseText[textSplitPos:] % (localeInfo.NumberToString(count) + "x " + item.GetItemName())
		textSplitPos = textEnd.find("x")
		textFront += textEnd[:textSplitPos+2]
		textEnd = textEnd[textSplitPos+1:]

		if item.GetIconImageFileName() == "Noname":
			fullText = "<TEXT outline=1 color=\"" + str(self.GetPriceColor(count)) + "\" text=\"" + textFront + "\">" + \
					   "<TEXT outline=1 color=\"" + str(self.GetPriceColor(count)) + "\" text=\"" + textEnd[1:] + "\">"
		else:
			fullText = "<TEXT outline=1 color=\"" + str(self.GetPriceColor(count)) + "\" text=\"" + textFront + "\">" + \
					   "<IMAGE path=\"" + item.GetIconImageFileName() + "\">" + \
					   "<TEXT outline=1 color=\"" + str(self.GetPriceColor(count)) + "\" text=\"" + textEnd + "\">"

		textLine = ui.ExtendedTextLine()
		textLine.SetParent(self)
		textLine.SetText(fullText)
		textLine.Show()

		textLine.SetPosition(0, self.toolTipHeight)
		textLine.SetWindowHorizontalAlignCenter()

		self.childrenList.append(textLine)

		self.toolTipHeight += max(self.TEXT_LINE_HEIGHT, textLine.GetHeight() + 3)
		self.ResizeToolTip()

		return textLine

	def AppendGayaPrice(self, price):
		self.AppendSpace(5)
		self.AppendTextLine(localeInfo.TOOLTIP_BUYPRICE % (localeInfo.NumberToGayaString(price)), self.GetGayaPriceColor(price))

	def AppendSellingPrice(self, price):
		if item.IsAntiFlag(item.ITEM_ANTIFLAG_SELL):			
			self.AppendTextLine(localeInfo.TOOLTIP_ANTI_SELL, self.DISABLE_COLOR)
			self.AppendSpace(5)
		else:
			self.AppendTextLine(localeInfo.TOOLTIP_SELLPRICE % (localeInfo.NumberToMoneyString(price)), self.GetPriceColor(price))
			self.AppendSpace(5)

	def AppendMetinInformation(self):
		affectType, affectValue = item.GetAffect(0)

		affectString = self.__GetAffectString(affectType, affectValue)

		if affectString:
			self.AppendSpace(5)
			color = self.GetChangeTextLineColor(affectValue)
			self.AppendTextLine(affectString, color)

	def AppendMetinWearInformation(self):

		self.AppendSpace(5)
		self.AppendTextLine(localeInfo.TOOLTIP_SOCKET_REFINABLE_ITEM, self.NORMAL_COLOR)

		flagList = (item.IsWearableFlag(item.WEARABLE_BODY),
					item.IsWearableFlag(item.WEARABLE_HEAD),
					item.IsWearableFlag(item.WEARABLE_FOOTS),
					item.IsWearableFlag(item.WEARABLE_WRIST),
					item.IsWearableFlag(item.WEARABLE_WEAPON),
					item.IsWearableFlag(item.WEARABLE_NECK),
					item.IsWearableFlag(item.WEARABLE_EAR),
					item.IsWearableFlag(item.WEARABLE_UNIQUE),
					item.IsWearableFlag(item.WEARABLE_SHIELD),
					item.IsWearableFlag(item.WEARABLE_ARROW))

		wearNames = ""
		for i in xrange(self.WEAR_COUNT):

			name = self.WEAR_NAMES[i]
			flag = flagList[i]

			if flag:
				wearNames += "  "
				wearNames += name

		textLine = ui.TextLine()
		textLine.SetParent(self)
		textLine.SetFontName(self.defFontName)
		textLine.SetPosition(self.toolTipWidth/2, self.toolTipHeight)
		textLine.SetHorizontalAlignCenter()
		textLine.SetPackedFontColor(self.NORMAL_COLOR)
		textLine.SetText(wearNames)
		textLine.Show()
		self.childrenList.append(textLine)

		self.toolTipHeight += self.TEXT_LINE_HEIGHT
		self.ResizeToolTip()

	#USE_PUT_INTO_ACCESSORY_SOCKET
	#USE_PUT_INTO_ACCESSORY_SOCKET_PERMA

	def GetMetinSocketType(self, number):
		if player.METIN_SOCKET_TYPE_NONE == number:
			return player.METIN_SOCKET_TYPE_NONE
		elif player.METIN_SOCKET_TYPE_SILVER == number:
			return player.METIN_SOCKET_TYPE_SILVER
		elif player.METIN_SOCKET_TYPE_GOLD == number:
			return player.METIN_SOCKET_TYPE_GOLD
		else:
			item.SelectItem(1, 2, number)
			if item.METIN_NORMAL == item.GetItemSubType():
				return player.METIN_SOCKET_TYPE_SILVER
			elif item.METIN_GOLD == item.GetItemSubType():
				return player.METIN_SOCKET_TYPE_GOLD
			elif "USE_PUT_INTO_ACCESSORY_SOCKET" == item.GetUseType(number):
				return player.METIN_SOCKET_TYPE_SILVER
			elif "USE_PUT_INTO_ACCESSORY_SOCKET_PERMA" == item.GetUseType(number):
				return player.METIN_SOCKET_TYPE_SILVER

		return player.METIN_SOCKET_TYPE_NONE

	def GetMetinItemIndex(self, number):
		if player.METIN_SOCKET_TYPE_SILVER == number:
			return 0
		if player.METIN_SOCKET_TYPE_GOLD == number:
			return 0

		return number

	def __AppendAccessoryMetinSlotInfo(self, metinSlot, mtrlVnum):		
		
		normalVnum 	= mtrlVnum[ 0 ]
		permaVnum 	= mtrlVnum[ 1 ]

		#tchat( "(testserver) ores for this item: normal => %d and perma => %d" % ( normalVnum, permaVnum ) )

		ACCESSORY_SOCKET_MAX_SIZE = 3

		permaOres 	= ( metinSlot[ 0 ] >> 8 ) & 0xff
		normalOres  = ( metinSlot[ 0 ] & 0xff )
		jewType = metinSlot[0] >> 16
		
		itemType = item.GetItemType()
		
		specialVnum = constInfo.GET_ACCESSORY_MATERIAL_VNUM_BY_TYPE(item.GetItemVnum(), jewType, item.GetItemType())

		if jewType > 0 and specialVnum[0]:
			(normalVnum, permaVnum) = specialVnum

		totalOres = normalOres + permaOres

		currentAmount 	= min( totalOres, ACCESSORY_SOCKET_MAX_SIZE )
		maxAmount 		= min( metinSlot[ 1 ], ACCESSORY_SOCKET_MAX_SIZE )

		# AFFECT TABLE
		affectType1, affectValue1 = item.GetAffect( 0 )
		affectList1 = [ 0, max( 1, affectValue1 * 10 / 100 ), max( 2, affectValue1 * 20 / 100 ), max( 3, affectValue1 * 40 / 100 ) ]

		affectType2, affectValue2 = item.GetAffect( 1 )
		affectList2 = [ 0, max( 1, affectValue2 * 10 / 100), max( 2, affectValue2 * 20 / 100 ), max( 3, affectValue2 * 40 / 100 ) ]

		affectType3, affectValue3 = item.GetAffect( 2 )
		affectList3 = [ 0, max( 1, affectValue3 * 10 / 100), max( 2, affectValue3 * 20 / 100 ), max( 3, affectValue3 * 40 / 100 ) ]

		oresTable = ( [ permaVnum ] * permaOres ) + ( [ normalVnum ] * normalOres ) + ( [ player.METIN_SOCKET_TYPE_SILVER ] * ( maxAmount - currentAmount ) )

		if len( oresTable ) > ACCESSORY_SOCKET_MAX_SIZE:
			return
		
		currentPermaNum = 0
		for i in range( maxAmount ):

			currentOre = oresTable[ i ]

			item.SelectItem(1, 2, currentOre )

			#tchat( str( item.GetItemSubType( ) ) )

			# Get affect strings
			affectString1 = self.__GetAffectString( affectType1, affectList1[ i + 1 ] - affectList1[ i ] )	
			affectString2 = self.__GetAffectString( affectType2, affectList2[ i + 1 ] - affectList2[ i ] )
			affectString3 = self.__GetAffectString( affectType3, affectList3[ i + 1 ] - affectList3[ i ] )
			specialAffectString = None
			if jewType != 0 and specialVnum[0] and (itemType != item.ITEM_TYPE_BELT or currentOre == permaVnum):
				if itemType == item.ITEM_TYPE_BELT:
					affectTypeSpec, affectValueSpec = item.GetAffect( currentPermaNum )
					specialAffectString = self.__GetAffectString( affectTypeSpec, affectValueSpec )	
					currentPermaNum += 1
				else:
					affectType1, affectValue1 = item.GetAffect( 0 )
					affectString1 = self.__GetAffectString( affectType1, affectValue1 )	
					affectString2 = None
					affectString3 = None

			leftTime = 0

			# Permanent
			if currentOre == permaVnum:
				leftTime = -1

			# Show remaining time if it's the last ore
			elif currentOre == normalVnum and ( i == totalOres - 1 ):
				leftTime = metinSlot[ 2 ]

			# Append socket data
			self.__AppendMetinSlotInfo_AppendMetinSocketData( i, currentOre, affectString1, affectString2, leftTime, affectString3, specialAffectString )

	def __AppendMetinSlotInfo(self, metinSlot):
		if self.__AppendMetinSlotInfo_IsEmptySlotList(metinSlot):
			return

		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			self.__AppendMetinSlotInfo_AppendMetinSocketData(i, metinSlot[i], "", "", 0)

	def __AppendMetinSlotInfo_IsEmptySlotList(self, metinSlot):
		if 0 == metinSlot:
			return 1

		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlotData=metinSlot[i]
			if 0 != self.GetMetinSocketType(metinSlotData):
				if 0 != self.GetMetinItemIndex(metinSlotData):
					return 0

		return 1

	def __AppendMetinSlotInfo_AppendMetinSocketData(self, index, metinSlotData, custumAffectString="", custumAffectString2="", leftTime=0, customAffectString3="", specialAffectString = None):

		slotType = self.GetMetinSocketType(metinSlotData)
		itemIndex = self.GetMetinItemIndex(metinSlotData)

		if 0 == slotType:
			return

		self.AppendSpace(5)

		slotImage = ui.ImageBox()
		slotImage.SetParent(self)
		slotImage.SetPosition(9, self.toolTipHeight-1)
		slotImage.Show()

		## Name
		nameTextLine = ui.TextLine()
		nameTextLine.SetParent(self)
		nameTextLine.SetFontName(self.defFontName)
		nameTextLine.SetPackedFontColor(self.NORMAL_COLOR)
		nameTextLine.SetPosition(50, self.toolTipHeight + 2)
		nameTextLine.SetOutline()
		nameTextLine.SetFeather()
		nameTextLine.Show()			

		self.childrenList.append(nameTextLine)

		if player.METIN_SOCKET_TYPE_SILVER == slotType:
			slotImage.LoadImage("d:/ymir work/ui/game/windows/metin_slot_silver.sub")
		elif player.METIN_SOCKET_TYPE_GOLD == slotType:
			slotImage.LoadImage("d:/ymir work/ui/game/windows/metin_slot_gold.sub")

		self.childrenList.append(slotImage)

		metinImage = ui.ImageBox()
		metinImage.SetParent(self)
		metinImage.SetPosition(10, self.toolTipHeight)
		metinImage.Show()
		self.childrenList.append(metinImage)

		if itemIndex:

			item.SelectItem(1, 2, itemIndex)

			## Image
			try:
				metinImage.LoadImage(item.GetIconImageFileName())
			except:
				dbg.TraceError("ItemToolTip.__AppendMetinSocketData() - Failed to find image file %d:%s" % 
					(itemIndex, item.GetIconImageFileName())
				)

			nameTextLine.SetText(item.GetItemName())
			
			## Affect		
			affectTextLine = ui.TextLine()
			affectTextLine.SetParent(self)
			affectTextLine.SetFontName(self.defFontName)
			affectTextLine.SetPackedFontColor(self.POSITIVE_COLOR)
			affectTextLine.SetPosition(50, self.toolTipHeight + 16 + 2)
			affectTextLine.SetOutline()
			affectTextLine.SetFeather()
			affectTextLine.Show()			
							
			if custumAffectString:
				affectTextLine.SetText(custumAffectString)
			elif itemIndex!=constInfo.ERROR_METIN_STONE:
				affectType, affectValue = item.GetAffect(0)
				realAffectValue = affectValue
				affectString = self.__GetAffectString(affectType, realAffectValue)
				if affectString:
					if affectValue != realAffectValue:
						affectTextLine.SetPackedFontColor(self.SOCKET_CHANGED_COLOR)
					affectTextLine.SetText(affectString)
			else:
				affectTextLine.SetText(localeInfo.TOOLTIP_APPLY_NOAFFECT)
			
			self.childrenList.append(affectTextLine)			

			if custumAffectString2:
				affectTextLine = ui.TextLine()
				affectTextLine.SetParent(self)
				affectTextLine.SetFontName(self.defFontName)
				affectTextLine.SetPackedFontColor(self.POSITIVE_COLOR)
				affectTextLine.SetPosition(50, self.toolTipHeight + 16 + 2 + 16 + 2)
				affectTextLine.SetOutline()
				affectTextLine.SetFeather()
				affectTextLine.Show()
				affectTextLine.SetText(custumAffectString2)
				self.childrenList.append(affectTextLine)
				self.toolTipHeight += 16 + 2

			if customAffectString3:
				affectTextLine = ui.TextLine()
				affectTextLine.SetParent(self)
				affectTextLine.SetFontName(self.defFontName)
				affectTextLine.SetPackedFontColor(self.POSITIVE_COLOR)
				affectTextLine.SetPosition(50, self.toolTipHeight + 16 + 2 + 16 + 2)
				affectTextLine.SetOutline()
				affectTextLine.SetFeather()
				affectTextLine.Show()
				affectTextLine.SetText(customAffectString3)
				self.childrenList.append(affectTextLine)
				self.toolTipHeight += 16 + 2
				
			if specialAffectString:
				affectTextLine = ui.TextLine()
				affectTextLine.SetParent(self)
				affectTextLine.SetFontName(self.defFontName)
				affectTextLine.SetPackedFontColor(self.POSITIVE_COLOR)
				affectTextLine.SetPosition(50, self.toolTipHeight + 16 + 2 + 16 + 2)
				affectTextLine.SetOutline()
				affectTextLine.SetFeather()
				affectTextLine.Show()
				affectTextLine.SetText(specialAffectString)
				self.childrenList.append(affectTextLine)
				self.toolTipHeight += 16 + 2

			if 0 != leftTime or leftTime == -1:

				timeText = ""
			
				if leftTime == -1:
					timeText = localeInfo.PERMANENT
				else:
					timeText = (localeInfo.LEFT_TIME + " : " + localeInfo.SecondToDHM(leftTime))

				timeTextLine = ui.TextLine()
				timeTextLine.SetParent(self)
				timeTextLine.SetFontName(self.defFontName)
				timeTextLine.SetPackedFontColor(self.POSITIVE_COLOR)
				timeTextLine.SetPosition(50, self.toolTipHeight + 16 + 2 + 16 + 2)
				timeTextLine.SetOutline()
				timeTextLine.SetFeather()
				timeTextLine.Show()
				timeTextLine.SetText(timeText)
				self.childrenList.append(timeTextLine)
				self.toolTipHeight += 16 + 2

		else:
				nameTextLine.SetText(localeInfo.TOOLTIP_SOCKET_EMPTY)

		self.toolTipHeight += 35
		self.ResizeToolTip()

	def __AppendFishInfo(self, size):
		if size > 0:
			self.AppendSpace(5)
			self.AppendTextLine(localeInfo.TOOLTIP_FISH_LEN % (float(size) / 100.0), self.NORMAL_COLOR)

	def AppendUniqueItemLastTime(self, restMin):
		restSecond = restMin*60
		self.AppendSpace(5)
		self.AppendTextLine(localeInfo.LEFT_TIME + " : " + localeInfo.SecondToHM(restSecond), self.NORMAL_COLOR)

	def AppendItemLastTime(self, restSecond):
		self.AppendSpace(5)
		self.AppendTextLine(localeInfo.LEFT_TIME + " : " + localeInfo.SecondToHM(restSecond), self.NORMAL_COLOR)

	def AppendMallItemLastTime(self, endTime):
		leftSec = max(0, endTime - app.GetGlobalTimeStamp())
		self.AppendSpace(5)
		self.AppendTextLine(localeInfo.LEFT_TIME + " : " + localeInfo.SecondToDHM(leftSec), self.NORMAL_COLOR)

class HyperlinkItemToolTip(ItemToolTip):
	def __init__(self):
		ItemToolTip.__init__(self, isPickable=True)

	def SetHyperlinkItem(self, tokens):
		#tchat("SetHyperlinkItem tokens %s" % str(tokens))
		minTokenCount = 3 + player.METIN_SOCKET_MAX_NUM
		maxTokenCount = minTokenCount + 2 * player.ATTRIBUTE_SLOT_MAX_NUM
		if tokens and len(tokens) >= minTokenCount and len(tokens) <= maxTokenCount:
			head, vnum, flag = tokens[:3]
			itemVnum = int(vnum, 16)
			metinSlot = [int(metin, 16) for metin in tokens[3:minTokenCount]]

			rests = tokens[minTokenCount:]
			if rests:
				attrSlot = []

				rests.reverse()
				while rests:
					key = int(rests.pop(), 16)
					if rests:
						val = int(rests.pop())
						attrSlot.append((key, val))
					else:
						attrSlot.append((0, 0))

				attrSlot += [(0, 0)] * (player.ATTRIBUTE_SLOT_MAX_NUM - len(attrSlot))
			else:
				attrSlot = [(0, 0)] * player.ATTRIBUTE_SLOT_MAX_NUM

			self.ClearToolTip()
			self.AddItemData(itemVnum, metinSlot, attrSlot)

			ItemToolTip.OnUpdate(self)

	def OnUpdate(self):
		pass

	def OnMouseLeftButtonDown(self):
		self.Hide()

class SkillToolTip(ToolTip):

	POINT_NAME_DICT = {
		player.LEVEL : localeInfo.SKILL_TOOLTIP_LEVEL,
		player.IQ : localeInfo.SKILL_TOOLTIP_INT,
	}

	SKILL_TOOL_TIP_WIDTH = 200
	PARTY_SKILL_TOOL_TIP_WIDTH = 340

	PARTY_SKILL_EXPERIENCE_AFFECT_LIST = (	( 2, 2,  10,),
											( 8, 3,  20,),
											(14, 4,  30,),
											(22, 5,  45,),
											(28, 6,  60,),
											(34, 7,  80,),
											(38, 8, 100,), )

	PARTY_SKILL_PLUS_GRADE_AFFECT_LIST = (	( 4, 2, 1, 0,),
											(10, 3, 2, 0,),
											(16, 4, 2, 1,),
											(24, 5, 2, 2,), )

	PARTY_SKILL_ATTACKER_AFFECT_LIST = (	( 36, 3, ),
											( 26, 1, ),
											( 32, 2, ), )

	SKILL_GRADE_NAME = {	player.SKILL_GRADE_MASTER : localeInfo.SKILL_GRADE_NAME_MASTER,
							player.SKILL_GRADE_GRAND_MASTER : localeInfo.SKILL_GRADE_NAME_GRAND_MASTER,
							player.SKILL_GRADE_PERFECT_MASTER : localeInfo.SKILL_GRADE_NAME_PERFECT_MASTER,
							player.SKILL_GRADE_LEGENDARY_MASTER : localeInfo.SKILL_GRADE_NAME_LEGENDARY_MASTER, }

	AFFECT_NAME_DICT =	{
							"HP" : localeInfo.TOOLTIP_SKILL_AFFECT_ATT_POWER,
							"ATT_GRADE" : localeInfo.TOOLTIP_SKILL_AFFECT_ATT_GRADE,
							"DEF_GRADE" : localeInfo.TOOLTIP_SKILL_AFFECT_DEF_GRADE,
							"ATT_SPEED" : localeInfo.TOOLTIP_SKILL_AFFECT_ATT_SPEED,
							"MOV_SPEED" : localeInfo.TOOLTIP_SKILL_AFFECT_MOV_SPEED,
							"DODGE" : localeInfo.TOOLTIP_SKILL_AFFECT_DODGE,
							"RESIST_NORMAL" : localeInfo.TOOLTIP_SKILL_AFFECT_RESIST_NORMAL,
							"REFLECT_MELEE" : localeInfo.TOOLTIP_SKILL_AFFECT_REFLECT_MELEE,
						}
	AFFECT_APPEND_TEXT_DICT =	{
									"DODGE" : "%",
									"RESIST_NORMAL" : "%",
									"REFLECT_MELEE" : "%",
								}

	def __init__(self):
		ToolTip.__init__(self, self.SKILL_TOOL_TIP_WIDTH)
	def __del__(self):
		ToolTip.__del__(self)

	def SetSkill(self, skillIndex, skillLevel = -1):

		if 0 == skillIndex:
			return

		if skill.SKILL_TYPE_GUILD == skill.GetSkillType(skillIndex):

			if self.SKILL_TOOL_TIP_WIDTH != self.toolTipWidth:
				self.toolTipWidth = self.SKILL_TOOL_TIP_WIDTH
				self.ResizeToolTip()

			self.AppendDefaultData(skillIndex)
			self.AppendSkillConditionData(skillIndex)
			self.AppendGuildSkillData(skillIndex, skillLevel)

		else:

			if self.SKILL_TOOL_TIP_WIDTH != self.toolTipWidth:
				self.toolTipWidth = self.SKILL_TOOL_TIP_WIDTH
				self.ResizeToolTip()

			slotIndex = player.GetSkillSlotIndex(skillIndex)
			skillGrade = player.GetSkillGrade(slotIndex)
			skillLevel = player.GetSkillLevel(slotIndex)
			skillCurrentPercentage = player.GetSkillCurrentEfficientPercentage(slotIndex)
			skillNextPercentage = player.GetSkillNextEfficientPercentage(slotIndex)

			self.AppendDefaultData(skillIndex)
			self.AppendSkillConditionData(skillIndex)
			self.AppendSkillDataNew(slotIndex, skillIndex, skillGrade, skillLevel, skillCurrentPercentage, skillNextPercentage)
			self.AppendSkillRequirement(skillIndex, skillLevel)

		self.ShowToolTip()

	def __GetRealSkillLevel(self, skillLevel, skillGrade):
		realSkillLevel = skillLevel
		if 1 == skillGrade:
			realSkillLevel += 19
		elif 2 == skillGrade:
			realSkillLevel += 29
		elif 3 == skillGrade:
			realSkillLevel = 40
		return realSkillLevel

	def SetSkillNew(self, slotIndex, skillIndex, skillGrade, skillLevel, efficienceByLevel = False):

		if 0 == skillIndex:
			return

		if player.SKILL_INDEX_TONGSOL == skillIndex:

			slotIndex = player.GetSkillSlotIndex(skillIndex)
			skillLevel = player.GetSkillLevel(slotIndex)

			self.AppendDefaultData(skillIndex)
			self.AppendPartySkillData(skillGrade, skillLevel)

		elif player.SKILL_INDEX_RIDING == skillIndex:

			slotIndex = player.GetSkillSlotIndex(skillIndex)
			self.AppendSupportSkillDefaultData(skillIndex, skillGrade, skillLevel, 3)

		elif player.SKILL_INDEX_SUMMON == skillIndex:

			maxLevel = 10

			self.ClearToolTip()
			self.__SetSkillTitle(skillIndex, skillGrade)

			## Description
			description = skill.GetSkillDescription(skillIndex)
			self.AppendDescription(description, 25)

			if skillLevel == 10:
				self.AppendSpace(5)
				self.AppendTextLine(localeInfo.TOOLTIP_SKILL_LEVEL_MASTER % (skillLevel), self.NORMAL_COLOR)
				self.AppendTextLine(localeInfo.SKILL_SUMMON_DESCRIPTION % (skillLevel*10), self.NORMAL_COLOR)

			else:
				self.AppendSpace(5)
				self.AppendTextLine(localeInfo.TOOLTIP_SKILL_LEVEL % (skillLevel), self.NORMAL_COLOR)
				self.__AppendSummonDescription(skillLevel, self.NORMAL_COLOR)

				self.AppendSpace(5)
				self.AppendTextLine(localeInfo.TOOLTIP_SKILL_LEVEL % (skillLevel+1), self.NEGATIVE_COLOR)
				self.__AppendSummonDescription(skillLevel+1, self.NEGATIVE_COLOR)

		elif skill.SKILL_TYPE_GUILD == skill.GetSkillType(skillIndex):

			if self.SKILL_TOOL_TIP_WIDTH != self.toolTipWidth:
				self.toolTipWidth = self.SKILL_TOOL_TIP_WIDTH
				self.ResizeToolTip()

			self.AppendDefaultData(skillIndex)
			self.AppendSkillConditionData(skillIndex)
			self.AppendGuildSkillData(skillIndex, skillLevel)

		else:

			if self.SKILL_TOOL_TIP_WIDTH != self.toolTipWidth:
				self.toolTipWidth = self.SKILL_TOOL_TIP_WIDTH
				self.ResizeToolTip()

			slotIndex = player.GetSkillSlotIndex(skillIndex)

			if efficienceByLevel:
				realSkillLevel = self.__GetRealSkillLevel(skillLevel, skillGrade)
				skillCurrentPercentage = player.GetSkillEfficientPercentage(realSkillLevel)
				if skillGrade != skill.SKILL_GRADE_COUNT:
					skillNextPercentage = player.GetSkillEfficientPercentage(realSkillLevel + 1)
				else:
					skillNextPercentage = skillCurrentPercentage
			else:
				skillCurrentPercentage = player.GetSkillCurrentEfficientPercentage(slotIndex)
				skillNextPercentage = player.GetSkillNextEfficientPercentage(slotIndex)

			self.AppendDefaultData(skillIndex, skillGrade)
			self.AppendSkillConditionData(skillIndex)
			self.AppendSkillDataNew(slotIndex, skillIndex, skillGrade, skillLevel, skillCurrentPercentage, skillNextPercentage)
			self.AppendSkillRequirement(skillIndex, skillLevel)

		self.ShowToolTip()

	def __SetSkillTitle(self, skillIndex, skillGrade):
		self.SetTitle(skill.GetSkillName(skillIndex, skillGrade))
		self.__AppendSkillGradeName(skillIndex, skillGrade)

	def __AppendSkillGradeName(self, skillIndex, skillGrade):		
		if self.SKILL_GRADE_NAME.has_key(skillGrade):
			self.AppendSpace(5)
			self.AppendTextLine(self.SKILL_GRADE_NAME[skillGrade] % (skill.GetSkillName(skillIndex, 0)), self.CAN_LEVEL_UP_COLOR)

	def SetSkillOnlyName(self, slotIndex, skillIndex, skillGrade):
		if 0 == skillIndex:
			return

		slotIndex = player.GetSkillSlotIndex(skillIndex)

		self.toolTipWidth = self.SKILL_TOOL_TIP_WIDTH
		self.ResizeToolTip()

		self.ClearToolTip()
		self.__SetSkillTitle(skillIndex, skillGrade)		
		self.AppendDefaultData(skillIndex, skillGrade)
		self.AppendSkillConditionData(skillIndex)		
		self.ShowToolTip()

	def AppendDefaultData(self, skillIndex, skillGrade = 0):
		self.ClearToolTip()
		self.__SetSkillTitle(skillIndex, skillGrade)

		## Level Limit
		levelLimit = skill.GetSkillLevelLimit(skillIndex)
		if levelLimit > 0:

			color = self.NORMAL_COLOR
			if player.GetStatus(player.LEVEL) < levelLimit:
				color = self.NEGATIVE_COLOR

			self.AppendSpace(5)
			self.AppendTextLine(localeInfo.TOOLTIP_ITEM_LIMIT_LEVEL % (levelLimit), color)

		## Description
		description = skill.GetSkillDescription(skillIndex)
		self.AppendDescription(description, 25)

	def AppendSupportSkillDefaultData(self, skillIndex, skillGrade, skillLevel, maxLevel):
		self.ClearToolTip()
		self.__SetSkillTitle(skillIndex, skillGrade)

		## Description
		description = skill.GetSkillDescription(skillIndex)
		self.AppendDescription(description, 25)

		if 1 == skillGrade:
			skillLevel += 19
		elif 2 == skillGrade:
			skillLevel += 29
		elif 3 == skillGrade:
			skillLevel = 40

		self.AppendSpace(5)
		self.AppendTextLine(localeInfo.TOOLTIP_SKILL_LEVEL_WITH_MAX % (skillLevel, maxLevel), self.NORMAL_COLOR)

	def AppendSkillConditionData(self, skillIndex):
		conditionDataCount = skill.GetSkillConditionDescriptionCount(skillIndex)
		if conditionDataCount > 0:
			self.AppendSpace(5)
			for i in xrange(conditionDataCount):
				self.AppendTextLine(skill.GetSkillConditionDescription(skillIndex, i), self.CONDITION_COLOR)

	def AppendGuildSkillData(self, skillIndex, skillLevel):
		skillMaxLevel = 7
		skillCurrentPercentage = float(skillLevel) / float(skillMaxLevel)
		skillNextPercentage = float(skillLevel+1) / float(skillMaxLevel)
		## Current Level
		if skillLevel > 0:
			if self.HasSkillLevelDescription(skillIndex, skillLevel):
				self.AppendSpace(5)
				if skillLevel == skillMaxLevel:
					self.AppendTextLine(localeInfo.TOOLTIP_SKILL_LEVEL_MASTER % (skillLevel), self.NORMAL_COLOR)
				else:
					self.AppendTextLine(localeInfo.TOOLTIP_SKILL_LEVEL % (skillLevel), self.NORMAL_COLOR)

				#####

				for i in xrange(skill.GetSkillAffectDescriptionCount(skillIndex)):
					self.AppendTextLine(skill.GetSkillAffectDescription(skillIndex, i, skillCurrentPercentage), self.ENABLE_COLOR)

				## Cooltime
				coolTime = skill.GetSkillCoolTime(skillIndex, skillCurrentPercentage)
				if coolTime > 0:
					self.AppendTextLine(localeInfo.TOOLTIP_SKILL_COOL_TIME + str(coolTime), self.ENABLE_COLOR)

				## SP
				needGSP = skill.GetSkillNeedSP(skillIndex, skillCurrentPercentage)
				if needGSP > 0:
					self.AppendTextLine(localeInfo.TOOLTIP_NEED_GSP % (needGSP), self.ENABLE_COLOR)

		## Next Level
		if skillLevel < skillMaxLevel:
			if self.HasSkillLevelDescription(skillIndex, skillLevel+1):
				self.AppendSpace(5)
				self.AppendTextLine(localeInfo.TOOLTIP_NEXT_SKILL_LEVEL_1 % (skillLevel+1, skillMaxLevel), self.DISABLE_COLOR)

				#####

				for i in xrange(skill.GetSkillAffectDescriptionCount(skillIndex)):
					self.AppendTextLine(skill.GetSkillAffectDescription(skillIndex, i, skillNextPercentage), self.DISABLE_COLOR)

				## Cooltime
				coolTime = skill.GetSkillCoolTime(skillIndex, skillNextPercentage)
				if coolTime > 0:
					self.AppendTextLine(localeInfo.TOOLTIP_SKILL_COOL_TIME + str(coolTime), self.DISABLE_COLOR)

				## SP
				needGSP = skill.GetSkillNeedSP(skillIndex, skillNextPercentage)
				if needGSP > 0:
					self.AppendTextLine(localeInfo.TOOLTIP_NEED_GSP % (needGSP), self.DISABLE_COLOR)

	def AppendSkillDataNew(self, slotIndex, skillIndex, skillGrade, skillLevel, skillCurrentPercentage, skillNextPercentage):

		if constInfo.ENABLE_LEGENDARY_SKILLS:
			self.skillMaxLevelStartDict = { 0 : 17, 1 : 7, 2 : 10, 3 : 10, 4 : 1 }
			self.skillMaxLevelEndDict = { 0 : 20, 1 : 10, 2 : 10, 3 : 10, 4 : 1 }
		else:
			self.skillMaxLevelStartDict = { 0 : 17, 1 : 7, 2 : 10, 3 : 1, }
			self.skillMaxLevelEndDict = { 0 : 20, 1 : 10, 2 : 10, 3 : 1, }

		skillLevelUpPoint = 1
		realSkillGrade = player.GetSkillGrade(slotIndex)
		skillMaxLevelStart = self.skillMaxLevelStartDict.get(realSkillGrade, 15)
		skillMaxLevelEnd = self.skillMaxLevelEndDict.get(realSkillGrade, 20)

		correctSkillLevel = 0
		if skillGrade == 0:
			correctSkillLevel = skillLevel
		else:
			correctSkillLevel = (skillGrade + 1) * 10 + skillLevel - 1

		## Current Level
		if skillLevel > 0:
			if self.HasSkillLevelDescription(skillIndex, skillLevel):
				self.AppendSpace(5)
				if skillGrade >= skill.SKILL_GRADE_COUNT:
					pass
				elif skillLevel == skillMaxLevelEnd:
					self.AppendTextLine(localeInfo.TOOLTIP_SKILL_LEVEL_MASTER % (skillLevel), self.NORMAL_COLOR)
				else:
					self.AppendTextLine(localeInfo.TOOLTIP_SKILL_LEVEL % (skillLevel), self.NORMAL_COLOR)
				
				
				self.AppendSkillLevelDescriptionNew(skillIndex, skillCurrentPercentage, correctSkillLevel, self.ENABLE_COLOR)

		## Next Level
		if skillGrade != skill.SKILL_GRADE_COUNT+1:
			if skillLevel < skillMaxLevelEnd:
				if self.HasSkillLevelDescription(skillIndex, skillLevel+skillLevelUpPoint):
					self.AppendSpace(5)
					## HP����, ����ȸ�� ������ų�� ���
					if skillIndex == 141 or skillIndex == 142:
						self.AppendTextLine(localeInfo.TOOLTIP_NEXT_SKILL_LEVEL_3 % (skillLevel+1), self.DISABLE_COLOR)
					else:
						self.AppendTextLine(localeInfo.TOOLTIP_NEXT_SKILL_LEVEL_1 % (skillLevel+1, skillMaxLevelEnd), self.DISABLE_COLOR)
					self.AppendSkillLevelDescriptionNew(skillIndex, skillNextPercentage, correctSkillLevel + 1, self.DISABLE_COLOR)

	def AppendSkillLevelDescriptionNew(self, skillIndex, skillPercentage, skillLevel, color):

		affectDataCount = skill.GetNewAffectDataCount(skillIndex)
		if affectDataCount > 0:
			for i in xrange(affectDataCount):
				type, minValue, maxValue = skill.GetNewAffectData(skillIndex, i, skillPercentage, skillLevel)

				if not self.AFFECT_NAME_DICT.has_key(type):
					continue

				minValue = int(minValue)
				maxValue = int(maxValue)
				affectText = self.AFFECT_NAME_DICT[type]

				if "HP" == type:
					if minValue < 0 and maxValue < 0:
						minValue *= -1
						maxValue *= -1

					else:
						affectText = localeInfo.TOOLTIP_SKILL_AFFECT_HEAL

				affectText += str(minValue)
				if minValue != maxValue:
					affectText += " - " + str(maxValue)
				affectText += self.AFFECT_APPEND_TEXT_DICT.get(type, "")

				self.AppendTextLine(affectText, color)
			
		else:
			for i in xrange(skill.GetSkillAffectDescriptionCount(skillIndex)):
				self.AppendTextLine(skill.GetSkillAffectDescription(skillIndex, i, skillPercentage, skillLevel), color)
		

		## Duration
		duration = skill.GetDuration(skillIndex, skillPercentage)
		if duration > 0:
			self.AppendTextLine(localeInfo.TOOLTIP_SKILL_DURATION % (duration), color)

		## Cooltime
		coolTime = skill.GetSkillCoolTime(skillIndex, skillPercentage)
		if coolTime > 0:
			self.AppendTextLine(localeInfo.TOOLTIP_SKILL_COOL_TIME + str(coolTime), color)

		## SP
		needSP = skill.GetSkillNeedSP(skillIndex, skillPercentage)
		if needSP != 0:
			continuationSP = skill.GetSkillContinuationSP(skillIndex, skillPercentage)

			if skill.IsUseHPSkill(skillIndex):
				self.AppendNeedHP(needSP, continuationSP, color)
			else:
				self.AppendNeedSP(needSP, continuationSP, color)

	def AppendSkillRequirement(self, skillIndex, skillLevel):

		skillMaxLevel = skill.GetSkillMaxLevel(skillIndex)

		if skillLevel >= skillMaxLevel:
			return

		isAppendHorizontalLine = False

		## Requirement
		if skill.IsSkillRequirement(skillIndex):

			if not isAppendHorizontalLine:
				isAppendHorizontalLine = True
				self.AppendHorizontalLine()

			requireSkillName, requireSkillLevel = skill.GetSkillRequirementData(skillIndex)

			color = self.CANNOT_LEVEL_UP_COLOR
			if skill.CheckRequirementSueccess(skillIndex):
				color = self.CAN_LEVEL_UP_COLOR
			self.AppendTextLine(localeInfo.TOOLTIP_REQUIREMENT_SKILL_LEVEL % (requireSkillName, requireSkillLevel), color)

		## Require Stat
		requireStatCount = skill.GetSkillRequireStatCount(skillIndex)
		if requireStatCount > 0:

			for i in xrange(requireStatCount):
				type, level = skill.GetSkillRequireStatData(skillIndex, i)
				if self.POINT_NAME_DICT.has_key(type):

					if not isAppendHorizontalLine:
						isAppendHorizontalLine = True
						self.AppendHorizontalLine()

					name = self.POINT_NAME_DICT[type]
					color = self.CANNOT_LEVEL_UP_COLOR
					if player.GetStatus(type) >= level:
						color = self.CAN_LEVEL_UP_COLOR
					self.AppendTextLine(localeInfo.TOOLTIP_REQUIREMENT_STAT_LEVEL % (name, level), color)

	def HasSkillLevelDescription(self, skillIndex, skillLevel):
		if skill.GetSkillAffectDescriptionCount(skillIndex) > 0:
			return True
		if skill.GetSkillCoolTime(skillIndex, skillLevel) > 0:
			return True
		if skill.GetSkillNeedSP(skillIndex, skillLevel) > 0:
			return True

		return False

	def AppendMasterAffectDescription(self, index, desc, color):
		self.AppendTextLine(desc, color)

	def AppendNextAffectDescription(self, index, desc):
		self.AppendTextLine(desc, self.DISABLE_COLOR)

	def AppendNeedHP(self, needSP, continuationSP, color):

		self.AppendTextLine(localeInfo.TOOLTIP_NEED_HP % (needSP), color)

		if continuationSP > 0:
			self.AppendTextLine(localeInfo.TOOLTIP_NEED_HP_PER_SEC % (continuationSP), color)

	def AppendNeedSP(self, needSP, continuationSP, color):

		if -1 == needSP:
			self.AppendTextLine(localeInfo.TOOLTIP_NEED_ALL_SP, color)

		else:
			self.AppendTextLine(localeInfo.TOOLTIP_NEED_SP % (needSP), color)

		if continuationSP > 0:
			self.AppendTextLine(localeInfo.TOOLTIP_NEED_SP_PER_SEC % (continuationSP), color)

	def AppendPartySkillData(self, skillGrade, skillLevel):

		if 1 == skillGrade:
			skillLevel += 19
		elif 2 == skillGrade:
			skillLevel += 29
		elif 3 == skillGrade:
			skillLevel =  40

		if skillLevel <= 0:
			return

		skillIndex = player.SKILL_INDEX_TONGSOL
		slotIndex = player.GetSkillSlotIndex(skillIndex)
		k = player.GetSkillCurrentEfficientPercentage(slotIndex)
		self.AppendSpace(5)
		self.AutoAppendTextLine(localeInfo.TOOLTIP_PARTY_SKILL_LEVEL % skillLevel, self.NORMAL_COLOR)

		tchat("k = " + str(k))
		if skillLevel>=10:
			self.AutoAppendTextLine(localeInfo.PARTY_SKILL_ATTACKER % chop( 10 + 88 * k ))

		if skillLevel>=20:
			self.AutoAppendTextLine(localeInfo.PARTY_SKILL_BERSERKER 	% chop(1 + 7.2 * k))
			self.AutoAppendTextLine(localeInfo.PARTY_SKILL_TANKER 	% chop(50 + 1960 * k))

		if skillLevel>=25:
			self.AutoAppendTextLine(localeInfo.PARTY_SKILL_BUFFER % chop(5 + 92 * k ))

		if skillLevel>=35:
			self.AutoAppendTextLine(localeInfo.PARTY_SKILL_SKILL_MASTER % chop(25 + 780 * k ))

		if skillLevel>=40:
			self.AutoAppendTextLine(localeInfo.PARTY_SKILL_DEFENDER % chop( 5 + 76 * k ))

		self.AlignHorizonalCenter()

	def __AppendSummonDescription(self, skillLevel, color):
		if skillLevel > 1:
			self.AppendTextLine(localeInfo.SKILL_SUMMON_DESCRIPTION % (skillLevel * 10), color)
		elif 1 == skillLevel:
			self.AppendTextLine(localeInfo.SKILL_SUMMON_DESCRIPTION % (15), color)
		elif 0 == skillLevel:
			self.AppendTextLine(localeInfo.SKILL_SUMMON_DESCRIPTION % (10), color)