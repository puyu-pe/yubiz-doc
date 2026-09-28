# Runbook de publicación en producción

La publicación se ejecuta al enviar cambios a `main` o manualmente para un SHA completo y revisado de `main`.
La configuración y las pruebas locales no publican el manual ni prueban el sitio
en producción.

## Preparación

1. Configure el entorno GitHub `production` con las variables `DEPLOY_HOST` y
   `DEPLOY_USER`, y los secretos `DEPLOY_KNOWN_HOSTS` y
   `DEPLOY_SSH_PRIVATE_KEY`.
2. Envíe el cambio revisado a `main` para publicar el SHA del evento, o despache
   **publish-manual** con un SHA completo, revisado y perteneciente a `main`.
3. El flujo ejecuta las pruebas, valida el manual y vincula el artefacto al SHA,
   la URL `https://yubiz.puyu.pe/manual/` y la base `/manual/` antes de actividad
   remota.

## Alcance y límites

La sincronización reemplaza directamente solo
`/var/www/vhosts/yubiz.puyu.pe/httpdocs/manual`. `rsync --delete` elimina
archivos obsoletos únicamente dentro de esa carpeta. Antes de sincronizar, el
flujo crea la carpeta aislada si falta y verifica o crea el enlace absoluto desde
`app-prod/current/public/manual`; rechaza un archivo, directorio o enlace que
apunte a otro destino en esa ruta.

La carga no es atómica: durante una sincronización puede haber una versión
parcialmente actualizada. Si una futura publicación de la aplicación reemplaza
`current`, su despliegue debe recrear el enlace `current/public/manual` hacia la
carpeta absoluta del manual. El flujo del manual vuelve a verificarlo sin
reemplazar `current` ni `public`.

## Verificación posterior

- [ ] HTTPS site and configured base path serve the expected manual.
- [ ] Internal assets, canonical URLs, search, and unknown-route 404 behave correctly.
- [ ] Cache behavior is checked after publication and after any activation switch.
- [ ] The result is recorded as runtime/deployed evidence only after observation.

## Recuperación

Vuelva a despachar un SHA previamente revisado solo si el artefacto conserva la
misma URL y base verificadas. Si necesita restaurar contenido, publique el SHA
anterior revisado; confirme el resultado observado antes de registrarlo como
evidencia de producción.
