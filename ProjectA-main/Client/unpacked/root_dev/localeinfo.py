import app
import constInfo
import chat

BLEND_POTION_NO_TIME = "BLEND_POTION_NO_TIME"
BLEND_POTION_NO_INFO = "BLEND_POTION_NO_INFO"

APP_TITLE = "Aeldra" if __SERVER__ == 1 else "Elonia"

GUILD_HEADQUARTER = "Main Building"
GUILD_FACILITY = "Facility"
GUILD_OBJECT = "Object"
GUILD_MEMBER_COUNT_INFINITY = "INFINITY"

LOGIN_FAILURE_WEB_BLOCK = "BLOCK_LOGIN(WEB)"
LOGIN_FAILURE_BLOCK_LOGIN = "BLOCK_LOGIN"
CHANNEL_NOTIFY_FULL = "CHANNEL_NOTIFY_FULL"

GUILD_BUILDING_LIST_TXT = app.GetLocaleBasePath() + "/GuildBuildingList.txt"
GUILD_BUILDING_NAME_LIST_TXT = app.GetLocalePath() + "/GuildBuildingName.txt"

GUILD_MARK_MIN_LEVEL = "3"
GUILD_MARK_NOT_ENOUGH_LEVEL = "±ćµĺ·ąş§ 3ŔĚ»ó şÎĹÍ °ˇ´ÉÇŐ´Ď´Ů."

ERROR_MARK_UPLOAD_NEED_RECONNECT = "UploadMark: Reconnect to game"
ERROR_MARK_CHECK_NEED_RECONNECT = "CheckMark: Reconnect to game"

VIRTUAL_KEY_ALPHABET_LOWERS  = r"[1234567890]/qwertyuiop\=asdfghjkl;`'zxcvbnm.,"
VIRTUAL_KEY_ALPHABET_UPPERS  = r'{1234567890}?QWERTYUIOP|+ASDFGHJKL:~"ZXCVBNM<>'
VIRTUAL_KEY_SYMBOLS    = '!@#$%^&*()_+|{}:"<>?~'
VIRTUAL_KEY_NUMBERS    = "1234567890-=\[];',./`"
VIRTUAL_KEY_SYMBOLS_BR    = '!@#$%^&*()_+|{}:"<>?~áŕăâéčęíěóňôőúůç'

__IS_ENGLISH	= app.LANG_ENGLISH == app.GetLanguage()
__IS_HONGKONG	= False
__IS_NEWCIBN	= False
__IS_EUROPE		= True
__IS_CANADA		= False
__IS_BRAZIL		= False
__IS_SINGAPORE	= False
__IS_VIETNAM	= False
__IS_ARABIC		= app.LANG_ARABIC == app.GetLanguage()
__IS_CIBN10		= False
__IS_WE_KOREA	= False
__IS_TAIWAN		= False
__IS_JAPAN		= False

if constInfo.ENABLE_CRYSTAL_SYSTEM:
	def GetCrystalClarityName(clarity_type):
		list = [
			CRYSTAL_CLARITY_WEAK,
			CRYSTAL_CLARITY_HEAVY,
			CRYSTAL_CLARITY_CLEAR,
			CRYSTAL_CLARITY_LEGENDARY,
			CRYSTAL_CLARITY_MYTHIC,
		]

		if clarity_type < 0 or clarity_type >= len(list):
			return "unknown[%s]" % clarity_type

		return list[clarity_type]

def LangIDToName(num):
	LANG_NAME_LIST = {
		app.LANG_ENGLISH : LANG_NAME_ENGLISH,
		app.LANG_GERMAN : LANG_NAME_GERMAN,
		app.LANG_ROMANIA : LANG_NAME_ROMANIA,
		app.LANG_TURKISH : LANG_NAME_TURKISH,
	}

	if LANG_NAME_LIST.has_key(num):
		return LANG_NAME_LIST[num]
	else:
		return "[INVALID_LANG_%s]" % str(num)

def FloatAsString(num, maxPrec=2):
	num = float(num)

	if maxPrec <= 0:
		return "%d" % int(num)

	s = ("%%.%df" % maxPrec) % num
	while s[len(s)-1] == '0':
		s = s[:len(s)-1]

	if s[len(s)-1] == '.':
		return "%d" % int(num)

	return s

def IsYMIR():
	return False

def IsJAPAN():
	global __IS_JAPAN
	return __IS_JAPAN

def IsENGLISH():
	global __IS_ENGLISH
	return __IS_ENGLISH

def IsHONGKONG():
	global __IS_HONGKONG
	return __IS_HONGKONG

def IsTAIWAN():
	global __IS_TAIWAN
	return __IS_TAIWAN

def IsNEWCIBN():
	global __IS_NEWCIBN
	return __IS_NEWCIBN

def IsCIBN10():
	global __IS_CIBN10
	return __IS_CIBN10
	
def IsEUROPE():
	global __IS_EUROPE
	return __IS_EUROPE

def IsCANADA():
	global __IS_CANADA
	return __IS_CANADA

