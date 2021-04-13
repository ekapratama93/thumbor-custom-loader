# thumbor-custom-single-loader

[![codecov](https://codecov.io/gh/ekapratama93/thumbor-custom-single-loader/branch/main/graph/badge.svg?token=BUFX825X3U)](https://codecov.io/gh/ekapratama93/thumbor-custom-single-loader)

Plugin for Thumbor HTTP Loader to replace host from a single source.

## Use Case

Example you have multiple source url which use single CDN resources.
You can replace foo.com or foo.id to either one so it will fetch from single source host.

```bash
                   +-------+
         +-------->|foo.com|
         |         +-------+
         |                 |
+--------+                 |        +-------+
| Thumbor|                 +------->|bar CDN|
+--------+                 |        +-------+
         |                 |
         |         +-------+
         +-------->|foo.id |
                   +-------+
```

## Configuration

`HTTP_LOADER_HOST_REPLACE_CANDIDATES` : Comma separated string of hosts to replace. Ex. `"foo.com,foo.id"`
`HTTP_LOADER_HOST_REPLACER` : Hostname to replace the candidate with. Ex. `"bar.com"`
