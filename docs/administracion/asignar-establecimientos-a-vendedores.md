<a id="asignar-establecimientos-a-vendedores"></a>

# 8.3 Asignar establecimientos a vendedores

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

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
La interfaz evita duplicar la combinación de usuario, establecimiento y rol en el
recorrido general. Los datos disponibles y validaciones finales pueden variar según la configuración disponible.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

Al confirmar, se registran el conjunto de establecimientos marcados y muestra un resultado
de actualización. La interfaz crea, actualiza u omite asociaciones según los datos
recibidos. Esto describe mecánica del formulario, no una aprobación ni un efecto de
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

## Enlaces relacionados

- [Gestionar usuarios](gestionar-usuarios.md)
- [Consultar roles disponibles](consultar-roles.md)
- [Administración](index.md)
