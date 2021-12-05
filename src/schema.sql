DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS SubProjects;
DROP TABLE IF EXISTS Bugs;

CREATE TABLE Projects (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE
);

CREATE TABLE SubProjects (
    id SERIAL PRIMARY KEY,
    name TEXT, 
    description TEXT,
    project_id REFERENCES Projects
);

CREATE TABLE Bugs (
    id SERIAL PRIMARY KEY,
    name TEXT,
    description TEXT,
    priority INTEGER,
    status INTEGER,
    subproject_id REFERENCES SubProjects
);