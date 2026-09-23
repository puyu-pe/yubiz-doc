# Asignar establecimientos a vendedores

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Revisar y, cuando el recorrido esté habilitado para una persona administradora
autorizada, actualizar los establecimientos asociados a un vendedor.

## Acceso condicional

La asignación depende de la sesión y de la configuración. No infiera que marcar
un establecimiento concede acceso efectivo, una función comercial o permisos.
Si no está autorizado, deténgase y contacte a la persona administradora.

## Requisitos y datos

- Un vendedor disponible en la gestión correspondiente.
- Establecimientos listados por el formulario.
- Confirmación organizacional antes de cambiar una asociación.

## Punto de partida

Desde el registro de un vendedor, abra **Establecimientos** únicamente si la
acción está habilitada.

## Pasos

1. Revise el nombre del vendedor y la tabla de establecimientos mostrada.
2. Identifique la descripción del establecimiento y su estado de selección.
3. Marque o desmarque solo los establecimientos confirmados por la persona autorizada.
4. Revise la selección completa antes de usar **Guardar**.
5. Espere la respuesta y vuelva a la gestión de vendedores para comprobar el resultado mostrado.

## Campos y validaciones observados

La pantalla presenta una tabla con selección por establecimiento, descripción,
dirección y ubicación. Incluye selección total y conserva el estado de cada fila.
La fuente evita duplicar la combinación de usuario, establecimiento y rol en el
recorrido general. Los datos disponibles y validaciones finales requieren runtime.

## Resultado revisado en fuente

El navegador envía el conjunto de establecimientos marcados y muestra un resultado
de actualización. La fuente crea, actualiza u omite asociaciones según los datos
recibidos. Esto describe mecánica de código, no una aprobación ni un efecto de
acceso, ventas o permisos en producción.

## Advertencias y casos límite

La selección total puede cambiar más de una fila; revísela antes de guardar. No
incluya datos personales, direcciones o identificadores de usuarios en solicitudes
fuera de los canales autorizados. Esta ficha no cubre asignación de módulos ni permisos.

## Problemas frecuentes y condiciones de detención

- Acción no disponible: no intente acceder por una ruta alternativa.
- Establecimiento o vendedor no identificable: deténgase antes de cambiar la selección.
- Respuesta de error o resultado incierto: no reenvíe; vuelva a consultar el estado.
- Solicitud de privilegios adicionales: escale a administración autorizada.

## Verificaciones pendientes en runtime

- Disponibilidad del recorrido y quién puede guardar cambios.
- Efecto de activar o desactivar una asociación.
- Relación entre establecimiento, función de vendedor, permisos y sesiones activas.

## Enlaces relacionados

- [Gestionar usuarios](gestionar-usuarios.md)
- [Consultar roles disponibles](consultar-roles.md)
- [Administración](index.md)
