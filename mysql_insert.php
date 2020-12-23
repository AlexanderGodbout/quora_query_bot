
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


$proj = isset($_POST['entry'])?$_POST['entry']:'';


#$json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

$json = '{"scrape_id":2,"model":"Alex","predict_type":"Ambiguity","prediction":-1, "version":"0.0.0.0"}';

#$json = $proj;
$json_php = json_decode($json, True);

var_dump($json_php);

var_dump($json_php["scrape_id"]);
$element = $json_php[scrape_id];
$sql = "INSERT INTO predicts (scrape_id, model, predict_type, prediction, version) VALUES ('" 
. $json_php[scrape_id] . "',"
. "'" . $json_php[model] . "',"
. "'" . $json_php[predict_type] . "',"
. "'" . $json_php[prediction] . "',"
. "'" . $json_php[version] . "')"
;
var_dump($sql);

#$sql = "INSERT INTO test (id) VALUES ('$proj')";
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

