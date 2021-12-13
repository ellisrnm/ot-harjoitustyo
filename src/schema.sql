DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS SubProjects;
DROP TABLE IF EXISTS Bugs;

CREATE TABLE Projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);

CREATE TABLE SubProjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT, 
    description TEXT,
    project_id INTEGER REFERENCES Projects,
    UNIQUE (project_id, name)
);

CREATE TABLE Bugs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    priority INTEGER,
    status INTEGER,
    subproject_id INTEGER REFERENCES SubProjects,
    UNIQUE (subproject_id, name)
);