def IsBRAZIL():
	global __IS_BRAZIL
	return __IS_BRAZIL

def IsVIETNAM():
	global __IS_VIETNAM
	return __IS_VIETNAM

def IsSINGAPORE():
	global __IS_SINGAPORE
	return __IS_SINGAPORE
	
def IsARABIC():
	if app.ARABIC_LANG:
		return False
	global __IS_ARABIC
	return __IS_ARABIC

def IsWE_KOREA():
	global __IS_WE_KOREA
	return __IS_WE_KOREA

def IsCHEONMA():
	return IsYMIR()

# SUPPORT_NEW_KOREA_SERVER
def LoadLocaleData():
	app.LoadLocaleData()

# END_OF_SUPPORT_NEW_KOREA_SERVER

def mapping(**kwargs): return kwargs

AVAIL_KEY_LIST = {
	app.DIK_A : "A",
	app.DIK_B : "B",
	app.DIK_C : "C",
	app.DIK_D : "D",
	app.DIK_E : "E",
	app.DIK_F : "F",
	app.DIK_G : "G",
	app.DIK_H : "H",
	app.DIK_I : "I",
	app.DIK_J : "J",
	app.DIK_K : "K",
	app.DIK_L : "L",
	app.DIK_M : "M",
	app.DIK_N : "N",
	app.DIK_O : "O",
	app.DIK_P : "P",
	app.DIK_Q : "Q",
	app.DIK_R : "R",
	app.DIK_S : "S",
	app.DIK_T : "T",
	app.DIK_U : "U",
	app.DIK_V : "V",
	app.DIK_W : "W",
	app.DIK_X : "X",
	app.DIK_Y : "Y",
	app.DIK_Z : "Z",
	app.DIK_0 : "0",
	app.DIK_1 : "1",
	app.DIK_2 : "2",
	app.DIK_3 : "3",
	app.DIK_4 : "4",
	app.DIK_5 : "5",
	app.DIK_6 : "6",
	app.DIK_7 : "7",
	app.DIK_8 : "8",
	app.DIK_9 : "9",
	app.DIK_F1 : "F1",
	app.DIK_F2 : "F2",
	app.DIK_F3 : "F3",
	app.DIK_F4 : "F4",
	app.DIK_F5 : "F5",
	app.DIK_F6 : "F6",
	app.DIK_F7 : "F7",
	app.DIK_F8 : "F8",
	app.DIK_F9 : "F9",
	app.DIK_F10 : "F10",
	app.DIK_F11 : "F11",
	app.DIK_F12 : "F12",
}

def SNA(text):	
	def f(x):
		return text
	return f

def SA(text):
	def f(x):
		try:
			if x == None:
				return text
			else:
				return text % x
		except:
			import dbg
			dbg.LogBox("Error[SA] %s" % text)
			return ""

	return f
	
localeDESADict = {}

def LoadDESAs():
	global localeDESADict
	localeDESADict = {}

	lineIndex = 1

	try:
		lines = pack_open("locale\\de\\locale_game.txt", "r").readlines()
	except IOError:
		import dbg
		dbg.LogBox("LoadLocaleSAsError")
		app.Abort()

	for line in lines:
		try:		
			tokens = line[:-1].split("\t")
			if len(tokens) == 2:
				pass
			elif len(tokens) >= 3:
				type = tokens[2].strip()
				if type:
					localeDESADict[tokens[0]] = type

			else:
				raise RuntimeError, "Unknown TokenSize"

			lineIndex += 1
		except:
			import dbg
			dbg.LogBox("LoadDESAs: line(%d): %s" % (lineIndex, line), "Error")
			raise

def LoadLocaleFile(srcFileName, localeDict):
	global localeDESADict
	if len(localeDESADict) == 0:
		LoadDESAs()

	funcDict = {"SA":SA, "SNA":SNA}

	lineIndex = 1

	try:
		lines = pack_open(srcFileName, "r").readlines()
	except IOError:
		import dbg
		dbg.LogBox("LoadLocaleError(%(srcFileName)s)" % locals())
		app.Abort()

	for line in lines:
		try:		
			tokens = line[:-1].split("\t")
			if len(tokens) >= 2:
				if localeDESADict.has_key(tokens[0]):
					localeDict[tokens[0]] = funcDict[localeDESADict[tokens[0]]](tokens[1])
				else:
					# Replace \n and /n to [ENTER]
					replacedToken = tokens[1].replace('\\n', '[ENTER]').replace('/n', '[ENTER]')
					localeDict[tokens[0]] = replacedToken

			else:
				raise RuntimeError, "Unknown TokenSize"

			lineIndex += 1
		except:
			import dbg
			dbg.LogBox("%s: line(%d): %s" % (srcFileName, lineIndex, line), "Error")
			raise

	
all = ["locale","error"]
FN_GM_MARK = "d:/ymir work/effect/gm.mse"
DEFAULT_LOCALE_FILE_NAME = "%s/locale_game.txt" % app.GetDefaultLocalePath()
LOCALE_FILE_NAME = "%s/locale_game.txt" % app.GetLocalePath()
constInfo.IN_GAME_SHOP_ENABLE = 1

