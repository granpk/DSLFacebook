__author__ = 'Joao'


import SolFB._FacebookUser as _User


class Experience:
     def __init__(self, id="",dictionary=dict()):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/experience/
         '''
         self.id=id
         self.description=""
         self.from_=""
         self.name=""
         self.with_=list()
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("description" in dictionary):
             self.description=dictionary["description"]
         if ("from" in dictionary):
             self.from_=_User.FacebookUser(dictionary= dictionary["from"])
         if ("name" in dictionary):
             self.name=dictionary["name"]
         if ("with" in dictionary):
             for user in dictionary["with"]:
                self.with_.append(_User.FacebookUser(dictionary=dictionary["with"]))


     def __str__(self):
         #print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "EXPERIENCE: "+str(dict)
