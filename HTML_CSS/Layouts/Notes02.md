# What are Layouts?

<dl>
    <dt> Layout</dt>
<dd> The way text, images and other content is placed and arranged on a webpage. </dd>
<dd> A way of introducing structure to our page into which we place our content.  </dd>

<dt> Building a Layout </dt>
<dd> Arranging page elements into a visual structure, instead of simply having them placed 
one after the other. (normal flow) </dd>

</dl>

# Page Layout vs Component Layout

<dl>
    <dt> Page Layout </dt>
<dd> Refers to the overall organization of a webpage consisting of various components. </dd>
  <dt> Component Layout </dt>
<dd> The organization of individual page components. </dd>

</dl>

# The 3 ways of building CSS layouts

1. Floats

The old way of building layouts of all sizes, using the css property `float`. Still used but getting outdated fast.

2. Flexbox

Modern way of laying out elements in a 1-dimensional row using floats. Perfect for component layouts.

3. CSS Grid

For laying out elements in a fully-fledged 2-dimensional grid. Perfect for page layouts and complex components.

# Using Floats

With this CSS property, the element being styled becomes sort of absolute positioned, causing other elements near it to
float around it:

```css
.author-image {
    float: left;
}
```

To make the other elements start AFTER the float element we can also give them the float property. This will cause them
to start after the floating elements.

```css
.main-author {
    margin-left: 90px;
    margin-top: 10px;
    float: left;
}
```

The `left` and `right` properties dictate what side of the container the element will start at. Also, a floated element
can still take `margin` properties which will follow conventional rules. <br>

When we float all the child elements of a parent element for example our `header`, we loose some padding and structure
of the page since technically, these elements are now floating. The height of the parent element now goes to `0`
since it now contains 0 elements. This is referred to as `the collapsing element`.

# Clearing Floats

Again, a parent element will collapse when all of its child elements are floated. To fix this, we insert a `div`
element with the class `clear` inside the parent element that collapsed and set its properties to:

```html

<header class="main-header">
    <h1> 📘 The Code Magazine</h1>
    
    
    <!--Grouping links together inside a nav element -->
    <nav class="navigation-links">
        <a href='other_page.html'> Other Page </a>
        <a href='#'> Challenges </a>
        <a href='#'> Flexbox</a>
        <a href='#'> Grid</a>
    </nav>
    
    <div class="clear"></div>
</header>
```

```css
.clear {
    clear: both;
}
```

However, we must note that this way of clearing floats is not practical because we introduce HTML code that holds no
value. We can instead use `the clear fix` hack. <br>

First we add the class `clearfix` to the parent element that is collapsing. In our example this is the `header`
element. Next we use the pseudo-element `after` in our CSS property declaration. This creates a "last child element"
for this parent element that is collapsing which is the same as adding an empty `div` manually. We then add the
following CSS properties to our pseudo-element:

```css
.clearfix::after {
    clear: both;
    display: block;
    content: '';
}
```

