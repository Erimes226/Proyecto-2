Este proyecto es una aplicación para gestionar veterinarias y mascotas utilizando una arquitectura basada en tres capas: acceso a datos, dominio y servicios:

    Acceso a datos:
        Se maneja la conexión a la base de datos usando SQLAlchemy (Database y DATABASE_URL).
        Define los modelos de la base de datos (Veterinaria, Mascota) en model.py.
        Contiene los Data Transfer Objects (DTO) que se usan para transferir datos entre las capas (VeterinariaDTO, MascotaDTO).

    Dominio:
        Es donde se definen las entidades centrales del proyecto (Veterinaria, Mascota) y sus correspondientes DTOs.

    Servicios:
        Se implementan servicios como VeterinariaService para gestionar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre las veterinarias y las mascotas.
        Se utiliza un servicio genérico (GenericRepository) que permite realizar operaciones CRUD de manera más abstracta y reutilizable para diferentes entidades.

    Interfaz de usuario:
        La aplicación presenta un menú interactivo en la consola donde el usuario puede gestionar veterinarias y mascotas.
        En el menú de veterinarias, se pueden crear, mostrar, buscar, actualizar y eliminar veterinarias.
        En el menú de mascotas, se pueden realizar operaciones similares, además de asignar una mascota a una veterinaria.

    Ejecución:
        La aplicación se ejecuta a través de la función main(), que inicia la base de datos y permite la interacción del usuario mediante el menú.
