import sys
import app
import dbg
import cfg
import __builtin__
import os
import net
import chat
import player
import item
if __USE_CYTHON__:
	import __main__
	import rootlib

ANTI_CHEAT_OPEN_HOOK = True
ANTI_CHEAT_OPEN_HOOK_RETURN = True

ANTI_CHEAT_IMPORT_WHITELIST = True
ANTI_CHEAT_IMPORT_WHITELIST_RETURN = True

sys.path.append("lib")

__DEBUG__ = 0
__COMMAND_LINE__ = ''

__main__.test_server = os.path.isfile("________dev.txt") or os.path.isfile("dev.txt")

def testlog(msg):
	if test_server: dbg.TraceError(msg)

def testchat(msg):
	if test_server:	chat.AppendChat(1,msg)
__builtins__.tchat = testchat
__builtins__.tlog = testlog

oldAppendWhisper = chat.AppendWhisper
def AddTimestampToAppendWhisper(type, name, line):
	if cfg.Get(cfg.SAVE_OPTION, "whisper_timestamp", "0") == "1":
		import time
		line = "%s %s" % (time.strftime('%H:%M'), line)
	oldAppendWhisper(type, name, line)
chat.AppendWhisper = AddTimestampToAppendWhisper

old_func = net.ConnectToAccountServer
def connect(*args):
	if net.IsConnect():
		dbg.TraceError("Connect Again Error detected?")
		return
	old_func(*args)
net.ConnectToAccountServer = connect

# Check Color Cheat
# OriginalSendChat = net.SendChatPacket
# def NewSendChat(*args):
# 	text = args[0].lower()
# 	if '|c' in text and '|cff00c0fc|h|h' not in text and 'item:' not in text:
# 		return
# 	if '|c' in text:
# 		for c in text.split('|c'):
# 			if '|h' in c and not c.startswith('ff00c0fc'):
# 				return
# 	OriginalSendChat(*args)
# net.SendChatPacket = NewSendChat

if ANTI_CHEAT_OPEN_HOOK:
	# Anti Cheat
	old_open = __builtin__.open
	def NewOpen(*args):
		file_whitelist = ['mouse.cfg', 'BGM/lastplay.inf', 'coords.txt', 'race_height.txt', 'race_specular.txt', 'syserr.txt', 'login.txt', 'select.txt']
		folder_whitelist = ['Camera', 'memory_leak', 'wiki']

		file_whitelist =  map(lambda x: x.lower(), file_whitelist)
		folder_whitelist = map(lambda x: x.lower(), folder_whitelist)

		if args[0].lower() not in file_whitelist:

			# Check if file is in whitelisted folder...
			for whitelisted_folder in folder_whitelist:
				if args[0].lower().startswith(whitelisted_folder):
					return old_open(*args)

			if net.IsConnect():
				net.PingPacket("open", args[0])

			if test_server:
				dbg.LogBox("OPEN HOOK : %s" % str(args))

			if ANTI_CHEAT_OPEN_HOOK_RETURN:
				args[0] = ''

		return old_open(*args)
	__builtin__.open = NewOpen


# def trace_calls_and_returns(frame, event, arg):
#     co = frame.f_code
#     func_name = co.co_name
#     if func_name == 'write':
#         # Ignore write() calls from print statements
#         return
#     line_no = frame.f_lineno
#     filename = co.co_filename
#     if event == 'call':
#         dbg.TraceError('Call to %s on line %s of %s' % (func_name, line_no, filename))
#         return trace_calls_and_returns
#     # elif event == 'return':
#     #     dbg.TraceError('%s => %s' % (func_name, arg))
#     return

# sys.settrace(trace_calls_and_returns)



OriginalselectItem = item.SelectItem
def NewSelectItem(*args):
	x = sys._getframe().f_back.f_code
	if x.co_filename == "<string>":
		# if net.IsConnect():
		net.PingPacket("item.SelectItem", "[%s]%s%d" % (x.co_name, x.co_filename, x.co_firstlineno))
		# tchat("[%s]%s%d" % (x.co_name, x.co_filename, x.co_firstlineno))
	return OriginalselectItem(*args)
