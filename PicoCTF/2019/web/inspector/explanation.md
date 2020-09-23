# Insp3ct0r - Points: 50 (Web Exploitation)

This is the introduction to the web exploitation category. If you inspect the html you can find the first part of the flag:

```html
  	(...)
    <p>I used these to make this site: <br/>
	  HTML <br/>
	  CSS <br/>
	  JS (JavaScript)
	</p>
	<!-- Html is neat. Anyways have 1/3 of the flag: picoCTF{tru3_d3 -->
      </div>

    </div>

  </body>
</html>
```

The second one on the css:

```css
.tabcontent {
  color: #111;
  display: none;
  padding: 50px;
  text-align: center;
}

#tabintro {
  background-color: #ccc;
}
#tababout {
  background-color: #ccc;
}

/* You need CSS to make pretty pages. Here's part 2/3 of the flag: t3ct1ve_0r_ju5t */
```

And finally, the last part is in the javascript:

```javascript
window.onload = function() {
  openTab("tabintro", this, "#222");
};

/* Javascript sure is neat. Anyways part 3/3 of the flag: _lucky?1638dbe7} */
```

So yeah, that's the first challenge done!
