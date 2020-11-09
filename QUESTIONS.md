### Cases not covered in the ACs

Should the program have error handling?  
 - assumed yes

Should we accept a float number of leftover food?  
 - assumed yes

Given the order of operations, in the case that our leftover food equals the minimum required, we are not ordering any extra food.  
 - proposed: order 20% more than the minimum, calculated prior to subtracting the leftover food.  

### Off the wall cases

What is the shelter's food storage capacity?  

Dogs being adopted/put down should be calculated as decimals for time spent at shelter.  

A pregnant dog which would exceed the 30 dog limit is not accounted for.  

Food for a months is not accounting for days in a given month e.g. 28 vs 31 days.  

Expiration of dog food is not accounted for. How many months can we roll over the excess food?  
 - Is dog food being used in a FIFO manner in order to avoid the rollover of expired food indefinitely?  
 
Should food be distinguished by puppy vs adult dogs  