if DEFAULT_LOCALE_FILE_NAME != LOCALE_FILE_NAME:
	LoadLocaleFile(DEFAULT_LOCALE_FILE_NAME, locals())
LoadLocaleFile(LOCALE_FILE_NAME, locals())

########################################################################################################
## NOTE : ľĆŔĚĹŰŔ» ąö¸±¶§ "ą«ľůŔ»/¸¦ ąö¸®˝Ă°Ú˝Ŕ´Ď±î?" ą®ŔÚż­ŔÇ Á¶»ç Ľ±ĹĂŔ» Ŕ§ÇŃ ÄÚµĺ
dictSingleWord = {
	"m":1, "n":1, "r":1, "M":1, "N":1, "R":1, "l":1, "L":1, "1":1, "3":1, "6":1, "7":1, "8":1, "0":1,
}

dictDoubleWord = {
	"°ˇ":1, "°Ľ":1, "°Ĺ":1, "°Ü":1, "°í":1, "±ł":1, "±¸":1, "±Ô":1, "±×":1, "±â":1, "°ł":1, "°Â":1, "°Ô":1, "°č":1, "°ú":1, "±Ą":1, "±Ĺ":1, "±Ë":1, "±«":1, "±Í":1, "±á":1,
	"±î":1, "˛Ą":1, "˛¨":1, "˛¸":1, "˛ż":1, "˛Ř":1, "˛Ů":1, "˛ó":1, "˛ô":1, "ł˘":1, "±ú":1, "Ć":1, "˛˛":1, "˛ľ":1, "˛Ę":1, "˛Ď":1, "˛ă":1, "˛ç":1, "˛Ň":1, "˛î":1, "…Ę":1,
	"łŞ":1, "łÄ":1, "łĘ":1, "łŕ":1, "łë":1, "´˘":1, "´©":1, "´ş":1, "´Ŕ":1, "´Ď":1, "ł»":1, "†v":1, "ł×":1, "łé":1, "łö":1, "‡R":1, "´˛":1, "´´":1, "łú":1, "´µ":1, "´Ě":1,
	"´Ů":1, "´ô":1, "´ő":1, "µ®":1, "µµ":1, "µÍ":1, "µÎ":1, "µŕ":1, "µĺ":1, "µđ":1, "´ë":1, "Ű":1, "µĄ":1, "µł":1, "µÂ":1, "µĹ":1, "µÖ":1, "µŘ":1, "µÇ":1, "µÚ":1, "µď":1,
	"µű":1, "‹x":1, "¶°":1, "¶Ĺ":1, "¶Ç":1, "ŚĂ":1, "¶Ń":1, "ŤŹ":1, "¶ß":1, "¶ě":1, "¶§":1, "‹š":1, "¶Ľ":1, "‹ó":1, "¶Ě":1, "¶Î":1, "Śô":1, "¶Ř":1, "¶Ď":1, "¶Ů":1, "¶ç":1,
	"¶ó":1, "·Ş":1, "·Ż":1, "·Á":1, "·Î":1, "·á":1, "·ç":1, "·ů":1, "¸Ł":1, "¸®":1, "·ˇ":1, "Žm":1, "·ą":1, "·Ę":1, "·Ö":1, "ŹO":1, "·ď":1, "·ń":1, "·Ú":1, "·ň":1, "l":1,
	"¸¶":1, "¸Ď":1, "¸Ó":1, "¸ç":1, "¸đ":1, "ą¦":1, "ą«":1, "ąÂ":1, "ąÇ":1, "ąĚ":1, "¸Ĺ":1, "Ů":1, "¸Ţ":1, "¸ď":1, "¸ú":1, "‘Ŕ":1, "ąą":1, "ąľ":1, "¸ţ":1, "ąż":1, "’Ţ":1,
	"ąŮ":1, "ąň":1, "ąö":1, "ş­":1, "ş¸":1, "şĚ":1, "şÎ":1, "şä":1, "şę":1, "şń":1, "ąč":1, "“Ž":1, "şŁ":1, "ş¶":1, "şÁ":1, "şÄ":1, "şŰ":1, "şŢ":1, "şĆ":1, "şß":1, "•‘":1,
	"şü":1, "»˛":1, "»µ":1, "»Ŕ":1, "»Ç":1, "»Ď":1, "»Ń":1, "»Ř":1, "»Ú":1, "»ß":1, "»©":1, "•ű":1, "»ľ":1, "–§":1, "–Ř":1, "–ô":1, "—¨":1, "—Ä":1, "»Î":1, "—ŕ":1, "u":1,
	"»ç":1, "»ţ":1, "Ľ­":1, "ĽĹ":1, "ĽŇ":1, "Ľî":1, "Ľö":1, "˝´":1, "˝ş":1, "˝Ă":1, "»ő":1, "Ľ¨":1, "ĽĽ":1, "ĽÎ":1, "ĽÝ":1, "Ľâ":1, "˝¤":1, "˝¦":1, "Ľč":1, "˝¬":1, "šĂ":1,
	"˝Î":1, "›X":1, "˝á":1, "›Ç":1, "˝î":1, "ľ¤":1, "ľĄ":1, "ťo":1, "ľ˛":1, "ľľ":1, "˝Ř":1, "›y":1, "˝ę":1, "›ă":1, "˝÷":1, "˝ű":1, "ľ¬":1, "ľ®":1, "˝ý":1, "ľŻ":1, "ľş":1,
	"ľĆ":1, "ľß":1, "ľî":1, "ż©":1, "żŔ":1, "żä":1, "żě":1, "ŔŻ":1, "Ŕ¸":1, "ŔĚ":1, "ľÖ":1, "ľę":1, "żˇ":1, "żą":1, "żÍ":1, "żÖ":1, "żö":1, "żţ":1, "żÜ":1, "Ŕ§":1, "ŔÇ":1,
	"ŔÚ":1, "Ŕđ":1, "Ŕú":1, "Á®":1, "Á¶":1, "ÁŇ":1, "ÁÖ":1, "Áę":1, "Áî":1, "Áö":1, "Ŕç":1, "Ŕ÷":1, "Á¦":1, "Áµ":1, "ÁÂ":1, "ÁČ":1, "Áŕ":1, "Áâ":1, "ÁË":1, "Áă":1, "Łp":1,
	"ÂĄ":1, "Âą":1, "ÂĽ":1, "ÂÇ":1, "ÂÉ":1, "§c":1, "ÂŢ":1, "Âé":1, "Âę":1, "Âî":1, "Â°":1, "¤Š":1, "ÂĹ":1, "Ą™":1, "ÂŇ":1, "ÂÖ":1, "Âĺ":1, "¨R":1, "ÂŘ":1, "Âč":1, "©n":1,
	"Â÷":1, "Ă­":1, "Ăł":1, "ĂÄ":1, "ĂĘ":1, "ĂÝ":1, "Ăß":1, "Ăň":1, "Ă÷":1, "Äˇ":1, "Ă¤":1, "Ş‰":1, "ĂĽ":1, "ĂÇ":1, "ĂŇ":1, "¬‚":1, "Ăç":1, "Ăé":1, "ĂÖ":1, "Ăë":1, "ŻM":1,
	"Ä«":1, "ÄĽ":1, "Äż":1, "ÄŃ":1, "ÄÚ":1, "Äě":1, "Äí":1, "ĹĄ":1, "Ĺ©":1, "Ĺ°":1, "Äł":1, "°m":1, "ÄÉ":1, "ÄŮ":1, "Äâ":1, "Äč":1, "Äő":1, "Äů":1, "Äę":1, "Äű":1, "´”":1,
	"Ĺ¸":1, "ĹË":1, "ĹÍ":1, "Ĺß":1, "Ĺä":1, "Ĺô":1, "Ĺő":1, "Ć©":1, "Ć®":1, "ĆĽ":1, "ĹÂ":1, "¶O":1, "Ĺ×":1, "Ĺâ":1, "Ĺí":1, "Ĺď":1, "Ĺý":1, "Ćˇ":1, "Ĺđ":1, "Ć˘":1, "Ć·":1,
	"ĆÄ":1, "ĆŮ":1, "ĆŰ":1, "Ćě":1, "Ć÷":1, "ÇĄ":1, "ÇŞ":1, "Ç»":1, "ÇÁ":1, "ÇÇ":1, "ĆĐ":1, "»—":1, "Ćä":1, "Ćó":1, "Çˇ":1, "˝Ť":1, "Ç´":1, "żR":1, "ÇŁ":1, "Ç¶":1, "Ŕc":1,
	"ÇĎ":1, "Çá":1, "Çă":1, "Çô":1, "ČŁ":1, "Čż":1, "ČÄ":1, "ČŢ":1, "Čĺ":1, "Č÷":1, "ÇŘ":1, "Á…":1, "Çě":1, "Çý":1, "Č­":1, "Čł":1, "ČĚ":1, "ČŃ":1, "Č¸":1, "ČÖ":1, "Čń":1,
}

