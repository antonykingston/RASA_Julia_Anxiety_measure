# **************************************************************************************
# WARNING: This is a static file, useful as a starting point. You may want to change it.
# **************************************************************************************

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk import FormValidationAction
from rasa_sdk.types import DomainDict
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk import ActionExecutionRejection
from rasa_sdk.forms import FormAction, REQUESTED_SLOT

from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType
import requests
import json

from rasa_sdk.events import SlotSet
from rasa_sdk.events import AllSlotsReset


class anxietyStateForm(FormAction):
    """Example of a custom form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "anxietystate_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["anxietystate_slot"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {"anxietystate_slot": [self.from_entity(entity="anxietystate_entity"),
                             self.from_text()]}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        
        # dispatcher.utter_template('utter_submit', tracker) #utter submit template

        msg = tracker.get_slot('anxietystate_slot')
        print (msg)

        dispatcher.utter_message(response="utter_anxiety_5", anxietystate_slot=msg)

        # return []
        # return [SlotSet("anxietystate_slot", None")] #this will reset a particular slot
        return [AllSlotsReset()] #this will reset all the slots


store={}
store["score"] = 0
class MyCustomAction(Action):

    def name(self) -> Text:
        return "action_final_score"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        print(tracker.latest_message["intent"]["name"])
        
        store["id"] = tracker.sender_id
        store["intent"] = tracker.latest_message["intent"]["name"]

        if tracker.latest_message["intent"]["name"] == "continue_path":
            if store["score"] in [8,9,10,11,12,13,14]:

                try:
                    url_1 = "https://bodhi.augray.com:4000/api/v1/facts/create"
                    id = tracker.sender_id
                    # id="624174f85e695c6d7f1f5fd9"
                    payload={'userId': id,
                        'factKey': 'anxiety_assessment',
                        'factLabel': 'anxiety level',
                        'factValue': 'You have no anxiety'}
                    resp = requests.request("POST", url_1, data=payload)
                    print(resp.json())
                except:
                    print("url =",url_1, "\nid =",id, "\npayload =",payload, "\nmessage =","anxiety level data not getting stored")

                dispatcher.utter_message(response="utter_gad7_anxiety-intent-0")
                dispatcher.utter_message(response="utter_gad7_anxiety-intent-1")

                dispatcher.utter_message(response="utter_gad7_no_anxiety-intent-0")
                dispatcher.utter_message(response="utter_gad7_no_anxiety-intent-1")

            if store["score"] in [15,16,17,18,19,20]:

                try:
                    url_1 = "https://bodhi.augray.com:4000/api/v1/facts/create"
                    id = tracker.sender_id
                    # id="624174f85e695c6d7f1f5fd9"
                    payload={'userId': id,
                        'factKey': 'anxiety_assessment',
                        'factLabel': 'anxiety level',
                        'factValue': 'You have low anxiety'}
                    resp = requests.request("POST", url_1, data=payload)
                    print(resp.json())
                except:
                    print("url =",url_1, "\nid =",id, "\npayload =",payload, "\nmessage =","anxiety level data not getting stored")

                dispatcher.utter_message(response="utter_gad7_anxiety-intent-0")
                dispatcher.utter_message(response="utter_gad7_anxiety-intent-1")

                dispatcher.utter_message(response="utter_gad7_mild_anxiety-intent-0")
                dispatcher.utter_message(response="utter_self_help_intro")
                dispatcher.utter_message(response="utter_self_help_intro_1")
                dispatcher.utter_message(response="utter_self_help_intro_2")
                dispatcher.utter_message(response="utter_self_help_intro_3")

            if store["score"] in [21,22,23,24,25,26]:

                try:
                    url_1 = "https://bodhi.augray.com:4000/api/v1/facts/create"
                    id = tracker.sender_id
                    # id="624174f85e695c6d7f1f5fd9"
                    payload={'userId': id,
                        'factKey': 'anxiety_assessment',
                        'factLabel': 'anxiety level',
                        'factValue': 'You have moderate anxiety'}
                    resp = requests.request("POST", url_1, data=payload)
                    print(resp.json())
                except:
                    print("url =",url_1, "\nid =",id, "\npayload =",payload, "\nmessage =","anxiety level data not getting stored")

                dispatcher.utter_message(response="utter_gad7_anxiety-intent-0")
                dispatcher.utter_message(response="utter_gad7_anxiety-intent-1")

                dispatcher.utter_message(response="utter_gad7_moderate_anxiety-intent-0")
                dispatcher.utter_message(response="utter_self_help_intro")
                dispatcher.utter_message(response="utter_self_help_intro_1")
                dispatcher.utter_message(response="utter_self_help_intro_2")
                dispatcher.utter_message(response="utter_self_help_intro_3")

            if store["score"] in [27,28,29,30,31]:

                try:
                    url_1 = "https://bodhi.augray.com:4000/api/v1/facts/create"
                    id = tracker.sender_id
                    # id="624174f85e695c6d7f1f5fd9"
                    payload={'userId': id,
                        'factKey': 'anxiety_assessment',
                        'factLabel': 'anxiety level',
                        'factValue': 'You have moderately severe anxiety'}
                    resp = requests.request("POST", url_1, data=payload)
                    print(resp.json())
                except:
                    print("url =",url_1, "\nid =",id, "\npayload =",payload, "\nmessage =","anxiety level data not getting stored")

                dispatcher.utter_message(response="utter_gad7_anxiety-intent-0")
                dispatcher.utter_message(response="utter_gad7_anxiety-intent-1")

                dispatcher.utter_message(response="utter_gad7_moderatelysevere_anxiety-intent-0")
                dispatcher.utter_message(response="utter_self_help_intro")
                dispatcher.utter_message(response="utter_self_help_intro_1")
                dispatcher.utter_message(response="utter_self_help_intro_2")
                dispatcher.utter_message(response="utter_self_help_intro_3")
            if store["score"] in [32,33,34,35,36,37,38,39,40,41]:

                try:
                    url_1 = "https://bodhi.augray.com:4000/api/v1/facts/create"
                    id = tracker.sender_id
                    # id="624174f85e695c6d7f1f5fd9"
                    payload={'userId': id,
                        'factKey': 'anxiety_assessment',
                        'factLabel': 'anxiety level',
                        'factValue': 'You have severe anxiety'}
                    resp = requests.request("POST", url_1, data=payload)
                    print(resp.json())
                except:
                    print("url =",url_1, "\nid =",id, "\npayload =",payload, "\nmessage =","anxiety level data not getting stored")

                dispatcher.utter_message(response="utter_gad7_anxiety-intent-0")
                dispatcher.utter_message(response="utter_gad7_anxiety-intent-1")

                dispatcher.utter_message(response="utter_gad7_severe_anxiety-intent-0")
                dispatcher.utter_message(response="utter_gad7_severe_anxiety-intent-1")
                dispatcher.utter_message(response="utter_gad7_severe_anxiety-intent-2")
                dispatcher.utter_message(response="utter_self_help_intro_2")
                dispatcher.utter_message(response="utter_self_help_intro_3")
            store["score"] = 0

        else:
            if tracker.latest_message["intent"]["name"] == "p1_path_2":
                if tracker.latest_message["entities"][0]["value"] == "Good":
                    store["score"] += 1
                    dispatcher.utter_message(response="utter_gad7_qna_path-intent-1")
                    dispatcher.utter_message(response="utter_p1_path_2")
                if tracker.latest_message["entities"][0]["value"] == "Average":
                    store["score"] += 2
                    dispatcher.utter_message(response="utter_gad7_qna_path-intent-1")
                    dispatcher.utter_message(response="utter_p1_path_2")
                if tracker.latest_message["entities"][0]["value"] == "Bad":
                    store["score"] += 3
                    dispatcher.utter_message(response="utter_gad7_qna_path-intent-1")
                    dispatcher.utter_message(response="utter_p1_path_2")
                if tracker.latest_message["entities"][0]["value"] == "Worse":
                    store["score"] += 4
                    dispatcher.utter_message(response="utter_gad7_qna_path-intent-1") 
                    dispatcher.utter_message(response="utter_p1_path_2")

            if tracker.latest_message["intent"]["name"] == "p1_path_3":
                if tracker.latest_message["entities"][0]["value"] == "Good":
                    store["score"] += 1
                    dispatcher.utter_message(response="utter_p1_path_3")
                if tracker.latest_message["entities"][0]["value"] == "Average":
                    store["score"] += 2
                    dispatcher.utter_message(response="utter_p1_path_3")
                if tracker.latest_message["entities"][0]["value"] == "Bad":
                    store["score"] += 3
                    dispatcher.utter_message(response="utter_p1_path_3") 
                if tracker.latest_message["entities"][0]["value"] == "Worse":
                    store["score"] += 4  
                    dispatcher.utter_message(response="utter_p1_path_3")

            if tracker.latest_message["intent"]["name"] == "p1_path_4":
                if tracker.latest_message["entities"][0]["value"] == "Good":
                    store["score"] += 1
                    dispatcher.utter_message(response="utter_gad7_qna_path-intent-2")
                    dispatcher.utter_message(response="utter_p1_path_4")
                if tracker.latest_message["entities"][0]["value"] == "Average":
                    store["score"] += 2
                    dispatcher.utter_message(response="utter_gad7_qna_path-intent-2")
                    dispatcher.utter_message(response="utter_p1_path_4")
                if tracker.latest_message["entities"][0]["value"] == "Bad":
                    store["score"] += 3
                    dispatcher.utter_message(response="utter_gad7_qna_path-intent-2")
                    dispatcher.utter_message(response="utter_p1_path_4")
                if tracker.latest_message["entities"][0]["value"] == "Worse":
                    store["score"] += 4
                    dispatcher.utter_message(response="utter_gad7_qna_path-intent-2")
                    dispatcher.utter_message(response="utter_p1_path_4")
    
            if tracker.latest_message["intent"]["name"] == "p1_path_5":
                if tracker.latest_message["entities"][0]["value"] == "Good":
                    store["score"] += 1
                    dispatcher.utter_message(response="utter_p1_path_5")
                if tracker.latest_message["entities"][0]["value"] == "Average":
                    store["score"] += 2
                    dispatcher.utter_message(response="utter_p1_path_5")
                if tracker.latest_message["entities"][0]["value"] == "Bad":
                    store["score"] += 3
                    dispatcher.utter_message(response="utter_p1_path_5")
                if tracker.latest_message["entities"][0]["value"] == "Worse":
                    store["score"] += 4      
                    dispatcher.utter_message(response="utter_p1_path_5")

            if tracker.latest_message["intent"]["name"] == "p1_path_6":
                if tracker.latest_message["entities"][0]["value"] == "Good":
                    store["score"] += 1
                    dispatcher.utter_message(response="utter_gad7_qna_path-intent-3")
                    dispatcher.utter_message(response="utter_p1_path_6")
                if tracker.latest_message["entities"][0]["value"] == "Average":
                    store["score"] += 2
                    dispatcher.utter_message(response="utter_gad7_qna_path-intent-3")
                    dispatcher.utter_message(response="utter_p1_path_6")
                if tracker.latest_message["entities"][0]["value"] == "Bad":
                    store["score"] += 3
                    dispatcher.utter_message(response="utter_gad7_qna_path-intent-3")
                    dispatcher.utter_message(response="utter_p1_path_6")
                if tracker.latest_message["entities"][0]["value"] == "Worse":
                    store["score"] += 4
                    dispatcher.utter_message(response="utter_gad7_qna_path-intent-3")
                    dispatcher.utter_message(response="utter_p1_path_6")

            if tracker.latest_message["intent"]["name"] == "p1_path_7":
                if tracker.latest_message["entities"][0]["value"] == "Good":
                    store["score"] += 1
                    dispatcher.utter_message(response="utter_p1_path_7")
                if tracker.latest_message["entities"][0]["value"] == "Average":
                    store["score"] += 2
                    dispatcher.utter_message(response="utter_p1_path_7")
                if tracker.latest_message["entities"][0]["value"] == "Bad":
                    store["score"] += 3
                    dispatcher.utter_message(response="utter_p1_path_7")
                if tracker.latest_message["entities"][0]["value"] == "Worse":
                    store["score"] += 4  
                    dispatcher.utter_message(response="utter_p1_path_7")

            if tracker.latest_message["intent"]["name"] == "p1_path_8":
                if tracker.latest_message["entities"][0]["value"] == "Good":
                    store["score"] += 1
                    dispatcher.utter_message(response="utter_gad7_qna_path-intent-4")
                    dispatcher.utter_message(response="utter_p1_path_8")
                if tracker.latest_message["entities"][0]["value"] == "Average":
                    store["score"] += 2
                    dispatcher.utter_message(response="utter_gad7_qna_path-intent-4")
                    dispatcher.utter_message(response="utter_p1_path_8")
                if tracker.latest_message["entities"][0]["value"] == "Bad":
                    store["score"] += 3
                    dispatcher.utter_message(response="utter_gad7_qna_path-intent-4")
                    dispatcher.utter_message(response="utter_p1_path_8")
                if tracker.latest_message["entities"][0]["value"] == "Worse":
                    store["score"] += 4
                    dispatcher.utter_message(response="utter_gad7_qna_path-intent-4")
                    dispatcher.utter_message(response="utter_p1_path_8")

            if tracker.latest_message["intent"]["name"] == "continue_path":
                if tracker.latest_message["entities"][0]["value"] == "Good":
                    dispatcher.utter_message(response="utter_continue_path")
                if tracker.latest_message["entities"][0]["value"] == "Average":
                    dispatcher.utter_message(response="utter_continue_path")
                if tracker.latest_message["entities"][0]["value"] == "Bad":
                    dispatcher.utter_message(response="utter_continue_path")
                if tracker.latest_message["entities"][0]["value"] == "Worse":
                    dispatcher.utter_message(response="utter_continue_path")

        print(store["score"])
        return