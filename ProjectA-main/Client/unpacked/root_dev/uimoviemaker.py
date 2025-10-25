import ui, chat, net, player, app, math, os, chr, background, cfg

class MovieMakerWindow(ui.ScriptWindow):

	SAVE_FILE_NAME = "Camera\\%s.txt"

	STATE_NONE = 0
	STATE_PLAY = 1
	STATE_MOVIE = 2

	def __init__(self, interface=None):
		ui.ScriptWindow.__init__(self)
		app.SetCamyActivityState(1)
		self.interface = interface
		self.Objects = []
		self.objectIdx = 0
		self.fileName = 'Camera_Objects.txt'
		self.state = self.STATE_NONE
		self.timeStart = 0
		self.__LoadDialog()
		self.Load()
		self.lastRota = 0.0

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadDialog(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/moviemaker.py")
		except:
			import exception
			exception.Abort("MovieMakerWindow.LoadDialog.LoadObject")

		try:
			GetObject = self.GetChild
			self.board = GetObject("board")
			self.currentLabel = GetObject("objects_lbl")
			self.lastBtn = GetObject("pos_left_btn")
			self.nextBtn = GetObject("pos_right_btn")
			self.editWnd = GetObject("editWnd")
			self.editInput = GetObject("edit_input")
			self.editBtn = GetObject("edit_save_btn")
			self.deleteBtn = GetObject("remove_btn")
			self.addInput = GetObject("add_input")
			self.addBtn = GetObject("add_btn")
			self.playBtn = GetObject("play_sel_btn")
			self.movieBtn = GetObject("play_all_btn")

			self.lastBtn.SetEvent(ui.__mem_func__(self.__OnSwitchPos), -1)
			self.nextBtn.SetEvent(ui.__mem_func__(self.__OnSwitchPos), 1)
			self.editBtn.SetEvent(ui.__mem_func__(self.__OnEdit))
			self.deleteBtn.SetEvent(ui.__mem_func__(self.__OnRemove))
			self.addBtn.SetEvent(ui.__mem_func__(self.__OnAdd))
			self.playBtn.SetEvent(ui.__mem_func__(self.__OnPlayCurrent))
			self.movieBtn.SetEvent(ui.__mem_func__(self.__OnPlayMovie))

			self.editInput.SetEscapeEvent(ui.__mem_func__(self.OnPressEscapeKey))
			self.addInput.SetEscapeEvent(ui.__mem_func__(self.OnPressEscapeKey))

		except:
			import exception
			exception.Abort("MovieMakerWindow.LoadDialog.GetChilds")

	def Close(self):
		app.SetDefaultCamera()
		self.Hide()

	def OnPressEscapeKey(self):
		if self.state == self.STATE_NONE:
			self.editInput.KillFocus()
			self.addInput.KillFocus()
			self.Close()
			return True
		else:
			self.StopMovie()
			return False
			
	def Destroy(self):
		self.Close()
		ui.ScriptWindow.Destroy(self)

	def __GetObjectData(self, obj):
		return obj["x"], obj["y"], obj["z"], obj["zoom"], obj["rotation"], obj["pitch"], obj["time"]

	def __MakeObjectData(self, x, y, z, zoom, rotation, pitch, time):
		return {
			"x" : float(x),
			"y" : float(y),
			"z" : float(z),
			"zoom" : float(zoom),
			"rotation" : float(rotation),
			"pitch" : float(pitch),
			"time" : float(time),
		}

	def __SetCameraPointByObject(self, obj):
		apply(self.__SetCameraPoint, (self.__GetObjectData(obj)))
		self.__RefreshCameraPoint(True)

	def __SetCameraPointByTimePct(self, obj1, obj2, timePct):
		x = obj1["x"] + (obj2["x"] - obj1["x"]) * timePct
		y = obj1["y"] + (obj2["y"] - obj1["y"]) * timePct
		z = obj1["z"] + (obj2["z"] - obj1["z"]) * timePct		
		zoom = obj1["zoom"] + (obj2["zoom"] - obj1["zoom"]) * timePct		
		rot1 = obj1["rotation"]
		rot2 = obj2["rotation"]
		if abs(rot2 - (rot1 + 360)) < abs(rot2 - rot1):
			rot1 += 360
		elif abs(rot2 + 360 - rot1) < abs(rot2 - rot1):
			rot2 += 360
		rotation = rot1 + (rot2 - rot1) * timePct
		if rotation >= 360:
			rotation -= 360
		
		pitch = obj1["pitch"] + (obj2["pitch"] - obj1["pitch"]) * timePct
		
		self.__SetCameraPoint(x, y, z, zoom, rotation, pitch)
		self.__RefreshCameraPoint(True)

	def __SetCameraPoint(self, x, y, z, zoom, rotation, pitch, time=0):
		self.curX = x
		self.curY = y
		self.curZ = z
		self.curZoom = zoom
		self.curRotation = rotation
		self.curPitch = pitch

	def __GetZoom(self, forceCurrent=False):
		if self.state != self.STATE_NONE or forceCurrent:
			return self.curZoom

		zoom, pitch, rotation, destHeight = app.GetCamera()
		return zoom

	def __GetRotation(self, forceCurrent=False):
		if self.state != self.STATE_NONE or forceCurrent:
			return self.curRotation

		zoom, pitch, rotation, destHeight = app.GetCamera()
		return rotation

	def __GetPitch(self, forceCurrent=False):
		if self.state != self.STATE_NONE or forceCurrent:
			return self.curPitch

		zoom, pitch, rotation, destHeight = app.GetCamera()
		return pitch

	def __RefreshCameraPoint(self, forceCurrent=False):
		rota = self.__GetRotation(forceCurrent)
		app.SetCameraSetting(self.curX, self.curY, self.curZ, self.__GetZoom(forceCurrent), rota, self.__GetPitch(forceCurrent))
		# chr.SetPixelPosition(self.curX, self.curY, self.curZ)

	def __OnSwitchPos(self, plus):
		nextIdx = self.objectIdx + plus
		if nextIdx >= 0 and nextIdx <= len(self.Objects)-1:
			self.objectIdx += plus
		self.SetCamActual()
		
	def SetCamActual(self):
		if not len(self.Objects):
			return
		obj = self.Objects[self.objectIdx]
		self.__SetCameraPointByObject(obj)
		
	def __OnEdit(self):
		try:
			self.Objects[self.objectIdx] = self.__MakeObjectData(self.curX, self.curY, self.curZ, self.__GetZoom(), self.__GetRotation(), self.__GetPitch(), self.editInput.GetText())
		except:
			import dbg
			dbg.LogBox("Please enter a number like 2 or 1.51255 which means 1,5 seconds.")
		self.editInput.KillFocus()
		self.addInput.KillFocus()
		self.Save()

	def __OnRemove(self):
		if not len(self.Objects):
			return
		del self.Objects[self.objectIdx]
		if self.objectIdx > 0 and self.objectIdx >= len(self.Objects):
			self.objectIdx -= 1
			
		tmp = self.Objects
		self.Objects.clear()
		for key, val in tmp.iteritems():
			self.Objects[str(len(self.Objects))] = val
			
		self.editInput.KillFocus()
		self.addInput.KillFocus()
		self.Save()
		self.SetCamActual()

	def __OnAdd(self):
		try:
			self.Objects.append(self.__MakeObjectData(self.curX, self.curY, self.curZ, self.__GetZoom(), self.__GetRotation(), self.__GetPitch(), self.addInput.GetText()))
			if self.objectIdx+1 < len(self.Objects):
				self.objectIdx += 1
		except:
			import dbg
			dbg.LogBox("Please enter a number like 1.51255 which means 1,5 seconds.")
		self.editInput.KillFocus()
		self.addInput.KillFocus()
		self.Save()

	def __OnPlayCurrent(self):
		if len(self.Objects) < 2:
			chat.AppendChat(1, "You need at least 2 saved objects.")
			return
		self.state = self.STATE_PLAY
		self.timeStart = app.GetTime()

	def __OnPlayMovie(self):
		if len(self.Objects) < 2:
			chat.AppendChat(1, "You need at least 2 saved objects.")
			return
		self.objectIdx = 0
		self.state = self.STATE_MOVIE
		self.timeStart = app.GetTime()
		#self.SavePosition()
		self.SetPosition(-500,0)
		self.interface.HideAllWindows()

	def StopMovie(self):
		self.state = self.STATE_NONE
		#self.LoadPosition()
		self.interface.ShowAllWindows()

	def Open(self):
		self.SetCenterPosition()
		self.SetTop()
		self.curX, self.curY, self.curZ, self.curZoom, self.curRotation, self.curPitch = app.GetCameraSettingNew()
		self.__RefreshCameraPoint()
		self.SetCamActual()
		self.Show()
		self.Refresh()
		chat.AppendChat(1, "Control with Numpad keys.")
		chat.AppendChat(1, "8 Foreward, 2 Backwards, 4 Left, 6 Right")
		chat.AppendChat(1, "7 Up, 9 Down")
		chat.AppendChat(1, "5 faster movement, 5+0 ultra movement")

	def Refresh(self):
		if not len(self.Objects):
			self.currentLabel.SetText("No Objects")
			self.editWnd.Hide()
			return
		if not self.editWnd.IsShow():
			self.editWnd.Show()
		self.currentLabel.SetText("%i/%i" % (self.objectIdx+1, len(self.Objects)))
		self.editInput.SetText(str(self.Objects[self.objectIdx]["time"]))

	def writeList(self, list, filename, sep='	'):
		with open(filename, "w+") as f:
			for obj in list:
				s = ""
				for key in obj:
					s += str(key) + sep + str(obj[key]) + sep
				f.write(s[:-1] + "\n")

	def readList(self, filename, sep='	'):
		with open(filename, "r") as f:
			list = []
			for line in f:
				values = line.split(sep)
				dict = {}
				try:
					for i in xrange(len(values) / 2):
						key = values[i * 2]
						val = values[i * 2 + 1]
						dict[key] = float(val)
				except:
					import dbg
					dbg.TraceError("Error Loading Floating Dict values")
				list.append(dict)
			return(list)

	def __GetMapName(self):
		mapName = background.GetCurrentMapName()
		if mapName.rfind("/") != -1:
			mapName = mapName[mapName.rfind("/")+1:]
		return mapName

	def Save(self):
		if not os.path.isdir("Camera"):
			os.makedirs("Camera")
		self.writeList(self.Objects, self.SAVE_FILE_NAME % self.__GetMapName())

	def Load(self):
		if os.path.isfile(self.SAVE_FILE_NAME % self.__GetMapName()):
			self.Objects = self.readList(self.SAVE_FILE_NAME % self.__GetMapName())

	def OnUpdate(self):
		self.Refresh()
		factor = 1.0
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL) or app.IsPressed(app.DIK_NUMPAD5):
			factor = 10.0
			if app.IsPressed(app.DIK_LSHIFT) or app.IsPressed(app.DIK_RSHIFT) or app.IsPressed(app.DIK_NUMPAD0):
				factor = 50.0
		moveChange = 0
		moveDir = "none"
		moveX = 0.0
		moveY = 0.0
		if app.IsPressed(app.DIK_NUMPAD4):
			moveChange = -6.0 * factor
			moveDir = "x"
		if app.IsPressed(app.DIK_NUMPAD6):
			moveChange = 6.0 * factor
			moveDir = "x"
		if app.IsPressed(app.DIK_NUMPAD2):
			moveChange = -6.0 * factor
			moveDir = "y"
		if app.IsPressed(app.DIK_NUMPAD8):
			moveChange = 6.0 * factor
			moveDir = "y"
		if app.IsPressed(app.DIK_PGUP) or app.IsPressed(app.DIK_NUMPAD9):
			self.MoveZ(6.0 * factor)
		if app.IsPressed(app.DIK_PGDN) or app.IsPressed(app.DIK_NUMPAD7):
			self.MoveZ(-6.0 * factor)

		if moveChange != 0.0:
			realRot = self.__GetRotation()
			if moveDir == "y":
				realRot = -realRot
			rot = abs(realRot)
			if rot < 90:
				newMoveX = moveChange * ((90 - rot) / 90.0)
				newMoveY = (-moveChange) * (rot / 90.0)
			else:
				newMoveX = (-moveChange) * ((rot - 90.0) / 90.0)
				newMoveY = (-moveChange) * ((180 - rot) / 90.0)

			if realRot < 0:
				newMoveY = -newMoveY

			if moveDir == "y":
				tmp = newMoveX
				newMoveX = newMoveY
				newMoveY = tmp

			self.MoveX(newMoveX)
			self.MoveY(newMoveY)
		elif moveY != 0.0:
			realRot = self.__GetRotation()
			rot = abs(realRot)

			if rot < 90:
				newMoveX = moveY * ((90 - rot) / 90.0)
				newMoveY = (-moveY) * (rot / 90.0)
			else:
				newMoveX = (-moveY) * ((rot - 90.0) / 90.0)
				newMoveY = moveY * ((180 - rot) / 90.0)

			if realRot < 0:
				newMoveX = -newMoveX

			self.MoveX(newMoveX)
			self.MoveY(newMoveY)

		newRota = self.__GetRotation()
		if newRota != self.lastRota:
			self.lastRota = newRota

	def GetDistance(self, p1, p2):
		return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)

	def OnRender(self):
		if self.state != self.STATE_NONE:
			if self.objectIdx+1 >= len(self.Objects):
				self.state = self.STATE_NONE
				return
			objStart = self.Objects[self.objectIdx]
			objEnd = self.Objects[self.objectIdx+1]
			timeDif = float(app.GetTime() - self.timeStart)
			pct = float(timeDif / objEnd["time"])
			if pct >= 1.0:
				while pct >= 1.0:
					timeDif -= objEnd["time"]
					self.timeStart = app.GetTime()
					self.objectIdx += 1
					objStart = self.Objects[self.objectIdx]
					if self.objectIdx+1 >= len(self.Objects) or self.state == self.STATE_PLAY:
						self.__SetCameraPointByObject(objStart)
						if self.state == self.STATE_MOVIE:
							self.StopMovie()
						self.state = self.STATE_NONE
						return
					else:
						objEnd = self.Objects[self.objectIdx+1]
						pct = timeDif / objEnd["time"]

			self.__SetCameraPointByTimePct(objStart, objEnd, pct)

	def MoveX(self, x):
		self.curX += x
		self.__RefreshCameraPoint()

	def MoveY(self, y):
		self.curY += y
		self.__RefreshCameraPoint()

	def MoveZ(self, z):
		self.curZ += z
		self.__RefreshCameraPoint()
