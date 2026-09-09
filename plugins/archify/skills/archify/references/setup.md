# Runtime setup

Upstream: [tt-a1i/archify](https://github.com/tt-a1i/archify).
Verified 2026-09-09: revision `10722002bb8777ecb639d93c49586fae4adf3ae4`, version `2.17.0-dev.1`.
Upstream license: MIT.
The runtime is an external dependency; this marketplace does not redistribute upstream source or grant its license.

Requires Git and Node.js >=18.
The verified revision is a development snapshot, pinned for reproducibility, not a stable-release recommendation.
Choose a new runtime directory outside the plugin cache, for example `.tools/archify` in the target workspace.

```bash
git clone https://github.com/tt-a1i/archify.git .tools/archify
git -C .tools/archify checkout --detach 10722002bb8777ecb639d93c49586fae4adf3ae4
git -C .tools/archify rev-parse HEAD
export ARCHIFY_UPDATE_CHECK_DISABLED=1
node .tools/archify/archify/bin/archify.mjs doctor
```

Inspect an existing checkout's revision and changes instead of overwriting it.
Packaged standalone validators make npm installation unnecessary for ordinary rendering.
Run authoring commands from `.tools/archify/archify`, resolving input/output paths from there.
Keep downloaded runtimes outside changes intended for delivery.

Download contacts GitHub.
The environment override disables the optional upstream update check and its state writes.
Rendering reads local JSON and writes output files without an account or API key.
Optional brand capture fetches a supplied website; preview starts a loopback server.
Neither is needed for ordinary rendering.
