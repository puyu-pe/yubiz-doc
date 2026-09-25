<a id="revisar-el-perfil-editar-datos-y-cerrar-sesión"></a>

# 1.4 Revisar el perfil, editar datos y cerrar sesión

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Revisar los datos propios, actualizar información personal cuando esté disponible
y cerrar la sesión al finalizar el trabajo.

## Acceso condicional

Las opciones de perfil y edición aparecen en la navegación disponible para la
sesión. No se documentan aquí acciones de administración de cuentas, roles o
módulos.

## Requisitos y datos

- Sesión iniciada.
- Datos personales que se desean revisar o actualizar.
- Si se cambia la clave, la clave actual y la nueva confirmación.

## Punto de partida

En el menú de personas usuarias, con una opción de perfil o edición disponible.

## Pasos

1. Abra **Mi perfil** para revisar nombre, apellido y usuario mostrados.
2. Si necesita actualizar datos propios, abra **Editar mis datos** cuando la
   opción esté disponible.
3. Revise los campos modificados antes de usar **Guardar Datos**.
4. Para cambiar la clave, complete la clave actual, la nueva clave y su
   confirmación antes de guardar.
5. Al terminar el trabajo, abra el menú de la persona usuaria y seleccione
   **Cerrar Sesión**.

## Campos y validaciones observados

El perfil muestra nombre, apellido, usuario y una clave enmascarada. La edición
revisada permite nombre y apellido; la interfaz exige nombre, apellido y teléfono.
Si se solicita cambio de clave, exige clave actual, una nueva clave de al menos
seis caracteres y coincidencia con la confirmación.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

La edición válida actualiza datos propios y redirige a la pantalla inicial. El
cierre de sesión elimina el contexto de sesión y dirige al inicio de acceso.

## Advertencias y casos límite

No comparta la clave actual ni la nueva. Si la edición no coincide con los datos
que desea conservar, no guarde y confirme el procedimiento aplicable.

## Problemas frecuentes y condiciones de detención

- Campos obligatorios incompletos: complete los datos antes de guardar.
- Nueva clave sin coincidencia o demasiado corta: corríjala antes de confirmar.
- Opción no visible: no intente administrar cuentas ajenas; confirme el alcance
  disponible para su sesión.

## Enlaces relacionados

- [Ubicarse en Yubiz y reconocer el menú disponible](ubicarse-en-yubiz.md)
- [Iniciar sesión y elegir establecimiento](iniciar-sesion.md)
