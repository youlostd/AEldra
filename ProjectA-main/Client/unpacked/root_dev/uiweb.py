import ui
import uiScriptLocale
import net
import snd
import app
import mouseModule
import constInfo
import uiCommon
import localeInfo
import cfg

class WebLoadingWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/WebLoadingWindow.py")
		except:
			import exception
			exception.Abort("WebLoadingWindow.LoadDialog.LoadScript")

		try:
			GetObject=self.GetChild
			self.board = GetObject("board")

		except:
			import exception
			exception.Abort("WebLoadingWindow.LoadDialog.BindObject")

		self.board.SetCloseEvent(ui.__mem_func__(self.Close))

	def Destroy(self):
		self.Close()
		ui.ScriptWindow.Destroy(self)

	def Open(self):
		self.SetCenterPosition()
		self.Show()
		self.SetTop()

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True

def GetWebWindowSize(wndWidth, wndHeight):
	return wndWidth - 16 - 23, wndHeight - 59 - 13

class WebWindow(ui.ScriptWindow):

	VOTE_FINISH_URL = "https://www.metin2pserver.info/out.php"

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.oldPos = None
		self.loadingWnd = WebLoadingWindow()
		self.loadingWnd.Close()
		self.closeTimeout = 0
		self.urlType = ""
		self.onReadyJavascript = ""

		self.questionDlg = uiCommon.QuestionDialog()
		self.questionDlg.SetText(localeInfo.WANT_NOT_VOTE_AGAIN_TODAY)
		self.questionDlg.SetAcceptText(localeInfo.NOT_VOTE_AGAIN_TODAY)
		self.questionDlg.SetCancelText(localeInfo.WANT_VOTE_AGAIN_TODAY)
		self.questionDlg.SetAcceptEvent(ui.__mem_func__(self.__OnClickQuestionAccept))
		self.questionDlg.SetCancelEvent(ui.__mem_func__(self.__OnClickQuestionCancel))
		self.questionDlg.Close()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self, pyFile = "UIScript/WebWindow.py"):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, pyFile)
		except:
			import exception
			exception.Abort("WebWindow.LoadDialog.LoadScript")

		try:
			GetObject=self.GetChild
			self.board = GetObject("board")
			self.wndRender = GetObject("webrender")

		except:
			import exception
			exception.Abort("WebWindow.LoadDialog.BindObject")

		self.board.SetCloseEvent(ui.__mem_func__(self.__OnCloseButtonClick))

		self.wndRender.SetMouseLeftButtonDownEvent(ui.__mem_func__(self.OnMouseLeftButtonDown))
		self.wndRender.SetMouseLeftButtonUpEvent(ui.__mem_func__(self.OnMouseLeftButtonUp))

	def Destroy(self):
		app.HideWebPage()
		self.ClearDictionary()
		self.board = None
		ui.ScriptWindow.Destroy(self)

	def GetWindowSize(self):
		return self.wndRender.GetWidth(), self.wndRender.GetHeight()

	def SetTitle(self, title):
		self.board.SetTitleName(title)

	def Open(self, url):
		self.urlType = constInfo.GET_URL_TYPE(url)
		self.onReadyJavascript = ""

# 		if self.urlType == "m2pserverinfo":
# 			self.onReadyJavascript = '''

# // CSS Hook
# var fileref = document.createElement("link");
# fileref.rel = "stylesheet";
# fileref.type = "text/css";
# fileref.href = "https://%s/css/IngameVoteHook.css" % constInfo.DOMAIN;
# fileref.id = "unique_id_idk";
# fileref.media = "all";
# document.getElementsByTagName("head")[0].appendChild(fileref);

# // JS Minifier
# (function() {
#     var script = document.createElement("SCRIPT");
#     script.src = 'https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js';
#     script.type = 'text/javascript';
#     script.onload = function() {
#         var $ = window.jQuery;
#         console.log($('body').html());
#         $('table').first().remove();
#         $('td').first().remove();
#         console.log($('body').html());
#     };
#     document.getElementsByTagName("head")[0].appendChild(script);
# })();


