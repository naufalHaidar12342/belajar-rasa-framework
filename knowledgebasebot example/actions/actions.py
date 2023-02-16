from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
import json
import logging
import os
import random
from rasa_sdk.executor import CollectingDispatcher

from typing import DefaultDict, Text, Callable, Dict, List, Any, Optional
from collections import defaultdict

from rasa_sdk import utils

class ActionMyKB(ActionQueryKnowledgeBase):
    def __init__(self):
        # load knowledge base with data from the given file
        knowledge_base = InMemoryKnowledgeBase("knowledge_base_data.json")

        # overwrite the representation function of the hotel object
        # by default the representation function is just the name of the object
        knowledge_base.set_representation_function_of_object("hotel", lambda obj: obj["name"] + " (" + obj["city"] + ")" )
        super().__init__(knowledge_base)

    #    utter_objects(text=f"Found the following objects of type '{object_type}':") 
    async def utter_objects(
        self,
        dispatcher: CollectingDispatcher,
        object_type: Text,
        objects: List[Dict[Text, Any]],
    ):
        """
        Utters a response to the user that lists all found objects.

        Args:
            dispatcher: the dispatcher
            object_type: the object type
            objects: the list of objects
        """
        if objects:
            dispatcher.utter_message(
                text=f"ada nih beberapa '{object_type}' yang ku inget :",
            )
        
            repr_function = await utils.call_potential_coroutine(
                self.knowledge_base.get_representation_function_of_object(object_type)
            )

            for i, obj in enumerate(objects, 1):
                dispatcher.utter_message(text=f"{i}: {repr_function(obj)}")
        else:
            dispatcher.utter_message(
                text=f"ngga ketemu jawabannya '{object_type}'."
            )