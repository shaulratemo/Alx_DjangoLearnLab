# Security Configuration

## Django Settings
- `SECURE_SSL_REDIRECT = True`: Forces all requests to use HTTPS.
- `SECURE_HSTS_SECONDS = 31536000`: Enforces HTTPS for 1 year via HSTS.
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`: Applies HSTS to subdomains.
- `SECURE_HSTS_PRELOAD = True`: Allows site to be included in browsers’ HSTS preload list.
- `SESSION_COOKIE_SECURE = True`: Ensures session cookies are sent only over HTTPS.
- `CSRF_COOKIE_SECURE = True`: Ensures CSRF cookies are sent only over HTTPS.
- `X_FRAME_OPTIONS = "DENY"`: Prevents clickjacking attacks.
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents browsers from MIME type sniffing.
- `SECURE_BROWSER_XSS_FILTER = True`: Enables XSS protection.

## Deployment
- SSL/TLS configured via Let’s Encrypt with Nginx (or Apache).
- All HTTP traffic is redirected to HTTPS by web server and Django.

## Testing
- Verified that non-HTTPS requests are redirected.
- Cookies flagged as `Secure` in browser dev tools.
- Tested forms for CSRF tokens.