import dbg
import app
import localeInfo
import wndMgr
import systemSetting
import mouseModule
import networkModule
import constInfo
import musicInfo

def RunApp():
	musicInfo.LoadLastPlayFieldMusic()
	app.SetHairColorEnable(constInfo.HAIR_COLOR_ENABLE)
	app.SetArmorSpecularEnable(constInfo.ARMOR_SPECULAR_ENABLE)
	app.SetWeaponSpecularEnable(constInfo.WEAPON_SPECULAR_ENABLE)
	app.SetMouseHandler(mouseModule.mouseController)
	wndMgr.SetMouseHandler(mouseModule.mouseController)
	wndMgr.SetScreenSize(systemSetting.GetWidth(), systemSetting.GetHeight())
	try:
		app.Create(localeInfo.APP_TITLE, systemSetting.GetWidth(), systemSetting.GetHeight(), 1)
	except RuntimeError, msg:
		msg = str(msg)
		if "CREATE_DEVICE" == msg:
			dbg.LogBox("Sorry, Your system does not support 3D graphics,\r\nplease check your hardware and system configeration\r\nthen try again.")
		else:
			dbg.LogBox("Metin2.%s" % msg)
		return
	app.SetCamera(1500.0, 30.0, 0.0, 180.0)
	mouseModule.mouseController.Create()
	mainStream = networkModule.MainStream()
	mainStream.Create()	
	mainStream.SetLoginPhase()
	app.Loop()
	mainStream.Destroy()

RunApp()