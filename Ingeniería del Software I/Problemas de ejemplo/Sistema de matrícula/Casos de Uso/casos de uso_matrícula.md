# Autenticarse en el sistema

```mermaid
useCaseDiagram
    %% Actores
    actor Estudiante as Estudiante
    actor Administrativo as Administrativo
    actor Jefe as "Jefe de Carrera"

    %% Casos de uso
    usecase UC1 as "Autenticarse en el sistema"
    usecase UC1_ext as "Mostrar mensaje de error (credenciales incorrectas)"

    %% Relaciones
    Estudiante --> UC1
    Administrativo --> UC1
    Jefe --> UC1
    UC1 ..> UC1_ext : <<extend>>

