create domain URL as (
    check (value ~* '^(https?://)?([a-zA-Z0-9-]+.)+[a-zA-Z]{2,}(:\d+)?(/[^\s]*)?$')
);

create domain RealGEZ as real
        check (value >= 0)

create domain RealGZ as real
        check (value > 0)

create domain IntegerGEZ as int
        check (value >= 0)

create domain Voto as int
        check (value >= 0 and value <=5)

create type CondUsato as enum (
        'ottimo', 'buono', 'discreto', 'da sistemare'
);

create table Utente (
    nome varchar not null,
    registrazione timestamp,
    primary key(nome)
);

create table Privato (
    utente varchar not null,
    primary key(utente),
    foreing key (utente) references Utente(nome)
);

create table VenditoreProf (
    vetrina URL not null,
    utente varchar not null,
    primary key(utente),
    foreing key (utente) references Utente(nome)
);

create table Categoria (
    nome varchar not null,
    primary key(nome),
    super_categoria varchar,
    foreing key (super_categoria) references Categoria(nome)
);

create table MetodoPagamento (
    nome varchar not null,
    primary key(nome)
);

create table Valuta (
    nome varchar not null
    primary key (nome)
);

create table Post (
    descrizione text not null,
    pubblicazione timestamp not null,
    anni_garanzia IntegerGEZ not null,
    prezzo RealGEZ not null,
    ha_feedback Boolean not null,
    voto Voto,
    commento text,
    nuovo Boolean not null,
    condizioni CondUsato,
    id serial not null,
    primary key(id),
    utente varchar not null,
    categoria varchar not null,
    metodo_pagamento varchar not null,
    valuta varchar not null,
    foreing key (utente) references Utente(nome),
    foreing key (categoria) references Categoria(nome),
    foreing key (metodo_pagamento) references MetodoPagamento(nome),
    foreing key (valuta) references Valuta(nome)
);

create table PostCompraloSubito (
    post serial not null,
    primary key(post),
    foreing key (post) references Post(post)
);

create table acquirente (
    post serial not null,
    utente varchar not null,
    istante timestamp not null,
    primary key(post, utente),
    foreing key (post) references PostCompraloSubito(post),
    foreing key (utente) references Privato(utente)
);

create table PostAsta (
    rialzo RealGZ not null,
    scadenza timestamp not null,
    post serial not null,
    primary key(post),
    foreing key (post) references Post(post)
);

create table Bid (
    post serial not null,
    utente varchar not null,
    istante timestamp not null,
    primary key(post, utente, istante),
    foreing key (post) references PostAsta(post),
    foreing key (utente) references Privato(utente)
);