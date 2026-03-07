import os
from fastapi import Request
from fastapi.responses import FileResponse

SITE_DIR = "sites"


async def subdomain_router(request: Request, call_next):

    host = request.headers.get("host", "")

    parts = host.split(".")

    if len(parts) >= 3:

        subdomain = parts[0]

        site_path = os.path.join(SITE_DIR, subdomain, "index.html")

        if os.path.exists(site_path):

            return FileResponse(site_path)

    return await call_next(request)