# Security Policy

## Supported Versions

| Version | Supported |
| ------- | --------- |
| latest  | Yes       |

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it
responsibly:

1. **Do not** open a public GitHub issue for security vulnerabilities.
2. Email the maintainer at the address listed in `pyproject.toml`, or use
   [GitHub's private vulnerability reporting](https://github.com/stickerdaniel/linkedin-mcp-server/security/advisories/new).
3. Include a description of the vulnerability, steps to reproduce, and any
   potential impact.

You should receive a response within 72 hours. Security fixes will be released
as patch versions and documented in the release notes.

## Security Considerations

This server manages LinkedIn session credentials (cookies, browser profiles).
Keep the following in mind:

- **Session files are sensitive.** The `~/.linkedin-mcp/` directory contains
  authentication cookies and browser state. Protect it with restrictive file
  permissions (0700 for directories, 0600 for files).
- **HTTP transport has no authentication.** When using `--transport streamable-http`,
  bind to `127.0.0.1` (default) unless you have a reverse proxy with
  authentication in front. Binding to `0.0.0.0` exposes your LinkedIn session
  to the network.
- **Trace mode captures private data.** When `LINKEDIN_TRACE_MODE` is set to
  `on_error` or `always`, full-page screenshots and page text are saved to disk.
  Only enable tracing for debugging.
- **Docker volume mounts share credentials.** The default `docker-compose.yml`
  mounts `~/.linkedin-mcp` into the container. Ensure the host directory
  permissions are restrictive.
