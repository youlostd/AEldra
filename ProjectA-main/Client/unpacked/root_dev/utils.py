import dbg
import item
import player

def ItemIsSwitchable(item_vnum):
	"""
		Checks whether an specific item is available to switch.
		
		Parameters
		----------
		item_vnum: int
			Vnum of the specific item.

		Returns
		-------
		boolean
			True if the item is switchable, otherwise False.
	"""

	# List containing all item-types which can contain bonis.
	SWITCHABLE_ITEM_TYPES = [
		item.ITEM_TYPE_ARMOR,
		item.ITEM_TYPE_WEAPON,
		item.ITEM_TYPE_COSTUME,
		item.ITEM_TYPE_TOTEM,
	]

	# Select the specific item to use item-functions
	item.SelectItem(1, 2, item_vnum)

	return item.GetItemType() in SWITCHABLE_ITEM_TYPES

def ItemHasBonis(slot_index, bonis, precisely=False, window=player.SLOT_TYPE_INVENTORY):
	"""
		Checks whether an item got specific bonis.
		
		Parameters
		----------
		slot_index: int
			Number of the slot in the specific window.

		bonis: list
			Contains all the bonis that should be checked as tuples like [(bonus_index, bonus_value), ...].

		precisely: bool
			Indicates whether the bonus should be 'exactly' or just 'exactly or higher'.

		window: SLOT_TYPE
			Location of the item (slot_index).

		Returns
		-------
		bool
			True if the item has all given bonis, otherwise False.
	"""

	# get all attributes from the selected item
	attributes = [player.GetItemAttribute(window, slot_index, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]

	# validate size
	if len(attributes) != len(bonis):
		return False

	# sorting
	attributes.sort()
	bonis.sort()

	if not precisely:
		for i in xrange(len(bonis)):
			wanted_bonus, wanted_value = bonis[i]
			indeed_bonus, indeed_value = attributes[i]

			if wanted_bonus != indeed_bonus or wanted_value < indeed_value:
				return False

		return True

	return cmp(attributes, bonis)


#stolen from urllib	
always_safe = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'
				'abcdefghijklmnopqrstuvwxyz'
				'0123456789' '_.-')
_safe_map = {}
for i, c in zip(xrange(256), str(bytearray(xrange(256)))):
	_safe_map[c] = c if (i < 128 and c in always_safe) else '%{:02X}'.format(i)
_safe_quoters = {}

def quote(s, safe='/'):
	"""quote('abc def') -> 'abc%20def'

	Each part of a URL, e.g. the path info, the query, etc., has a
	different set of reserved characters that must be quoted.

	RFC 2396 Uniform Resource Identifiers (URI): Generic Syntax lists
	the following reserved characters.

	reserved    = ";" | "/" | "?" | ":" | "@" | "&" | "=" | "+" |
				"$" | ","

	Each of these characters is reserved in some component of a URL,
	but not necessarily in all of them.

	By default, the quote function is intended for quoting the path
	section of a URL.  Thus, it will not encode '/'.  This character
	is reserved, but in typical usage the quote function is being
	called on a path where the existing slash characters are used as
	reserved characters.
	"""
	# fastpath
	if not s:
		if s is None:
			raise TypeError('None object cannot be quoted')
		return s
	cachekey = (safe, always_safe)
	try:
		(quoter, safe) = _safe_quoters[cachekey]
	except KeyError:
		safe_map = _safe_map.copy()
		safe_map.update([(c, c) for c in safe])
		quoter = safe_map.__getitem__
		safe = always_safe + safe
		_safe_quoters[cachekey] = (quoter, safe)
	if not s.rstrip(safe):
		return s
	return ''.join(map(quoter, s))

def quote_plus(s, safe=''):
	"""Quote the query fragment of a URL; replacing ' ' with '+'"""
	if ' ' in s:
		s = quote(s, safe + ' ')
		return s.replace(' ', '+')
	return quote(s, safe)

print quote_plus('akflkj 2$%')