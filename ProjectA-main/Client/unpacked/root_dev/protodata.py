import app
import player
import item

ATTRTREE = "attrtree"

## loader
class ProtoLoader():

	def init(self):
		self.data = {}

		# load protos
		self.__LoadAttrTree("%s/attrtree.txt" % app.GetLocaleBasePath())

	def __LoadAttrTree(self, srcFileName):
		data = {}
		self.data[ATTRTREE] = data

		try:
			lines = pack_open(srcFileName, "r").readlines()
		except IOError:
			import dbg
			dbg.LogBox("LoadAttrtreeError(%s)" % srcFileName)
			app.Abort()

		lineIndex = 1
		for line in lines:
			try:
				tokens = line.replace("\n", "").split("\t")
				if len(tokens) >= 4:
					row = int(tokens[0]) - 1
					col = int(tokens[1]) - 1
					apply_type = item.GetApplyTypeByName(tokens[2])
					max_apply_value = int(tokens[3])

					insertData = {"type" : apply_type, "value" : max_apply_value}
					if data.has_key(row):
						data[row][col] = insertData
					else:
						data[row] = {col : insertData}
				else:
					raise RuntimeError, "Unknown TokenSize"

				lineIndex += 1
			except:
				import dbg
				dbg.LogBox("%s: line(%d): %s" % (srcFileName, lineIndex, line), "Error")
				raise

loader = ProtoLoader()
loader.init()

def Get(name):
	if loader.data.has_key(name):
		return loader.data[name]

	import dbg
	dbg.TraceError("protoData : cannot get by name [%s]" % name)
	return None