locale = mapping(
)

def GetAuxiliaryWordType(text):
	textLength = len(text)
	if textLength > 1:

		singleWord = text[-1]

		if (singleWord >= '0' and singleWord <= '9') or\
			(singleWord >= 'a' and singleWord <= 'z') or\
			(singleWord >= 'A' and singleWord <= 'Z'):
			if not dictSingleWord.has_key(singleWord):
				return 1

		elif dictDoubleWord.has_key(text[-2:]):
			return 1

	return 0

def CutMoneyString(sourceText, startIndex, endIndex, insertingText, backText):
	sourceLength = len(sourceText)
	if sourceLength < startIndex:
		return backText

	text = sourceText[max(0, sourceLength-endIndex):sourceLength-startIndex]
	if not text:
		return backText

	if int(text) <= 0:
		return backText

	text = str(int(text))
	if backText:
		backText = " " + backText

	return text + insertingText + backText

def GetStringByTimestamp(timestamp):
	iSec, iMin, iHour, iDay, iMonth, iYear = app.GetDateByTimestamp(timestamp)
	iMin = round((float(iMin) * 60.0 + float(iSec)) / 60.0)
	if iMin >= 60:
		iHour += 1
		iMin -= 60
	if iHour >= 24:
		iDay += 1
		iHour -= 24

	return "%02d.%02d. %02d:%02d" % (iDay, iMonth + 1, iHour, iMin)
