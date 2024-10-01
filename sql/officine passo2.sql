create domain Stringa_not_null as varchar(100)
    check (value is not null);

create domain Int_not_null as int
    check (value is not null) and (value > 0);

create type Indirizzo as (
    via Stringa_not_null,
    civico Int_not_null
);

create domain CodFisc as (
    check (value ~* '[A-Z]{6}[0-9]{9}[A-Z][0-9]{2}[0-9A-Z]{5}$')
);

create table Nazione (
    nome varchar(100) not null,
    primary key(nome)
);

create table Regione (
    nome varchar(100) not null,
    nazione varchar(100) not null,
    primary key(nome, nazione),
    foreing key(nazione) references Nazione(nome)
);

create table Citta (
    nome varchar(100) not null,
    regione varchar(100) not null,
    nazione varchar(100) not null,
    primary key(nome, regione, nazione),
    foreing key(regione, nazione) references Regione(nome, nazione)
);

create table Marca(
    nome varchar(100) not null,
    primary key(nome)
);

create table TipoVeicolo(
    nome varchar(100) not null,
    primary key(nome)
);

create table Modello(
    nome varchar(100) not null,
    marca varchar(100) not null,
    tipo_veicolo varchar(100) not null
    primary key (nome, marca),
    foreing key (marca) references Marca(nome)
    foreing key (tipo_veicolo) references TipoVeicolo(nome)
);
create table Persona(
    cf CodFisc not null,
    nome varchar(100) not null,
    indirizzo Indirizzo not null,
    telefono varchar(100) not null,
    citta varchar(100) not null,
    regione varchar(100) not null,
    nazione varchar(100) not null,
    primary key(cf),
    foreing key (citta, regione, nazione) references Citta(nome, regione, nazione)
)

create table Cliente(
    persona CodFisc not null,
    primary key(persona),
    foreing key (persona) references Persona(cf)
);

create table Veicolo(
    targa varchar(100) not null,
    immatricolazione int not null,
    modello varchar(100) not null,
    cliente CodFisc not null,
    marca varchar(100) not null,
    primary key(targa),
    foreing key (modello, marca) references Modello(nome, marca)
    foreing key (cliente) references Cliente(persona)
);

create table Staff(
    persona CodFisc not null,
    primary key(persona),
    foreing key (persona) references Persona(cf)
);

create table Direttore(
    staff CodFisc not null,
    nascita date not null
    primary key(staff),
    foreing key (staff) references Staff(persona)
);

create table Officina(
    nome varchar(100) not null,
    indirizzo Indirizzo not null
    id int not null,
    citta varchar(100) not null,
    regione varchar(100) not null,
    nazione varchar(100) not null,
    direttore CodFisc not null,
    primary key(id),
    foreing key (citta, regione, nazione) references Citta(nome, regione, nazione),
    foreing key (direttore) references Direttore(staff)
);

create table Dipendente(
    staff CodFisc not null,
    officina int not null,
    data_assunzione date not null,
    primary key(staff),
    foreing key (staff) references Staff(persona),
    foreing key (officina) references Officina(id)
);

create table Riparazione(
    riconsegna timestamp,
    codice int not null,
    officina int not null,
    primary key(codice),
    foreing key (officina) references Officina(id)
);