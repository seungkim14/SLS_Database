CREATE TABLE USER
    (Username     VARCHAR(100)                                         NOT NULL,
     Email        VARCHAR(100)                                         NOT NULL,
     Password     VARCHAR(100)                                         NOT NULL,
     UserType     ENUMB(‘City Scientist’, ‘City Official’, ‘Admin’)    NOT NULL,
     CONSTRAINT USERPK
         PRIMARY KEY(Username)
     CONSTRAINT USERCK
         UNIQUE(Email)) engine = innodb;

CREATE TABLE CITYOFFICIAL
    (Username     VARCHAR(100)                                         NOT NULL,
     Title        VARCHAR(100)                                         NOT NULL,
     Status       ENUM(‘Pending’, ‘Accepted’, ‘Rejected’)              NOT NULL,
     City         VARCHAR(100)                                         NOT NULL,
     State        VARCHAR(100)                                         NOT NULL,
     CONSTRAINT COPK
         PRIMARY KEY(Username),
     CONSTRAINT COFKA
         FOREIGN KEY(Username) REFERENCES USER(Username)
             ON DELETE CASCADE ON UPDATE CASCADE,
     CONSTRAINT COFKB
         FOREIGN KEY(City, State) REFERENCES LOCATION(City, State)
             ON DELETE CASCADE ON UPDATE CASCADE) engine = innodb;

CREATE TABLE LOCATION
    (City         VARCHAR(100)                                         NOT NULL,
     State        VARCHAR(100)                                         NOT NULL,
     CONSTRAINT LOCPK
         PRIMARY KEY(City, State)) engine = innodb;

CREATE TABLE POI
    (Name         VARCHAR(100)                                         NOT NULL,
     Flag         BOOLEAN                                              NOT NULL,
     DateFlagged  DATE                                                         ,
     Zipcode      INT                                                  NOT NULL,
     City         VARCHAR(100)                                         NOT NULL,
     STATE        VARCHAR(100)                                         NOT NULL,
     CONSTRAINT POIPK
         PRIMARY KEY(Name),
     CONSTRAINT POIFK
         FOREIGN KEY(City, State) REFERENCES LOCATION(City, State),
             ON DELETE CASCADE ON UPDATE CASCADE) engine = innodb;

CREATE TABLE DATAPOINT
    (TimeDate     TIMESTAMP                                            NOT NULL,
     Name         VARCHAR(100)                                         NOT NULL,
     Status       ENUM(‘Pending’,’Accepted’,’Rejected’)                NOT NULL,
     DataValue    INT                                                  NOT NULL,
     Type         VARCHAR(100)                                         NOT NULL,
     CONSTRAINT DPPK
         PRIMARY KEY(TimeDate, Name)
     CONSTRAINT DPFKA
         FOREIGN KEY(Name) REFERENCES POI(Name)
             ON DELETE CASCADE ON UPDATE CASCADE,
     CONSTRAINT DPFKB
         FOREIGN KEY(Type) REFERENCES DATATYPE(Type)
             ON DELETE CASCADE ON UPDATE CASCADE) engine = innodb;

CREATE TABLE DATATYPE
    (Type         VARCHAR(100)                                         NOT NULL,
         CONSTRAINT DTPK
             PRIMARY KEY(Type)) engine = innodb;
