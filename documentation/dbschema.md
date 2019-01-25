TABLE task ( </br>
    id INTEGER NOT NULL, </br>
    date_created DATETIME, </br>
    date_modified DATETIME, </br>
    name VARCHAR(144) NOT NULL, </br>
    done BOOLEAN NOT NULL, </br>
    PRIMARY KEY (id), </br>
    CHECK (done IN (0, 1)) </br>
)
