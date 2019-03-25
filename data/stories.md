## story_greet <!--- The name of the story. It is not mandatory, but useful for debugging. --> 
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. --> 
 - utter_greet <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' --> 
 
## story_goodbye
* goodbye
 - utter_goodbye

## whereabouts
* ask_whereabouts
 - utter_whereabouts

## threaten
* threaten
 - utter_threat_response

## ask_about_object
* ask_about_stolen_object
 - utter_stolen_object_response

## ask_more_info
* ask_more_info
 - utter_more_info

## ask_to_describe_events
* ask_about_knowledge_of_event
  - utter_affirm_knowledge_of_events
* ask_to_describe_events
  - utter_events_description
* ask_where_abouts{"date": "tuesday"}
  - slot{"date": "tuesday"}
  - utter_whereabouts
* ask_what_were_they_doing
  - utter_what_they_were_doing
* ask_about_stolen_object
 - utter_stolen_object_response

## ask_about_events
* ask_about_knowledge_of_event
  - utter_affirm_knowledge_of_events
* ask_to_describe_events
  - utter_events_description

## ask_what_they_were_doing
* ask_what_were_they_doing
  - utter_what_they_were_doing

## ask_about_suspects
* ask_about_suspects
    - utter_knowledge_of_suspect

## conversation_about_events
* greet
    - utter_greet
* ask_what_were_they_doing
    - utter_what_they_were_doing
* ask_about_knowledge_of_event
    - utter_affirm_knowledge_of_events
* ask_to_describe_events
    - utter_events_description
* ask_about_suspects
    - utter_knowledge_of_suspects

## Generated Story 6637974751492485532
* greet
    - utter_greet
* ask_where_abouts{"date": "tuesday"}
    - slot{"date": "tuesday"}
    - utter_whereabouts
* ask_about_knowledge_of_event
    - utter_affirm_knowledge_of_events
* ask_to_describe_events
    - utter_events_description
* ask_about_suspects
    - utter_knowledge_of_suspect

