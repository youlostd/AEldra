import app

AUTOBAN_QUIZ_ANSWER = "ANSWER"
AUTOBAN_QUIZ_REFRESH = "REFRESH"
AUTOBAN_QUIZ_REST_TIME = "REST_TIME"

OPTION_SHADOW = "SHADOW"

#CUBE_TITLE = "Cube Window"

def LoadLocaleFile(srcFileName, localeDict):
	try:
		lines = pack_open(srcFileName, "r").readlines()
	except IOError:
		import dbg
		dbg.LogBox("LoadUIScriptLocaleError(%(srcFileName)s)" % locals())
		app.Abort()

	for line in lines:
		tokens = line[:-1].split("\t")
		
		if len(tokens) >= 2:
			localeDict[tokens[0]] = tokens[1]			
		else:
			print len(tokens), lines.index(line), line

		name = app.GetLocalePath()
	else:
		name = "locale/ymir"

base_name = app.GetLocaleBasePath()
default_name = app.GetDefaultLocalePath()
name = app.GetLocalePath()

IMG_LANG_EXTENSION = "_%s" % app.GetShortLanguageName(app.GetLanguage())
if app.GetLanguage() == app.LANG_GERMAN:
	IMG_LANG_EXTENSION = ""

LOCALE_UISCRIPT_PATH = "%s/ui/" % (base_name)
LOGIN_PATH = "%s/ui/login/" % (base_name)
EMPIRE_PATH = "%s/ui/empire/" % (base_name)
GUILD_PATH = "%s/ui/guild/" % (base_name)
SELECT_PATH = "%s/ui/select/" % (base_name)
WINDOWS_PATH = "%s/ui/windows/" % (base_name)
MAPNAME_PATH = "%s/ui/mapname/" % (base_name)

JOBDESC_WARRIOR_PATH = "%s/jobdesc_warrior.txt" % (name)
JOBDESC_ASSASSIN_PATH = "%s/jobdesc_assassin.txt" % (name)
JOBDESC_SURA_PATH = "%s/jobdesc_sura.txt" % (name)
JOBDESC_SHAMAN_PATH = "%s/jobdesc_shaman.txt" % (name)
# JOBDESC_WOLFMAN_PATH = "%s/jobdesc_wolfman.txt" % (name)

EMPIREDESC_A = "%s/empiredesc_a.txt" % (name)
EMPIREDESC_B = "%s/empiredesc_b.txt" % (name)
EMPIREDESC_C = "%s/empiredesc_c.txt" % (name)

DEFAULT_LOCALE_INTERFACE_FILE_NAME = "%s/locale_interface.txt" % (default_name)
LOCALE_INTERFACE_FILE_NAME = "%s/locale_interface.txt" % (name)

if DEFAULT_LOCALE_INTERFACE_FILE_NAME != LOCALE_INTERFACE_FILE_NAME:
	LoadLocaleFile(DEFAULT_LOCALE_INTERFACE_FILE_NAME, locals())
LoadLocaleFile(LOCALE_INTERFACE_FILE_NAME, locals())

def GetLocals():
	return globals()
