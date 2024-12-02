-- This script was generated by the ERD tool in pgAdmin 4.
-- Please log an issue at https://github.com/pgadmin-org/pgadmin4/issues/new/choose if you find any bugs, including reproduction steps.
BEGIN;


CREATE TABLE IF NOT EXISTS public.acessorio
(
    id serial NOT NULL,
    nome character varying COLLATE pg_catalog."default" NOT NULL,
    "tipo_veicolo_compatibilità" character varying COLLATE pg_catalog."default" NOT NULL,
    descrizione character varying COLLATE pg_catalog."default" NOT NULL,
    prezzo numeric(10, 2) NOT NULL,
    CONSTRAINT acessorio_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.automobile
(
    targa character varying COLLATE pg_catalog."default" NOT NULL,
    marca character varying COLLATE pg_catalog."default" NOT NULL,
    modello character varying COLLATE pg_catalog."default" NOT NULL,
    prezzo_base numeric(10, 2),
    filiale integer NOT NULL DEFAULT 1,
    CONSTRAINT automobile_pkey PRIMARY KEY (targa)
);

CREATE TABLE IF NOT EXISTS public.filiale
(
    id serial NOT NULL,
    nome character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT filiale_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.motocicletta
(
    targa character varying COLLATE pg_catalog."default" NOT NULL,
    marca character varying COLLATE pg_catalog."default" NOT NULL,
    modello character varying COLLATE pg_catalog."default" NOT NULL,
    prezzo_base numeric(10, 2),
    filiale integer NOT NULL DEFAULT 1,
    CONSTRAINT motocicletta_pkey PRIMARY KEY (targa)
);

CREATE TABLE IF NOT EXISTS public.utente
(
    username character varying COLLATE pg_catalog."default" NOT NULL,
    password character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT utente_pkey PRIMARY KEY (username)
);

CREATE TABLE IF NOT EXISTS public.vendita_auto
(
    id serial NOT NULL,
    targa_auto character varying COLLATE pg_catalog."default" NOT NULL,
    data_vendita date NOT NULL,
    prezzo_vendita numeric(10, 2) NOT NULL,
    CONSTRAINT vendita_auto_pkey PRIMARY KEY (id),
    CONSTRAINT vendita_auto_targa_auto_key UNIQUE (targa_auto)
);

CREATE TABLE IF NOT EXISTS public.vendita_moto
(
    id serial NOT NULL,
    targa_moto character varying COLLATE pg_catalog."default" NOT NULL,
    data_vendita date NOT NULL,
    prezzo_vendita numeric(10, 2) NOT NULL,
    CONSTRAINT vendita_moto_pkey PRIMARY KEY (id),
    CONSTRAINT vendita_moto_targa_moto_key UNIQUE (targa_moto)
);

ALTER TABLE IF EXISTS public.automobile
    ADD CONSTRAINT fk_filiale FOREIGN KEY (filiale)
    REFERENCES public.filiale (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.motocicletta
    ADD CONSTRAINT fk_filiale FOREIGN KEY (filiale)
    REFERENCES public.filiale (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.vendita_auto
    ADD CONSTRAINT vendita_auto_targa_auto_fkey FOREIGN KEY (targa_auto)
    REFERENCES public.automobile (targa) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;
CREATE INDEX IF NOT EXISTS vendita_auto_targa_auto_key
    ON public.vendita_auto(targa_auto);


ALTER TABLE IF EXISTS public.vendita_moto
    ADD CONSTRAINT vendita_moto_targa_moto_fkey FOREIGN KEY (targa_moto)
    REFERENCES public.motocicletta (targa) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;
CREATE INDEX IF NOT EXISTS vendita_moto_targa_moto_key
    ON public.vendita_moto(targa_moto);

END;