def ZodiacTimeReturn(time):
	text = ""
	if time < 0:
		time *= -1
		text = "-"

	second = int(time % 60)
	minute = int((time / 60) % 60)
	hour = int((time / 60) / 60)
	
	if hour > 0:
		if hour < 10:
			text += "0" + str(hour) + ":"
		else:
			text += str(hour) + ":"
	else:
		text += "00:"
		
	if minute > 0:
		if minute < 10:
			text += "0" + str(minute) + ":"
		else:
			text += str(minute) + ":"
	else:
		text += "00:"
		
	if second > 0:
		if second < 10:
			text += "0" + str(second) + ""
		else:
			text += str(second) + ""
	else:
		text += "00"

	return text
def SecondToDHMS(time, ignoreSecTime = -1, useShortName = True):
	text = ""
	if time < 0:
		time *= -1
		text = "-"

	second = int(time % 60)
	minute = int((time / 60) % 60)
	hour = int(((time / 60) / 60) % 24)
	day = int(((time / 60) / 60) / 24)

	if ignoreSecTime > 0 and time >= ignoreSecTime:
		second = 0

	if day > 0:
		if day == 1:
			text += str(day) + " " + TIME_DAY + " "
		else:
			text += str(day) + " " + TIME_DAYS + " "

	if hour > 0:
		text += str(hour) + " "
		if useShortName == True:
			text += TIME_S_HOUR + " "
		else:
			if hour == 1:
				text += TIME_HOUR + " "
			else:
				text += TIME_HOURS + " "

	if minute > 0:
		text += str(minute) + " "
		if useShortName == True:
			text += TIME_S_MIN + " "
		else:
			if minute == 1:
				text += TIME_MINUTE + " "
			else:
				text += TIME_MINUTES + " "

	if (second > 0 or (hour == 0 and minute == 0)) and (day == 0):
		text += str(second) + " "
		if useShortName == True:
			text += TIME_S_SEC + " "
		else:
			if second == 1:
				text += TIME_SEC + " "
			else:
				text += TIME_SECS + " "

	return text[:-1]

def SecondToDHM(time):
	if time < 60:
		if IsARABIC():
			return "%.2f %s" % (time, SECOND)
		else:
			return "0" + MINUTE
		
	second = int(time % 60)
	minute = int((time / 60) % 60)
	hour = int((time / 60) / 60) % 24
	day = int(int((time / 60) / 60) / 24)

	text = ""

	if day > 0:
		text += str(day) + DAY
		text += " "

	if hour > 0:
		text += str(hour) + HOUR
		text += " "

	if minute > 0:
		text += str(minute) + MINUTE

	return text

def SecondToHM(time):
	if time < 60:
		if IsARABIC():
			return "%.2f %s" % (time, SECOND)
		else:
			return "0" + MINUTE

	second = int(time % 60)
	minute = int((time / 60) % 60)
	hour = int((time / 60) / 60)

	text = ""

	if hour > 0:
		text += str(hour) + HOUR
		if hour > 0:
			text += " "

	if minute > 0:
		text += str(minute) + MINUTE

	return text

def SecondToDHMSShort(time):
	days = int(time / (24 * 60 * 60))
	time -= 24 * 60 * 60 * days
	hours = int(time / (60 * 60))
	time -= 60 * 60 * hours
	mins = int(time / 60)
	time -= 60 * mins
	secs = int(time)

	return "%02d:%02d:%02d:%02d" % (days, hours, mins, secs)

OPTION_PVPMODE_MESSAGE_DICT = {
	0 : PVP_MODE_NORMAL,
	1 : PVP_MODE_REVENGE,
	2 : PVP_MODE_KILL,
	3 : PVP_MODE_PROTECT,
	4 : PVP_MODE_GUILD,
}

error = mapping(
	CREATE_WINDOW = GAME_INIT_ERROR_MAIN_WINDOW,
	CREATE_CURSOR = GAME_INIT_ERROR_CURSOR,
	CREATE_NETWORK = GAME_INIT_ERROR_NETWORK,
	CREATE_ITEM_PROTO = GAME_INIT_ERROR_ITEM_PROTO,
	CREATE_MOB_PROTO = GAME_INIT_ERROR_MOB_PROTO,
	CREATE_NO_DIRECTX = GAME_INIT_ERROR_DIRECTX,
	CREATE_DEVICE = GAME_INIT_ERROR_GRAPHICS_NOT_EXIST,
	CREATE_NO_APPROPRIATE_DEVICE = GAME_INIT_ERROR_GRAPHICS_BAD_PERFORMANCE,
	CREATE_FORMAT = GAME_INIT_ERROR_GRAPHICS_NOT_SUPPORT_32BIT,
	NO_ERROR = ""
)