item.SelectItem = NewSelectItem

# originals = dict()
# def hooked(name, *args):
# 	dbg.TraceError("%s" % name)
# 	return originals[str(name)](*args)

# for module in ['net']:
# 	for func in dir(module):
# 		if "function" in str(getattr(module, str(func))):
# 			originals.append(str(func) : func)
# 			func = 



def strToUpper(s):
	return s.upper().replace("ä", "Ä").replace("ö", "Ö").replace("ü", "Ü")
__builtins__.strUpper = strToUpper

whitelist = ['_cython_0_29_3', '_cython_0_29_7', 'uiWheelOfFright', "LoginWindow_s2", 'WheelOfFright', 'uiReactEvent', 'newgameoptiondialog', 'uicombatzone', 'whispermgr','loginwindow', 'blackjack', 'battlepass', 'fractionwindow', 'choosefractionwindow', 'rankwindow', 'uirank', 'weakref', 'gc','wiki', 'inGameWiki', 'inGameWikiUI','xmasevent','switchbotwindow','SplitItemDialog','skinsystemwindow', 'moviemaker', 'eventannouncement', 'newofflineshopwindow', 'runetutorialwindow','offlineshopwindow', 'newofflineshopwindow_visuals', 'splititemdialog', '_cython_0_29_6', 'cython_runtime', 'rootlib', 'system', 'xmasevent', \
				'encodings.utf_8','encodings.utf8','uiscriptlib','Prototype', 'uiPlantHp', 'uiPassiveSkill','uisoulsystem', 'uiSkillColor', 'datetime', 'uiXmasEvent', 'uiNewOfflineShop', 'uiMovieMaker', 'uisystemannounce', 'uiMiniGameFishEvent', 'uiMiniGame', 'uieventannouncement', 'uieventicon', 'uimasthp', 'uinewtimer', 'uistatsboard', 'utils', 'uiRune', 'uiSwitchbot2','timer','uiCostumeBonusTransfer','backports', 'uiSplitItem', 'uiShopSearch', 'uiAttrTree', 'uiGuildPopup', 'uiTimer', 'uiGuildList', 'uiGuildBank', 'protoData', 'uiAttrTree', 'uiGuildPopup', 'uiswitchbot', 'binascii', 'shop', 'functools', 'dbg', 'sysconfig', 'encodings.encodings', 'skill', 'ime', 'bio', 'zipimport', 'quest', 'grpImage', 'background', 'signal', 'item', 'accmgr', 'nonplayer', 'eventMgr', 'genericpath', 'locale', 'cfg', 'snd', 'encodings', 'event', 'abc', 'pet', 're', 'messenger', 'ntpath', 'net', 'exchange', 'UserDict', 'rodinia', 'wndMgr', 'news', '_functools', '_locale', 'textTail', 'auction', 'traceback', 'os', '_sre', 'app', 'codecs', '__builtin__', 'operator', 'errno', 'whispermgr', 'sre_constants', 'chr', 'os.path', 'sphaera', '_warnings', 'encodings.__builtin__', '_codecs', 'safebox', 'fly', 'guild', 'profiler', 'admin', 'encodings.aliases', 'exceptions', 'sre_parse', 'pack', 'miniMap', 'copy_reg', 'sre_compile', 'site', 'player', 'chat', '__main__', 'chrmgr', 'grp', 'linecache', 'encodings.codecs', 'systemSetting', '_abcoll', 'nt', 'guildRanking', 'stat', 'warnings', 'effect', 'sys', 'types', 'ServerStateChecker', '_weakref', '_weakrefset', 'grpText', 'uiSash', 'uiAuction', 'uiSelectMetinDetach', 'uiInfo', 'uiSelectItem', 'uiAcce', 'uiTarget', 'uiCommon', 'uiNewMessenger', 'uiSelectAttrRemove', 'uiAttachMetin', 'imp', 'uiChat', 'new_introSelect', 'uiScriptLocale', 'uiGuildNew', 'localeInfo', 'debugInfo', 'introLoading', 'uiOption', 'uiNews', 'uiPet', 'game', 'playerSettingModule', 'uiParty_new', 'uiGameButton', 'uiItemDesign', 'uiSelectMusic', 'uiPrivateShopBuilder', 'uiPhaseCurtain', 'uiToolTip', 'uiMessenger', 'stringCommander', 'math', 'uiUppitemInventory', 'uiSafebox', 'uiAlchemy', 'uiMaintenance', 'musicInfo', 'uiInventory', 'uiBlackJack', 'marshal', 'emotion', 'uiEquipmentDialog', 'textReader', 'uiRefine', 'uiMapNameShower', 'uiSystem', 'introLanguage', 'uiHorseUpgrade', 'colorInfo', 'uiPointReset', 'uiAccountSecurity', 'uiQuest', 'interfaceModule', 'uiEvent', 'uiTip', 'uiWhisper', 'uiItemRefund', 'uiSphaera', 'uiMiniMap', 'uiAffectShower', 'exception', 'uiTaskBar', 'introLogin', 'ui', 'uiRodinia', 'uiSystemOption', 'uiSkillbookInventory', 'uiAdminManager', 'uiPickMoney', 'networkModule', 'uiGuildRanking', 'uiRestart', 'uiShop', 'uiBio', 'mouseModule', 'uiWeb', 'uiCube', 'consoleModule', 'uiPlayerGauge', 'uiCandidate', 'uiExchange', 'uiGameOption', 'uiGuild', 'uiCharacter', 'constInfo', 'uiSkillbookExchange', 'time', 'uiUploadMark', 'uiOfflineShop', 'new_introCreate', 'introEmpire', '__future__', 'encodings.cp1254', 'uiMovieMaker', 'uiParty', 'uiKingHorseMelt', 'uiPerformanceOption', 'uiPVPRanking', 'uiFakeBuff', 'uiAutoHunt', 'uiCrafting', 'uiLoginReward', 'uidungeon','uicards','uiitemattrrevert','uirune','rune', 'uiApp', 'uiDragonSoul', 'uiAnimal', 'uiGaya', 'uiHelp', 'dragon_soul_refine_settings', 'uidragonlairranking', 'renderTargetManagerTest', 'uicostumeviewer', 'uizodiacanimasphere', 'uiZodiac', 'ui12zirewardwindow', 'uirankingzodiac',
				'reactevent', 'uiFractionWar','battlepass','uiBattlePass','uiNewGameOption', 'uiequipmentchanger', 'equipmentchanger', 'uiequipmentdialog', 'shopsellnotification', 'uihotkey', 'hotkeywindow', 'combatzonewindow', 'uiQuestTask', "uiDmgMeter", ]
