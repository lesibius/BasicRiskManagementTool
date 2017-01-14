# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 21:00:07 2017

@author: clem
"""

class Security:
    
    """
    The Security class is the basis class on which all securities in the program are modelled.
    
    It can be seen as an abstract class for securities, and as such, it should be avoided to
    use Security instances.
    """    
    
    def __init__(self,sid,name):
        
        """
        Parameters
        ----------
        sid: str
            ID of the Security (e.g. it's ISIN)
        name: str
            Name of the security
            
        Returns
        -------
        type: Security
            A new instance of Security
        """
        self.ID = sid
        self.Name = name
        
    def __str__(self):
        
        """
        Provide a str representation of the Security instance
        
        The user should override this method for different implementation of the abstract 
        Security class
        
        Parameters
        ----------
        None
        
        Returns
        -------
        type: str
            A string representation of the Security
        """