# Day 32 SMTPLIB & Datetime

## Exercise 32-1: Motivational Monday Quotes

### Instructions

1. Create variables to fill and store:
   1. Email
   2. Password
   3. To [List]
   4. Subject
   5. Body
2. Import SMTPLIB
   1. Create:
      1. SSL Connection
      2. EHLO
      3. Login
      4. SendMail
      5. Close
3. Fill out the content for your email and test
4. Using the `Datetime` module
   1. Schedule emails to send on Monday's

### Example Input

#### quotes.json

```json
{
    "1": {
        "quote": "When you have a dream, you've got to grab it and never let go.",
        "author": "- Carol Burnett"
    },
    "2": {
        "quote": "Be courageous. Challenge orthodoxy. Stand up for what you believe in. When you are in your rocking chair talking to your grandchildren many years from now, be sure you have a good story to tell.",
        "author": "- Amal Clooney"
    },
    "3": {
        "quote": "You make a choice: continue living your life feeling muddled in this abyss of self-misunderstanding, or you find your identity independent of it. You draw your own box.",
        "author": "- Duchess Meghan"
    },
    "4": {
        "quote": "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "author": "- Winston Churchill"
    },
    "5": {
        "quote": "You define your own life. Don't let other people write your script.",
        "author": "- Oprah Winfrey"
    }
    // ...
}
```

### Example Output

```sha
Success is not final, failure is not fatal: it is the courage to continue that counts. 
- Winston Churchill
```

### Comments

I chose to go a bit further and added error handling and an external JSON data file with pre-filled quotes to use in the body of the email. This was not part of the lesson, but seemed reasonable to add this feature for automating the email on Monday's with Datetime.