whitelist = map(lambda x: x.lower(), whitelist)

def CheckModules():
	abuse_list = ""
	abuse_list_len = 0
	for key,val in sys.modules.iteritems():
		if key.lower() not in whitelist and 'encoding' not in key and 'codec' not in key:
			abuse_list = abuse_list + "'" + key + "', "
	if len(abuse_list):
		net.PingPacket("sys.modules", abuse_list)
		abuse_list_len = len(abuse_list)
		if test_server and abuse_list_len != len(abuse_list):
			dbg.LogBox(1, "whitelist module %s" % abuse_list)
sys.CheckModules = CheckModules

class TraceFile:
	def write(self, msg):
		dbg.Trace(msg)

class TraceErrorFile:
	def write(self, msg):
		dbg.TraceError(msg)
		dbg.RegisterExceptionString(msg)

class LogBoxFile:
	def __init__(self):
		self.stderrSave = sys.stderr
		self.msg = ""

	def __del__(self):
		self.restore()

	def restore(self):
		sys.stderr = self.stderrSave

	def write(self, msg):
		self.msg = self.msg + msg

	def show(self):
		dbg.LogBox(self.msg,"Error")

sys.stdout = TraceFile()
sys.stderr = TraceErrorFile()

#
# pack file support (must move to system.py, systemrelease.pyc)
#

