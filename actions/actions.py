# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []



class ActionDuplcate_checking(Action):

    def name(self) -> Text:
        return "action_Duplcate_checking"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #print(collection_conver)
      #  dispatcher.utter_message(text="Hello World! FanboFanbo")
        collection_conver=tracker.events_after_latest_restart()
        message_from_user=[]
        for element in collection_conver:
            if element['event']=='user':
                if element['text']:
                    message_from_user.append(element['text'])
        if len(message_from_user)>1:
            if message_from_user[-1] in message_from_user[:-1]:
                dispatcher.utter_message(text="the message has been asked before, do you want to further proceed with it? Or if you are not happy with the answer, please check with the tutor: https://asu.zoom.us/j/81868714615#success")
            #else:
            #    dispatcher.utter_message(text="Hello World! FanboFanbo")
        #else:

        #    dispatcher.utter_message(text="This the first message")

        #dispatcher.utter_message(text=str(collection_conver))

        return []
