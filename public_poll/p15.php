<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1" />

<title>Website Design Ranking</title>

<style>
html, body { margin:0; padding:0; font:16px/1.75 Verdana, Arial, Helvetica, sans-serif }
.page-content { padding:1em; max-width:64em; margin:auto }
.imgsrc{margin-top:10px;width:50px;height:50px;float:right;margin-right:20px;}
.rating { font-size:3em; line-height:1.5; text-align:center; overflow:hidden }
.rating a { position:relative; float:right; color:#bbb; text-decoration:none; letter-spacing:0.125em }
.rating a:first-child { margin-right:0.05em }
.rating a, .rating a:after { transition:color .4s }
.rating a:hover, .rating a:hover:after { -webkit-animation:pop 0.2s; animation:pop 0.2s }
.rating a:active, .rating a:active:after { -webkit-animation:push 0.2s; animation:push 0.2s }
.rating[data-rating] a:hover, .rating[data-rating] a:hover:after, .rating[data-rating] a:hover ~ a, .rating[data-rating] a:hover ~ a:after,
.rating[data-rating] a:focus, .rating[data-rating] a:focus:after, .rating[data-rating] a:focus ~ a, .rating[data-rating] a:focus ~ a:after { color:tomato; outline:none }
.rating-stars { display:inline-block }
.rating-votes { clear:both; font-size:0.275em; line-height:1; color:#999 }
.rating a:before { content:'\2605'; position:absolute; z-index:-1; color:#e5e5e5; transform:scale(1.5); transform-origin:44% 54% }
[data-rating^="1.5"] .star-2:after, [data-rating^="2.5"] .star-3:after, [data-rating^="3.5"] .star-4:after, [data-rating^="4.5"] .star-5:after { content:'\2605'; position:absolute; left:0; right:56%; overflow:hidden }
[data-rating^="1"] .star-1, [data-rating^="1.5"] .star-2:after, 
[data-rating^="2"] .star-2, [data-rating^="2"] .star-2 ~ a, [data-rating^="2.5"] .star-3:after, 
[data-rating^="3"] .star-3, [data-rating^="3"] .star-3 ~ a, [data-rating^="3.5"] .star-4:after, 
[data-rating^="4"] .star-4, [data-rating^="4"] .star-4 ~ a, [data-rating^="4.5"] .star-5:after, 
[data-rating^="5"] .star-5, [data-rating^="5"] .star-5 ~ a { color:orange }
@-webkit-keyframes pop { 50% { -webkit-transform:scale(1.2) } }
@keyframes pop { 50% { transform:scale(1.2) } }
@-webkit-keyframes push { 50% { -webkit-transform:scale(0.8) } }
@keyframes push { 50% { transform:scale(0.8) } }
#rating-message { font-size:0.275em; font-weight:bold; color:transparent }
#rating-message.voted { -webkit-animation:pop 0.2s ease 0.2s; animation:pop 0.2s ease 0.2s; color:#999; transition:color .4s }
/* U+FE0E VARIATION SELECTOR-15 needed for Safari - https://stackoverflow.com/a/38362138 / http://unicode.org/emoji/charts/emoji-variants.html#2b1c */
#rating-message.voted:before { content:'\2714\fe0e'; display:inline; vertical-align:middle; font-size:3.5em; line-height:1.5; margin:0 0.125em 0 -0.5em; color:yellowgreen }
.imgmain{width:100%;height:70%;}
</style>

<!--[if lte IE 8]>
<style>
#rating-message.voted:before { font-size:1em } 
</style>
<![endif]-->
</head>
<body>
<h2 style="text-align:center;">Website Design Review : User Review</h2>
<p style="text-align:center;">
<img src=images/15.png class=imgmain>
</p>
<div class="page-content">
<?php 
$file = 'data/15.txt';
$all_lines = file($file, FILE_IGNORE_NEW_LINES);
foreach($all_lines as $line){
	list($item, $num) = explode('||', $line);
	$count[$item] = $num;
	}
if(array_sum($count) != 0){
	$avg = number_format(($count['star-1']*1 + $count['star-2']*2 + $count['star-3']*3 + $count['star-4']*4 + $count['star-5']*5) / array_sum($count),2,'.','');
	$intVal = intval($avg);
	$round = ($avg - $intVal < .5) ? $intVal : round($intVal).'.5';
	} else {
	$avg = $round = 0;
	}
?>

<div class="rating" data-rating="<?php echo $round;?>">
	<div class="rating-stars">
		<a href="#5" class="click-trigger star-5" data-click-id="star-5" title="Vote 5 stars">&#x2605</a>
		<a href="#4" class="click-trigger star-4" data-click-id="star-4" title="Vote 4 stars">&#x2605</a>
		<a href="#3" class="click-trigger star-3" data-click-id="star-3" title="Vote 3 stars">&#x2605</a>
		<a href="#2" class="click-trigger star-2" data-click-id="star-2" title="Vote 2 stars">&#x2605</a>
		<a href="#1" class="click-trigger star-1" data-click-id="star-1" title="Vote 1 star">&#x2605</a>
	</div>
	<div class="rating-votes">
		Rated <span id="count-avg"><?php echo $avg;?></span>/5 (<span id="count-total"><?php echo array_sum($count);?></span> Votes)
	</div>
	<div id="rating-message"></div>
</div>
<a href=p16.php>
<div><h2 style="float:left;text-decoration:none;color:#000;margin-left:40px">Next</h2>
<img src="images/ar.png" class=imgsrc>
</div>
</a>
</div>

<script>
(function(){
var clicks = document.querySelectorAll('.click-trigger'),
    voted = localStorage.getItem('rating'),
    message = document.getElementById('rating-message'),
    length = clicks.length, i, id, post, req, countArray;
for(i = 0; i < length; i++){
	clicks[i].onclick = function(){
		if (voted == 'voted') {
			} else {
			id = this.getAttribute('data-click-id');
			post = 'id='+id; // post string
			req = new XMLHttpRequest();
			req.open('POST', 'c15.php', true);
			req.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
			req.onreadystatechange = function(){
				if (req.readyState != 4 || req.status != 200) return; 
				countArray = req.responseText.split('||');
				document.getElementById('count-avg').innerHTML = countArray[0];
				document.getElementById('count-total').innerHTML = countArray[1];
				document.querySelector('.rating').setAttribute('data-rating', countArray[2]);
				};
			req.send(post);
			}
		}
	}
})();

(function(l){var i,s={touchend:function(){}};for(i in s)l.addEventListener(i,s)})(document); // sticky hover fix in iOS
</script>

</body>
</html>
