from abc import ABC, abstractmethod

class Connector(ABC):
      
    @abstractmethod     
    def connect(self):
        return 'Connect'
    
    @abstractmethod
    def disconnect(self):
        return 'Diconnect'


    def create(self):
        return 'Create'
    

    def read(self):
        return 'Read'

    
    def update(self):
        return 'Update'
    
    
    def delete(self):
        return 'Delete'