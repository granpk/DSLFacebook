__author__ = 'Joao'
from SolTw import _WeakAccess as _WeakAccess
from SolTw import  _StrongAccess as _StrongAccess
from SolTw import  _Actions as _Actions
from SolTw import  _Entity as _Entity
from SolTw import  _TwitterUser as _TwitterUser
from  SolTw import  _Contributor as _Contributor
from  SolTw import  _Utils as _Utils
from  SolTw import _Coordinates as _Coordinates
from SolTw import  _Place as _Place
import lib.tweepy as tweepy
class Tweet:
     def __init__(self,id="", dictionary=dict()):

         dictionary= _Utils.CastToDictionary(dictionary)
         dictionary= _Utils.removeEmptyFields(dictionary)
         self.annotations=""
         self.contributors=list()
         self.coordinates=""
         self.created_at=""
         self.current_user_retweet=""
         self.entities=""
         self.favorite_count=""
         self.favorited=""
         self.filter_level=""
         self.id=id
         self.id_str=""
         self.in_reply_to_screen_name=""
         self.lang=""
         self.place=""
         self.possibly_sensitive=""
         self.quoted_status_id=""
         self.quoted_status_id_str=""
         self.quoted_status=""
         self.scopes=""
         self.retweet_count=""
         self.retweeted=""
         self.retweeted_status=""
         self.source=""
         self.text=""
         self.truncated=""
         self.user=""
         self.withheld_copyright=""
         self.withheld_in_countries=""
         self.withheld_scope=""
         if ("annotations" in dictionary):
             self.annotations=dictionary["annotations"]
         if ("contributors" in dictionary):
             for cont in dictionary["contributors"]:
                self.contributors.append(_Contributor.Contributor(dictionary=cont))
         if ("coordinates" in dictionary):
             self.coordinates= _Coordinates.Coordinates(dictionary=dictionary["coordinates"])
         if ("created_at" in dictionary):
             self.created_at=dictionary["created_at"]
         if ("current_user_retweet" in dictionary):
             self.current_user_retweet=dictionary["current_user_retweet"]
         if ("entities" in dictionary):
             self.entities= _Entity.Entity(dictionary=dictionary["entities"])
         if ("favorite_count" in dictionary):
             self.favorite_count=dictionary["favorite_count"]
         if ("favorited" in dictionary):
             self.favorited=dictionary["favorited"]
         if ("filter_level" in dictionary):
             self.filter_level=dictionary["filter_level"]
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("id_str" in dictionary):
             self.id_str=dictionary["id_str"]
         if ("in_reply_to_screen_name" in dictionary):
             self.in_reply_to_screen_name=dictionary["in_reply_to_screen_name"]
         if ("lang" in dictionary):
             self.lang=dictionary["lang"]
         if ("place" in dictionary):
             self.place= _Place.Place(dictionary=dictionary["place"])
         if ("possibly_sensitive" in dictionary):
             self.possibly_sensitive=dictionary["possibly_sensitive"]
         if ("quoted_status_id" in dictionary):
             self.quoted_status_id=dictionary["quoted_status_id"]
         if ("quoted_status_id_str" in dictionary):
             self.quoted_status_id_str=dictionary["quoted_status_id_str"]
         if ("quoted_status" in dictionary):
             self.quoted_status=Tweet(dictionary=dictionary["quoted_status"])
         if ("scopes" in dictionary):
             self.scopes=dictionary["scopes"]
         if ("retweet_count" in dictionary):
             self.retweet_count=dictionary["retweet_count"]
         if ("retweeted" in dictionary):
             self.retweeted=dictionary["retweeted"]
         if ("retweeted_status" in dictionary):
             self.retweeted_status=Tweet(dictionary=dictionary["retweeted_status"])
         if ("source" in dictionary):
             self.source=dictionary["source"]
         if ("text" in dictionary):
             self.text=dictionary["text"]
         if ("truncated" in dictionary):
             self.truncated=dictionary["truncated"]
         if ("user" in dictionary):
             self.user= _TwitterUser.TwitterUser(dictionary=dictionary["user"])
         if ("withheld_copyright" in dictionary):
             self.withheld_copyright=dictionary["withheld_copyright"]
         if ("withheld_in_countries" in dictionary):
             self.withheld_in_countries=dictionary["withheld_in_countries"]
         if ("withheld_scope" in dictionary):
             self.withheld_scope=dictionary["withheld_scope"]


     def getRetweets(self, Access : _WeakAccess.WeakAccess = None, count=None):
         '''Reference https://dev.twitter.com/rest/reference/get/statuses/show/%3Aid
         '''
         return _Actions.Actions.getRetweetsFromTweet(id=self.id,Access=Access,count=count)

     def getShow(self, Access : _WeakAccess.WeakAccess = None):
         '''Reference https://dev.twitter.com/rest/reference/get/statuses/show/%3Aid
         '''
         return _Actions.Actions.getTweet(id=self.id,Access=Access)

     def getRetweeters(self, Access : _WeakAccess.WeakAccess = None, cursor=None, stringify_ids=None):
         '''Reference https://dev.twitter.com/rest/reference/get/statuses/retweeters/ids
         '''
         return _Actions.Actions.getRetweetersFromTweet(id=self.id,cursor=cursor,stringify_ids=stringify_ids,Access=Access)

     def postDestroy(self, Access : _StrongAccess.StrongAccess = None):
         '''
         Documentado em https://dev.twitter.com/rest/reference/post/statuses/destroy/%3Aid
         '''
         return _Actions.Actions.postDestroyTweetById(id=self.id,Access=Access)

     def postReply(self, msg,latitude=None,longitude=None,place_id=None,Access : _StrongAccess.StrongAccess = None):
         """ :reference: https://dev.twitter.com/rest/reference/post/statuses/update
            :allowed_param:'status', 'in_reply_to_status_id', 'lat', 'long', 'source', 'place_id', 'display_coordinates', 'media_ids'
         """
         return _Actions.Actions.postReply(id=self.id,msg=msg,latitude=latitude,longitude=longitude,place_id=place_id,Access=Access)

     def postRetweet(self,Access : _StrongAccess.StrongAccess = None ):
         '''Reference:  https://dev.twitter.com/rest/reference/post/statuses/retweet/%3Aid
         '''
         return _Actions.Actions.postRetweet(self.id,Access)

     def postFavoriteCreate(self,Access  : _StrongAccess.StrongAccess = None ):
         ''' :reference:https://dev.twitter.com/rest/reference/post/favorites/create
         '''
         return _Actions.Actions.postFavoriteTweetCreate(id=self.id,Access=Access)

     def postFavoriteDestroy(self,Access  : _StrongAccess.StrongAccess = None ):
         ''' :reference:https://dev.twitter.com/rest/reference/post/favorites/destroy
         '''
         return _Actions.Actions.postFavoriteTweetDestroy(id=self.id,Access=Access)



     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "TWEET: "+str(dic)

     def __repr__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "TWEET: "+str(dic)