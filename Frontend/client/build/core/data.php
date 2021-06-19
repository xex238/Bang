<?php
$conn = mysqli_connect("localhost", "root", "", "bang");
$result = mysqli_query($conn, "SELECT name,games,sex FROM users");
$data = array();
while ($row = mysqli_fetch_object($result))
{
    array_push($data, $row);
}
echo json_encode($data);
exit();
         ?>