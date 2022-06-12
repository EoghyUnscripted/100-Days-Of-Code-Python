# Day 45 Web Scraping with Beautiful Soup

## Exercise 45-1: Parsing Local HTML

### Instructions

Using the provided HTML file:

1. Extract the data from the file
2. Create a Beautiful Soup object with the contents
3. Explore the functions to access tags

#### local.html

```html
<!DOCTYPE html>
<html>

<head>
 <meta charset="utf-8">
 <title>Angela's Personal Site</title>
</head>

<body>
 <h1 id="name">Angela Yu</h1>
 <p><em>Founder of <strong><a href="https://www.appbrewery.co/">The App Brewery</a></strong>.</em></p>
 <p>I am an iOS and Web Developer. I ❤️ coffee and motorcycles.</p>
 <hr>
 <h3 class="heading">Books and Teaching</h3>
 <ul>
  <li>The Complete iOS App Development Bootcamp</li>
  <li>The Complete Web Development Bootcamp</li>
  <li>100 Days of Code - The Complete Python Bootcamp</li>
 </ul>
 <hr>
 <h3 class="heading">Other Pages</h3>
 <a href="https://angelabauer.github.io/cv/hobbies.html">My Hobbies</a>
 <a href="https://angelabauer.github.io/cv/contact-me.html">Contact Me</a>
</body>

</html>
```

### Example Input

```python
# Get first anchor tag
print(soup.a)

# Get string from anchor tag
print(soup.a.string)

# Find all anchor tags
print(soup.findAll(name="a"))

# Get all href links in the a tags
for tag in soup.findAll(name="a"):
    print(tag.get("href"))
    
# Get a specific element
print(soup.find(name="h1", id="name"))
```

### Example Output

```sha
<a href="https://www.appbrewery.co/">The App Brewery</a>
The App Brewery
[<a href="https://www.appbrewery.co/">The App Brewery</a>, <a href="https://angelabauer.github.io/cv/hobbies.html">My Hobbies</a>, <a href="https://angelabauer.github.io/cv/contact-me.html">Contact Me</a>]
https://www.appbrewery.co/
https://angelabauer.github.io/cv/hobbies.html
https://angelabauer.github.io/cv/contact-me.html
<h1 id="name">Angela Yu</h1>
```

## Exercise 45-2: Parsing Live Website HTML

### Instructions

Using [Hacker News](https://news.ycombinator.com):

1. Extract the html data from the page
2. Create a Beautiful Soup object with the contents
3. Get all of the:
   1. Article Titles
   2. Article Links
   3. Article Upvotes
4. With the data in step 3, put the data into lists
5. Find the id of the largest number of upvotes
   1. Print the title
   2. Print the link

### Example Input

```python
# Get first anchor tag
print(soup.a)

# Get string from anchor tag
print(soup.a.string)

# Find all anchor tags
print(soup.findAll(name="a"))

# Get all href links in the a tags
for tag in soup.findAll(name="a"):
    print(tag.get("href"))
    
# Get a specific element
print(soup.find(name="h1", id="name"))
```

### Example Output

```sha
MIT researchers uncover ‘unpatchable’ flaw in Apple M1 chips https://techcrunch.com/2022/06/10/apple-m1-unpatchable-flaw/
```
