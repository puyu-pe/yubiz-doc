<a id="consultar-roles-disponibles"></a>

# 8.2 Consultar roles disponibles

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Consultar los roles que la sesión muestra y revisar sus datos visibles sin
presuponer que pueda modificarlos o asignar privilegios.

## Acceso condicional

La lista y sus acciones dependen de la sesión. La interfaz reserva la asignación de
módulos y permisos a un contexto sensible; esa operación no forma parte de esta
guía. Si necesita cambiar privilegios, deténgase y contacte a la persona
administradora autorizada.

## Requisitos y datos

- Acceso a la lista de roles si está disponible.
- Un rol identificado para su consulta.

## Punto de partida

Abra **Gestión de Roles** y revise la lista antes de seleccionar cualquier acción.

## Pasos

1. Localice el rol por código, nombre o descripción visibles.
2. Revise su estado y la fecha de actualización mostrada.
3. Abra el detalle solo si la acción de consulta está habilitada.
4. Si el sistema ofrece editar o crear, confirme con la persona autorizada antes de guardar.
5. No continúe hacia módulos, permisos ni acciones de acceso desde este recorrido.

## Campos y validaciones observados

La lista revisada muestra código, nombre del rol, descripción, estado y
actualización. En el formulario, código, nombre y estado son obligatorios, y el
código debe ser único. El estado se muestra como activo o inactivo. La aplicación
de estas reglas en la sesión debe confirmarse en el entorno de trabajo.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

El navegador puede mostrar los datos de roles y restringe las acciones según el
contexto. El flujo incluye mecanismos sensibles de módulos y permisos fuera del
alcance público; esta ficha no describe su uso ni asegura privilegios.

## Advertencias y casos límite

Un rol activo no demuestra acceso efectivo a una opción. No use código, nombre o
estado como sustituto de una revisión autorizada de permisos. No invente roles ni
suponga una jerarquía por sus nombres.

## Problemas frecuentes y condiciones de detención

- No se muestra la lista o una acción: no intente acceder por otra vía.
- Código duplicado o campos incompletos: no guarde hasta que la persona autorizada los revise.
- Necesita módulos o permisos: detenga el proceso y escale a administración autorizada.
- Cambio inesperado: vuelva a consultar el rol antes de continuar.

## Enlaces relacionados

- [Gestionar usuarios](gestionar-usuarios.md)
- [Asignar establecimientos a vendedores](asignar-establecimientos-a-vendedores.md)
- [Administración](index.md)
