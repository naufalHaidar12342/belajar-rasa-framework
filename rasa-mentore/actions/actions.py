from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
# import json
# import logging
# import os
# import random
from rasa_sdk.executor import CollectingDispatcher

from typing import DefaultDict, Text, Callable, Dict, List, Any, Optional
from collections import defaultdict

from rasa_sdk import utils, Tracker, Action


class ActionTeknologiInformasi(ActionQueryKnowledgeBase):
    def name(self) -> Text:
        return "action_query_teknologi_informasi"

    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase("knowledge_base.json")

        knowledge_base.set_representation_function_of_object(
            "teknologi_informasi", lambda obj: obj["judul"]
        )
        super().__init__(knowledge_base)
 
    def utter_attribute_value(
        self,
        dispatcher: CollectingDispatcher,
        object_name: Text,
        attribute_name: Text,
        attribute_value: Text,
    ):
        if attribute_value:
            dispatcher.utter_message(
                text=f"{attribute_value}."
            )
        else:
            dispatcher.utter_message(
                text=f"Mohon maaf, saya tidak tahu tentang {attribute_name} pada {object_name}."
            )
    
    async def utter_objects(
        self,
        dispatcher: CollectingDispatcher,
        object_type: Text,
        objects: List[Dict[Text, Any]],
    ):
        if objects:
            repr_function = await utils.call_potential_coroutine(
                self.knowledge_base.get_representation_function_of_object(object_type)
            )

            if len(objects) == 1:
                for i, obj in enumerate(objects, 1):
                    dispatcher.utter_message(text=f"{object_type} {repr_function(obj)}")
            else:
                dispatcher.utter_message(
                    text=f"Disini ada beberapa materi tentang {object_type} seperti :",
                )
                for i, obj in enumerate(objects, 1):
                    dispatcher.utter_message(text=f"{i}: {repr_function(obj)}")
            
        else:
            dispatcher.utter_message(
                text=f"Maaf, saya kurang paham mengenai materi {object_type} tersebut."
            )
