



<?php
$servername = "mysql.queryquarry.tech";
$username = "scopesdbu";
$password = "mmlja5ja5ja%";
$dbname = "quora_query_db";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


$sql = "SELECT max(scrape_id) as start FROM predicts";
$result = $conn->query($sql);
$start_idx = $result -> fetch_assoc()[start];
$end_idx = intval($start_idx) + 50;


$sql = "SELECT * FROM scrapes WHERE id between $start_idx and $end_idx";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
	// output data of each row
	$to_encode = array();
    while($row = $result->fetch_assoc()) {
		$to_encode[] = $row;
	}
	echo json_encode($to_encode);
} else {
    echo "0 results";
}

$conn->close();
?>
