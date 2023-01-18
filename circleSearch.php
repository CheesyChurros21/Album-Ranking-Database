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

$circleAlbums = array();
$counter = 0;

$searchType = $_POST['circleSearch'];

if (mysqli_num_rows($result) > 0) {
    while($row = mysqli_fetch_assoc($result)) {

        if ($row["circleName"] == $searchType) {
            array_push($circleAlbums, $row);
        }
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
    "<header class='websiteTitle'>"
);

echo(
    "Album Database (" . $searchType  . " Edition)"
);

echo(
    "</header>"
);

print("<br>");

echo(
    "<main><section class='mediumText'>"
);

print("<br><br><br>");

for ($i = 0; $i < count($circleAlbums); $i = $i + 1) {

    $pictureURL = $circleAlbums[$i]["pictureURL"];
    $albumURL = $circleAlbums[$i]["albumURL"];
    echo(
        "Album Number: " . $circleAlbums[$i]["orderNumber"] . "<br><br><br> <img src='$pictureURL' width='50%' height='50%'> <br> <a href=" . $albumURL . " target='_blank' rel='noopener noreferrer'>" . $circleAlbums[$i]["albumTitle"] . "</a><br> Total Songs: " . $circleAlbums[$i]["songAmount"] . "<br> Subjective Ratings: &nbsp;&nbsp;&nbsp;&nbsp; Jordan - " . $circleAlbums[$i]["subjectiveJordan"] . "/10 &nbsp;&nbsp;&nbsp;&nbsp; Nick - " . $circleAlbums[$i]["subjectiveNick"] . "/10" . "<br> &nbsp; Objective Ratings: &nbsp;&nbsp;&nbsp;&nbsp; Jordan - " . $circleAlbums[$i]["objectiveJordan"] . "/10 &nbsp;&nbsp;&nbsp;&nbsp; Nick - " . $circleAlbums[$i]["objectiveNick"] . "/10 <br><br><br><br><br><br>"
    );
    
}

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