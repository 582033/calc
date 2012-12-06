<?
function cnt($num1, $num2, $operator){	//	{{{
	switch ($operator) {
		case '+':	
			$return = $num1 + $num2;
			break;
		case '-':	
			$return = $num1 - $num2;
			break;
		case '*':	
			$return = $num1 * $num2;
			break;
		case '/':	
			$return = $num1 / $num2;
			break;
	}
	return $return;
}	//	}}}

function symbol($art, $params){	//	{{{
	foreach ($art as $k => $v) {
		if(in_array($v, $params)){
			$v = cnt($art[$k-1], $art[$k+1], $v);	
			array_splice($art, $k-1, 3, array($v));
			return symbol($art, $params);
		}
	}
	return $art;
}	//	}}}

function sout($arr) {	//	{{{
	$a = symbol($arr, array('*', '/'));
	return symbol($a, array('+', '-'));
}	//	}}}
	//if (in_array('(', $num)) return sou($num);

function brackets($arr, $mark=array()) {	//	{{{
	$new = array();
	foreach ($arr as $k => $v) {
		$new[] = str_replace('(', ')', $v);
		if (in_array($v, array(')'))){
			$mark[] = $k;
			array_pop($new);
			$new = array_reverse($new);
			return brackets($new, $mark);
		}
	}
	$return = array(sout($arr), $mark);
	return $return;
}	//	}}}	


function sou($num){
	$arr = brackets($num);
	if (isset($arr[1]) && $arr[1] != array()){
		$a = $arr[1][0];
		$b = $arr[1][1];
		array_splice($num, $a-$b-1, $b+2, $arr[0]);
	}
	if (in_array('(', $num)) return sou($num);
	print_r(sout($num));
}

$num = array('5', '+', '1', '*', '(',  '(', '(', '8', '+', '5', '-', '1', ')', '+', '3', ')', '/', '5', ')', '*', '10');
//$num = array('5', '+', '1', '*', '(',  '(', '12', '+', '3', ')', '/', '5', ')', '*', '10');
sou($num);
print"\n";
