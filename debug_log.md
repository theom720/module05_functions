# debug_log.md

# Author: Theo

## Bug 1

Error type: KeyError: 'amount'  
File + line: week8_buggy.py, line 13  
What the error means: One record does not have an "amount" key.  
What I told the duck: The loop checks each record and adds its amount to the total.  
What I tried: I printed each record and saw that the first record used "amout" instead of "amount".  
How I fixed it: I corrected "amout" to "amount" and removed the debug print.

## Bug 2

Error type: TypeError  
File + line: week8_buggy.py, line 18  
What the error means: Python cannot compare an integer and a string using `>`.  
How I fixed it: I changed "1000" from a string to the integer 1000.

## After Fixing Both Bugs

Final output: Total: $5150.00 across 3 records, followed by True  
Did pytest pass? Yes — 13 passed

## AI Literacy Reflection

Did I use AI? Yes  
If yes -- exact prompt I used: "help me do the lab"  
What AI explained: AI explained the traceback errors and guided me through each checkpoint.  
What I changed myself: I edited the code, removed the debug print, ran Ruff and pytest, and committed each step.  
Can I explain every fixed line? Yes

## What I learned

I learned to read tracebacks from the bottom and use `print()` to inspect data. I also learned that dictionary keys must match exactly and that Python cannot compare an integer with a string.
