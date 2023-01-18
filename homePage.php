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

$circleList = array();
$counter = 0;


if (mysqli_num_rows($result) > 0) {
    while($row = mysqli_fetch_assoc($result)) {
        if (!in_array($row["circleName"], $circleList)) {
            $circleList[$counter] = $row["circleName"];
            $counter = $counter + 1;
        }
    }
}

usort($circleList, 'strnatcasecmp');

mysqli_close($connect);

?>

<script>

function checkEmptySearchSortSubmit() {
    if (document.getElementById("searchType").value == "No Input Detected" && document.getElementById("sortType").value == "No Input Detected") {
        alert("No Option Submitted For Both Search Type and Sort Type. \nMake Sure to Select An Option.")
        return false
    }

    else if (document.getElementById("searchType").value == "No Input Detected") {
        alert("No Option Submitted For Search Type. \nMake Sure to Select An Option.")
        return false
    }

    else if (document.getElementById("sortType").value == "No Input Detected") {
        alert("No Option Submitted For Sort Type. \nMake Sure to Select An Option.")
        return false
    }
}

function checkEmptyCircleSubmit() {
    if (document.getElementById("circleSearch").value == "No Input Detected") {
        alert("No Option Submitted For Circle Search. \nMake Sure to Select An Option.")
        return false
    }
}

</script>

<?php

echo(
    "<body>"
);

echo(
    "<head>
        <link rel='stylesheet' href='website.css'>
    </head>"
);

echo(
    "<header class='websiteTitle'>
        Album Database Browser
    </header>"
);

print("<br>");

echo(
    "<main><section class='mediumText center'>"
);

echo(
'<form action="sortChoice.php" method="post" onsubmit="return checkEmptySearchSortSubmit()">
    <label for="searchType">Search Type</label>

    <select id="searchType" name="searchType">

        <option value="No Input Detected" style="display: none;">Select An Option</option>
        <option value="orderNumber">Date Added</option>
        <option value="circleName">Circle Name</option>
        <option value="albumTitle">Album Title</option>
        <option value="songAmount">Song Amount</option>
        <option value="subjectiveJordan">Jordan Rating (Subjective)</option>
        <option value="objectiveJordan">Jordan Rating (Objective)</option>
        <option value="subjectiveNick">Nick Rating (Subjective)</option>
        <option value="objectiveNick">Nick Rating (Objective)</option>

    </select>

    <br>
    
    <label for="sortType"> Sort Type: </label>

    <select id="sortType" name="sortType">

        <option value="No Input Detected" style="display: none;">Select An Option</option>
        <option value="Ascending Order">Ascending Order</option>
        <option value="Descending Order">Descending Order</option>

    </select>

    <br><br>

    <input type="submit" value="Submit">

</form>
<br><br><br><br><br><br>'
);

?>

<?php

echo(
    '<form action="circleSearch.php" method="post" onsubmit="return checkEmptyCircleSubmit()">
        <label for="circleSearch">Circle Search</label>
    
        <select id="circleSearch" name="circleSearch">

            <option value="No Input Detected" style="display: none;">Select An Option</option>
');

for ($i = 0; $i < count($circleList); $i = $i + 1) {
    echo('<option value="' . $circleList[$i] . '">' . $circleList[$i] . '</option>');
}

echo('
        </select>
    
        <br><br>
    
        <input type="submit" value="Submit">
    
    </form>
    <br><br><br><br><br><br>'
);



?>

<?php

echo(
    "</section></main>"
);

echo(
    "</body>"
);

?>

</html>