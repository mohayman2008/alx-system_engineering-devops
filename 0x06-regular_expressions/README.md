# 0x06. Regular expressions

The files in this folder are ruby scripts that depends on regular expressions (RegEx) to solve  
the problems in the tasks of this project

## The following ruby scripts uses **regex** to realize the required matching criteria, join the matched strings in the passed-in argument together and print the result to stdout:

### **0-simply_match_school.rb**
* Matches "*School*" exactly.

### **1-repetition_token_0.rb**
* Matches: 
    + "*hbttn*" 
    + "*hbtttn*"
    + "*hbttttn*"
    + "*hbtttttn*"

* Doesn't match: 
    + "*hbn*" 
    + "*hbtn*"
    + "*hbttttttn*"

### **2-repetition_token_1.rb**
* Matches:
    + "*htn*"
    + "*hbtn*"

* Doesn't match:
    + "*hbbtn*"
    + "*hbbbtn*"

### **3-repetition_token_2.rb**
* Matches:
    + "*hbtn*"
    + "*hbttn*"
    + "*hbtttn*"
    + "*hbttttn*"

* Doesn't match:
    + "*hbn*"

### **4-repetition_token_3.rb**
* Matches:
    + "*hbn*" 
    + "*hbtn*" 
    + "*hbttn*" 
    + "*hbtttn*" 
    + "*hbttttn*"

* Doesn't match: 
    + "*hbon*"

### **5-beginning_and_end.rb**
* Matches any string starting with '*h*', ending with '*n*' and containing any single character in between

* Matches:
    + "*hbn*" 
    + "*h8n*" 

* Doesn't match: 
    + "*hn*"
    + "*hbtn*"
    + "*Hhn*"

### **6-phone_number.rb**
* Matches any 10 digit phone number.

* Matches:
    + "*1234567890*"
    + "*4155049898*" 

* Doesn't match: 
    + "*123456789*"
    + "*12345678900*"
    + *" 4155049898"*
    + "*415 504 9898*"
    + "*415-504-9898*"

### **7-OMG_WHY_ARE_YOU_SHOUTING.rb**
* Only matches capital letters.

* Matches:
    + "*ILOVESYSADMIN*" in "*I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream*"
    + "*WHATSAY*" in "*WHAT do you SAY?*"

* Doesn't match anything in:
    + "*cannot read you*"

## 
### **100-textme.rb**
This ruby script parses any ***log entry*** in [**text messages transactions log file of TextMe app**](text_messages.log),  
implementening regular expressions to extraxt:
* The sender phone number or name (including country code if present)
* The receiver phone number or name (including country code if present)
* The flags that were used

then print them out in the following format "***[SENDER],[RECEIVER],[FLAGS]***"

#### **Example**:  

**Input**:  
```
Feb 1 11:00:00 ip-10-0-0-11 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE1] [SVC:] [ACT:]
[BINF:] [FID:] [from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1] [msg:127:This planet has - or rather had -
a problem, which was this: most of the people on it were unhappy for pretty much of the time.] [udh:0:]
```

**Output**:  
```
Google,+16474951758,-1:0:-1:0:-1
```

