import logging
logging.basicConfig(filename = "list.log", level = logging.INFO, format = "%(asctime)s - %(levelname)s -  %(message)s")
class ls:
    """ls is a list class"""
    def __init__(self, ls):
        self.ls = ls
            
    def ls_not_list(self):
        """This function check whether the data is list class or not 
        if it is list type it will  return 1 or else it will give an error message"""
        if type(self.ls) != list:
            raise Exception("It is not list data type")
        else:
            return 1
    
    def ls_append(self, a):
        """Append function adds a element at the end of the list"""
        try:
            logging.info("It is a append function of list")
            if self.ls_not_list():
                self.ls.append(a)
                logging.info(f"After appending the value {a} then the list : {self.ls}")
        except Exception as e:
            logging.error("The Error has occured")
            logging.exception(f"The occured error is {e}")
    
    def ls_clear(self):
        """Clear function removes the all elements and return a empty list"""
        try : 
            logging.info("It is a clear function of list")
            if self.ls_not_list():
                self.ls.clear()
                logging.info(f"After clear the all values then the list : {self.ls}")
        except Exception as e:
            logging.error("The Error has occured")
            logging.exception(f"The occured error is {e}")
        
    def ls_extend(self, b):
        """Extend fucntion add the one or more elements at the end of the list"""
        try:
            logging.info("It is a extend function of list")
            if self.ls_not_list():
                self.ls.extend(b)
                logging.info(f"After extending the value {b} then the list : {self.ls}")
        except Exception as e:
            logging.error("The Error has occured")
            logging.exception(f"The occured error is {e}")
        
    def ls_count(self, c):
        """count function gives the number of times a specified element is occured"""
        try:
            logging.info("It is a count function of list")
            if self.ls_not_list():
                f = self.ls.count(c)
                logging.info(f"The count of value {c} in the list is : {f}")
        except Exception as e:
            logging.error("The Error has occured")
            logging.exception(f"The occured error is {e}")
        
    def ls_index(self, d):
        """Index function gives the index place of the specified element in the list"""
        try:
            logging.info("It is a index function of list")
            if self.ls_not_list():
                k = self.ls.index(d)
                logging.info(f"The index value of {d} is : {k}")
        except Exception as e:
            logging.error("The Error has occured")
            logging.exception(f"The occured error is {e}")
    
    def ls_insert(self, i, v):
        """By using insert function we can add a element or data value in required index place"""
        try:
            logging.info("It is a insert function of list")
            self.ls.insert(i, v)
            logging.info(f"Insert a value {v} in the index number {i} then the list : {self.ls}")
        except Exception as e:
            logging.error("The Error has occured")
            logging.exception(f"The occured error is {e}")
        
    def ls_pop(self):
        """ Pop function removes the last element of the list"""
        try:
            logging.info("It is a pop function of list")
            if self.ls_not_list():
                g = self.ls.pop()
                logging.info(f"Removing the last value in the list {g}")
        except Exception as e:
            logging.error("The Error has occured")
            logging.exception(f"The occured error is {e}")
        
    def ls_remove(self, j):
        """It removes the specified data value from the list"""
        try:
            logging.info("It is a remove function of list")
            if self.ls_not_list():
                logging.info(f"The current list is {self.ls}")
                self.ls.remove(j)
                logging.info(f"Final list is {self.ls}")
        except Exception as e:
            logging.error("The Error has occured")
            logging.exception(f"The occured error is {e}")
        
    def ls_reverse(self):
        """It reverse the entire list"""
        try:
            logging.info("It is a reverse function of list")
            if self.ls_not_list():
                self.ls.reverse()
                logging.info(f"The Reverse order of list is {self.ls}")
        except Exception as e:
            logging.error("The Error has occured")
            logging.exception(f"The occured error is {e}")
        
    def ls_sort(self):
        """Sort function arrange the elements in ascending order"""
        try:
            logging.info("It is a sort function of list")
            if self.ls_not_list():
                self.ls.sort()
                logging.info(f"After the sorting the list : {self.ls}")
        except Exception as e:
            logging.error("The Error has occured")
            logging.exception(f"The occured error is {e}")