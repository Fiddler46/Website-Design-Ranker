<?php 

$file = 'counter.txt'; // path to text file that stores counts
$fh = fopen($file, 'r+');
$id = $_REQUEST['id']; // posted from page
$lines = '';
while(!feof($fh)){
	$line = explode('||', fgets($fh));
	$item = trim($line[0]);
	$num = trim($line[1]);
	if(!empty($item)){
		if($item == $id){
			$num++; // increment count by 1
			}
		$lines .= "$item||$num\r\n";
		}
	} 
file_put_contents($file, $lines);
fclose($fh);


/* #### - rating average and total votes - #### */

$all_lines = file($file, FILE_IGNORE_NEW_LINES);
foreach($all_lines as $line){
	list($item, $num) = explode('||', $line);
	$count[$item] = $num;
	}
$avg = ($count['star-1']*1 + $count['star-2']*2 + $count['star-3']*3 + $count['star-4']*4 + $count['star-5']*5) / array_sum($count);
$intVal = intval($avg);
$round = ($avg - $intVal < .5) ? $intVal : round($intVal).'.5';

echo number_format($avg,2,'.','').'||'.array_sum($count).'||'.$round; // sent back to page

?>	