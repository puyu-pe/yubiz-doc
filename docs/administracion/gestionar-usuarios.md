# Gestionar usuarios

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Consultar los registros de usuarios y, solo si los controles están habilitados
para su sesión, actualizar la información visible de un registro autorizado.

## Acceso condicional

La disponibilidad de lista, alta, edición y estado depende de la sesión y de la
configuración. La presencia de un botón no prueba que la operación esté permitida
por el servidor. Si no tiene una acción habilitada, contacte a la persona
administradora autorizada.

## Requisitos y datos

- Acceso a **Gestión de Usuarios** cuando la opción esté disponible.
- Identificación del registro que necesita revisar.
- Nombre, apellido, usuario, teléfono y estado solo cuando el formulario los muestre.

## Punto de partida

Abra la lista de usuarios y localice el registro sin compartir credenciales ni
datos de acceso en esta guía.

## Pasos

1. Revise las columnas de nombre, apellido, usuario, estado y actualización.
2. Abra un registro únicamente si la acción de consulta o edición está habilitada.
3. Verifique los campos visibles antes de guardar un cambio permitido.
4. Si se solicita una contraseña, use el procedimiento seguro definido por su organización; no la anote ni la comunique.
5. Vuelva a la lista y compruebe el resultado mostrado antes de realizar otra acción.

## Campos y validaciones observados

El formulario fuente incluye nombre, apellido, usuario, teléfono, contraseña y
estado. Nombre, usuario y contraseña se declaran obligatorios en el alta, y el
usuario debe ser único. Estado se presenta como activo o inactivo. La validación
exacta y las acciones disponibles requieren verificación en runtime.

## Resultado revisado en fuente

La fuente renderiza una lista y formularios con esos campos, limita los controles
según el contexto de sesión y evita exportación e impresión desde ese recorrido.
No se afirma que crear, editar, desactivar o cambiar una clave tenga aprobación,
permiso o efecto desplegado.

## Advertencias y casos límite

No use esta ficha para recuperar acceso, revelar contraseñas, operar cuentas
especiales ni asignar módulos o permisos. No deduzca que un usuario puede acceder
a un establecimiento solo por aparecer en la lista.

## Problemas frecuentes y condiciones de detención

- No aparece la acción esperada: no intente forzarla; contacte a administración autorizada.
- Usuario duplicado o campo obligatorio vacío: corrija el dato visible antes de guardar.
- Resultado inesperado: detenga cambios posteriores y vuelva a revisar la lista.
- Solicitud de privilegios, módulos o permisos: no continúe en este recorrido.

## Verificaciones pendientes en runtime

- Alcance de consulta, alta, edición y estado para cada sesión.
- Mensajes, reglas de contraseña y efecto real de un cambio.
- Auditoría, notificaciones y efectos sobre accesos o sesiones existentes.

## Enlaces relacionados

- [Consultar roles disponibles](consultar-roles.md)
- [Asignar establecimientos a vendedores](asignar-establecimientos-a-vendedores.md)
- [Perfil y cierre de sesión](../inicio/perfil-y-cierre-de-sesion.md)
