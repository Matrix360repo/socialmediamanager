# Lakhotia n8n Cloud bridge v0.5

## Constraint
n8n Cloud cannot access `127.0.0.1:8001` or `host.docker.internal:8001` on your computer. A public HTTPS endpoint is required for the existing Matrix 360 FastAPI application.

## Required before testing
1. Deploy the application on a server or managed Python web host with HTTPS. A serverless platform with ephemeral storage is **not suitable unchanged**: this prototype stores SQLite data and rendered PNGs on its local disk. Use a persistent disk, or migrate to PostgreSQL and object storage.
2. **Do not publish the existing v0.3 app publicly as-is.** It has no enforced login or access protection on `/`, `/api/drafts`, previews or approvals. Configure private network access with a secure proxy, or add verified authentication/RBAC to every sensitive endpoint.
3. Add a server-side secret check to `/api/generate` and require the `X-Matrix360-Key` header. Keep the secret in host environment secrets. Header auth is transport authentication only and does not replace full user RBAC.
4. Test `GET /health` if you add a health endpoint (the v0.3 app does not provide one); otherwise test a protected API endpoint with valid/invalid credentials.
5. In n8n Cloud: Workflows → Import from File → `lakhotia_n8n_cloud_drafts_v05.json`.
6. In **Call Lakhotia Draft API**, change the example domain to the real HTTPS domain. Under Credentials create **Header Auth**, name `X-Matrix360-Key` and value the securely stored server-side key. Select this credential; do not embed the key in the exported JSON.
7. In **Create Review Queue Entries**, change the example `base` domain to the same HTTPS host. The draft page URL must be checked against the actual app routes; v0.3 uses `/draft/{id}`.
8. Execute manually with dummy briefs first. Verify three API calls and nine candidate objects, check review access, reject one draft and approve a compliant one manually.
9. Keep the workflow inactive until checks pass. There is deliberately no Instagram/LinkedIn publication or ad-spend node.

## Agent phase 1
Manual Trigger → Campaign Briefs → Protected Matrix 360 Content API → Format Review Queue.

## Known unresolved items
- API authentication, user login, role permissions, tenant isolation and audit logs are not implemented in v0.3.
- Cloud-hosted app deployment is not yet performed.
- No n8n Cloud execution has been verified.
- Existing copy generation may operate offline and should be labeled a demonstration unless model credentials are configured.
- Existing creative outputs are proofs and need brand QA.
