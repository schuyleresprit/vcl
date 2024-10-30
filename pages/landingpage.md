---
layout: homedefault
permalink: /
---

<div class="row">
<div class="col-sm-1">

</div>

<div class="col-sm-10">
<h1> Welcome to <br> Visualizing Caribbean Literature</h1>
<div class="button">
<a href="{{ site.baseurl }}/home/"> ENTER</a>
</div>
</div>

<div class="col-sm-1">

</div>

</div>

<style>

@-webkit-keyframes bg-scrolling-reverse {
	100% {
		background-position: 300% 0px;
	}
}
@-moz-keyframes bg-scrolling-reverse {
	100% {
		background-position: 300% 0px;
	}
}
@-o-keyframes bg-scrolling-reverse {
	100% {
		background-position: 300% 0px;
	}
}
@keyframes bg-scrolling-reverse {
	100% {
		background-position: 300% 0px;
	}
}
@-webkit-keyframes bg-scrolling {
	0% {
		background-position: 0px 0px;
	}
}
@-moz-keyframes bg-scrolling {
	0% {
		background-position: 0px 0px;
	}
}
@-o-keyframes bg-scrolling {
	0% {
		background-position: 0px 0px;
	}
}
@keyframes bg-scrolling {
	0% {
		background-position: 0px 0px;
	}
}

/* Animation End */

body{
	background: url(" {{ site.baseurl }}/assets/img/background-3.png");
	background-attachment: fixed;
	/* Add Animation */
	-webkit-animation: bg-scrolling-reverse 30s infinite;
	/* Safari 4+ */
	-moz-animation: bg-scrolling-reverse 30s infinite;
	/* Fx 5+ */
	-o-animation: bg-scrolling-reverse 30s infinite;
	/* Opera 12+ */
	animation: bg-scrolling-reverse 30s infinite;
	/* IE 10+ */
	-webkit-animation-timing-function: linear;
	-moz-animation-timing-function: linear;
	-o-animation-timing-function: linear;
	animation-timing-function: linear;
}

.background {
    background: none;
}

.overlay {
    background: none;
}

.col-sm-10 h1 {
    font-family: Arial Black;
    text-shadow: 2px 2px 3px #999;
}

.col-sm-10 {
    text-align: center;
    opacity: 0.9;
}

nav.navbar-0.navbar-expand-lg.navbar-dark.bg-dark {
    display: none;
}

.footer {
    display: none;
}

.button a {
    color: #fff;
    background: #198754;
    text-decoration: none;
    padding: 25px 63px;
    border-radius: 19px;
    font-weight: 600;
}

.button {
    margin-top: 60px;
}

</style>