from exceptions import ResourceNotFoundException
from abc import ABC, abstractmethod	

class KVStoreABS(ABC):
	@abstractmethod
	def getValue(self,key):
		pass

	@abstractmethod
	def putValue(self, key, value):
		pass


class KVStore(KVStoreABS):
	def __init__(self):
		self.store = {}
	
	def getValue(self, key):
		val = self.store.get(key)
		return val

	def putValue(self, key, value):
		self.store[key] = value
