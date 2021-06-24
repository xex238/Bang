<?php
require_once 'config.php';

$name = trim($_POST['name']);
$email = trim($_POST['email']);
$text = trim($_POST['text']);

if ($name =='' OR $text=='' OR $email==''){
    echo 2;
    die;
}

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sql = "INSERT INTO contact (name, email, text) VALUES ('".$name."', '".$email."', '".$text."')";

if ($conn->query($sql) === TRUE) {
    echo 1;
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>