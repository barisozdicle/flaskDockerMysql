use SuadiyeDB;

create table Furniture
(
    Id             int primary key,
    FurnitureName  varchar(99) not null,
    FurnitureImage varchar(99) not null
);

INSERT INTO Furniture (Id, FurnitureName, FurnitureImage) VALUES (1, 'Televizyon', 'TV Resmi');
