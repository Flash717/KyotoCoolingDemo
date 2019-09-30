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