import marshal
import imp
import timer

class pack_file_iterator(object):
	def __init__(self, packfile):
		self.pack_file = packfile
		
	def next(self):
		tmp = self.pack_file.readline()
		if tmp:
			return tmp
		raise StopIteration

_chr = __builtins__.chr

class pack_file(object):

	def __init__(self, filename, mode = 'rb'):
		assert mode in ('r', 'rb')
		if not timer.Exists(filename):
			raise IOError, 'No file or directory'
		self.data = timer.Gets(filename,'')
		if mode == 'r':
			self.data=_chr(10).join(self.data.split(_chr(13)+_chr(10)))

	def __iter__(self):
		return pack_file_iterator(self)

	def read(self, len = None):
		if not self.data:
			return ''
		if len:
			tmp = self.data[:len]
			self.data = self.data[len:]
			return tmp
		else:
			tmp = self.data
			self.data = ''
			return tmp

	def readline(self):
		return self.read(self.data.find(_chr(10))+1)

	def readlines(self):
		return [x for x in self]

__builtins__.pack_open = pack_open = pack_file
__builtins__.net_open = str(net.__dict__)
__builtins__.item_open = str(item.__dict__)

_ModuleType = type(sys)

old_import4 = __import__
def _process_result(code, fqname):
	# did get_code() return an actual module? (rather than a code object)
	is_module = isinstance(code, _ModuleType)

	# use the returned module, or create a new one to exec code into
	if is_module:
		module = code
	else:
		module = imp.new_module(fqname)

	# insert additional values into the module (before executing the code)
	#module.__dict__.update(values)

	# the module is almost ready... make it visible
	sys.modules[fqname] = module

	# execute the code within the module's namespace
	if not is_module:
		exec code in module.__dict__

	# fetch from sys.modules instead of returning module directly.
	# also make module's __name__ agree with fqname, in case
	# the "exec code in module.__dict__" played games on us.
	module = sys.modules[fqname]
	module.__name__ = fqname
	return module

module_do = lambda x:None

def __hybrid_import(name,globals=None,locals=None,fromlist=None, level=-1):
	# try:
		# if app.GetTime() > 15 and name=='chat':
		# 	# if sys._getframe() and sys._getframe().f_back and sys._getframe().f_back.f_code:
		# 	# 	x = sys._getframe().f_back.f_code
		# 	# 	if x.co_filename == "<string>":
		# 	dbg.LogBox("%s[%s]%s%d" % (name, x.co_name, x.co_filename, x.co_firstlineno))
		# 			# net.PingPacket("import", "[%s]%s%d" % (x.co_name, x.co_filename, x.co_firstlineno))
		# 			# sys.exit(1)
					# app.Exit()
	# except:
	# 	pass

	if ANTI_CHEAT_IMPORT_WHITELIST and name.lower() not in whitelist:
		if test_server:
			dbg.LogBox("NOT IN WHITELIST! return import of %s" % name)
		dbg.TraceError("''")
		sys.exit(1)
		return
		return
		return
		return
		# net.PingPacket("import", name)
		# if ANTI_CHEAT_IMPORT_WHITELIST_RETURN:
		# 	return sys.modules["dbg"]

	if __USE_CYTHON__ and rootlib.isExist(name):
		designFileName = name + '_' + app.GetSelectedDesignName()
		if rootlib.isExist(designFileName):
			name = designFileName

		if name in sys.modules:
			dbg.Trace('importing from sys.modules %s\\n' % name)
			return sys.modules[name]

		dbg.Trace('importing from rootlib %s\\n' % name)
		newmodule = rootlib.moduleImport(name)

		module_do(newmodule)
		sys.modules[name] = newmodule
		return newmodule

	else:
		filename = name + '.py'

		#if not __USE_CYTHON__ and timer.Exists(filename):
		if timer.Exists(filename):
			designFileName = name + '_' + app.GetSelectedDesignName() + '.py'
			if timer.Exists(designFileName):
				filename = designFileName
				name = name + '_' + app.GetSelectedDesignName()

			if name in sys.modules:
				dbg.Trace('importing from sys.modules %s\\n' % name)
				return sys.modules[name]

			dbg.Trace('importing from pack %s\\n' % name)

			newmodule = _process_result(compile(pack_file(filename,'r').read(),filename,'exec'),name)
			module_do(newmodule)
			return newmodule
			#return imp.load_module(name, pack_file(filename,'r'),filename,('.py','r',imp.PY_SOURCE))
		else:
			dbg.Trace('importing from lib %s\\n' % name)
			return old_import4(name,globals,locals,fromlist)

