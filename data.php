<?php

$result = mysql_query("SELECT field_name, field_value
                       FROM the_table");
$to_encode = array();
while($row = mysql_fetch_assoc($result)) {
  $to_encode[] = $row;
}
echo json_encode($to_encode);


?>
