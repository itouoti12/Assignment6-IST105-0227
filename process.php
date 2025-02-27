<?php
$num1 = escapeshellarg($_POST['num1']);
$num2 = escapeshellarg($_POST['num2']);
$num3 = escapeshellarg($_POST['num3']);
$num4 = escapeshellarg($_POST['num4']);
$num5 = escapeshellarg($_POST['num5']);

$command = escapeshellcmd("python3 data_management.py $num1 $num2 $num3 $num4 $num5");

$output = shell_exec($command);

echo "$output";
?>