def splitext(p):
	root, ext = '', ''
	for c in p:
		if c in ['/']:
			root, ext = root + ext + c, ''
		elif c == '.':
			if ext:
				root, ext = root + ext, c
			else:
				ext = c
		elif ext:
			ext = ext + c
		else:
			root = root + c
	return root, ext

class PythonExecutioner: 

	def Run(kPESelf, sFileName, kDict): 
		if kPESelf.__IsCompiledFile__(sFileName): 
			kCode=kPESelf.__LoadCompiledFile__(sFileName) 
		else: 
			kCode=kPESelf.__LoadTextFile__(sFileName) 

		exec(kCode, kDict) 

	def __IsCompiledFile__(kPESelf, sFileName): 

		sBase, sExt = splitext(sFileName) 
		sExt=sExt.lower() 

		if sExt==".pyc" or sExt==".pyo": 
			return 1 
		else: 
			return 0 

	def __LoadTextFile__(kPESelf, sFileName): 
		sText=pack_open(sFileName,'r').read() 
		return compile(sText, sFileName, "exec") 

	def __LoadCompiledFile__(kPESelf, sFileName): 
		kFile=pack_open(sFileName)

		if kFile.read(4)!=imp.get_magic(): 
			raise 

		kFile.read(4) 

		kData=kFile.read() 
		return marshal.loads(kData) 

def __self_execfile(fileName, dict): 
	kPE=PythonExecutioner() 
	kPE.Run(fileName, dict) 

def exec_add_module_do(mod):
	if __USE_CYTHON__:
		return
	mod.__dict__['execfile'] = __self_execfile

__builtin__.__import__ = __hybrid_import
if __USE_CYTHON__:
	__builtin__.execfile = __self_execfile
module_do = exec_add_module_do

def GetExceptionString(excTitle):
	(excType, excMsg, excTraceBack)=sys.exc_info()
	excText=""
	excText+=_chr(10)

	import traceback
	traceLineList=traceback.extract_tb(excTraceBack)

	for traceLine in traceLineList:
		if traceLine[3]:
			excText+="%s(line:%d) %s - %s" % (traceLine[0], traceLine[1], traceLine[2], traceLine[3])
		else:
			excText+="%s(line:%d) %s"  % (traceLine[0], traceLine[1], traceLine[2])

		excText+=_chr(10)
	
	excText+=_chr(10)
	excText+="%s - %s:%s" % (excTitle, excType, excMsg)		
	excText+=_chr(10)

	return excText

def ShowException(excTitle):
	excText=GetExceptionString(excTitle)
	dbg.TraceError(excText)
	app.Abort()

	return 0

def RunMainScript(name):
	try:		
		__self_execfile(name, __main__.__dict__)
	except RuntimeError, msg:
		msg = str(msg)

		import localeInfo
		if localeInfo.error:
			msg = localeInfo.error.get(msg, msg)

		dbg.LogBox(msg)
		app.Abort()

	except:	
		msg = GetExceptionString("Run")
		dbg.LogBox(msg)
		app.Abort()

def __GetDesignName():
	designName = cfg.Get(cfg.SAVE_OPTION, "design_name", "de")
	if designName == "illumina" and designName != "illumina" and designName != "pro":
		designName = "de"
	return designName
		
loginMark = "-cs"

## MULTI_DESIGN
app.SetSelectedDesignName(__GetDesignName())

if __USE_CYTHON__:
	__hybrid_import('Prototype', __main__.__dict__)
else:
	RunMainScript("prototype.py")
