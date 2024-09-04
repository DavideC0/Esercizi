CREATE TYPE Strutturato AS ENUM ('Ricercatore', 'Professore Associato', 'Professore Ordinario');

CREATE TYPE LavoroProgetto AS ENUM ('Ricerca e Sviluppo', 'Dimostrazione', 'Management', 'Altro');

CREATE TYPE LavoroNonProgettuale AS ENUM ('Didattica', 'Ricerca', 'Missione', 'Incontro Dipartimentale', 'Incontro Accademico', 'Altro');

CREATE TYPE CausaAssenza AS ENUM ('Chiusura Universitaria', 'Maternita', 'Malattia');

CREATE DOMAIN PosInteger AS INTEGER CHECK (VALUE >= 0);

CREATE DOMAIN StringaM AS VARCHAR(100);

CREATE DOMAIN NumeroOre AS INTEGER CHECK (VALUE BETWEEN 0 AND 8);

CREATE DOMAIN Denaro AS REAL CHECK (VALUE >= 0);

CREATE TABLE Persona (
    id PosInteger PRIMARY KEY,
    nome StringaM NOT NULL,
    cognome StringaM NOT NULL,
    posizione Strutturato NOT NULL,
    stipendio Denaro NOT NULL
);

CREATE TABLE Progetto (
    id PosInteger PRIMARY KEY,
    nome StringaM NOT NULL UNIQUE, -- VincoloDB.1
    inizio DATE NOT NULL,
    fine DATE NOT NULL,
    budget Denaro NOT NULL,
    CHECK (inizio < fine) -- VincoloDB.2
);

CREATE TABLE WP (
    progetto PosInteger NOT NULL,
    id PosInteger NOT NULL,
    nome StringaM NOT NULL,
    inizio DATE NOT NULL,
    fine DATE NOT NULL,
    PRIMARY KEY (progetto, id),
    UNIQUE (progetto, nome), -- VincoloDB.4
    CHECK (inizio < fine), -- VincoloDB.3
    FOREIGN KEY (progetto) REFERENCES Progetto(id) -- VincoloDB.5
);

CREATE TABLE AttivitaProgetto (
    id PosInteger PRIMARY KEY,
    persona PosInteger NOT NULL,
    progetto PosInteger NOT NULL,
    wp PosInteger NOT NULL,
    giorno DATE NOT NULL,
    tipo LavoroProgetto NOT NULL,
    oreDurata NumeroOre NOT NULL,
    FOREIGN KEY (persona) REFERENCES Persona(id), -- VincoloDB.6
    FOREIGN KEY (progetto, wp) REFERENCES WP(progetto, id) -- VincoloDB.7
);

CREATE TABLE AttivitaNonProgettuale (
    id PosInteger PRIMARY KEY,
    persona PosInteger NOT NULL,
    tipo LavoroNonProgettuale NOT NULL,
    giorno DATE NOT NULL,
    oreDurata NumeroOre NOT NULL,
    FOREIGN KEY (persona) REFERENCES Persona(id) -- VincoloDB.8
);

CREATE TABLE Assenza (
    id PosInteger PRIMARY KEY,
    persona PosInteger NOT NULL,
    tipo CausaAssenza NOT NULL,
    giorno DATE NOT NULL,
    UNIQUE (persona, giorno), -- VincoloDB.9
    FOREIGN KEY (persona) REFERENCES Persona(id) -- VincoloDB.10
);
