<!DOCTYPE html>

<html>

<?php

$host = "placeholder";
$database = "placeholder";
$username = "placeholder";
$password = "placeholder";

$connect = mysqli_connect($host, $username, $password, $database) 
or die(mysqli_error($connect));

if($connect){
    print("Connection Established Successfully<br>");
}

else{
    print("Connection Failed<br>");
}

$sql = "SELECT * FROM Albums";
$result = mysqli_query($connect, $sql);

$stringSearchTypes = array("circleName", "albumTitle");
$infoList = array();
$selectedSearchList = array();
$sortedInfoList = array();
$counter = 0;

$searchType = $_POST['searchType'];
$sortType = $_POST['sortType'];

if (mysqli_num_rows($result) > 0) {
    while($row = mysqli_fetch_assoc($result)) {
        $infoList[$counter][0] = $row["orderNumber"];
        $infoList[$counter][1] = $row["circleName"];
        $infoList[$counter][2] = $row["albumTitle"];
        $infoList[$counter][3] = $row["songAmount"];
        $albumURL = $row["albumURL"];
        $infoList[$counter][4] = "<a href=$albumURL>Album Redirect Link</a>";
        $pictureURL = $row["pictureURL"];
        $infoList[$counter][5] = "<a href=$pictureURL>Picture Redirect Link</a>";
        $infoList[$counter][6] = $row["subjectiveJordan"];
        $infoList[$counter][7] = $row["subjectiveNick"];
        $infoList[$counter][8] = $row["objectiveJordan"];
        $infoList[$counter][9] = $row["objectiveNick"];



        $selectedSearchList[$counter] = $row[$searchType];
        $counter = $counter + 1;
    }

    while (count($selectedSearchList) > 0) {

        $biggest = $selectedSearchList[0];
        $index = 0;

        for ($ii = 1; $ii < count($selectedSearchList); $ii = $ii + 1) {

            if (in_array($searchType, $stringSearchTypes)) {

                if (strcasecmp($biggest, $selectedSearchList[$ii]) <= 0) {

                    $biggest = $selectedSearchList[$ii];
                    $index = $ii;
    
                }

            }

            else {

                if ($biggest <= $selectedSearchList[$ii]) {

                    $biggest = $selectedSearchList[$ii];
                    $index = $ii;

                }
            }

        }

        if ($sortType == "Ascending Order" ) {
            array_unshift($sortedInfoList, $infoList[$index]);
        }

        else {
            array_push($sortedInfoList, $infoList[$index]);
        }

        array_splice($infoList, $index, 1);
        array_splice($selectedSearchList, $index, 1);

    }

} 

else {
  echo "No results.<br>";
}

mysqli_close($connect);

?>

<?php

echo(
    "<body>"
);

echo(
    "<head>
        <link rel='stylesheet' href='albumWebsite.css'>
    </head>"
);

echo(
    "<header class='websiteTitle'>
        Album Database
    </header>"
);

print("<br>");

echo(
    "<main><section class='mediumText'>"
);

echo("<table border='1' align='center'>");

echo("<tr>");

echo(
    "<th>Database Number</th>
    <th>Circle Name</th>
    <th>Album Title</th>
    <th>Song Amount</th>
    <th>Album URL</th>
    <th>Picture URL</th>
    <th>Subjective Jordan</th>
    <th>Subjective Nick</th>
    <th>Objective Jordan</th>
    <th>Objective Nick</th>"
);

echo("</tr>");

for ($i = 0; $i < count($sortedInfoList); $i = $i + 1) {

    echo("<tr>");

    for ($ii = 0; $ii < count($sortedInfoList[$i]); $ii = $ii + 1) {

        echo "<td>";
        echo $sortedInfoList[$i][$ii];
        echo "</td>";
        
    }

    echo("</tr>");

}

echo("</table>");

echo(
    "</section>"
);

echo(
    '<form method="post" action="homePage.php">
        <input type="submit" id="bottomRight" value="Go Back"/>
    </form>'
);

echo(
    "</main>"
);

echo(
    "</body>"
);

?>

</html>