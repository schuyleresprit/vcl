---
layout: page
title: Authors Search
permalink: /az
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>A-Z Dictionary</title>
    <link rel="stylesheet" type="text/css" href="assets/css/az.css">
</head>
<body>
    <div class="summary">
        <div class="left_container">
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        </div>
        <div class="right_container"></div>
    </div>
    <div class="spacer"></div>
    <div class="main_container">
        <div class="sidebar">
            <form class="searchForm">
                <input type="text" class="searchInput" placeholder="Search...">
                <button id="enter" type="submit">Search</button>
            </form>
            <select class="filterDropdown">
                <option value="all">All Categories</option>
                <option value="category1">Language</option>
                <option value="category2">Genre</option>
                <option value="category3">Country</option>
                <option value="category4">Translation</option>
                <option value="category5">Publisher</option>
            </select>
            <select class="sortDropdown">
                <option value="asc">Sort A-Z</option>
                <option value="desc">Sort Z-A</option>
            </select>
            <ul class="wordList">
                <!-- Dictionary entries -->
                <p>A</p>
                <div class ="wordMenuA"></div>
                <p>B</p>
                <div class ="wordMenuB"></div>
                <p>C</p>
                <div class ="wordMenuC"></div>
                <p>D</p>
                <div class ="wordMenuD"></div>
                <p>E</p>
                <div class ="wordMenuE"></div>
                <p>F</p>
                <div class ="wordMenuF"></div>
                <p>G</p>
                <div class ="wordMenuG"></div>
                <p>H</p>
                <div class ="wordMenuH"></div>
                <p>I</p>
                <div class ="wordMenuI"></div>
                <p>J</p>
                <div class ="wordMenuJ"></div>
                <p>K</p>
                <div class ="wordMenuK"></div>
                <p>L</p>
                <div class ="wordMenuL"></div>
                <p>M</p>
                <div class ="wordMenuM"></div>
                <p>N</p>
                <div class ="wordMenuN"></div>
                <p>O</p>
                <div class ="wordMenuO"></div>
                <p>P</p>
                <div class ="wordMenuP"></div>
                <p>Q</p>
                <div class ="wordMenuQ"></div>
                <p>R</p>
                <div class ="wordMenuR"></div>
                <p>S</p>
                <div class ="wordMenuS"></div>
                <p>T</p>
                <div class ="wordMenuT"></div>
                <p>U</p>
                <div class ="wordMenuU"></div>
                <p>V</p>
                <div class ="wordMenuV"></div>
                <p>W</p>
                <div class ="wordMenuW"></div>
                <p>X</p>
                <div class ="wordMenuX"></div>
                <p>Y</p>
                <div class ="wordMenuY"></div>
                <p>Z</p>
                <div class ="wordMenuZ"></div>
                <!-- Add links for other letters -->
            </ul>
        </div>
        <div class="button-container">
            <button id="letter-a" data="data/a.json" target="">A</button>
            <button id="letter-b" data="data/b.json" target="">B</button>
            <button id="letter-c" data="data/c.json" target="">C</button>
            <button id="letter-d" data="data/d.json" target="">D</button>
            <button id="letter-e" data="data/e.json" target="">E</button>
            <button id="letter-f" data="data/f.json" target="">F</button>
            <button id="letter-g" data="data/g.json" target="">G</button>
            <button id="letter-h" data="data/h.json" target="">H</button>
            <button id="letter-i" data="data/i.json" target="">I</button>
            <button id="letter-j" data="data/j.json" target="">J</button>
            <button id="letter-k" data="data/k.json" target="">K</button>
            <button id="letter-l" data="data/l.json" target="">L</button>
            <button id="letter-m" data="data/m.json" target="">M</button>
            <button id="letter-n" data="data/n.json" target="">N</button>
            <button id="letter-o" data="data/o.json" target="">O</button>
            <button id="letter-p" data="data/p.json" target="">P</button>
            <button id="letter-q" data="data/q.json" target="">Q</button>
            <button id="letter-r" data="data/r.json" target="">R</button>
            <button id="letter-s" data="data/s.json" target="">S</button>
            <button id="letter-t" data="data/t.json" target="">T</button>
            <button id="letter-u" data="data/u.json" target="">U</button>
            <button id="letter-v" data="data/v.json" target="">V</button>
            <button id="letter-w" data="data/w.json" target="">W</button>
            <button id="letter-x" data="data/x.json" target="">X</button>
            <button id="letter-y" data="data/y.json" target="">Y</button>
            <button id="letter-z" data="data/z.json" target="">Z</button>
            <!-- Add buttons for other letters -->
        </div>
        <div class="content">
            <!-- Main content goes here -->
        </div>
    </div>
     <script src="assets/author_az.js"></script>
</body>
</html>