GUILDWAR_NORMAL_DESCLIST = [GUILD_WAR_USE_NORMAL_MAP, GUILD_WAR_LIMIT_30MIN, GUILD_WAR_WIN_CHECK_SCORE]
GUILDWAR_WARP_DESCLIST = [GUILD_WAR_USE_BATTLE_MAP, GUILD_WAR_WIN_WIPE_OUT_GUILD, GUILD_WAR_REWARD_POTION]
GUILDWAR_CTF_DESCLIST = [GUILD_WAR_USE_BATTLE_MAP, GUILD_WAR_WIN_TAKE_AWAY_FLAG1, GUILD_WAR_WIN_TAKE_AWAY_FLAG2, GUILD_WAR_REWARD_POTION]

MINIMAP_ZONE_NAME_DICT = {
	"metin2_map_a1"  : MAP_A1,
	"metin2_map_a3"  : MAP_A3,
	"metin2_map_b1"  : MAP_B1,
	"metin2_map_b3"  : MAP_B3,
	"metin2_map_c1"  : MAP_C1,
	"metin2_map_c3"  : MAP_C3,
	"metin_map_n_snow" : MAP_SNOW,
	"metin2_map_n_flame" : MAP_FLAME,
	"metin2_map_n_desert" : MAP_DESERT,
	"metin2_map_milgyo" : MAP_TEMPLE,
	"metin2_map_spiderdungeon_01" : MAP_SPIDER,
	"metin2_map_deviltower" : MAP_SKELTOWER,
	"metin2_map_guild_01" : MAP_AG,
	"metin2_map_guild_02" : MAP_BG,
	"metin2_map_guild_03" : MAP_CG,
	"metin2_map_trent_01" : MAP_TREE,
	"metin2_map_trent_02" : "MAP_TREE2",
}

JOBINFO_TITLE = [
	[JOB_WARRIOR0, JOB_WARRIOR1, JOB_WARRIOR2,],
	[JOB_ASSASSIN0, JOB_ASSASSIN1, JOB_ASSASSIN2,],
	[JOB_SURA0, JOB_SURA1, JOB_SURA2,],
	[JOB_SHAMAN0, JOB_SHAMAN1, JOB_SHAMAN2,],
]

WHISPER_ERROR = {
	chat.WHISPER_TYPE_NOT_LOGIN : CANNOT_WHISPER_NOT_LOGON,
	chat.WHISPER_TYPE_NOT_EXIST : CANNOT_WHISPER_NOT_EXIST,
	chat.WHISPER_TYPE_TARGET_BLOCKED : CANNOT_WHISPER_DEST_REFUSE,
	chat.WHISPER_TYPE_SENDER_BLOCKED : CANNOT_WHISPER_SELF_REFUSE,
	chat.WHISPER_TYPE_NOAUTH : CANNOT_WHISPER_NO_AUTH,
}

NOTIFY_MESSAGE = {
	"CANNOT_EQUIP_SHOP" : CANNOT_EQUIP_IN_SHOP,
	"CANNOT_EQUIP_EXCHANGE" : CANNOT_EQUIP_IN_EXCHANGE,
}


SHOT_ERROR_TAIL_DICT = {
	"EMPTY_ARROW" : CANNOT_SHOOT_EMPTY_ARROW,
	"IN_SAFE" : CANNOT_SHOOT_SELF_IN_SAFE,
	"DEST_IN_SAFE" : CANNOT_SHOOT_DEST_IN_SAFE,
}
	
USE_SKILL_ERROR_TAIL_DICT = {	
	"IN_SAFE" : CANNOT_SKILL_SELF_IN_SAFE,
	"NEED_TARGET" : CANNOT_SKILL_NEED_TARGET,
	"NEED_EMPTY_BOTTLE" : CANNOT_SKILL_NEED_EMPTY_BOTTLE,
	"NEED_POISON_BOTTLE" : CANNOT_SKILL_NEED_POISON_BOTTLE,
	"REMOVE_FISHING_ROD" : CANNOT_SKILL_REMOVE_FISHING_ROD,
	"NOT_YET_LEARN" : CANNOT_SKILL_NOT_YET_LEARN,
	"NOT_MATCHABLE_WEAPON" : CANNOT_SKILL_NOT_MATCHABLE_WEAPON,
	"WAIT_COOLTIME" : CANNOT_SKILL_WAIT_COOLTIME,
	"NOT_ENOUGH_HP" : CANNOT_SKILL_NOT_ENOUGH_HP,
	"NOT_ENOUGH_SP" : CANNOT_SKILL_NOT_ENOUGH_SP,
	"CANNOT_USE_SELF" : CANNOT_SKILL_USE_SELF,
	"ONLY_FOR_ALLIANCE" : CANNOT_SKILL_ONLY_FOR_ALLIANCE,
	"CANNOT_ATTACK_ENEMY_IN_SAFE_AREA" : CANNOT_SKILL_DEST_IN_SAFE,
	"CANNOT_APPROACH" : CANNOT_SKILL_APPROACH,
	"CANNOT_ATTACK" : CANNOT_SKILL_ATTACK,
	"ONLY_FOR_CORPSE" : CANNOT_SKILL_ONLY_FOR_CORPSE,
	"EQUIP_FISHING_ROD" : CANNOT_SKILL_EQUIP_FISHING_ROD, 
	"NOT_HORSE_SKILL" : CANNOT_SKILL_NOT_HORSE_SKILL,
	"HAVE_TO_RIDE" : CANNOT_SKILL_HAVE_TO_RIDE,
}

