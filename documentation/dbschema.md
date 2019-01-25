TABLE task (
    id INTEGER NOT NULL, 
    date_created DATETIME, 
    date_modified DATETIME, 
    name VARCHAR(144) NOT NULL, 
    done BOOLEAN NOT NULL, 
    PRIMARY KEY (id), 
    CHECK (done IN (0, 1))
)
