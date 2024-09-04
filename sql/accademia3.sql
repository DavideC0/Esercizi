-- Definizione del dominio 'Strutturato'
CREATE TYPE Strutturato AS ENUM ('Ricercatore', 'Professore Associato', 'Professore Ordinario');

-- Definizione del dominio 'LavoroProgetto'
CREATE TYPE LavoroProgetto AS ENUM ('Ricerca e Sviluppo', 'Dimostrazione', 'Management', 'Altro');

-- Definizione del dominio 'LavoroNonProgettuale'
CREATE TYPE LavoroNonProgettuale AS ENUM ('Didattica', 'Ricerca', 'Missione', 'Incontro Dipartimentale', 'Incontro Accademico', 'Altro');

-- Definizione del dominio 'CausaAssenza'
CREATE TYPE CausaAssenza AS ENUM ('Chiusura Universitaria', 'Maternita', 'Malattia');

-- Definizione del dominio 'PosInteger'
CREATE DOMAIN PosInteger AS INTEGER CHECK (VALUE >= 0);

-- Definizione del dominio 'StringaM'
CREATE DOMAIN StringaM AS VARCHAR(100);

-- Definizione del dominio 'NumeroOre'
CREATE DOMAIN NumeroOre AS INTEGER CHECK (VALUE BETWEEN 0 AND 8);

-- Definizione del dominio 'Denaro'
CREATE DOMAIN Denaro AS REAL CHECK (VALUE >= 0);

-- Tabella 'Persona'
CREATE TABLE Persona (
    id PosInteger PRIMARY KEY,
    nome StringaM NOT NULL,
    cognome StringaM NOT NULL,
    posizione Strutturato NOT NULL,
    stipendio Denaro NOT NULL
);

-- Tabella 'Progetto'
CREATE TABLE Progetto (
    id PosInteger PRIMARY KEY,
    nome StringaM NOT NULL UNIQUE, -- VincoloDB.1: nome è una chiave alternativa
    inizio DATE NOT NULL,
    fine DATE NOT NULL,
    budget Denaro NOT NULL,
    CHECK (inizio < fine) -- VincoloDB.2: inizio deve essere minore di fine
);

-- Tabella 'WP'
CREATE TABLE WP (
    progetto PosInteger NOT NULL,
    id PosInteger NOT NULL,
    nome StringaM NOT NULL,
    inizio DATE NOT NULL,
    fine DATE NOT NULL,
    PRIMARY KEY (progetto, id), -- Combinazione di progetto e id come chiave primaria
    UNIQUE (progetto, nome), -- VincoloDB.4: altra chiave
    CHECK (inizio < fine), -- VincoloDB.3: inizio deve essere minore di fine
    FOREIGN KEY (progetto) REFERENCES Progetto(id) -- VincoloDB.5: foreign key
);

-- Tabella 'AttivitaProgetto'
CREATE TABLE AttivitaProgetto (
    id PosInteger PRIMARY KEY,
    persona PosInteger NOT NULL,
    progetto PosInteger NOT NULL,
    wp PosInteger NOT NULL,
    giorno DATE NOT NULL,
    tipo LavoroProgetto NOT NULL,
    oreDurata NumeroOre NOT NULL,
    FOREIGN KEY (persona) REFERENCES Persona(id), -- VincoloDB.6: foreign key
    FOREIGN KEY (progetto, wp) REFERENCES WP(progetto, id) -- VincoloDB.7: foreign key
);

-- Tabella 'AttivitaNonProgettuale'
CREATE TABLE AttivitaNonProgettuale (
    id PosInteger PRIMARY KEY,
    persona PosInteger NOT NULL,
    tipo LavoroNonProgettuale NOT NULL,
    giorno DATE NOT NULL,
    oreDurata NumeroOre NOT NULL,
    FOREIGN KEY (persona) REFERENCES Persona(id) -- VincoloDB.8: foreign key
);

-- Tabella 'Assenza'
CREATE TABLE Assenza (
    id PosInteger PRIMARY KEY,
    persona PosInteger NOT NULL,
    tipo CausaAssenza NOT NULL,
    giorno DATE NOT NULL,
    UNIQUE (persona, giorno), -- VincoloDB.9: combinazione unica di persona e giorno
    FOREIGN KEY (persona) REFERENCES Persona(id) -- VincoloDB.10: foreign key
);
