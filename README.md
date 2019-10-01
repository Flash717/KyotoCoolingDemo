# Kyoto Cooling Demo

### Background:

We are trying build an API that answers questions about a network of people.

There are two data sets. First file contains list of 100 people and their names. Second file has the relationship of each person with at least 5 other folks on the list.

---  

### Requirements:

Create an API Server with the following functionality:  
- Get a user by id  
- Get the connections from user id=X  
- How many total connections  does user id=X has?  
- Who can introduce user id=X to user id=Y?  
- Which connections are common between user id=X and user id=Y?  
- Which user has the most connections?  
- Which user has the least connections?  
- The APIs should accept “degree” as a parameter:   
    - 1st-degree connections - People you're directly connected.  
    - 2nd-degree connections - People who are connected to your 1st-degree connections.  
    - 3rd-degree connections - People who are connected to your 2nd-degree connections  
    - Nth-degree connections – People who are connected to your (n-1)th-degree connections  

---

### Setup
Requires python3 to be installed.
- Clone repo locally (`git clone https://github.com/Flash717/KyotoCoolingDemo.git`)
- Run `pip install -r requirements.txt` to install required python libraries
- Run `python app.py` to start http-server on localhost port 8081

---

### Endpoints
- GET `/` -> show user stats (min and max connections)
- GET `/user/<user_id>` -> show user information
- GET `/user/<user_id>/connections?degree=<int>&allowLoops=<True/False>` -> shows connection information for user
    - parameter `degree` -> connection to Nth degree
    - parameter `allowLoops` -> if `True` then circular references (loops) are counted, otherwise already found id's from earlier degree-levels are not further counted
- GET `/user/<user_id>/introduction/<other_id>` -> shows chain of who can introduce `user_id` with `other_id`
- GET `/user/<user_id>/common/<other_id>` -> shows common connection between two users