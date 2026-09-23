# Publication activation runbook

Publication is **blocked by default**. Local proof and CI configuration do not
publish the manual or prove a live website.

## Operator path

1. Verify the HTTPS site URL, base path, host, SSH user and port, canonical
   marker-owned target root, and explicit activation mechanism with the hosting owner.
2. Put only verified values in `documentation/deployment-target.yml`; set both
   `activation` and `verification_state` to `verified` in the reviewed change.
3. Configure the protected GitHub `production` environment with
   `PUBLISH_KNOWN_HOSTS` and `PUBLISH_SSH_PRIVATE_KEY`. These names are generic;
   do not commit values, keys, hosts, or known-host entries.
4. Dispatch **publish-manual** with a full reviewed `main` SHA. It repeats tests,
   validates the manual, binds the artifact to that SHA, verified site URL, and base path, and rejects an unborn,
   foreign, or non-ancestor ref before remote activity.

## Gates and limits

The upload creates only a new isolated `releases/<sha>` directory after the
remote marker and root checks pass. It never uses `rsync --delete`, removes no
release, and does not switch a current-release pointer. Server activation is not
implemented here; an operator must use the verified host-specific mechanism.

## Live acceptance checklist

- [ ] HTTPS site and configured base path serve the expected manual.
- [ ] Internal assets, canonical URLs, search, and unknown-route 404 behave correctly.
- [ ] Cache behavior is checked after publication and after any activation switch.
- [ ] The result is recorded as runtime/deployed evidence only after observation.

## Recovery

Rebuild or republish a previously reviewed SHA and its validated artifact only when its site URL and base path match the verified target, into a
new isolated release directory. Preserve old release directories. Because rsync
is non-atomic, do not claim an atomic upload; perform any activation or rollback
only through the verified server mechanism after confirming the prior artifact.
