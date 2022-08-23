# True:use lock pin 
# False:lock screen skipped
uselock = True

# lock pin(array) 
# 1:Button1 2:Button2 3:Button3
lockpin = [3,2,3,1,2,4]

# True: use tiny buzzer when waking up and pin succeeded
# False silent
buzzer = True

# Key board Layout Type
# en:US key layout 
# jp:Japanese key layout
layoutType = "jp"

# enabled > True:use section False:skip section
# data > Display label and key config (array 3)
#   label > Display label
#   value > String value it send to PC when it pressed 
keymap = [
           { "enabled": True,
             "data": [
               { "label": "Custom Label01", "value": "Key Input value01" },
               { "label": "Custom Label02", "value": "Key Input value02" },
               { "label": "Custom Label03", "value": "Key Input value03" },
               { "label": "Custom Label04", "value": "Key Input value04" }	
             ]
           },
           { "enabled": True,
             "data": [
               { "label": "Custom Label11", "value": "Key Input value11" },
               { "label": "Custom Label12", "value": "Key Input value12" },
               { "label": "Custom Label13", "value": "Key Input value13" },
               { "label": "Custom Label14", "value": "Key Input value14" }		
             ]
           },
           { "enabled": True,
             "data": [
               { "label": "Custom Label21", "value": "Key Input value21" },
               { "label": "Custom Label22", "value": "Key Input value22" },
               { "label": "Custom Label23", "value": "Key Input value23 },
               { "label": "Custom Label24", "value": "Key Input value24" }		
             ]
           },
           { "enabled": True,
             "data": [
               { "label": "Custom Label31", "value": "Key Input value31" },
               { "label": "Custom Label32", "value": "Key Input value32" },
               { "label": "Custom Label33", "value": "Key Input value33" },
               { "label": "Custom Label34", "value": "Key Input value34" }		
             ]
           },
           { "enabled": True,
             "data": [
               { "label": "Custom Label41", "value": "Key Input value41" },
               { "label": "Custom Label42", "value": "Key Input value42" },
               { "label": "Custom Label43", "value": "Key Input value43" },
               { "label": "Custom Label44", "value": "Key Input value44" }		
             ]
           }
]