# '''

		self.closeTimeout = 0
		self.SetCenterPosition()
		sx, sy = self.wndRender.GetGlobalPosition()
		if constInfo.NEW_WEBBROWSER:
			ex, ey = sx + self.wndRender.GetWidth(), sy + self.wndRender.GetHeight()
			app.SetWebEventHandler(self)
			app.ShowWebPage(url, (sx, sy, ex, ey), constInfo.GET_URL_TYPE(url), self, "BINARY_RealOpen")
			self.loadingWnd.Open()
		else:
			self.Refresh()
			self.Show()
			sx, sy = x + 16, y + 35
			ex, ey = sx + self.GetWidth() - 16 - 23, sy + self.GetHeight() - 35 - 10
			app.ShowWebPage(url, (sx, sy, ex, ey))

	def BINARY_RealOpen(self):
		self.Refresh()
		self.Show()
		self.loadingWnd.Close()

	def CloseLoading(self):
		self.loadingWnd.Close()

	def Close(self):
		app.HideWebPage()
		app.KillWebPageFocus()
		self.Hide()
		self.loadingWnd.Close()

		if self.urlType == "m2pserverinfo":
			if self.closeTimeout == 0:
				self.questionDlg.Open()
			else:
				net.SendVoteSuccessPacket()
				self.closeTimeout = 0

	def __OnClickQuestionAccept(self):
		cfg.Set(cfg.SAVE_GENERAL, "vote_disable_day", str(app.GetDayOfYear()))
		self.questionDlg.Close()

	def __OnClickQuestionCancel(self):
		self.questionDlg.Close()

	def Clear(self):
		self.Refresh()

	def Refresh(self):
		pass

	def __OnCloseButtonClick(self):
		self.Close()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	## WEB_EVENTS
	def OnMouseLeftButtonDown(self):
		if app.ENABLE_WEB_OFFSCREEN:
			if self.wndRender.IsIn():
				app.CallWebEvent(app.EVENT_MOUSE_LEFT_DOWN)

	def OnMouseLeftButtonUp(self):
		if app.ENABLE_WEB_OFFSCREEN:
			if self.wndRender.IsIn():
				app.CallWebEvent(app.EVENT_MOUSE_LEFT_UP)

	def OnMouseWheel(self, num):
		if app.ENABLE_WEB_OFFSCREEN:
			if self.wndRender.IsIn():
				app.CallWebEvent(app.EVENT_MOUSE_WHEEL, num)
				return True

	def WebOnChangeTargetURL(self, newAddress):
		if self.IsShow():
			if newAddress.find(self.VOTE_FINISH_URL) != -1:
				self.closeTimeout = app.GetTime() + 1.5

	def WebOnDocumentReady(self, url):
		if self.onReadyJavascript != "":
			app.WebExecuteJavascript(self.onReadyJavascript)
			self.onReadyJavascript = ""

		widthDiffer = self.GetWidth() - self.wndRender.GetWidth()
		heightDiffer = self.GetHeight() - self.wndRender.GetHeight()

		if test_server:
			newWidth, newHeight = app.WebGetWindowSize()
			import dbg
			dbg.TraceError("width %d height %d" % (newWidth, newHeight))

#		app.WebResize((sx, sy, ex, ey), constInfo.GET_URL_TYPE(url), self, "BINARY_RealOpen")
	## END_OF_WEB_EVENTS

	def OnUpdate(self):
		if self.closeTimeout != 0 and app.GetTime() >= self.closeTimeout:
			self.Close()
			return

		if self.wndRender.IsIn():
			mouseX, mouseY = self.wndRender.GetMouseLocalPosition()
			if mouseX < 0 or mouseX >= self.wndRender.GetWidth() or mouseY < 0 or mouseY >= self.wndRender.GetHeight():
				return

			app.CallWebEvent(app.EVENT_MOUSE_MOVE, mouseX, mouseY)

		newPos = self.wndRender.GetGlobalPosition()
		if newPos == self.oldPos:
			return

		self.oldPos = newPos

		sx, sy = newPos
		ex, ey = sx + self.wndRender.GetWidth(), sy + self.wndRender.GetHeight()
		app.MoveWebPage((sx, sy, ex, ey))

	def OnAfterRender(self):
		if app.ENABLE_WEB_OFFSCREEN:
			newPos = self.wndRender.GetGlobalPosition()
			if newPos != self.oldPos:
				self.oldPos = newPos

				sx, sy = newPos
				ex, ey = sx + self.wndRender.GetWidth(), sy + self.wndRender.GetHeight()
				app.MoveWebPage((sx, sy, ex, ey))

			app.RenderWebPage()
