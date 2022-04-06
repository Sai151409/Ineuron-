import logging
logging.basicConfig(filename = "dict.log", level = logging.INFO, format = "%(asctime)s - %(levelname)s - %(message)s")

class d_p:
    """d_p is a dictionary class"""
    def __init__(self, d):
        self.d = d
    def not_dict(self):
        if type(self.d) != dict:
            raise Exception(self.d, "It is not a dictionary")
        else:
            return 1
    
    def dp_clear(self):
        try:
            if self.not_dict():
                self.d.clear()
                logging.info(f"After clear the all values from the dict : {self.d}")
        except Exception as e:
            logging.error("The Error has occured")
            logging.exception(f"The occured error is {e}")  
    
    def dp_copy(self):
        try:
            if self.not_dict():
                logging.info("Copy the entire dictionary and assing to another variable")
                return self.d
        except Exception as e:
            logging.error("The Error has occured")
            logging.exception(f"The occured error is {e}")
            
            
    def dp_get(self, k):
        try:
            if self.not_dict():
                logging.info(f"The value of {k} : {self.d.get(k)}" )
        except Exception as e:
            logging.error("The Error has occured")
            logging.exception(f"The occured error is {e}")
    
    def dp_items(self):
        try:
            if self.not_dict():
                logging.info(f"List of keys and values of dictionary : {self.d.items()}")
        except Exception as e:
            logging.error("The Error has occured")
            logging.exception(f"The occured error is {e}")
            
            
    def dp_keys(self):
        try:
            if self.not_dict():
                logging.info(f"The keys of dictionary : {self.d.keys()}" )
        except Exception as e:
            logging.error("The Error has occured")
            logging.exception(f"The occured error is {e}")
    
    def dp_pop(self, e):
        try:
            if self.not_dict():
                logging.info(f"Remove the specified key {e} and value {self.d[e]} in dict" )
                self.d.pop(e)
                logging.info(f"The final dict is : {self.d}")
        except Exception as e:
            logging.error("The Error has occured")
            logging.exception(f"The occured error is {e}")
        
        
    def dp_popitem(self):
        try:
            if self.not_dict():
                logging.info(f"It removes the last element of dict" )
                self.d.popitem()
                logging.info(f"The final dict is : {self.d}")
        except Exception as e:
            logging.error("The Error has occured")
            logging.exception(f"The occured error is {e}")  
    
    def dp_setdefault(self, key, default = None):
        try:
            if self.not_dict():
                logging.info("if key is not dict, by default it will add a required key and value")
                self.d.setdefault(key, default)
                logging.info(f"The final dict is : {self.d}")
        except Exception as e:
                logging.error("The Error has occured")
                logging.exception(f"The occured error is {e}")
        
    def dp_update(self, key, value):
        try:
            if self.not_dict():
                self.d.update({key : value})
                logging.info(f"After Updating the dictionary {self.d}")
        except Exception as e:
            logging.error("The Error has occured")
            logging.exception(f"The occured error is {e}")
                             
    def dp_values(self):
        try:
            if self.not_dict():
                logging.info(f"The values of dictionary : {self.d.values()}" )
        except Exception as e:
            logging.error("The Error has occured")
            logging.exception(f"The occured error is {e}")