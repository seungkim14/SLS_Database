1) Login Screen

// When user clicks login, retrieve password from the database that matches the $Username
SELECT Password from USER where Username = $Username;

// Check user type
SELECT UserType from USER where Username = $Username AND Password = $Password;

2) Register Screen

// Retrieve cities to populate city dropdown menu
SELECT DISTINCT City from LOCATION;

// Retrieve states to populate state dropdown menu
SELECT DISTINCT State from LOCATION;

// Retrieve all the usernames to check if the username is already in the database
SELECT Username from USER;

// Retrieve all email addresses to check if the email address is already in the database
SELECT Email from USER;

// Check if the city and state match
SELECT State from LOCATION where City = $City;

// When select create and the city official credentials are filled, insert City Official into CityOfficial
INSERT INTO CITYOFFICIAL VALUES($Username, $Title, $Status, $City, $State);

// When select create, insert User into User
INSERT INTO USER VALUES($Username, $Email, $Password, $UserType);

=======================City Scientist=======================

3) Add a new data point Screen

// Retrieve POI location names to populate dropdown menu
SELECT DISTINCT Name from POI;

// Retrieve DataType to populate dropdown menu
SELECT DISTINCT Type from DATATYPE;

// When click submit, insert datapoint into Datapoint
INSERT INTO DATAPOINT VALUES($TimeDate, $Name, $Status, $DataValue, $Type);

4) Add a new location Screen

// Retrieve cities to populate city dropdown menu
SELECT DISTINCT City from LOCATION;

// Retrieve states to populate state dropdown menu
SELECT DISTINCT State from LOCATION;

// When click submit, insert new location into POI
INSERT INTO POI (Name, Zipcode, City, State) VALUES($Name, $Zipcode, $City, $State);

=======================Admin=======================
5) Pending data points screen

// Retrieve all the pending data points
SELECT Name, Type, DataValue, TimeDate FROM DATAPOINT WHERE Status = 'Pending';

// Accept pending data points
UPDATE DATAPOINT SET Status = 'Accepted' where TimeDate = $TimeDate AND Name = $Name;

// Reject pending data points
UPDATE DATAPOINT SET Status = 'Rejected' where TimeDate = $TimeDate AND Name = $Name;

6) Pending city officials screen

// Retrieve all the pending city officials
SELECT USER.Username, Email, City, State, Title FROM USER, CITYOFFICIAL WHERE USER.Username = CITYOFFICIAL.Username AND Status = 'Pending';

// Accept pending city official
UPDATE CITYOFFICIAL SET Status='Accepted' WHERE Username = $Username;

// Reject pending city official
UPDATE CITYOFFICIAL SET Status='Rejected' WHERE Username = $Username;

=======================City Official=======================
7) View POIs Screen

// Retrieve Name from POI to populate POI location name
SELECT DISTINCT Name from POI ORDER BY Name;

// Retrieve cities to populate city dropdown menu
SELECT DISTINCT City from LOCATION ORDER BY City;

// Retrieve states to populate state dropdown menu
SELECT DISTINCT State from LOCATION ORDER BY State;

// Retrieve all the filtered POIs (Using string concatenation)
FilterQuery = "SELECT Name, City, State, Zipcode, Flag, DateFlagged FROM POI WHERE "

if location != "":
    FilterQuery += "Name = '"
    FilterQuery += location
    FilterQuery += "' AND "
if city != "":
    FilterQuery += "City = '"
    FilterQuery += city
    FilterQuery += "' AND "
if state != "":
    FilterQuery += "State = '"
    FilterQuery += state
    FilterQuery += "' AND "
if zip_code != "":
    FilterQuery += "Zipcode = '"
    FilterQuery += zip_code
    FilterQuery += "' AND "
FilterQuery += "Flag = '"
FilterQuery += str(flagged_yn)
FilterQuery += "' AND "
if DateFlaggedStart != "":
    FilterQuery += "DateFlagged >= '"
    FilterQuery += DateFlaggedStart
    FilterQuery += "' AND "
if DateFlaggedEnd != "":
    FilterQuery += "DateFlagged <= '"
    FilterQuery += DateFlaggedEnd
    FilterQuery += "' AND "
FilterQuery = FilterQuery[:-5]
FilterQuery += ";"

8) POI detail screen

// Retrieve Type to populate dropdown menu
SELECT Type FROM DATATYPE ORDER BY Type;

// Retrieve all the filtered data points (Using string concatenation)
DetailFilterQuery = "SELECT Type, DataValue, TimeDate FROM DATAPOINT WHERE "
DetailFilterQuery += "Name = '%s' AND " % $Selected_POI
if Type == "Mold":
    DetailFilterQuery += "Type = 'Mold' AND "
elif Type == "Air Quality":
    DetailFilterQuery += "Type = 'Air Quality' AND "
if DataValueStart > 0:
    DetailFilterQuery += "DataValue >= '"
    DetailFilterQuery += str(DataValueStart)
    DetailFilterQuery += "' AND "
if DataValueEnd > 0:
    DetailFilterQuery += "DataValue <= '"
    DetailFilterQuery += str(DataValueEnd)
    DetailFilterQuery += "' AND "
if TimeDateStart != "":
    DetailFilterQuery += "TimeDate >= '"
    DetailFilterQuery += str(TimeDateStart)
    DetailFilterQuery += "' AND "
if TimeDateEnd != "":
    DetailFilterQuery += "TimeDate <= '"
    DetailFilterQuery += str(TimeDateEnd)
    DetailFilterQuery += "' AND "
DetailFilterQuery += "Status = 'Accepted' ORDER BY TimeDate DESC"
DetailFilterQuery += ";"

// Retrieve current flag status
SELECT Flag FROM POI WHERE Name = $Name;

// Flag unflagged POI
UPDATE POI SET Flag = '1', DateFlagged = $DateFlagged WHERE Name = $Name;

// Unflag flagged POI
UPDATE POI SET Flag = '0', DateFlagged = NULL WHERE Name = $Name;

9) POI Report Screen

// Retrieve all POI locations
SELECT DISTINCT Name, City, State, Flag from POI ORDER BY Name;

// Retrieve the number of Mold data type
for each $Name
    SELECT COUNT(DataValue) FROM DATAPOINT Where Name = $Name AND Type = 'Mold' AND Status = 'Accepted';

    // Retrieve the Min value of Mold data type
    SELECT MIN(DataValue) FROM DATAPOINT Where Name = $Name AND Type = 'Mold' AND Status = 'Accepted';

    // Retrieve the Avg Value of Mold data type
    SELECT AVG(DataValue) FROM DATAPOINT Where Name = $Name AND Type = 'Mold' AND Status = 'Accepted';

    // Retrieve the Max value of Mold data type
    SELECT MAX(DataValue) FROM DATAPOINT Where Name = $Name AND Type = 'Mold' AND Status = 'Accepted';

    // Retrieve the number of Air Quality data type
    SELECT COUNT(DataValue) FROM DATAPOINT Where Name = $Name AND Type = 'Air Quality' AND Status = 'Accepted';

    // Retrieve the Min value of Air Quality data type
    SELECT MIN(DataValue) FROM DATAPOINT Where Name = $Name AND Type = 'Air Quality' AND Status = 'Accepted';

    // Retrieve the Avg Value of Air Quality data type
    SELECT AVG(DataValue) FROM DATAPOINT Where Name = $Name AND Type = 'Air Quality' AND Status = 'Accepted';

    // Retrieve the Max value of Air Quality data type
    SELECT MAX(DataValue) FROM DATAPOINT Where Name = $Name AND Type = 'Air Quality' AND Status = 'Accepted';
end for