LEVEL_LIST=["", HORSE_LEVEL1, HORSE_LEVEL2, HORSE_LEVEL3]

HEALTH_LIST=[
	HORSE_HEALTH0,
	HORSE_HEALTH1, 
	HORSE_HEALTH2,
	HORSE_HEALTH3,
]


USE_SKILL_ERROR_CHAT_DICT = {	
	"NEED_EMPTY_BOTTLE" : SKILL_NEED_EMPTY_BOTTLE,
	"NEED_POISON_BOTTLE" : SKILL_NEED_POISON_BOTTLE, 
	"ONLY_FOR_GUILD_WAR" : SKILL_ONLY_FOR_GUILD_WAR,
}

SHOP_ERROR_DICT = {
	"NOT_ENOUGH_MONEY" : SHOP_NOT_ENOUGH_MONEY,
	"NOT_ENOUGH_MONEY_EX" : SHOP_NOT_ENOUGH_MONEY_EX,
	"SOLDOUT" : SHOP_SOLDOUT,
	"INVENTORY_FULL" : SHOP_INVENTORY_FULL,
	"INVALID_POS" : SHOP_INVALID_POS,
	"ZODIAC_SHOP" : ZODIAC_SHOP_ALREADY_BOUGHT,
}

if (app.COMBAT_ZONE):
	SHOP_ERROR_DICT.update({
		"NOT_ENOUGH_POINTS" : COMBAT_ZONE_SHOP_NOT_ENOUGH_BATTLE_POINT,
		"MAX_LIMIT_POINTS" : COMBAT_ZONE_SHOP_EXCEED_LIMIT_TODAY,
		"OVERFLOW_LIMIT_POINTS" : COMBAT_ZONE_SHOP_OVERFLOW_LIMIT_TODAY
		}
	)

STAT_MINUS_DESCRIPTION = {
	"HTH-" : STAT_MINUS_CON,
	"INT-" : STAT_MINUS_INT,
	"STR-" : STAT_MINUS_STR,
	"DEX-" : STAT_MINUS_DEX,
}

MODE_NAME_LIST = ( PVP_OPTION_NORMAL, PVP_OPTION_REVENGE, PVP_OPTION_KILL, PVP_OPTION_PROTECT, )
TITLE_NAME_LIST = ( PVP_LEVEL0, PVP_LEVEL1, PVP_LEVEL2, PVP_LEVEL3, PVP_LEVEL4, PVP_LEVEL5, PVP_LEVEL6, PVP_LEVEL7, PVP_LEVEL8, )

LETTER_NAME_LIST = {
	"open" : {
		0 : "icon/scroll_open.tga",
		1 : "icon/battlepass_scroll_open.tga",
	},
	"close" : {
		0 : "icon/scroll_close.tga",
		1 : "icon/battlepass_scroll_close.tga",
	},
}

def GetLetterImageName(catID = 0):
	data = LETTER_NAME_LIST["close"]
	return data.get(catID, data[0])
def GetLetterOpenImageName(catID = 0):
	data = LETTER_NAME_LIST["open"]
	return data.get(catID, data[0])
def GetLetterCloseImageName(catID = 0):
	data = LETTER_NAME_LIST["close"]
	return data.get(catID, data[0])

def DO_YOU_SELL_ITEM(sellItemName, sellItemCount, sellItemPrice):
	if sellItemCount > 1 :
		return DO_YOU_SELL_ITEM2 % (sellItemName, sellItemCount, NumberToMoneyString(sellItemPrice) )
	else:
		return DO_YOU_SELL_ITEM1 % (sellItemName, NumberToMoneyString(sellItemPrice) )

def DO_YOU_SELL_MULTI_ITEM(sellItemCount, sellItemCountSum, sellItemPrice):
	if sellItemCountSum > sellItemCount:
		return DO_YOU_SELL_MULTI_ITEM2 % (sellItemCount, NumberToString(sellItemCountSum), NumberToMoneyString(sellItemPrice))
	else:
		return DO_YOU_SELL_MULTI_ITEM1 % (sellItemCount, NumberToMoneyString(sellItemPrice))

def DO_YOU_BUY_ITEM(buyItemName, buyItemCount, buyItemPrice) :
	if buyItemCount > 1 :
		return DO_YOU_BUY_ITEM2 % ( buyItemName, buyItemCount, buyItemPrice )
	else:
		return DO_YOU_BUY_ITEM1 % ( buyItemName, buyItemPrice )

