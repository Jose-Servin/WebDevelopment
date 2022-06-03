# What is CSS?

CSS describes the visual style and presentation of the content written in HTML. <br>

CSS takes on the format of a dictionary consisting on `property: value` pairs which make up a `declaration/style`.
Multiple `declarations/styles` are in the `declaration block` which in turn make up a `CSS rule`.

# Inline, Internal and External CSS

* Inline CSS <br>
  Writing the CSS inside the HTML element. Note that inline styling should never be used because it creates entanglement
  between HTML and CSS elements. Goes against "separation of concern" (SoC): a design principle separating a computer
  program into distinct sections.

````html
<h1 style="color:cornflowerblue;"> 📘 The Code Magazine</h1>
````

* Internal CSS <br>
  Declaring a `<style> </style>` element in the `<head> </head>` of our HTML doc. This is a good beginner option but
  presents issues since it can drastically increase the length of our HTML document.

```html

<head>
    <meta charset="UTF-8">
    <title>The Basic Language of the Web: HTML </title>
    <!-- <link href="main_style.css" rel="stylesheet"> -->
    <style>
        h1 {
            color: cornflowerblue;
        }
    </style>
</head>
```

* External CSS <br>
  Using a `style.css` sheet to hold the various CSS properties for our HTML elements. This is the best option since it
  properly separates out HTML code from our CSS rules. To implement:

First we declare the style sheet in our HTML doc:

```html

<head>
    <meta charset="UTF-8">
    <title>The Basic Language of the Web: HTML </title>
    <link href="main_style.css" rel="stylesheet">

</head>
```

Second, we define our CSS rules in `style.css`:

```css
h1 {
    color: firebrick;
}
```

# Styling Text

There are various text properties that can be applied to most HTML elements. Some of the most common ones are:

```css
h1 {
    color: firebrick;
    font-size: 26px;
    font-family: 'League Gothic', sans-serif;
    text-transform: uppercase;
    font-style: normal;
    text-align: center;
}
```

It is important to note that for `<ol>` or `<ul>` elements, only the `<li>` elements can be styled. So, we style the
list item not the actual list structure. We also see how inheritance works in CSS because all other elements inside
our `<p>` elements get styled based on the rules set for those p elements.

# Combining Selectors

Before combining selectors we have:

```css
h1 {
    color: firebrick;
    font-size: 26px;
    font-family: 'League Gothic', sans-serif;
    text-transform: uppercase;
    font-style: normal;
    text-align: center;
}

h2 {
    font-size: 40px;
    font-family: 'League Gothic', sans-serif;
    font-style: normal;
}

h3 {
    font-size: 30px;
    font-family: 'League Gothic', sans-serif;
}


h4 {
    font-size: 20px;
    font-family: 'League Gothic', sans-serif;
    text-transform: uppercase;
    text-align: center;
}

p {
    font-size: 22px;
    font-family: 'League Gothic', sans-serif;
    line-height: 1.5;
    color: dimgrey;
}

li {
    font-family: 'League Gothic', sans-serif;
    font-size: 20px;
}
```

Which shows how some properties are repeated. We can eliminate this redundancy and implement best practices by combining
selectors using `list selectors`:

```css
h1, h2, h3, h4, p, li {
    font-family: 'League Gothic', sans-serif;
}
```

Now, any change in the font-family will be implemented on all elements, and we won't have to change them one by one.

## Descendent Selector

To change the `<p>` text of the `<footer>` we use descendent selectors to specify we would like to change the p text of
the footer only.

```css
footer p {
    font-size: 12px;
}
```

Here we are saying "select the child p element of the footer element." It is important to note that descendent selectors
can present issues when the same parent-child relationships exists in our HTML doc.

```html

<div>
    <header>
        <p> What we want to style </p>
    </header>
</div>
<article>
    <header>
        <p> We do not want to style this </p>
    </header>
</article>
```

In this example, if we use descendent selector we would use `header p` but this would select both `p` tags in our doc.
To fix this, we use nested-descendent selectors:

```css
article header p {
    color: red;
}
```

# Class and ID Selectors

Class and ID selectors are a better option vs descendent selectors because it removes the HTML encoding in our css file.
In order to implement class and ID selectors we must first declare them in our HTML doc:

```html
<p id="author">
    Posted by <strong> Laura Jones</strong> on Monday. June 21st 2017
</p>
```

and then select them using the (hash) `#` in our css file:

```css
#author {
    color: red;
}
```

## ID vs Classes

The big difference between ID's and Classes is that we are not allowed to repeat ID names. We can have multiple HTML
elements with the same class, such as the "related post" author names (CSS convention is to use dashes -):

```html
<p class="author-name"> By Jonas Schmedtmann </p>
```

To style this, we use the class selector in css `.`:

```css
.author-name {
    color: saddlebrown;
}
```

It is noted that by default, we will stick mostly to using classes in order to prepare for future changes and limit
potential bugs.

# Working with Colors

Colors in CSS can be specified using two ways.

1. RGB Notation <br>
   Defined using the `rgb()`function. Can take a 4th value specifying the "alpha" (0.0 - 1.0).
2. Hexadecimal Notation <br>
   Written using `#00ffff`

## Shades of Grey

Grey colors are created when all three values in either RGB function or Hex pairs are the same. `rgb(183, 183, 183)`
and `#b7b7b7` are the same color.

# Pseudo-Classes

By definition, a pseudo-class is used to define a special state of an element. They are implemented using a colon
`:`. One way we can bold the first element on a list is:

```css
.first-li {
    font-weight: bold;
}
```

But we can use pseudo-classes to select the first child element as shown:

```css
li:first-child {
    font-weight: bold;
}
```

This wil select ALL list elements that are the first child of their parent element which can be either `ol` or `ul`. A
powerful function to use is `li:nth-child(x)`. Here we can specify integer location or keywords such as `odd` or
`even`. One thing to remember is that pseudo classes, when specified, select the first child of the parent element, so
it must be a direct child-parent relationship AND must be first or last. We cannot style the first `p` inside of
`article` because the `p` is not a direct child of `article`, it is a child of the `header`.

First we make sure the last-child of the `article` element is a `p` element.

```html
<p> Hopefully you learned something new here. See you next time! </p>
<!--  <button> Email Me</button> -->
</article>
```

Now we can use the pseduo-class `article p:last-child` to style that last child `p` element.

```css
article p:last-child {
    color: red;
}
```

# Styling Hyperlinks (LVHA)

Styling hyperlinks best practice is to style a pseudo class in order to style different states of the link.

1. Styling links requires us to find `a` tags that contain `href`.

```css
a:link {
    color: red;
    text-decoration: none;
}
```

There are other pseudo classes for links such as:

- `a:vistied`
- `a:hover`
- `a:active`

The order of these link pseudo classes matter and must always follow:

1. Link
2. Visited
3. Hover
4. Active

# CSS Theory #1: Conflicts Between Selectors 