def DO_YOU_TAKE_OUT_ITEM(buyItemName, buyItemCount) :
	if buyItemCount > 1 :
		return DO_YOU_TAKE_OUT_ITEM2 % ( buyItemName, buyItemCount )
	else:
		return DO_YOU_TAKE_OUT_ITEM1 % ( buyItemName )
		
def REFINE_FAILURE_CAN_NOT_ATTACH(attachedItemName) :
	return REFINE_FAILURE_CAN_NOT_ATTACH0 % (attachedItemName)

def REFINE_FAILURE_NO_SOCKET(attachedItemName) :
	return REFINE_FAILURE_NO_SOCKET0 % (attachedItemName)

def REFINE_FAILURE_NO_GOLD_SOCKET(attachedItemName) :
	return REFINE_FAILURE_NO_GOLD_SOCKET0 % (attachedItemName)

def HOW_MANY_ITEM_DO_YOU_DROP(dropItemName, dropItemIsMoney, dropItemCount):
	if dropItemIsMoney:
		if dropItemCount > 1:
			return HOW_MANY_ITEM_DO_YOU_DROP2 % (dropItemCount, dropItemName)
		else:	
			return HOW_MANY_ITEM_DO_YOU_DROP1 % (dropItemName)
	else:
		if dropItemCount > 1:
			return HOW_MANY_ITEM_DO_YOU_DROP_OR_DESTROY2 % (dropItemCount, dropItemName)
		else:	
			return HOW_MANY_ITEM_DO_YOU_DROP_OR_DESTROY1 % (dropItemName)

def HOW_MANY_ITEM_DO_YOU_DESTROY(dropItemName, dropItemCount):
	if dropItemCount > 1 :
		return HOW_MANY_ITEM_DO_YOU_DESTROY2 % (dropItemCount, dropItemName)
	else:
		return HOW_MANY_ITEM_DO_YOU_DESTROY1 % (dropItemName)

def FISHING_NOTIFY(isFish, fishName) :
	if isFish :
		return FISHING_NOTIFY1 % ( fishName )
	else :
		return FISHING_NOTIFY2 % ( fishName )

def FISHING_SUCCESS(isFish, fishName) :
	if isFish :
		return FISHING_SUCCESS1 % (fishName)
	else :
		return FISHING_SUCCESS2 % (fishName)
		
def NumberToMoneyString(n, writeText = True) :
	if writeText:
		if n <= 0 :
			return "0 %s" % (MONETARY_UNIT0)

	if writeText:
		return "%s %s" % ('.'.join([ i-3<0 and str(n)[:i] or str(n)[i-3:i] for i in range(len(str(n))%3, len(str(n))+1, 3) if i ]), MONETARY_UNIT0) 
	else:
		return '.'.join([ i-3<0 and str(n)[:i] or str(n)[i-3:i] for i in range(len(str(n))%3, len(str(n))+1, 3) if i ])

if (app.COMBAT_ZONE):
	def NumberToCombatZoneCoinString(n) :
		if n <= 0 :
			return "0 %s" % (MONETARY_COMBAT_ZONE)
		return "%s %s" % ('.'.join([ i-3<0 and str(n)[:i] or str(n)[i-3:i] for i in range(len(str(n))%3, len(str(n))+1, 3) if i ]), MONETARY_COMBAT_ZONE)

def NumberToGayaString(n) :
	if n <= 0 :
		return "0 %s" % (MONETARY_UNIT_GAYA)

	return "%s %s" % ('.'.join([ i-3<0 and str(n)[:i] or str(n)[i-3:i] for i in range(len(str(n))%3, len(str(n))+1, 3) if i ]), MONETARY_UNIT_GAYA) 

def NumberToString(n):
	if n <= 0:
		return str(n)

	try:
		if n >= 1000000000:
			addon_text = ''
			while str(n).endswith('000'):
				n = str(n)[:-3]
				addon_text = addon_text + "K"
			if addon_text != '':
				return "%s %s" % (('.'.join([i-3<0 and str(n)[:i] or str(n)[i-3:i] for i in range(len(str(n))%3, len(str(n))+1, 3) if i])), addon_text)
			else:
				n = str(n)[:-6]
				return "%s KK" % ('.'.join([i-3<0 and str(n)[:i] or str(n)[i-3:i] for i in range(len(str(n))%3, len(str(n))+1, 3) if i]))
				
	except:
		tchat('NumberToStringERR')

	return "%s" % ('.'.join([i-3<0 and str(n)[:i] or str(n)[i-3:i] for i in range(len(str(n))%3, len(str(n))+1, 3) if i]))

def GET_TIME_STRING_BY_TIMESTAMP(timestamp):
	warSec, warMin, warHour, warDay, warMonth, warYear = app.GetDateByTimestamp(timestamp)
	warMin = round((float(warMin) * 60.0 + float(warSec)) / 60.0)
	if warMin >= 60:
		warHour += 1
		warMin -= 60
	if warHour >= 24:
		warDay += 1
		warHour -= 24

	return "%02d.%02d. %02d:%02d" % (warDay, warMonth + 1, warHour, warMin)
	
def GetLocals():
	return globals()
